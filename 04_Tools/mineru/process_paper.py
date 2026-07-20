#!/usr/bin/env python3
"""
Process a single Zotero paper through MinerU CLI + Normalization.

Usage:
    python process_paper.py <Zotero_Item_Key>

Example:
    python process_paper.py 9W23DNVG

The Item Key can be EITHER:
- A paper key (e.g., 5L2QLL47)
- An attachment key (e.g., 9W23DNVG)

The script resolves both cases automatically.

Steps:
    1. Resolve Item Key -> paper key + PDF path
    2. Check if MinerU output already exists (skip if yes)
    3. Run MinerU CLI (pipeline backend, txt method)
    4. Run normalization layer (convert to full.md format)
    5. Verify full.md exists
    6. Log results

Architecture:
    Zotero storage/{att_key}/{pdf}.pdf
        -> MinerU CLI
        -> MinerU_md/{paper}/full.md
        -> Agent Literature Processing
"""

import os
import sys
import subprocess
import sqlite3
from pathlib import Path
from datetime import datetime

# Configuration
ZOTERO_DATA_DIR = Path("/home/lco/ResearchAI_Data/Zotero")
ZOTERO_DB = ZOTERO_DATA_DIR / "zotero.sqlite"
ZOTERO_STORAGE = ZOTERO_DATA_DIR / "storage"
MINERU_MD = Path("/home/lco/ResearchAI_Data/Paper/MinerU_md")
MINERU_LOGS = Path("/home/lco/ResearchAI_Data/Paper/MinerU_logs")
NORMALIZE_SCRIPT = Path(__file__).parent / "normalize_mineru_output.py"
MINERU_BIN = "/home/lco/miniconda3/envs/mineru/bin/mineru"


def log_message(msg, logger=None):
    """Print and optionally log a message."""
    print(msg)
    if logger:
        logger.write(msg + "\n")


def resolve_paper_key(conn, item_key):
    """
    Given an Item Key (paper or attachment), resolve to paper key and attachment info.
    
    Returns: (paper_key, att_key, storage_path, title)
    """
    cur = conn.cursor()
    
    # Get the item's type
    cur.execute("SELECT itemTypeID FROM items WHERE key = ?", (item_key,))
    row = cur.fetchone()
    if not row:
        return None, None, None, None
    
    item_type_id = row[0]
    
    if item_type_id == 3:
        # It's an attachment - find its parent paper
        cur.execute("""
            SELECT pa.key, ia.path
            FROM items pa
            JOIN itemAttachments ia ON pa.itemID = ia.parentItemID
            WHERE ia.itemID = (SELECT itemID FROM items WHERE key = ?)
            LIMIT 1
        """, (item_key,))
        paper_row = cur.fetchone()
        if paper_row:
            return paper_row[0], item_key, paper_row[1], None
        return None, None, None, None
    else:
        # It's a paper item - find its attachment
        cur.execute("""
            SELECT att.key, ia.path
            FROM itemAttachments ia
            JOIN items att ON ia.itemID = att.itemID
            WHERE ia.parentItemID = (SELECT itemID FROM items WHERE key = ?)
            AND ia.path LIKE 'storage:%'
            LIMIT 1
        """, (item_key,))
        attach_row = cur.fetchone()
        if attach_row:
            return item_key, attach_row[0], attach_row[1], None
        return None, None, None, None


def get_title_from_db(conn, paper_key):
    """Get the paper title from Zotero itemData."""
    cur = conn.cursor()
    cur.execute("""
        SELECT dv.value
        FROM itemData idata
        JOIN items i ON idata.itemID = i.itemID
        JOIN fields f ON idata.fieldID = f.fieldID
        JOIN itemDataValues dv ON idata.valueID = dv.valueID
        WHERE i.key = ? AND f.fieldName = 'title'
        LIMIT 1
    """, (paper_key,))
    row = cur.fetchone()
    return row[0] if row else None


def query_zotero_pdf(item_key):
    """
    Query Zotero SQLite for the PDF attachment of a paper.
    
    Handles both paper keys and attachment keys.
    PDFs are stored under: storage/{attachment_key}/{pdf_filename}
    """
    conn = sqlite3.connect(str(ZOTERO_DB))
    
    # Resolve paper key and attachment info
    paper_key, att_key, storage_path, _ = resolve_paper_key(conn, item_key)
    
    if not paper_key or not storage_path:
        conn.close()
        return None, None, None, f"Item key {item_key} not found or has no PDF attachment"
    
    # Get title
    title = get_title_from_db(conn, paper_key)
    
    # Extract PDF filename from storage:path
    pdf_filename = storage_path.split(":", 1)[1] if ":" in storage_path else storage_path
    pdf_path = ZOTERO_STORAGE / att_key / pdf_filename
    
    conn.close()
    return pdf_path, title, att_key, None


def check_existing_output(item_key, title):
    """Check if MinerU output already exists for this paper."""
    for d in MINERU_MD.iterdir():
        if not d.is_dir():
            continue
        name_lower = d.name.lower()
        key_lower = item_key.lower()
        
        # Match by item key in folder name
        if key_lower in name_lower:
            full_md = d / "full.md"
            if full_md.exists():
                return d, True
            # Check for unnormalized output
            if (d / "txt").exists() or (d / "hybrid_auto").exists():
                return d, False

    return None, False


def run_mineru_cli(pdf_path, output_dir):
    """Run MinerU CLI on a PDF file."""
    cmd = [
        MINERU_BIN,
        "-p", str(pdf_path),
        "-o", str(output_dir),
        "-b", "pipeline",
        "-m", "txt",
        "-l", "ch",
        "--formula", "true",
        "--table", "true",
    ]

    # Strip proxy env vars
    env = os.environ.copy()
    for var in ["http_proxy", "https_proxy", "ALL_PROXY", "all_proxy",
                "HTTP_PROXY", "HTTPS_PROXY", "NO_PROXY"]:
        env.pop(var, None)

    result = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=600)

    if result.returncode != 0:
        return False, result.stderr

    return True, result.stdout


def run_normalization(output_dir):
    """Run the normalization layer on MinerU output."""
    cmd = [sys.executable, str(NORMALIZE_SCRIPT), str(output_dir)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0, result.stdout + result.stderr


def main():
    if len(sys.argv) < 2:
        print("Usage: python process_paper.py <Zotero_Item_Key>")
        print("Example: python process_paper.py 9W23DNVG")
        print("  (Item Key can be paper key OR attachment key)")
        sys.exit(1)

    item_key = sys.argv[1]
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    log_file = MINERU_LOGS / f"{timestamp}.log"

    # Ensure log directory exists
    MINERU_LOGS.mkdir(parents=True, exist_ok=True)

    logger = open(str(log_file), "w", encoding="utf-8")

    try:
        log_message(f"\n{'='*60}", logger)
        log_message(f"MinerU Paper Processor - {item_key}", logger)
        log_message(f"{'='*60}", logger)
        log_message(f"Start time: {datetime.now().isoformat()}", logger)

        # Step 1: Query Zotero for PDF
        log_message("\n[1/5] Querying Zotero...", logger)
        pdf_path, title, att_key, error = query_zotero_pdf(item_key)
        if error:
            log_message(f"  ERROR: {error}", logger)
            logger.flush()
            return 1
        log_message(f"  PDF: {pdf_path}", logger)
        log_message(f"  Title: {title}", logger)
        log_message(f"  Attachment key: {att_key}", logger)

        # Step 2: Check existing output
        log_message("\n[2/5] Checking existing output...", logger)
        output_dir, already_processed = check_existing_output(item_key, title)
        if already_processed:
            log_message(f"  SKIP: Already processed at {output_dir}", logger)
            log_message(f"  full.md exists - no action needed.", logger)
            logger.flush()
            return 0
        if output_dir:
            log_message(f"  Output exists but not normalized: {output_dir}", logger)
            log_message(f"  Running normalization...", logger)
            success, msg = run_normalization(output_dir)
            if success:
                log_message(f"  Normalization complete.", logger)
                log_message(f"  Done.", logger)
                logger.flush()
                return 0
            else:
                log_message(f"  Normalization failed: {msg}", logger)
                logger.flush()
                return 1

        # Step 3: Create output directory
        log_message("\n[3/5] Creating output directory...", logger)
        safe_title = (title or item_key).replace("/", "_").replace("\\", "_")
        output_dir = MINERU_MD / f"{safe_title}-{item_key}"
        output_dir.mkdir(parents=True, exist_ok=True)
        log_message(f"  Output dir: {output_dir}", logger)

        # Step 4: Run MinerU CLI
        log_message("\n[4/5] Running MinerU CLI...", logger)
        success, output = run_mineru_cli(pdf_path, output_dir)
        if not success:
            log_message(f"  ERROR: MinerU CLI failed:\n{output}", logger)
            logger.flush()
            return 1
        log_message(f"  MinerU CLI completed successfully.", logger)

        # Step 5: Run normalization
        log_message("\n[5/5] Running normalization layer...", logger)
        success, msg = run_normalization(output_dir)
        if not success:
            log_message(f"  ERROR: Normalization failed:\n{msg}", logger)
            logger.flush()
            return 1

        # Verify full.md exists
        full_md = output_dir / "full.md"
        if full_md.exists():
            size = full_md.stat().st_size
            log_message(f"  OK full.md created ({size} bytes)", logger)
        else:
            log_message(f"  FAIL full.md NOT found after normalization!", logger)
            logger.flush()
            return 1

        log_message(f"\nDone. Output: {full_md}", logger)
        log_message(f"End time: {datetime.now().isoformat()}", logger)

        # Write to log
        logger.flush()
        return 0

    except Exception as e:
        log_message(f"\nFATAL ERROR: {e}", logger)
        logger.flush()
        return 1
    finally:
        logger.close()


if __name__ == "__main__":
    sys.exit(main())
