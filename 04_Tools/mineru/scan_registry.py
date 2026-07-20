#!/usr/bin/env python3
"""
Paper Processing Registry Scanner

Scans Zotero DB + MinerU_md + KnowledgeVault to generate
Paper_Processing_State.yaml — the single source of truth for paper processing state.

Usage:
    python scan_registry.py              # Generate/overwrite registry
    python scan_registry.py --report     # Print summary only, no file write
    python scan_registry.py --filter MINERU_PENDING  # List papers in specific state
"""

import os
import sys
import sqlite3
import argparse
import re
from pathlib import Path
from datetime import datetime

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

# Configuration
ZOTERO_DB = Path("/home/lco/ResearchAI_Data/Zotero/zotero.sqlite")
MINERU_MD = Path("/home/lco/ResearchAI_Data/Paper/MinerU_md")
KV_PAPERS_DIR = Path("/home/lco/ResearchAI/02_KnowledgeVault/01_Papers")
REGISTRY_PATH = Path("/home/lco/ResearchAI/08_Agent_Config/Paper_Processing_State.yaml")

# Agent state field definitions
AGENT_STATE_FIELDS = ['literature_card', 'deep_read', 'method_extraction', 'obsidian_note']
AGENT_STATE_VALUES = ['PENDING', 'IN_PROGRESS', 'COMPLETE']

VALID_TYPES = {'journalArticle', 'conferencePaper', 'thesis', 'report', 'bookSection', 'preprint'}


def _strip_bom(text):
    """Remove UTF-8 BOM if present."""
    if text.startswith('\ufeff'):
        return text[1:]
    return text


def extract_title_from_kv_file(filepath):
    """Extract paper title from a KnowledgeVault file.

    Tries YAML frontmatter first (handles BOM), falls back to # Title: line.
    Returns the title string or None.
    """
    try:
        raw = filepath.read_text(encoding='utf-8')
    except Exception:
        return None

    # Strip BOM before parsing
    text = _strip_bom(raw)

    # Try YAML frontmatter: title: "..." or title: '...'
    fm_match = re.search(r'^---\s*\ntitle:\s*"([^"]+)"', text, re.MULTILINE)
    if fm_match:
        return fm_match.group(1)
    fm_match2 = re.search(r"^---\s*\ntitle:\s*'([^']+)'", text, re.MULTILINE)
    if fm_match2:
        return fm_match2.group(1)

    # Fallback: # Title: ...
    hash_match = re.search(r'^#\s*Title:\s*(.+)$', text, re.MULTILINE)
    if hash_match:
        return hash_match.group(1).strip()

    return None


def scan_knowledgevault():
    """Scan KnowledgeVault papers directory and return file-to-title mappings.

    Returns dict keyed by filename stem prefix (e.g., lv2026_dttp).
    Each entry has note_type, agent_field, title, filename.
    """
    if not KV_PAPERS_DIR.exists():
        return {}

    result = {}
    for f in KV_PAPERS_DIR.iterdir():
        if not f.is_file() or f.name == 'README.md':
            continue
        fname = f.stem  # e.g., lv2026_dttp_card
        # Extract type suffix
        type_match = re.match(r'^(.+?)_(card|note|method|logic|survey)$', fname, re.IGNORECASE)
        if not type_match:
            continue

        prefix = type_match.group(1)  # e.g., lv2026_dttp
        note_type = type_match.group(2).lower()  # card, note, method, logic, survey

        title = extract_title_from_kv_file(f)

        # Map note_type to agent_state field
        field_map = {
            'card': 'literature_card',
            'note': 'deep_read',
            'method': 'method_extraction',
            'logic': 'obsidian_note',
            'survey': 'literature_card'  # surveys are treated as completed cards
        }
        agent_field = field_map.get(note_type)

        result[prefix] = {
            'note_type': note_type,
            'agent_field': agent_field,
            'title': title,
            'filename': f.name
        }

    return result


def _clean_title(t):
    """Normalize a title for comparison: lowercase, strip punctuation, collapse spaces."""
    c = re.sub(r'[^\w\s]', '', t.lower()).strip()
    return re.sub(r'\s+', ' ', c)


def _find_best_match(kv_title, zotero_index):
    """Find the best Zotero paper_key matching a KV file title.

    Uses a scoring approach:
    1. Exact match on cleaned title
    2. Substring match (either direction)
    3. Keyword overlap scored by ratio (overlap / max(word_counts))
    """
    kv_clean = _clean_title(kv_title)
    kv_words = set(w for w in kv_clean.split() if len(w) > 3)

    best_pk = None
    best_score = 0

    for zc_title, pk in zotero_index.items():
        # Strategy 1: exact match
        if zc_title == kv_clean:
            return pk

        # Strategy 2: substring match
        if kv_clean in zc_title or zc_title in kv_clean:
            return pk

        # Strategy 3: keyword overlap with scoring
        if not kv_words:
            continue
        zc_words = set(w for w in zc_title.split() if len(w) > 3)
        overlap = kv_words & zc_words
        if len(overlap) < 3:
            continue

        # Score: overlap ratio — how well does this Zotero title explain the KV title?
        # Higher ratio = better match
        denom = max(len(kv_words), len(zc_words), 1)
        score = len(overlap) / denom

        if score > best_score:
            best_score = score
            best_pk = pk

    return best_pk


def build_kv_to_paper_mapping(kv_files, zotero_papers):
    """
    Build a mapping from Zotero paper_key -> dict of agent_state fields -> status.
    Matches KV files to Zotero papers by title comparison.
    """
    # Index Zotero papers by cleaned title
    zotero_index = {}
    for pk, zp in zotero_papers.items():
        title = zp.get('title', '').strip()
        clean_title = _clean_title(title)
        zotero_index[clean_title] = pk

    # Map: paper_key -> dict of agent_state fields
    paper_agent_state = {}

    for kv_prefix, kv_info in kv_files.items():
        kv_title = kv_info.get('title', '')
        if not kv_title:
            continue

        matched_pk = _find_best_match(kv_title, zotero_index)

        if matched_pk:
            if matched_pk not in paper_agent_state:
                paper_agent_state[matched_pk] = {}
            agent_field = kv_info.get('agent_field')
            if agent_field:
                paper_agent_state[matched_pk][agent_field] = 'COMPLETE'

    return paper_agent_state


def scan_zotero():
    """Scan Zotero database for all papers with PDF attachments."""
    if not ZOTERO_DB.exists():
        print(f"ERROR: Zotero DB not found: {ZOTERO_DB}")
        return {}

    conn = sqlite3.connect(str(ZOTERO_DB))
    cur = conn.cursor()

    cur.execute("""
        SELECT DISTINCT
            pa.key as paper_key,
            att.key as att_key,
            it.typeName,
            ia.path as storage_path,
            pa.dateAdded,
            dv.title_value
        FROM items pa
        JOIN itemTypes it ON pa.itemTypeID = it.rowID
        JOIN itemAttachments ia ON pa.itemID = ia.parentItemID
        JOIN items att ON ia.itemID = att.itemID
        LEFT JOIN (
            SELECT idata.itemID, dv.value as title_value
            FROM itemData idata
            JOIN fields f ON idata.fieldID = f.fieldID
            JOIN itemDataValues dv ON idata.valueID = dv.valueID
            WHERE f.fieldName = 'title'
        ) dv ON dv.itemID = pa.itemID
        WHERE it.typeName IN ('journalArticle', 'conferencePaper', 'thesis',
                              'report', 'bookSection', 'preprint')
        AND ia.path LIKE 'storage:%'
        ORDER BY pa.dateAdded DESC
    """)

    papers = {}
    for row in cur.fetchall():
        paper_key, att_key, paper_type, storage_path, date_added, title = row
        pdf_filename = storage_path.split(':', 1)[1] if ':' in storage_path else storage_path
        pdf_path = Path("/home/lco/ResearchAI_Data/Zotero/storage") / att_key / pdf_filename

        papers[paper_key] = {
            'paper_key': paper_key,
            'att_key': att_key,
            'type': paper_type,
            'date_added': date_added,
            'title': title or 'Unknown',
            'pdf_filename': pdf_filename,
            'pdf_path': str(pdf_path),
            'pdf_exists': pdf_path.exists()
        }

    conn.close()
    return papers


def scan_mineru():
    """Scan MinerU output directories."""
    if not MINERU_MD.exists():
        return {}

    result = {}
    for d in MINERU_MD.iterdir():
        if not d.is_dir():
            continue
        full_md = d / 'full.md'
        has_full = full_md.exists()
        images_dir = d / 'images'
        has_images = images_dir.is_dir()
        img_count = len([f for f in images_dir.iterdir() if f.is_file()]) if has_images else 0
        size = full_md.stat().st_size if has_full else 0

        result[d.name] = {
            'folder': d.name,
            'has_full': has_full,
            'has_images': has_images,
            'img_count': img_count,
            'size': size
        }
    return result


def cross_reference(zotero_papers, mineru_folders):
    """Match Zotero papers to MinerU folders and determine state."""
    state_map = []

    for pk, zp in sorted(zotero_papers.items()):
        att_key = zp['att_key']
        pdf_fn = zp['pdf_filename'].replace('.pdf', '').lower()

        matched_folder = None
        for mname in mineru_folders:
            mname_lower = mname.lower()
            if (att_key in mname_lower or
                pdf_fn in mname_lower or
                mname_lower in pdf_fn or
                pk.lower() in mname_lower):
                matched_folder = mname
                break

        if matched_folder:
            minfo = mineru_folders[matched_folder]
            if minfo['has_full'] and minfo['has_images']:
                state = 'MINERU_COMPLETE'
            elif minfo['has_full']:
                state = 'MINERU_PARTIAL'
            else:
                state = 'MINERU_PENDING'
        else:
            state = 'MINERU_PENDING'

        state_map.append({
            'paper_key': pk,
            'att_key': att_key,
            'title': zp['title'],
            'type': zp['type'],
            'date_added': zp['date_added'],
            'pdf_exists': zp['pdf_exists'],
            'mineru_folder': matched_folder,
            'mineru_state': state
        })

    return state_map


def assign_agent_state(state_map, paper_agent_state):
    """Add agent_state fields to each paper entry based on KnowledgeVault scan."""
    for entry in state_map:
        pk = entry['paper_key']
        if pk in paper_agent_state:
            agent_fields = {}
            for field in AGENT_STATE_FIELDS:
                agent_fields[field] = paper_agent_state[pk].get(field, 'PENDING')
            entry['agent_state'] = agent_fields
        else:
            # Default: all PENDING
            entry['agent_state'] = {field: 'PENDING' for field in AGENT_STATE_FIELDS}

    return state_map


def compute_agent_summary(state_map):
    """Compute summary counts for agent_state fields."""
    summary = {}
    for field in AGENT_STATE_FIELDS:
        counts = {val: 0 for val in AGENT_STATE_VALUES}
        for p in state_map:
            as_state = p.get('agent_state', {})
            val = as_state.get(field, 'PENDING')
            if val in counts:
                counts[val] += 1
        summary[field] = counts
    return summary


def generate_registry():
    """Generate the full Paper_Processing_State.yaml."""
    zotero_papers = scan_zotero()
    mineru_folders = scan_mineru()
    state_map = cross_reference(zotero_papers, mineru_folders)

    # Scan KnowledgeVault for existing agent state
    kv_files = scan_knowledgevault()
    paper_agent_state = build_kv_to_paper_mapping(kv_files, zotero_papers)

    # Assign agent_state to each paper entry
    state_map = assign_agent_state(state_map, paper_agent_state)

    output = {
        'registry': {
            'version': '1.0',
            'generated': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            'source': 'scan_registry.py automated scan',
            'zotero_db': str(ZOTERO_DB),
            'mineru_md': str(MINERU_MD),
            'knowledgevault_dir': str(KV_PAPERS_DIR)
        },
        'summary': {
            'total_zotero_papers': len(zotero_papers),
            'pdfs_available': sum(1 for p in state_map if p['pdf_exists']),
            'mineru_complete': sum(1 for p in state_map if p['mineru_state'] == 'MINERU_COMPLETE'),
            'mineru_partial': sum(1 for p in state_map if p['mineru_state'] == 'MINERU_PARTIAL'),
            'mineru_pending': sum(1 for p in state_map if p['mineru_state'] == 'MINERU_PENDING'),
            'agent_state': compute_agent_summary(state_map)
        },
        'papers': state_map
    }

    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_PATH.write_text(
        yaml.dump(output, default_flow_style=False, allow_unicode=True, sort_keys=False),
        encoding='utf-8'
    )

    return output


def print_summary(data):
    """Print a human-readable summary."""
    s = data['summary']
    print(f"\n{'='*60}")
    print(f"Paper Processing Registry — Summary")
    print(f"{'='*60}")
    print(f"Generated: {data['registry']['generated']}")
    print(f"Total Zotero papers: {s['total_zotero_papers']}")
    print(f"PDFs available: {s['pdfs_available']}")
    print(f"MinerU complete: {s['mineru_complete']}")
    print(f"MinerU partial: {s['mineru_partial']}")
    print(f"MinerU pending: {s['mineru_pending']}")
    print(f"{'='*60}")

    # Print agent state summary
    agent_s = s.get('agent_state', {})
    if agent_s:
        print(f"\nAgent State Summary:")
        for field, counts in agent_s.items():
            total = sum(counts.values())
            complete = counts.get('COMPLETE', 0)
            print(f"  {field}: {complete}/{total} COMPLETE, "
                  f"{counts.get('IN_PROGRESS', 0)} IN_PROGRESS, "
                  f"{counts.get('PENDING', 0)} PENDING")

    pending = [p for p in data['papers'] if p['mineru_state'] == 'MINERU_PENDING']
    if pending:
        print(f"\nPapers needing MinerU processing ({len(pending)}):")
        for p in pending:
            print(f"  {p['paper_key']} | {p['title'][:60]} | pdf={'Yes' if p['pdf_exists'] else 'No'}")


def print_filter(data, state_filter):
    """Print papers matching a specific state."""
    filtered = [p for p in data['papers'] if p['mineru_state'] == state_filter]
    print(f"\nPapers with state '{state_filter}' ({len(filtered)}):")
    for p in filtered:
        folder = p['mineru_folder'][:60] + '...' if p['mineru_folder'] else 'N/A'
        print(f"  {p['paper_key']} | {p['title'][:50]} | {folder}")


def main():
    parser = argparse.ArgumentParser(description="Paper Processing Registry Scanner")
    parser.add_argument('--report', action='store_true', help='Print summary only')
    parser.add_argument('--filter', type=str, default=None,
                        help='Filter by state: MINERU_COMPLETE, MINERU_PARTIAL, MINERU_PENDING')
    args = parser.parse_args()

    data = generate_registry()

    if args.filter:
        print_filter(data, args.filter)
    elif args.report:
        print_summary(data)
    else:
        print_summary(data)
        print(f"\nRegistry saved to: {REGISTRY_PATH}")


if __name__ == "__main__":
    main()
