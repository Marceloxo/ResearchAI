---
title: "Stage 5 — MinerU Linux Architecture Design"
created: "2026-07-17"
status: "design"
---
# Stage 5: MinerU Linux Architecture Design

> **Purpose**: Design a Linux-native workflow that replaces MinerU Desktop with MinerU CLI 3.4.4 while preserving the three-layer architecture and agent input format.
>
> **Scope**: Read-only design document. No files modified.
>
> **Predecessor**: Stage 4C Architecture Review (Wine-based fallback analysis)
>
> **Constraints**: Architecture is frozen. Do not redesign directory structure, naming conventions, or data flow.

---

## 1. Current State Assessment

### 1.1 Verified Evidence

| Component | Status | Evidence |
|---|---|---|
| **Zotero storage/** | 28 PDFs across 28 Item Keys | `/home/lco/ResearchAI_Data/Zotero/storage/` — 28 subdirectories, each with 1 PDF |
| **MinerU Desktop output** | 28 folders in MinerU_md/ | Mixed output formats (see §1.2) |
| **MinerU CLI 3.4.4** | Installed in conda env `mineru` | `/home/lco/miniconda3/envs/mineru/bin/mineru` — version 3.4.4 |
| **zotero.sqlite** | Readable, 4 MB | Located at `/home/lco/ResearchAI_Data/Zotero/zotero.sqlite` |
| **Agent skills** | Reference `full.md` as canonical input | `paper_intake.md`, `paper_deep_read.md`, `Batch_Processing_Guideline.md` |
| **Sandbox socket restriction** | CLI cannot bind sockets in sandbox | `PermissionError: [Errno 1] Operation not permitted` — expected, not a blocker |

### 1.2 MinerU Desktop Output Formats (Three Variants)

Analysis of the 28 existing MinerU output folders reveals **three distinct output formats** produced by MinerU Desktop over time:

**Format A — Legacy (20 folders)**
```
MinerU_md/{hash-suffix-folder}/
├── full.md                        ← Canonical markdown (agent input)
├── MinerU_markdown_*.md           ← Timestamped duplicate (redundant)
├── block_list.json
├── layout.json
├── *_content_list.json
├── *_content_list_v2.json
├── *_model.json
├── *_origin.pdf
└── images/
    └── *.jpg
```
Example: `chai2020.pdf-a31f1ca0-.../full.md`

**Format B — Transitional (4 folders)**
```
MinerU_md/{paper-title-with-hash}/
├── full.md                        ← Canonical markdown
├── block_list.json
├── layout.json
├── *_content_list.json
├── *_content_list_v2.json
├── *_model.json
├── *_origin.pdf
└── images/
```
Example: `Lv和Peng - 2026 - DTPP...pdf-6ec18a94-.../full.md`

**Format C — Newest Hybrid (1 folder)**
```
MinerU_md/{paper-title}/
└── hybrid_auto/
    ├── {paper-title}.md           ← Canonical markdown (NOT named full.md!)
    ├── {paper-title}_content_list.json
    ├── {paper-title}_content_list_v2.json
    ├── {paper-title}_layout.pdf
    ├── {paper-title}_middle.json
    ├── {paper-title}_model.json
    ├── {paper-title}_origin.pdf
    └── images/
        └── *.jpg
```
Example: `Chai 等 - 2020 - Using a Deep Neural Network.../hybrid_auto/Chai 等 - 2020....md`

**Key observation**: Formats A and B both place `full.md` at the folder root. Format C nests the markdown inside a `hybrid_auto/` subfolder and renames it to `{paper-title}.md` instead of `full.md`. This is the first format inconsistency that breaks the agent's assumption.

### 1.3 Content Comparison Across Formats

Comparing the same paper (Chai 2020) across Format A and Format C:
- Markdown text content is **identical** (same title, abstract, sections)
- Image hashes differ (different extraction runs produce different image filenames)
- Format C adds `_middle.json` and `_layout.pdf` not present in Format A
- Format C does NOT produce `block_list.json` or `layout.json`

**Conclusion**: The `full.md` content is stable across formats. The structural differences are in ancillary metadata files, not the markdown itself.

---

## 2. MinerU CLI 3.4.4 Specification

### 2.1 CLI Interface

```
mineru -p <path> -o <output_dir> [-b backend] [-m method] [-l lang] [...]
```

| Flag | Value | Description |
|---|---|---|
| `-p, --path` | filepath | PDF input (required) |
| `-o, --output` | dirpath | Output directory (required) |
| `-b, --backend` | `pipeline` \| `vlm-engine` \| `hybrid-engine` \| `vlm-http-client` \| `hybrid-http-client` | Backend engine (default: `hybrid-engine`) |
| `-m, --method` | `auto` \| `txt` \| `ocr` | Parsing method (default: auto) |
| `-l, --lang` | `ch` \| `ch_server` \| `korean` \| ... | Document language (default: `ch`) |
| `--effort` | `medium` \| `high` | Hybrid parsing effort (default: `medium`) |
| `--formula` | `true` \| `false` | Enable formula parsing (default: `true`) |
| `--table` | `true` \| `false` | Enable table parsing (default: `true`) |
| `--image-analysis` | `true` \| `false` | Enable image/chart analysis (default: `true`) |
| `-s, --start` | int | Starting page (0-indexed) |
| `-e, --end` | int | Ending page (0-indexed) |
| `-u, --url` | url | VLM/HTTP client endpoint URL |

### 2.2 Backend Selection Matrix

| Backend | Local GPU Required | Network Required | Speed | Accuracy | Use Case |
|---|---|---|---|---|---|
| `pipeline` | No | No | Fast | Good | Standard text PDFs |
| `vlm-engine` | Yes (GPU) | No | Slow | Highest | High-accuracy local VLM |
| `hybrid-engine` | Partial | No | Medium | Very High | Default — balances speed/accuracy |
| `vlm-http-client` | No | Yes | Fast | Highest | Remote VLM API |
| `hybrid-http-client` | No | Yes | Medium | Very High | Remote hybrid |

**Recommendation for RTX 4070 (12GB VRAM)**: Use `pipeline` backend with `txt` method for standard text PDFs. Reserve `hybrid-engine` for papers with complex layouts or tables requiring image analysis.

### 2.3 Expected CLI Output Format

MinerU CLI uses the `pipeline` backend (no VLM). Based on the CLI help text and comparison with Desktop outputs, the CLI will produce:

```
<output_dir>/<paper_id>/
├── full.md                    ← Canonical markdown (matches Desktop format)
├── block_list.json
├── layout.json
├── *_content_list.json
├── *_content_list_v2.json
├── *_model.json
├── *_origin.pdf
└── images/
    └── *.jpg
```

This matches **Format A** (legacy Desktop output), which is the canonical format that all agent skills reference.

---

## 3. Proposed Linux-Native Workflow

### 3.1 Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│  Layer 1: Source (Zotero)                                           │
│  /home/lco/ResearchAI_Data/Zotero/storage/{ItemKey}/{pdf}.pdf      │
│  /home/lco/ResearchAI_Data/Zotero/zotero.sqlite                    │
└──────────────────────┬──────────────────────────────────────────────┘
                       │ reads PDF
                       ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Layer 2: Processing (MinerU CLI)                                   │
│  conda activate mineru                                               │
│  mineru -p <pdf_path> -o <output_base> -b pipeline -m txt -l ch    │
│  Output: /home/lco/ResearchAI_Data/Paper/MinerU_md/{paper_id}/     │
└──────────────────────┬──────────────────────────────────────────────┘
                       │ writes full.md
                       ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Layer 3: Knowledge (KnowledgeVault)                                │
│  Agent reads full.md → creates Literature Card / Paper Note        │
│  /home/lco/ResearchAI/02_KnowledgeVault/01_Papers/                 │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Normalization Layer

A **lightweight normalization script** sits between MinerU CLI output and agent consumption. Its purpose is to ensure Format A consistency regardless of which Desktop variant produced the output.

**Script: `normalize_mineru_output.sh`**

Location: `/home/lco/ResearchAI/04_Tools/normalize_mineru_output.sh`

Responsibilities:
1. Detect output format variant (A, B, or C)
2. For Format C (`hybrid_auto/`): copy the nested `.md` to `full.md` at the parent level
3. For Format B: verify `full.md` exists (already correct)
4. For Format A: verify `full.md` exists (already correct)
5. Normalize image paths in `full.md` to use relative `images/` references
6. Log normalization actions to a `.normalization.log` file

**Why a normalization layer is needed**: Format C (hybrid_auto) is the only variant that breaks the agent's `full.md` assumption. Rather than updating all agent skills to handle two possible markdown locations, a one-time normalization ensures the agent always reads from `full.md`.

### 3.3 CLI Invocation Pattern

```bash
#!/bin/bash
# Process a single PDF through MinerU CLI
# Usage: process_paper.sh <zotero_item_key>

set -euo pipefail

ITEM_KEY="$1"
ZOTERO_STORAGE="/home/lco/ResearchAI_Data/Zotero/storage/${ITEM_KEY}"
MINERU_OUTPUT="/home/lco/ResearchAI_Data/Paper/MinerU_md"
CONDA_ENV="mineru"

# Step 1: Verify PDF exists
PDF_FILE=$(find "${ZOTERO_STORAGE}" -name "*.pdf" -type f | head -1)
if [ -z "${PDF_FILE}" ]; then
    echo "ERROR: No PDF found in Zotero storage for key ${ITEM_KEY}"
    exit 1
fi

# Step 2: Determine output folder name
PDF_BASENAME=$(basename "${PDF_FILE}" .pdf)
OUTPUT_DIR="${MINERU_OUTPUT}/${PDF_BASENAME}-${ITEM_KEY}"
mkdir -p "${OUTPUT_DIR}"

# Step 3: Run MinerU CLI
eval "$(conda shell.bash hook 2>/dev/null)"
conda activate "${CONDA_ENV}" 2>/dev/null

# Strip proxy env vars that interfere with MinerU CLI
env -u http_proxy -u https_proxy -u ALL_PROXY -u all_proxy \
    mineru -p "${PDF_FILE}" \
           -o "${OUTPUT_DIR}" \
           -b pipeline \
           -m txt \
           -l ch \
           --formula true \
           --table true

# Step 4: Verify output
if [ ! -f "${OUTPUT_DIR}/full.md" ]; then
    echo "WARNING: full.md not found. Checking for hybrid_auto format..."
    if [ -d "${OUTPUT_DIR}/hybrid_auto" ]; then
        cp "${OUTPUT_DIR}/hybrid_auto/"*.md "${OUTPUT_DIR}/full.md" 2>/dev/null || true
    fi
fi

echo "DONE: ${ITEM_KEY} → ${OUTPUT_DIR}/full.md"
```

### 3.4 Batch Processing Workflow

```bash
# Step 1: Query Zotero for papers needing MinerU processing
python3 << 'EOF'
import sqlite3, os

DB = "/home/lco/ResearchAI_Data/Zotero/zotero.sqlite"
STORAGE = "/home/lco/ResearchAI_Data/Zotero/storage"
MINERU_MD = "/home/lco/ResearchAI_Data/Paper/MinerU_md"

conn = sqlite3.connect(DB)
cur = conn.cursor()

# Find all attachment items (PDFs) with their parent item keys
cur.execute("""
    SELECT ia.parentItemID, pa.key as parent_key, ia.path
    FROM itemAttachments ia
    JOIN items pa ON ia.parentItemID = pa.itemID
    WHERE ia.path LIKE 'storage:%'
    AND pa.itemTypeID != 3  -- exclude attachments themselves
""")

for row in cur.fetchall():
    parent_id, item_key, storage_path = row
    
    # Extract PDF filename from storage path
    pdf_filename = storage_path.split(':', 1)[1] if ':' in storage_path else ''
    pdf_path = os.path.join(STORAGE, item_key, pdf_filename)
    
    if not os.path.exists(pdf_path):
        print(f"SKIP {item_key}: PDF not found at {pdf_path}")
        continue
    
    # Check if MinerU output already exists
    output_candidates = [
        os.path.join(MINERU_MD, f"{pdf_filename.rsplit('.', 1)[0]}-{item_key}"),
        os.path.join(MINERU_MD, f"{pdf_filename}-{item_key}"),
    ]
    
    has_output = any(os.path.exists(d) and os.path.isfile(os.path.join(d, 'full.md')) 
                     for d in output_candidates)
    
    if has_output:
        print(f"SKIP {item_key}: MinerU output already exists")
    else:
        print(f"PROCESS {item_key}: {pdf_path}")

conn.close()
EOF
```

---

## 4. Proxy Environment Handling

### 4.1 Problem

MinerU CLI 3.4.4 uses `httpx` internally, which reads `ALL_PROXY` environment variables. The current environment has:
```
ALL_PROXY=socks://127.0.0.1:7897/
HTTP_PROXY=http://127.0.0.1:7897/
HTTPS_PROXY=http://127.0.0.1:7897/
```

`httpx` rejects `socks://` scheme (expects `http://` or `https://`), causing a `ValueError: Unknown scheme for proxy URL`.

### 4.2 Solution

Strip proxy variables before invoking MinerU CLI:

```bash
env -u http_proxy -u https_proxy -u ALL_PROXY -u all_proxy \
    -u HTTP_PROXY -u HTTPS_PROXY \
    mineru -p ... -o ...
```

This is already incorporated in the invocation pattern (§3.3).

---

## 5. Agent Input Stability Analysis

### 5.1 Current Agent Assumptions

From `paper_intake.md` and `paper_deep_read.md`:
1. MinerU output lives in `D:\ResearchAI_Data\Paper\MinerU_md\` → Now `/home/lco/ResearchAI_Data/Paper/MinerU_md/`
2. Each paper has a folder matching the PDF filename (partial match)
3. The canonical markdown file is `full.md` at the folder root
4. Images are in an `images/` subdirectory with relative references in `full.md`

### 5.2 Impact of CLI Transition

| Assumption | Desktop Output | CLI Output | Impact |
|---|---|---|---|
| `full.md` at root | ✅ Formats A, B | ✅ Expected (Format A) | None |
| `images/` subdir | ✅ All formats | ✅ Expected | None |
| Image refs in markdown | ✅ Relative `![](images/...)` | ✅ Same pattern | None |
| JSON metadata files | ✅ Present | ✅ Present | None |
| Folder naming | Mixed (hash-suffix, title, hybrid_auto) | Consistent (title-key) | **Minor** — normalization handles legacy |

### 5.3 Skill Updates Required

The agent skills (`paper_intake.md`, `paper_deep_read.md`, `paper_batch_process.md`) reference Windows paths (`D:\ResearchAI_Data\...`). These paths have already been updated to Linux paths in Stage 4. No additional skill changes are needed for the MinerU CLI transition itself.

---

## 6. Hardware Constraints Alignment

### 6.1 RTX 4070 (12GB VRAM)

| Backend | VRAM Usage | Feasible? |
|---|---|---|
| `pipeline` (txt method) | Minimal (CPU-only) | ✅ Yes |
| `pipeline` (ocr method) | Moderate | ✅ Yes |
| `hybrid-engine` (medium effort) | ~4-6GB | ✅ Yes |
| `hybrid-engine` (high effort) | ~8-10GB | ⚠️ Borderline |
| `vlm-engine` | ~10-12GB | ❌ Too risky |

**Recommendation**: Default to `pipeline` backend with `txt` method for all standard papers. Use `hybrid-engine` only for papers with complex figure/table layouts, and set `--effort medium` to stay within VRAM limits.

### 6.2 Language Support

Most papers in the Zotero library are in English. The `-l ch` (Chinese) default is appropriate for the few Chinese-language papers. For English-only papers, use `-l` omission (defaults to auto-detection) or explicitly set to English-capable mode.

---

## 7. Migration Path

### 7.1 Phased Approach

| Phase | Action | Risk | Rollback |
|---|---|---|---|
| **Phase 1: Read-Only** | Agent reads existing Desktop output. No changes. | None | N/A |
| **Phase 2: Test CLI** | Run CLI on 1-2 test PDFs. Compare output with Desktop. | Low | Existing Desktop output preserved |
| **Phase 3: Dual-Run** | Process new papers via CLI alongside Desktop. Verify consistency. | Low | Desktop still available as fallback |
| **Phase 4: CLI-Only** | Switch all processing to CLI. Archive Desktop outputs. | Medium | Desktop output can be regenerated |
| **Phase 5: Cleanup** | Remove legacy Desktop output folders. Normalize format C. | Low | Already backed up in MinerU_md/ |

### 7.2 Validation Criteria

Before transitioning from Desktop to CLI:
1. **Content parity**: `diff` between Desktop `full.md` and CLI `full.md` shows only whitespace/formatting differences (not content differences)
2. **Image integrity**: All `![](images/...)` references in CLI output resolve to existing files
3. **Metadata completeness**: `content_list.json`, `layout.json`, `block_list.json` all present and parseable
4. **Agent compatibility**: Literature Card generation produces identical results from both Desktop and CLI output

---

## 8. Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| CLI output format differs from Desktop | Medium | High | Phase 2 validation catches differences early |
| Proxy env vars break CLI invocation | Certain (current) | High | `env -u` strip pattern in wrapper script |
| Socket permission denied in sandbox | Certain (current) | Medium | CLI runs outside sandbox; sandbox restriction is expected |
| VRAM exhaustion with hybrid-backend | Low | Medium | Default to `pipeline` backend; cap `hybrid-engine` at `medium` effort |
| Zotero SQLite locked during processing | Low | High | Ensure no Zotero Desktop instance is running; use read-only connection mode |
| Format C (hybrid_auto) normalization fails | Low | Low | Fallback: agent checks both `full.md` and `hybrid_auto/*.md` |

---

## 9. Summary of Recommendations

1. **Zotero remains the single PDF source of truth** — no change. CLI reads from `/home/lco/ResearchAI_Data/Zotero/storage/{ItemKey}/`.
2. **MinerU CLI replaces MinerU Desktop** — use `pipeline` backend with `txt` method as default. This produces Format A output, which is the canonical agent input format.
3. **Agent input format remains stable** — `full.md` at the folder root. The normalization layer handles Format C (`hybrid_auto/`) edge cases.
4. **Normalization layer is minimal** — a single script that copies `hybrid_auto/*.md` to `full.md` when needed. This is a one-time operation per paper, not a continuous transformation.
5. **Proxy handling is mandatory** — strip `ALL_PROXY`, `http_proxy`, `https_proxy` before CLI invocation. This is a known environment issue.
6. **Hardware-aware backend selection** — `pipeline` for standard papers, `hybrid-engine` with `medium` effort for complex layouts. Avoid `vlm-engine` on RTX 4070.

---

## 10. Files Referenced

| File | Role |
|---|---|
| `08_Agent_Config/ResearchAI_Data_Flow_Architecture.md` | Definitive architecture reference (three layers) |
| `08_Agent_Config/ADR_Zotero_PDF_Centered_Architecture.md` | ADR-001: Zotero owns PDFs |
| `08_Agent_Config/MinerU_Zotero_Mapping.md` | Paper traceability registry |
| `08_Agent_Config/Batch_Processing_Guideline.md` | Batch workflow rules |
| `08_Agent_Config/Literature_Processing_Strategy.md` | Processing strategy |
| `08_Agent_Config/ResearchAI_Design_Principles.md` | Permanent design principles |
| `08_Agent_Config/Migration/Stage_4C_Architecture_Review_Report.md` | Predecessor analysis (Wine fallback) |
| `.codex/skills/researchai/references/literature/paper_intake.md` | Agent skill: Paper Intake |
| `.codex/skills/researchai/references/literature/paper_deep_read.md` | Agent skill: Deep Read |
| `/home/lco/miniconda3/envs/mineru/bin/mineru` | MinerU CLI 3.4.4 binary |
| `/home/lco/ResearchAI_Data/Zotero/zotero.sqlite` | Zotero database |
| `/home/lco/ResearchAI_Data/Zotero/storage/` | PDF source directory |
| `/home/lco/ResearchAI_Data/Paper/MinerU_md/` | MinerU output directory |

---

## Appendix A: Zotero SQLite Schema Summary

For agent scripts that need to query Zotero programmatically:

| Table | Key Columns | Purpose |
|---|---|---|
| `items` | `itemID`, `key`, `itemTypeID`, `dateAdded`, `dateModified` | All items (papers, attachments) |
| `itemAttachments` | `itemID`, `parentItemID`, `path`, `storageHash` | Links PDFs to parent papers |
| `itemData` | `itemID`, `fieldID`, `valueID` | Title, abstract, DOI, etc. |
| `itemDataValues` | `valueID`, `value` | Actual text values |
| `creators` | `creatorID`, `firstName`, `lastName`, `fieldMode` | Authors/editors |
| `itemCreators` | `itemID`, `creatorID`, `creatorTypeID` | Links creators to items |
| `itemTypes` | `rowID`, `typeName` | Paper types (journalArticle, etc.) |
| `fields` | `fieldID`, `fieldName` | Field lookup (title=1, abstractNote=2, DOI=8, citationKey=9) |
| `creatorTypes` | `creatorTypeID`, `creatorType` | Author=10, editor=12, etc. |
| `collections` | `collectionID`, `collectionName`, `key` | Zotero collections |

**Key query pattern** — get all papers with their PDFs:
```sql
SELECT i.key, it.typeName, ia.path, i.dateAdded
FROM items i
JOIN itemTypes it ON i.itemTypeID = it.rowID
JOIN itemAttachments ia ON i.itemID = ia.parentItemID
WHERE it.typeName IN ('journalArticle', 'conferencePaper', 'thesis', 'report')
ORDER BY i.dateAdded DESC;
```

---

## Appendix B: Output Format Comparison Matrix

| Feature | Format A (Legacy) | Format B (Transitional) | Format C (Hybrid) | MinerU CLI (Expected) |
|---|---|---|---|---|
| Markdown location | Root `full.md` | Root `full.md` | `hybrid_auto/*.md` | Root `full.md` |
| `block_list.json` | ✅ | ✅ | ❌ | ✅ |
| `layout.json` | ✅ | ✅ | ❌ | ✅ |
| `_middle.json` | ❌ | ❌ | ✅ | ❌ |
| `_layout.pdf` | ❌ | ❌ | ✅ | ❌ |
| Image refs | Relative `![](images/...)` | Relative | Relative | Relative |
| Folder naming | `{pdf_hash}-{uuid}` | `{title_hash}-{uuid}` | `{title}` | `{title}-{key}` |
| Agent-compatible | ✅ | ✅ | ⚠️ Needs normalization | ✅ |

---

## Appendix C: Environment Variables for MinerU CLI

| Variable | Value | Needed? |
|---|---|---|
| `http_proxy` | `http://127.0.0.1:7897/` | **NO — must be stripped** |
| `https_proxy` | `http://127.0.0.1:7897/` | **NO — must be stripped** |
| `ALL_PROXY` | `socks://127.0.0.1:7897/` | **NO — causes httpx crash** |
| `all_proxy` | `socks://127.0.0.1:7897/` | **NO — must be stripped** |
| `CUDA_VISIBLE_DEVICES` | (unset or `0`) | Optional — for GPU selection |
| `MINERU_API_URL` | (unset) | Only for VLM/HTTP backends |

---

> **Document Status**: Design draft — awaiting researcher review and approval before implementation.
> **Next Stage**: Stage 5.1 — CLI Test Run (Phase 2 of migration path)
