# 01_Literature — Literature Intake Layer

## Purpose

This directory holds **raw and processed paper materials** that feed into `02_KnowledgeVault`. It is NOT a knowledge base — it is the intake and archival layer.

**Knowledge extraction happens in `02_KnowledgeVault/`.**

## Architecture

```
Zotero (/home/lco/Zotero/storage/)
    ︙
    PDF storage + metadata (single source of truth)
    ︙
    ↓
MinerU Desktop (reads from Zotero storage)
    ︙
    PDF → Markdown + Figures
    ︙
    ↓
/home/lco/ResearchAI_Data/Paper/MinerU_md/
    ︙
    Raw MinerU output (full.md, images, layout.json)
    ︙
    ↓
AI Agent reads full.md → creates KnowledgeVault notes
    ︙
    ↓
02_KnowledgeVault/
    ︙
    Structured knowledge (cards, notes, methods, tasks, datasets)
```

**The only valid pipeline: Zotero → MinerU → KnowledgeVault.**

## Deprecated Directories

The following subdirectories exist but are **deprecated** and no longer used:

| Directory | Reason |
|---|---|
| `Markdown/` | MinerU output lives on ResearchAI_Data, not here |
| `PDFs/` | PDFs are managed by Zotero (ADR-001) |
| `01_PDFs/` | Duplicate of PDFs/, also deprecated |
| `02_MinerU_Output/` | MinerU output lives on ResearchAI_Data/Paper/MinerU_md/ |
| `03_Processed_Markdown/` | Processed markdown is transient, not archived here |

These directories are empty placeholders. They have been marked deprecated but are NOT physically removed to avoid breaking any legacy references.

## Active Directories

| Directory | Purpose |
|---|---|
| `00_Inbox/` | New papers arriving, unprocessed |
| `04_Literature_Index/` | Master index of all papers in the system |
| `References/` | BibTeX bibliography file |

## Relationship to Other Directories

- **Feeds into** `02_KnowledgeVault/` — source materials for knowledge extraction
- **Replaced by** `/home/lco/ResearchAI_Data/Paper/MinerU_md/` — actual MinerU output location
- **Replaced by** `/home/lco/Zotero/` — actual PDF storage location
- **Links to** `06_Writing/` — manuscripts cite papers from this layer
- **Informs** `07_Research_Ideas/` — gaps discovered in literature

## Configuration

- Paper ID rules: `Paper_ID_Rules.md`
- Literature Index: `04_Literature_Index/Literature_Index.md`
- Intake Template: `Literature_Intake_Template.md`
- Intake Workflow: `08_Agent_Config/Literature_Intake_Workflow.md`
- Decision Framework: `08_Agent_Config/Paper_Processing_Decision_Framework.md`
- Paper Naming: `08_Agent_Config/Paper_File_Naming_Rules.md`
