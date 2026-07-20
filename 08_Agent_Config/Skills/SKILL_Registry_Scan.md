# SKILL_Registry_Scan

## Purpose
Scan Zotero DB + MinerU output + KnowledgeVault to generate/update Paper_Processing_State.yaml.

## When to Use
- Before any batch processing to identify pending papers
- After batch processing to update state
- On demand when agent needs to know current paper processing status
- Before creating KnowledgeVault notes to avoid duplicates

## Prerequisites
- pyyaml installed: `pip install pyyaml`
- Access to Zotero DB: `/home/lco/ResearchAI_Data/Zotero/zotero.sqlite`
- Access to MinerU MD: `/home/lco/ResearchAI_Data/Paper/MinerU_md/`
- Writable to: `/home/lco/ResearchAI/08_Agent_Config/Paper_Processing_State.yaml`

## Execution

```bash
# Full scan and overwrite registry
python 04_Tools/mineru/scan_registry.py

# Summary only (no file write)
python 04_Tools/mineru/scan_registry.py --report

# Filter by state
python 04_Tools/mineru/scan_registry.py --filter MINERU_PENDING
python 04_Tools/mineru/scan_registry.py --filter MINERU_COMPLETE

# List papers missing PDFs
python 04_Tools/mineru/scan_registry.py --filter MINERU_PENDING
```

## Output Format
Generates YAML with:
- `registry.meta`: version, timestamp, source
- `summary`: counts by state
- `papers[]`: array of paper objects with `paper_key`, `att_key`, `title`, `type`, `date_added`, `pdf_exists`, `mineru_folder`, `mineru_state`

## States
- `MINERU_COMPLETE` — full.md + images/ exist
- `MINERU_PARTIAL` — full.md exists but missing images/
- `MINERU_PENDING` — no MinerU output folder found

## Agent Workflow Integration

### Before Batch Processing
```
1. Run: python 04_Tools/mineru/scan_registry.py --filter MINERU_PENDING
2. Filter results: pdf_exists == true AND mineru_state == MINERU_PENDING
3. These are the papers ready for batch processing
```

### After Batch Processing
```
1. Run: python 04_Tools/mineru/scan_registry.py
2. Verify: mineru_complete count increased by processed count
3. Check: no new MINERU_PENDING with pdf_exists==true
```

### Before KnowledgeVault Creation
```
1. Load Paper_Processing_State.yaml
2. Find paper by key or title
3. Verify mineru_state == MINERU_COMPLETE before creating KV notes
4. Prevent duplicate KV creation by checking 02_KnowledgeVault/01_Papers/
```

## Safety
- Read-only scan of Zotero DB (no modifications)
- Read-only scan of MinerU_md (no modifications)
- Overwrites only the registry YAML file
- Does NOT touch existing papers, templates, or notes

## Dependencies
- Python 3.10+
- pyyaml
- sqlite3 (stdlib)
