#!/usr/bin/env python3
"""
Batch MinerU processor for Zotero papers.

Queries Zotero database for papers needing processing, then runs
MinerU CLI + normalization on each.

Usage:
    python batch_process.py              # Dry run (default)
    python batch_process.py --execute    # Actually process papers
    python batch_process.py --key 9W23DNVG  # Process single key

Architecture:
    Zotero zotero.sqlite -> paper list -> MinerU CLI -> normalize -> full.md
"""

import os
import sys
import argparse
import sqlite3
import subprocess
from pathlib import Path
from datetime import datetime

# Configuration
ZOTERO_DB = Path("/home/lco/ResearchAI_Data/Zotero/zotero.sqlite")
MINERU_MD = Path("/home/lco/ResearchAI_Data/Paper/MinerU_md")
MINERU_LOGS = Path("/tmp/ResearchAI_Paper/MinerU_logs")
NORMALIZE_SCRIPT = Path(__file__).parent / "normalize_mineru_output.py"
MINERU_BIN = "/home/lco/miniconda3/envs/mineru/bin/mineru"


def get_zotero_papers():
    """Query Zotero for all papers with PDF attachments."""
    conn = sqlite3.connect(str(ZOTERO_DB))
    cur = conn.cursor()

    cur.execute("""
        SELECT pa.key as paper_key, att.key as att_key,
               it.typeName, ia.path, pa.dateAdded
        FROM items pa
        JOIN itemTypes it ON pa.itemTypeID = it.rowID
        JOIN itemAttachments ia ON pa.itemID = ia.parentItemID
        JOIN items att ON ia.itemID = att.itemID
        WHERE it.typeName IN ('journalArticle', 'conferencePaper', 'thesis',
                              'report', 'bookSection', 'preprint')
        AND ia.path LIKE 'storage:%'
        ORDER BY pa.dateAdded DESC
    """)

    papers = []
    seen_keys = set()
    for row in cur.fetchall():
        paper_key, att_key, paper_type, storage_path, date_added = row
        if paper_key in seen_keys:
            continue
        seen_keys.add(paper_key)

        pdf_filename = storage_path.split(":", 1)[1] if ":" in storage_path else storage_path
        pdf_path = Path("/home/lco/ResearchAI_Data/Zotero/storage") / att_key / pdf_filename

        if pdf_path.exists():
            papers.append({
                "key": paper_key,
                "att_key": att_key,
                "type": paper_type,
                "date_added": date_added,
                "pdf_path": str(pdf_path),
                "pdf_filename": pdf_filename,
            })

    conn.close()
    return papers


def check_already_processed(item_key, pdf_filename):
    """
    Check if MinerU output already exists for this paper.
    Matches by BOTH paper key AND PDF filename for robustness.
    """
    key_lower = item_key.lower()
    base_name = pdf_filename.replace(".pdf", "").lower()
    
    for d in MINERU_MD.iterdir():
        if not d.is_dir():
            continue
        
        folder_lower = d.name.lower()
        
        # Match by paper key in folder name
        if key_lower in folder_lower:
            full_md = d / "full.md"
            if full_md.exists():
                return True, d
            if (d / "txt").exists() or (d / "hybrid_auto").exists():
                return False, d
        
        # Match by PDF filename in folder name
        if base_name in folder_lower or folder_lower in base_name:
            full_md = d / "full.md"
            if full_md.exists():
                return True, d
            if (d / "txt").exists() or (d / "hybrid_auto").exists():
                return False, d

    return False, None


def run_mineru_on_paper(paper_info, dry_run=False):
    """Run MinerU CLI + normalization on a single paper."""
    item_key = paper_info["key"]
    pdf_path = paper_info["pdf_path"]
    pdf_filename = paper_info["pdf_filename"]

    safe_title = pdf_filename.replace(".pdf", "").replace("/", "_").replace("\\", "_")
    output_dir = MINERU_MD / f"{safe_title}-{item_key}"

    log_entry = {
        "key": item_key,
        "pdf": pdf_path,
        "start": datetime.now().isoformat(),
        "status": "",
        "error": "",
    }

    if dry_run:
        log_entry["status"] = "DRY_RUN"
        return log_entry

    # Run MinerU CLI (hybrid-engine backend for GPU acceleration)
    cmd = [
        MINERU_BIN, "-p", pdf_path, "-o", str(output_dir),
        "-b", "hybrid-engine", "--effort", "medium",
    ]
    env = os.environ.copy()
    for var in ["http_proxy", "https_proxy", "ALL_PROXY", "all_proxy",
                "HTTP_PROXY", "HTTPS_PROXY", "NO_PROXY"]:
        env.pop(var, None)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=600)
        if result.returncode != 0:
            log_entry["status"] = "FAILED"
            log_entry["error"] = f"MinerU exit {result.returncode}: {result.stderr[:200]}"
            return log_entry
    except subprocess.TimeoutExpired:
        log_entry["status"] = "TIMEOUT"
        log_entry["error"] = "MinerU exceeded 600s timeout"
        return log_entry
    except Exception as e:
        log_entry["status"] = "FAILED"
        log_entry["error"] = str(e)
        return log_entry

    # Run normalization
    norm_cmd = [sys.executable, str(NORMALIZE_SCRIPT), str(output_dir)]
    norm_result = subprocess.run(norm_cmd, capture_output=True, text=True)
    if norm_result.returncode != 0:
        log_entry["status"] = "NORMALIZATION_FAILED"
        log_entry["error"] = norm_result.stderr[:200]
        return log_entry

    # Verify
    full_md = output_dir / "full.md"
    if full_md.exists():
        log_entry["status"] = "SUCCESS"
    else:
        log_entry["status"] = "FAILED"
        log_entry["error"] = "full.md not found after normalization"

    log_entry["end"] = datetime.now().isoformat()
    return log_entry


def main():
    parser = argparse.ArgumentParser(description="Batch MinerU processor")
    parser.add_argument("--execute", action="store_true",
                        help="Actually process papers (default: dry run)")
    parser.add_argument("--key", type=str,
                        help="Process a single Zotero item key")
    args = parser.parse_args()

    dry_run = not args.execute

    # Single key mode
    if args.key:
        papers = [{"key": args.key}]
        conn = sqlite3.connect(str(ZOTERO_DB))
        cur = conn.cursor()
        cur.execute("""
            SELECT pa.key as paper_key, att.key as att_key,
                   it.typeName, ia.path
            FROM items pa
            JOIN itemTypes it ON pa.itemTypeID = it.rowID
            JOIN itemAttachments ia ON pa.itemID = ia.parentItemID
            JOIN items att ON ia.itemID = att.itemID
            WHERE pa.key = ?
            LIMIT 1
        """, (args.key,))
        row = cur.fetchone()
        if row:
            paper_key, att_key, paper_type, storage_path = row
            pdf_filename = storage_path.split(":", 1)[1] if ":" in storage_path else storage_path
            pdf_path = Path("/home/lco/ResearchAI_Data/Zotero/storage") / att_key / pdf_filename
            papers[0]["pdf_path"] = str(pdf_path)
            papers[0]["pdf_filename"] = pdf_filename
            papers[0]["type"] = paper_type
        conn.close()
    else:
        papers = get_zotero_papers()

    # Categorize papers
    to_process = []
    to_skip = []

    for paper in papers:
        item_key = paper["key"]
        pdf_filename = paper["pdf_filename"]
        exists, output_dir = check_already_processed(item_key, pdf_filename)
        if exists:
            to_skip.append({"key": item_key, "dir": str(output_dir)})
        elif output_dir:
            to_process.append({**paper, "needs_normalization_only": True, "existing_dir": output_dir})
        else:
            to_process.append(paper)

    # Print results
    print(f"\n{'='*60}")
    print(f"MinerU Batch Processor")
    print(f"{'='*60}")
    print(f"Mode: {'DRY RUN' if dry_run else 'EXECUTE'}")
    print(f"Total papers in Zotero: {len(papers)}")
    print(f"Papers to process: {len(to_process)}")
    print(f"Papers already processed: {len(to_skip)}")
    print(f"{'='*60}")

    if to_skip:
        print("\nSKIP (already processed):")
        for p in to_skip:
            print(f"  {p['key']} -> {p['dir']}")

    if to_process:
        print(f"\nPROCESS ({len(to_process)} papers):")
        for p in to_process:
            if p.get("needs_normalization_only"):
                print(f"  [NORMALIZE] {p['key']} -> {p['existing_dir']}")
            else:
                status = "RUNNING" if not dry_run else "WOULD RUN"
                print(f"  [{status}] {p['key']}")

    # Execute if not dry run
    if not dry_run and to_process:
        print("\n" + "="*60)
        print("Executing...")
        print("="*60)

        logs_dir = MINERU_LOGS
        logs_dir.mkdir(parents=True, exist_ok=True)
        log_file = logs_dir / f"{datetime.now().strftime('%Y-%m-%d')}_batch.log"

        with open(str(log_file), "w", encoding="utf-8") as lf:
            lf.write(f"Batch run: {datetime.now().isoformat()}\n")
            lf.write(f"Papers to process: {len(to_process)}\n\n")

            for i, paper in enumerate(to_process, 1):
                if paper.get("needs_normalization_only"):
                    print(f"\n[{i}/{len(to_process)}] Normalizing {paper['key']}...")
                    norm_cmd = [sys.executable, str(NORMALIZE_SCRIPT), str(paper['existing_dir'])]
                    result = subprocess.run(norm_cmd, capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"  Status: SUCCESS")
                        lf.write(f"{paper['key']}: SUCCESS (normalization)\n")
                    else:
                        print(f"  Status: FAILED - {result.stderr[:100]}")
                        lf.write(f"{paper['key']}: FAILED\n")
                else:
                    print(f"\n[{i}/{len(to_process)}] Processing {paper['key']}...")
                    result = run_mineru_on_paper(paper, dry_run=False)
                    print(f"  Status: {result['status']}")
                    if result.get("error"):
                        print(f"  Error: {result['error'][:100]}")
                    lf.write(f"{result['key']}: {result['status']}\n")
                    if result.get("error"):
                        lf.write(f"  Error: {result['error']}\n")

        print(f"\nLog written to: {log_file}")

    print(f"\n{'='*60}")
    if dry_run:
        print("Dry run complete. Use --execute to process papers.")
    else:
        print("Batch processing complete.")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
