# SKILL: Paper Batch Process

## Purpose

Process multiple papers through the Level 1 (Literature Card) pipeline in batch mode.

## Input

Multiple Zotero Item Keys (space-separated or newline-separated):

```
76SW77W3 6VTKJ8W2 NCKCP6BS
```

## Permission Model

**Semi-Automatic Mode (Mode B)** — Execution plan presented before any modifications.

## Prerequisites

1. `Batch_Processing_Guideline.md` is available and current
2. `MinerU_Zotero_Mapping.md` exists
3. `Batch_Processing_Log.md` exists (or will be created)

## Workflow

### Step 1 — Parse Input

Extract Zotero Item Keys from input. Validate each key:
- Must be 8-character alphanumeric
- Must exist in `D:\ResearchAI_Data\Zotero\storage/<Key>/`

### Step 2 — Pre-Processing Verification

For each paper:
1. Verify Zotero storage (PDF exists)
2. Verify MinerU output (full.md exists)
3. Check `MinerU_Zotero_Mapping.md` for existing entries
4. Check `Paper_Index.md` for duplicates
5. Check `02_KnowledgeVault/01_Papers/` for existing files

Record results in a verification table:

| Item Key | Zotero | MinerU | Mapping | Duplicate | Status |
|---|---|---|---|---|---|
| 76SW77W3 | ✅ | ✅ | ✅ | No | READY |

Skip papers that fail any check. Report skipped papers to human.

### Step 3 — Classification

For each ready paper, determine:
- Paper type (Survey/Research Article/Benchmark/Technical Report)
- Processing category (A/B/C1/C2/D per Decision Framework)
- Recommended level (Level 1 / Level 2 / Level 3)

### Step 4 — Generate Execution Plan

Present plan to human:

```
Batch Processing Plan:

Total papers: <N>
Ready for processing: <M>
Skipped (issues): <K>

Processing breakdown:
  Level 1 (Cards): <L1>
  Level 2 (Notes): <L2>
  Level 3 (Logic): <L3>

Files to create: <L1> cards + <L2> notes + <L3> logics
Files to modify: MinerU_Zotero_Mapping.md, Paper_Index.md, Batch_Processing_Log.md

Waiting for confirmation.
```

### Step 5 — Execute Batch (After Confirmation)

For each paper in order:

1. **Zotero verification** — confirm Item Key and PDF
2. **Mapping verification** — confirm MinerU output
3. **Duplicate check** — verify no existing KV files
4. **Processing decision** — apply Decision Framework
5. **Literature Card creation** — using Literature_Card_Template.md
6. **Zotero section** — add Status and Item Key
7. **Mapping update** — append row to MinerU_Zotero_Mapping.md
8. **Index update** — add entry to Paper_Index.md
9. **Log update** — record in Batch_Processing_Log.md

### Step 6 — Post-Batch Summary

Generate summary:

```
Batch Complete:

Total: <N>
Processed: <M>
Skipped: <K>
Duplicates found: <D>
Errors: <E>

New files created: <count>
New mapping rows: <count>
```

## Constraints

- Follow `Batch_Processing_Guideline.md` exactly
- Do NOT skip duplicate checks
- Do NOT auto-promote beyond Level 1 without explicit criteria
- Do NOT create knowledge nodes automatically
- Do NOT modify templates
- Do NOT change directory structure

## Error Handling

| Condition | Action |
|---|---|
| Zotero PDF missing | Skip paper, log reason |
| MinerU output missing | Skip paper, log reason |
| Duplicate detected | Skip paper, log existing file |
| Processing level disputed | Flag for human review |
| All papers fail | STOP, report to human |
