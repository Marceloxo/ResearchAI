---
title: "Stage 5.2 — MinerU Production Pipeline Report"
created: "2026-07-17"
---
# Stage 5.2: MinerU Production Pipeline Report

**Date:** 2026-07-17
**Predecessor:** Stage 5.1 CLI Test (PASS)
**Scope:** Build production MinerU CLI processing pipeline

---

## 1. Architecture

```
Zotero
  |
  | PDF attachment (storage/{att_key}/{pdf})
  v
Zotero storage/{ItemKey}/
  |
  v
MinerU CLI 3.4.4 (pipeline + txt)
  |
  v
Normalization Layer (normalize_mineru_output.py)
  |
  v
MinerU_md/{paper}/full.md
  |
  v
Agent Literature Processing
```

---

## 2. Files Created

| File | Purpose |
|---|---|
| `04_Tools/mineru/process_paper.py` | Single paper processor — queries Zotero, runs CLI, normalizes, logs |
| `04_Tools/mineru/batch_process.py` | Batch processor — dry-run by default, `--execute` to run |
| `04_Tools/mineru/normalize_mineru_output.py` | Normalization layer (updated from Stage 5.1) |
| `04_Tools/mineru/README.md` | Tool documentation |
| `MinerU_logs/` | Log directory created under ResearchAI_Data |

**No existing files modified.** No existing KnowledgeVault files changed. No existing MinerU outputs deleted.

---

## 3. Commands

### Single Paper Processing
```bash
python process_paper.py <Zotero_Item_Key>
# Works with both paper keys and attachment keys
# Example: python process_paper.py 9W23DNVG
```

### Batch Processing
```bash
python batch_process.py              # Dry run (default)
python batch_process.py --execute    # Actually process
python batch_process.py --key 9W23DNVG  # Single key execute
```

### Normalization
```bash
python normalize_mineru_output.py <folder>
# Handles: full.md (skip), hybrid_auto/ (copy), txt/ (copy + fix paths)
```

---

## 4. Test Results

### Test 1: Skip Mechanism (9W23DNVG — Chai 2020)

| Check | Result |
|---|---|
| Zotero query | PASS — resolved attachment key 9W23DNVG to paper 5L2QLL47 |
| PDF detection | PASS — found PDF at storage/9W23DNVG/ |
| Skip detection | PASS — existing full.md detected at MinerU_md/ |
| Exit code | 0 (skipped cleanly) |

### Test 2: Paper with Tables (8PQBD3RU — Wang 2023 Segformer)

| Check | Result |
|---|---|
| Zotero query | PASS — resolved paper key 8PQBD3RU, att_key J2ML7W6A |
| PDF detection | PASS — PDF exists at storage/J2ML7W6A/ |
| MinerU CLI | PASS — completed in ~16s, 16 pages |
| full.md | PASS — 44KB generated |
| Images | PASS — 37 images extracted |
| Normalization | PASS — full.md at root, images/ at root |
| Log | PASS — MinerU_logs/2026-07-17_211702.log |

### Test 3: Paper with Many Figures (YUB9FY6Q — Monteiro 2024 Review)

| Check | Result |
|---|---|
| Zotero query | PASS — resolved paper key YUB9FY6Q, att_key SGUIYBB2 |
| PDF detection | PASS — PDF exists at storage/SGUIYBB2/ |
| MinerU CLI | PASS — completed in ~23s |
| full.md | PASS — 152KB generated (larger due to review content) |
| Images | PASS — 28 images extracted |
| Normalization | PASS — full.md at root, images/ at root |
| Log | PASS — MinerU_logs/2026-07-17_211841.log |

---

## 5. Known Limitations

| Limitation | Impact | Mitigation |
|---|---|---|
| Folder names use full paper titles (long) | Unwieldy paths | Acceptable — uniqueness guaranteed |
| Zotero titles stored in itemData (not items table) | Requires separate query | Fixed in process_paper.py |
| Attachment key vs paper key ambiguity | Script resolves both | Works correctly for both |
| Sandbox blocks /ResearchAI_Data/ writes | Requires escalation | Confirmed working with require_escalated |
| CLI requires proxy env var stripping | Breaks without it | Handled automatically in scripts |
| No automatic Zotero watch | Manual trigger required | Belongs to Stage 5.3+ |

---

## 6. Recommendation for Stage 5.3

### Proceed: YES

All 3 tests passed. The production pipeline is functional:
- Zotero query resolves both paper and attachment keys
- MinerU CLI processes papers successfully
- Normalization layer produces agent-compatible `full.md`
- Skip mechanism prevents duplicate processing
- Logging captures all operations

### Proposed Stage 5.3 Scope

1. **Normalize existing Format C folders** — Run normalizer on the 1 hybrid_auto folder
2. **Update agent skills** — Reference the normalization layer in `paper_intake.md`
3. **Build Zotero-first CLI wrapper** — Integrate into the skill system
4. **Validate with all 27 Zotero papers** — Full batch validation

### Do NOT proceed yet with:

- Automatic Zotero file watching (too complex for current scope)
- Cron/systemd automation (belongs to Stage 5.4+)
- Multi-GPU or VLM backend testing (not needed for current RTX 4070 constraint)

---

> **Status:** Stage 5.2 Complete. Pipeline validated on 3 papers.
> **Next:** Stage 5.3 — Normalize existing outputs + skill integration.
