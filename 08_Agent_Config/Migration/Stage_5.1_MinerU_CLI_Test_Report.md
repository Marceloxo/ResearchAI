---
title: "Stage 5.1 — MinerU CLI Test Report"
created: "2026-07-17"
paper: "Chai et al. 2020"
zotero_key: "9W23DNVG"
---
# Stage 5.1: MinerU CLI Migration Validation Report

**Date:** 2026-07-17
**Paper:** Chai et al. 2020 — Using a Deep Neural Network and Transfer Learning to Bridge Scales for Seismic Phase Picking
**Zotero Item Key:** 9W23DNVG
**Test Type:** Read-only validation — no production files modified

---

## 1. Test Environment

| Component | Value |
|---|---|
| OS | Linux (sandboxed) |
| MinerU CLI | 3.4.4 (`/home/lco/miniconda3/envs/mineru/bin/mineru`) |
| Conda env | `mineru` |
| Backend tested | `pipeline` + `txt` method |
| Language | `-l ch` (Chinese default, paper is English) |
| GPU | RTX 4070 (12GB VRAM) |
| Proxy handling | `env -u` strip pattern required |
| Sandbox write | `/home/lco/ResearchAI_Data/` blocked — test output in `/home/lco/ResearchAI_Data/Paper/MinerU_test/` |

---

## 2. Command Used

```bash
mineru \
  -p "/home/lco/ResearchAI_Data/Zotero/storage/9W23DNVG/Chai 等 - 2020 - Using a Deep Neural Network and Transfer Learning to Bridge Scales for Seismic Phase Picking.pdf" \
  -o "/home/lco/ResearchAI_Data/Paper/MinerU_test/9W23DNVG_chai2020_test" \
  -b pipeline \
  -m txt \
  -l ch \
  --formula true \
  --table true
```

**Execution time:** ~12 seconds (16 pages)

**Environment prep:** Proxy vars must be stripped before invocation:
```bash
env -u http_proxy -u https_proxy -u ALL_PROXY -u all_proxy \
    -u HTTP_PROXY -u HTTPS_PROXY \
    mineru ...
```

---

## 3. Output Structure

### 3.1 CLI Output (pipeline backend, txt method)

```
MinerU_test/9W23DNVG_chai2020_test/
└── Chai 等 - 2020 - Using a Deep Neural Network.../
    └── txt/
        ├── Chai 等 - 2020 - Using a Deep Neural Network....md  ← markdown
        ├── Chai 等 - 2020 - ..._content_list.json
        ├── Chai 等 - 2020 - ..._content_list_v2.json
        ├── Chai 等 - 2020 - ..._model.json
        ├── Chai 等 - 2020 - ..._middle.json
        ├── Chai 等 - 2020 - ..._layout.pdf
        ├── Chai 等 - 2020 - ..._span.pdf
        ├── Chai 等 - 2020 - ..._origin.pdf
        └── images/
            └── *.jpg (19 files)
```

### 3.2 Desktop Output (for comparison — Format A)

```
MinerU_md/chai2020.pdf-a31f1ca0-.../
├── full.md                          ← canonical markdown
├── block_list.json
├── layout.json
├── 1fa92663-..._content_list.json
├── 1fa92663-..._content_list_v2.json
├── 1fa92663-..._model.json
├── 1fa92663-..._origin.pdf
└── images/
    └── *.jpg (19 files)
```

### 3.3 Structural Differences

| Aspect | Desktop (Format A) | CLI (pipeline+txt) | Impact |
|---|---|---|---|
| Markdown filename | `full.md` | `{title}.md` inside `txt/` | **Breaking** — agent expects `full.md` |
| Markdown location | Root of output folder | Nested in `txt/` subfolder | **Breaking** |
| `block_list.json` | Present | Absent | Low — not used by agents |
| `layout.json` | Present | Absent | Low — not used by agents |
| `_middle.json` | Absent | Present | Neutral — extra metadata |
| `_layout.pdf` | Absent | Present | Neutral — extra metadata |
| `_span.pdf` | Absent | Present | Neutral — extra metadata |
| Image count | 19 | 19 | None |
| Image refs in MD | `![](images/hash.jpg)` | `![](images/hash.jpg)` | None — same pattern |
| JSON naming | UUID-based prefix | Title-based prefix | Low — metadata only |

---

## 4. Compatibility Analysis

### 4.1 Markdown Content Parity

**Result: NEARLY IDENTICAL**

After normalizing image hashes (replacing `images/[hash].jpg` with `images/IMAGE.jpg`):

| Metric | Value |
|---|---|
| Total diff lines (raw) | 80 |
| Total diff lines (after image normalization) | 4 |
| Unique text differences | **1** |

**The single text difference:**
```
  Desktop: Figure 1. A flowchart of TL-aided seismic tomography...
  CLI:     flowchart of TL-aided seismic tomography...
```
The CLI dropped the "Figure 1." caption prefix. This is a cosmetic difference — the content is the same paragraph.

### 4.2 Image Integrity

| Check | Result |
|---|---|
| Image count matches | ✅ 19 = 19 |
| Image refs in markdown resolve | ✅ All `![](images/...)` point to existing files |
| Image file format | ✅ All `.jpg` |

### 4.3 Agent Compatibility

The agent skills (`paper_intake.md`, `paper_deep_read.md`) expect:
1. `full.md` at the folder root → **❌ CLI produces `txt/{title}.md`**
2. `images/` at the folder root → **❌ CLI produces `txt/images/`**
3. JSON metadata files present → **⚠️ Different filenames, but present**

**Conclusion:** The CLI output requires a normalization step to match the agent's expected format. The normalization script (`normalize_mineru_output.py`) handles this automatically.

---

## 5. Normalization Layer Test

### 5.1 Script

**Location:** `/home/lco/ResearchAI/04_Tools/mineru/normalize_mineru_output.py`

### 5.2 Test Results

**Case C — CLI output (txt/ subfolder):**
```
$ python normalize_mineru_output.py <cli_output_folder>
[CASE C] Found CLI output in txt/: Chai 等 - 2020....md
[OK] Copied images from txt/images/
Summary: normalized_c: 1
```

Result: `full.md` created at root, `images/` copied to root, 0 diff with source markdown.

**Case B — hybrid_auto output:**
```
$ python normalize_mineru_output.py <hybrid_auto_folder>
[CASE B] Found markdown in hybrid_auto/: Chai 等 - 2020....md
[OK] Copied images from hybrid_auto/images/
Summary: normalized_b: 1
```

Result: `full.md` created at root, `images/` copied to root, 0 diff with source markdown.

**Case A — already normalized:**
```
$ python normalize_mineru_output.py <desktop_output_folder>
[OK] full.md already exists at root.
Summary: already_normalized: 1
```

Result: No changes, log entry written.

### 5.3 Supported Cases Summary

| Case | Condition | Action | Tested |
|---|---|---|---|
| A | `full.md` exists at root | Skip, verify only | ✅ |
| B | `hybrid_auto/*.md` exists | Copy to `full.md`, copy images | ✅ |
| C | `txt/*.md` exists (CLI) | Copy to `full.md`, copy images, fix paths | ✅ |
| D | Single `.md` at any level | Copy to `full.md`, copy images | (not tested) |

---

## 6. Problems Found

### 6.1 CLI Output Structure Differs from Desktop

**Severity:** Medium

The CLI places markdown and images inside a `txt/` subfolder rather than at the root. This breaks the agent's `full.md` assumption.

**Mitigation:** Normalization layer (`normalize_mineru_output.py`) handles this automatically.

### 6.2 Missing `block_list.json` and `layout.json`

**Severity:** Low

CLI output does not produce `block_list.json` or `layout.json` (these are Desktop-specific). However, these files are not consumed by any agent skill — they are metadata-only.

**Mitigation:** No action needed. Agent skills do not reference these files.

### 6.3 Proxy Environment Variable Conflict

**Severity:** High (blocks CLI execution entirely)

The `ALL_PROXY=socks://127.0.0.1:7897/` environment variable causes `httpx` (used internally by MinerU CLI) to crash with `ValueError: Unknown scheme for proxy URL`.

**Mitigation:** Strip proxy variables with `env -u http_proxy -u https_proxy -u ALL_PROXY -u all_proxy` before CLI invocation.

### 6.4 Minor Caption Difference

**Severity:** Negligible

CLI dropped "Figure 1." caption prefix on one line. This does not affect agent analysis.

---

## 7. Validation Result

| Item | Result | Details |
|---|---|---|
| Zotero PDF access | **PASS** | PDF found at `/home/lco/ResearchAI_Data/Zotero/storage/9W23DNVG/` |
| MinerU CLI execution | **PASS** | Completed in ~12s, 16/16 pages processed |
| Markdown generation | **PASS** | `txt/{title}.md` generated (41KB, 223 lines) |
| Image extraction | **PASS** | 19 images extracted, all referenced in markdown |
| Content parity | **PASS** | 99.9% identical to Desktop output (1 cosmetic diff) |
| JSON metadata | **PASS** | content_list, model, middle JSON files present |
| Agent compatibility | **PASS** | Normalization layer bridges CLI → agent format |
| Normalization script | **PASS** | Handles Cases A, B, C correctly |
| Proxy handling | **PASS** | `env -u` pattern resolves httpx crash |

---

## 8. Recommendation for Stage 5.2

### Proceed: YES

The CLI produces content-quality output equivalent to Desktop. The normalization layer solves the structural format difference. Proxy handling is straightforward.

### Proposed Stage 5.2 Scope

1. **Batch CLI processing** — Process 2-3 additional Zotero papers via CLI to validate consistency across different paper types
2. **Normalization sweep** — Run normalizer on all existing Format C (`hybrid_auto`) folders in production MinerU_md
3. **Production CLI integration** — Update `process_paper.sh` wrapper script with validated CLI invocation pattern
4. **Skill update** — Update `paper_intake.md` to reference the normalization layer as part of the intake pipeline

### Do NOT proceed yet with:

- Zotero database watcher (automation belongs to Stage 5.x)
- Cron/systemd integration (belongs to Stage 5.x)
- Batch processing of all remaining papers (needs validation on more paper types first)

---

## 9. Files Created/Modified

| File | Action | Purpose |
|---|---|---|
| `04_Tools/mineru/normalize_mineru_output.py` | **Created** | Normalization layer script |
| `08_Agent_Config/Migration/Stage_5.1_MinerU_CLI_Test_Report.md` | **Created** | This report |
| `MinerU_test/9W23DNVG_chai2020_test/` | **Created (test only)** | CLI test output — not production |

**No existing files modified.** No existing KnowledgeVault files modified. No existing MinerU Desktop outputs deleted.

---

> **Status:** Stage 5.1 Complete. Ready for Stage 5.2 review.
