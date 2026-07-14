# SKILL: Paper Deep Read

## Purpose

Generate a technical Paper Note (Level 2 analysis) for a paper already processed at Level 1.

## Input

```
Zotero Item Key
```

Example:
```
6VTKJ8W2
```

## Permission Model

**Semi-Automatic Mode (Mode B)** — No modifications before human confirmation.

## Prerequisites

Before executing this skill, verify:
1. Literature Card already exists in `02_KnowledgeVault/01_Papers/`
2. Paper was classified as "Deep Read" at Level 1
3. Paper has valid MinerU `full.md` output

## Workflow

### Step 1 — Locate Source Materials

1. Read MinerU output:
   ```
   D:\ResearchAI_Data\Paper\MinerU_md/<folder>/full.md
   ```

2. Read existing Literature Card:
   ```
   02_KnowledgeVault/01_Papers/<paper>_card.md
   ```

3. Read existing Paper Note if any:
   ```
   02_KnowledgeVault/01_Papers/<paper>_note.md
   ```
   If exists: STOP — paper already has a note. Offer to update instead.

### Step 2 — Determine Filename

Extract from `full.md`:
- Author surname (first author)
- Year
- Keyword (derived from title/topic)

Construct filename:
```
{author}{year}_{keyword}_note.md
```

Example: `fang2022_snunet_cd_note.md`

### Step 3 — Check for Duplicates

Search `02_KnowledgeVault/01_Papers/` for existing files matching the pattern.

If duplicate found: STOP — offer to update existing note.

### Step 4 — Analyze Paper Content

Extract from `full.md`:

1. **Problem**: What research problem does the paper address?
2. **Motivation**: Why is this problem important? What gap does it fill?
3. **Contributions**: List each contribution clearly.
4. **Architecture**: Overall system architecture and design.
5. **Method Details**: Key modules, algorithms, formulas.
6. **Training Strategy**: Loss functions, optimization, hyperparameters.
7. **Results**: Key quantitative results, comparisons, tables.
8. **Ablation Study**: Module-level effectiveness analysis.
9. **Limitations**: Author-admitted and agent-identified.
10. **Transferability**: How can this apply to seismic AI research?
11. **Reproducibility**: Code availability, dataset access, environment specs.

### Step 5 — Handle Unknown Information

For any field that cannot be determined from the paper:
- Use "Not Found Yet" for code availability
- Do NOT fabricate repository URLs
- Do NOT invent hyperparameters
- Do NOT guess dataset specifications

Record honestly:
```
**Code Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked
```

### Step 6 — Generate Execution Plan

Present plan to human:

```
Execution Plan:

Input:
  Zotero Item Key: <key>
  Source: MinerU/full.md

Will create:
  02_KnowledgeVault/01_Papers/<filename>_note.md

Will analyze:
  - Problem, motivation, contributions
  - Architecture and method details
  - Results and ablation study
  - Limitations and transferability
  - Reproducibility assessment

Waiting for confirmation.
```

### Step 7 — Generate Paper Note (After Confirmation)

Create note using `Paper_Template.md` as reference.

Required sections:
1. YAML frontmatter (title, authors, year, venue, task, methods, datasets, metrics, code, importance, status, paper_type, tags, created)
2. Paper Type classification
3. One Sentence Summary
4. Research Background
5. Problem Definition (input/output)
6. Motivation
7. Main Contributions (numbered list)
8. Method (overall framework, key modules, mathematical formulation)
9. Dataset (table format)
10. Experimental Setup
11. Results (with tables where applicable)
12. Ablation Study
13. Limitation
14. My Analysis (Transferable Ideas, Potential Improvements)
15. Reproducibility Analysis (Code Status, Missing Components, Difficulty Assessment)
16. Related Notes (wikilinks to existing Methods, Tasks, Datasets)

### Step 8 — Post-Processing

1. Update `MinerU_Zotero_Mapping.md` — update status to LEVEL_2_DONE or PROCESSED
2. Update `Paper_Index.md` — add note entry under appropriate section
3. Update `Batch_Processing_Log.md` — if part of batch processing

## Constraints

- Do NOT fabricate information
- Do NOT invent code repositories
- Do NOT guess hyperparameters or training details
- Do NOT modify templates
- Do NOT create knowledge nodes automatically
- Do NOT skip reproducibility analysis

## Error Handling

| Condition | Action |
|---|---|
| No Literature Card exists | STOP — run Paper Intake first |
| MinerU output missing | STOP — report incomplete processing |
| Paper already has note | STOP — offer update instead |
| Paper type mismatch (e.g., survey) | Use Survey_Template instead |
