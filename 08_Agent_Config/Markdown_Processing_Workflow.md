# Markdown Processing Workflow

## Purpose

Define the step-by-step process for converting raw MinerU output into processed markdown ready for AI analysis.

---

## Overview

```
MinerU Raw Output
    ↓
Extract full.md
    ↓
Clean Structure
    ↓
Generate Processed Markdown
    ↓
Level 1 Literature Screening
```

This workflow sits between Step 5 (Store Raw Output) and Step 8 (Begin Level 1 Screening) of the Literature Intake Workflow.

---

## Step 1: Extract full.md

**Input**: Raw MinerU output folder in `02_MinerU_Output/{paper_id}/`

**Action**: Locate and read `full.md`.

**Verify**:
- File exists and is not empty
- File is in UTF-8 encoding
- File contains expected sections (title, abstract, introduction, etc.)

**If missing**: Note in Literature Index, try re-running MinerU.

---

## Step 2: Clean Structure

**Input**: Raw `full.md`

**Actions**:

### Remove
- Page headers/footers (look for repeated lines at top/bottom of pages)
- Page numbers
- Layout JSON image references: `![](uuid_hash.jpg)` → keep description, remove hash
- Model JSON references
- Content list file references
- Any `*_model.json` or `*_content_list.json` mentions
- Duplicate text blocks (same paragraph appearing twice)

### Keep
- All section headings and their content
- Mathematical formulas (LaTeX notation)
- Tables
- Abstract and keywords
- Method descriptions
- Results and figures
- Conclusions

### Fix
- Encoding issues (Chinese characters, special symbols)
- Broken line breaks within paragraphs
- Inconsistent heading levels

---

## Step 3: Generate Processed Markdown

**Input**: Cleaned content

**Action**: Apply the `Processed_Markdown_Template.md` structure:

```markdown
---
paper_id: "YYYY_FirstAuthor_ShortTitle"
title: "Paper Title"
authors: [...]
year: YYYY
paper_type: research_article
source: "downloaded from ..."
mineru_source: "02_MinerU_Output/YYYY_FirstAuthor_ShortTitle/"
processed_date: "2026-07-08"
---

# Metadata
...

# Abstract
...

# Keywords
...

# Introduction Summary
...

# Research Problem
...

# Main Contribution
...

# Method
...

# Experiment
...

# Results
...

# Conclusion
...

# References
...

# Notes for AI Agent
- Parsing quality: Good/Fair/Poor
- Missing sections: ...
- Encoding issues: ...
```

**Output**: `{paper_id}.md` in `03_Processed_Markdown/`

---

## Step 4: Quality Assessment

Before proceeding to Level 1 Screening:

| Check | Pass Criteria |
|---|---|
| Title present | Yes |
| Abstract present | Yes |
| Main sections present | At least 3 of: Intro, Method, Results, Conclusion |
| Formulas intact | No garbled math notation |
| Tables readable | Markdown table format preserved |
| Encoding correct | No replacement characters (�) |
| No duplicates | Same paragraph does not appear twice |

**If any check fails**: Go back to Step 2 and fix.
**If all pass**: Proceed to Step 5.

---

## Step 5: Begin Level 1 Screening

**Input**: Processed markdown in `03_Processed_Markdown/`

**Action**: Read the processed markdown and create a Literature Card using `Literature_Card_Template.md`.

**Decision**: Deep Read / Keep Reference / Ignore

---

## Current Mode vs. Future Mode

### Current: Manual (Stage 1.4B)

- Human or AI agent reads `full.md`
- Manually applies cleaning rules
- Manually generates processed markdown
- Manually proceeds to screening

### Future: Automated (Post CLI)

When MinerU CLI is available:

```bash
# Watch folder for new MinerU output
watch-folder 02_MinerU_Output/
    ↓
# Auto-extract and clean full.md
mineru-clean --input {folder}/full.md --output 03_Processed_Markdown/{paper_id}.md
    ↓
# Auto-assess quality
quality-check 03_Processed_Markdown/{paper_id}.md
    ↓
# Auto-trigger Level 1 screening
trigger-screening {paper_id}
```

This automation is **not** part of Stage 1.4B. The current manual process validates the pipeline before automation is attempted.

---

## File Locations

| Step | Input | Output |
|---|---|---|
| Extract | `02_MinerU_Output/{id}/full.md` | Raw text |
| Clean | Raw text | Cleaned text |
| Generate | Cleaned text + Template | `03_Processed_Markdown/{id}.md` |
| Assess | Processed markdown | Quality report |
| Screen | Processed markdown | Literature Card |
