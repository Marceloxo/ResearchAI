# SKILL: Paper Intake

## Purpose

Handle newly imported papers through the complete intake pipeline.

## Input

```
Zotero Item Key
```

Example:
```
76SW77W3
```

## Permission Model

**Semi-Automatic Mode (Mode B)** — No modifications before human confirmation.

## Workflow

### Step 1 — Zotero Verification

Verify Zotero storage exists:
```
D:\ResearchAI_Data\Zotero\storage\<ItemKey>\
```

Confirm:
- PDF file exists in the directory
- PDF is readable

If missing: STOP and report "PDF not found in Zotero storage."

### Step 2 — Locate PDF

Record:
- PDF filename
- File size
- Last modified date

### Step 3 — Locate MinerU Output

Search MinerU output directory:
```
D:\ResearchAI_Data\Paper\MinerU_md\
```

Find folder matching the PDF filename (case-insensitive partial match).

Verify:
- Folder exists
- `full.md` exists
- `images/` or `resources/` directory exists (if figures present)

If MinerU output missing: STOP and report "MinerU processing not complete."

### Step 4 — Check Mapping Registry

Read:
```
08_Agent_Config/MinerU_Zotero_Mapping.md
```

Check if this Zotero Item Key already has an entry.

If found: STOP and report "Paper already processed."

### Step 5 — Check Duplicates

Cross-reference against:
- `02_KnowledgeVault/00_Meta/Paper_Index.md` — search by title/author
- `02_KnowledgeVault/01_Papers/` — search by `{author}{year}_*` pattern
- `MinerU_Zotero_Mapping.md` — search by Item Key

If duplicate detected: STOP and report duplicate. Do not create files.

### Step 6 — Determine Processing Level

Read `full.md` and extract:
- Title
- Authors
- Year
- Paper type (Survey/Research Article/Benchmark/Technical Report)
- Research topic relevance

Apply `Paper_Processing_Decision_Framework.md`:

| Level | Output | When |
|---|---|---|
| Level 1 | Literature Card | All papers — mandatory |
| Level 2 | Paper Note | Deep Read decision at Level 1 |
| Level 3 | Paper Logic | Argument Mining triggers met |

Default: Level 1 only. Escalate to Level 2/3 only with human confirmation.

### Step 7 — Generate Execution Plan

Present plan to human:

```
Execution Plan:

Input:
  Zotero Item Key: <key>
  PDF: <filename>

Detected:
  MinerU: <folder>/full.md
  Paper Type: <type>
  Processing Level: <level>

Will create:
  02_KnowledgeVault/01_Papers/<filename>.md

Will modify:
  MinerU_Zotero_Mapping.md (append row)
  Paper_Index.md (add entry)
  Batch_Processing_Log.md (if batch mode)

Waiting for confirmation.
```

### Step 8 — Execute (After Confirmation)

1. Create Literature Card using `Literature_Card_Template.md`
2. Add Zotero section with Item Key
3. Append row to `MinerU_Zotero_Mapping.md`
4. Update `Paper_Index.md`
5. Update `Batch_Processing_Log.md` if batch mode

## Constraints

- Do NOT modify templates
- Do NOT modify directory structure
- Do NOT process papers without Zotero verification
- Do NOT auto-promote beyond Level 1
- Do NOT create knowledge nodes without reuse check

## Error Handling

| Condition | Action |
|---|---|
| Zotero storage missing | STOP — report missing PDF |
| MinerU output missing | STOP — report incomplete processing |
| Duplicate detected | STOP — report existing paper |
| Paper type unclear | FLAG for human review |
| Processing level disputed | FLAG for human review |
