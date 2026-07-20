# MinerU Processing Tools

Linux-native MinerU CLI pipeline for ResearchAI paper processing.

## Architecture

```
Zotero storage/{att_key}/{pdf}.pdf
    → MinerU CLI (pipeline + txt)
    → normalize_mineru_output.py
    → MinerU_md/{paper}/full.md
    → Agent Literature Processing
```

## Scripts

### process_paper.py — Single Paper Processing

Process one Zotero paper through MinerU CLI + normalization.

```bash
python process_paper.py <Zotero_Item_Key>
```

Example:
```bash
python process_paper.py 9W23DNVG
```

The Item Key can be EITHER a paper key or an attachment key — the script resolves both.

Steps:
1. Query Zotero storage for PDF
2. Check if output already exists (skip if yes)
3. Run MinerU CLI (`pipeline` backend, `txt` method)
4. Run normalization layer (converts to `full.md` format)
5. Verify `full.md` exists
6. Log results

### batch_process.py — Batch Processing

Query Zotero for all papers and process them in batch.

```bash
python batch_process.py              # Dry run (default)
python batch_process.py --execute    # Actually process
python batch_process.py --key 9W23DNVG  # Single key with execute
```

**Default behavior is DRY RUN.** Use `--execute` to actually process papers.

### normalize_mineru_output.py — Normalization Layer

Converts MinerU output variants into stable `full.md` format.

```bash
python normalize_mineru_output.py <folder>
```

Supported cases:
- **Case A**: `full.md` already exists → skip
- **Case B**: `hybrid_auto/*.md` → copy to `full.md`
- **Case C**: `txt/*.md` (CLI output) → copy to `full.md`
- **Case D**: Single `.md` → copy to `full.md`

### validate_mineru_output.py — Output Validation

Check whether MinerU folders are Agent-compatible.

```bash
python validate_mineru_output.py              # Validate all
python validate_mineru_output.py <folder>     # Validate single
python validate_mineru_output.py --report     # Save report to file
```

Checks:
- `full.md` exists
- `images/` directory exists
- All markdown image references resolve

## Agent Integration

MinerU output is **not directly consumed** by agents. The required sequence is:

1. `process_paper.py` — runs MinerU CLI on a Zotero paper
2. `normalize_mineru_output.py` — converts output to stable format
3. `validate_mineru_output.py` — verifies Agent compatibility
4. Agent literature skills consume `full.md`

**`full.md` is the stable interface contract.** Agents must assume:
- Input: `/home/lco/ResearchAI_Data/Paper/MinerU_md/{paper_folder}/full.md`
- Images: `images/` directory at the folder root
- Do NOT directly read `txt/*.md` or `hybrid_auto/*.md` — normalization handles this

The Agent must NOT call MinerU itself. The Agent only consumes normalized output.

## Environment

- Conda env: `mineru`
- MinerU CLI: 3.4.4
- Backend: `pipeline` + `txt` method
- Proxy vars stripped automatically

## Logging

Logs written to: `/home/lco/ResearchAI_Data/Paper/MinerU_logs/`
Format: `YYYY-MM-DD_batch.log` or `YYYY-MM-DD_HHMMSS.log`

## Output Structure

```
/home/lco/ResearchAI_Data/Paper/MinerU_md/{paper}-{key}/
├── full.md              ← Agent-readable markdown
├── images/
│   └── *.jpg
└── .normalization.log   ← Normalization history
```
