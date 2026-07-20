# Literature Intake Workflow

## Overview

This document defines the step-by-step workflow for processing a new paper through the ResearchAI literature system.

---

## New Paper Intake

### Input

A new PDF file (from download, email, colleague, database).

### Workflow Steps

#### Step 1: Receive

Place the PDF in:
```
C:\ResearchAI\01_Literature\00_Inbox\
```

#### Step 2: Assign Paper ID

Read the paper's metadata (title, authors, year). Assign a Paper ID per `Paper_ID_Rules.md`.

Format: `YYYY_FirstAuthor_ShortTitle`

#### Step 3: Archive PDF

Move the PDF to:
```
C:\ResearchAI\01_Literature\01_PDFs\
```

Rename using Paper ID: `YYYY_FirstAuthor_ShortTitle.pdf`

#### Step 4: Run MinerU

Process the PDF through MinerU Desktop GUI.

Output will be a UUID-named folder containing:
- `full.md`
- `origin.pdf`
- `images/`
- `layout.json`
- `*_content_list.json`

#### Step 5: Store Raw Output

Move the MinerU output folder to:
```
C:\ResearchAI\01_Literature\02_MinerU_Output\
```

Rename the UUID folder to use the Paper ID.

#### Step 6: Generate Cleaned Markdown

Extract and clean `full.md`:
- Remove non-essential MinerU artifacts
- Fix encoding issues
- Standardize headings
- Save to:
```
C:\ResearchAI\01_Literature\03_Processed_Markdown\
```

Filename: `YYYY_FirstAuthor_ShortTitle.md`

#### Step 7: Create Intake Record

Create a Literature Intake record in:
```
C:\ResearchAI\01_Literature\04_Literature_Index\
```

Use `Literature_Intake_Template.md`.

#### Step 8: Begin Level 1 Screening

Read the cleaned markdown. Create a Literature Card using `Literature_Card_Template.md`.

Decision: Deep Read / Keep Reference / Ignore

---

## Workflow Diagram

```
PDF arrives
    鈫?[Zotero Import] 鈥?MUST be completed first (Step 0)
    鈫?[00_Inbox/] 鈥?Place PDF here
    鈫?Assign Paper ID (YYYY_FirstAuthor_ShortTitle)
    鈫?[01_PDFs/] 鈥?Archive PDF with Paper ID name
    鈫?MinerU Desktop GUI 鈫?Processing
    鈫?[02_MinerU_Output/] 鈥?Store raw UUID folder, rename to Paper ID
    鈫?Clean full.md
    鈫?[03_Processed_Markdown/] 鈥?Store cleaned markdown
    鈫?[Literature Index] 鈥?Create intake record
    鈫?[Level 1 Screening] 鈥?Literature Card 鈫?Decision
```

---

## Agent Instructions

When an AI agent receives a new paper:

1. Follow this workflow step by step.
2. Do not skip steps 鈥?each step has a specific purpose.
3. If a step fails (e.g., MinerU output is corrupted), note it in the Literature Index.
4. After Level 1 screening, follow `Literature_Processing_Strategy.md` for next steps.
5. Never place raw MinerU output directly into KnowledgeVault 鈥?always clean first.

