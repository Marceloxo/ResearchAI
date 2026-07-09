# Zotero Storage Strategy

## Overview

This document defines where Zotero stores its data and how it relates to the ResearchAI workspace.

## Zotero Data Directory

### Location

```
D:\ResearchAI_Data\
```

**Confirmed.** This is the actual Zotero data directory.

### Contents

| File/Directory | Purpose |
|---|---|
| `zotero.sqlite` | Database — bibliographic metadata |
| `storage/` | PDF files — single source of truth for all paper PDFs |
| `styles/` | Citation styles |
| `translators/` | Import translators |
| `locate/` | Full-text indexing |

### Drive: Large Capacity Disk

Zotero data includes PDFs which are large files. Storing on the D: drive keeps the C: drive lean.

### Backup

Regularly backup the entire `D:\ResearchAI_Data\` directory (excluding `Paper/`, `Datasets/`, etc. which are separate). This is the single point of failure for all bibliographic data and PDFs.

## ResearchAI Workspace

### What Belongs Here

- `01_Literature/` — paper processing pipeline (MinerU output, processed markdown, index)
- `02_KnowledgeVault/` — structured knowledge notes
- `03_Projects/` — research code
- `04_Tools/` — tool integrations and scripts
- `05_Experiments/` — experiment records
- `06_Writing/` — manuscripts and drafts
- `07_Research_Ideas/` — research ideas
- `08_Agent_Config/` — agent instructions and configurations

### What Does NOT Belong Here

- Zotero database files (`.sqlite`) — stored in `D:\ResearchAI_Data\`
- Zotero storage (PDFs) — stored in `D:\ResearchAI_Data\storage\`
- Large raw datasets (stored in `D:\ResearchAI_Data\`)
- Model checkpoints (stored in `D:\ResearchAI_Data\models\`)

## PDF Source of Truth

### Zotero-Centered Architecture (ADR-001)

All paper PDFs are stored in:

```
D:\ResearchAI_Data\storage\
```

**MinerU reads PDFs from this location.** There is no separate Origin_pdf directory.

### Why This Works

1. Zotero is the authoritative source for PDFs — one copy, one source of truth
2. MinerU can read PDFs from `storage/` without modifying Zotero
3. When a paper is added to Zotero, it is immediately available for processing
4. The KnowledgeVault stores knowledge, not PDFs — keeping the workspace lean

### MinerU Workflow

```
MinerU reads PDF from: D:\ResearchAI_Data\storage\{hash}.pdf
MinerU outputs to:     D:\ResearchAI_Data\Paper\MinerU_md\{paper_id}\
ResearchAI processes:  03_Processed_Markdown\ → 02_KnowledgeVault\
```

## Summary

| Component | Location | Purpose |
|---|---|---|
| Zotero data (DB + PDFs) | `D:\ResearchAI_Data\` | Single source of truth |
| MinerU output | `D:\ResearchAI_Data\Paper\MinerU_md\` | Processed markdown |
| Datasets | `D:\ResearchAI_Data\Datasets\` | Dataset files |
| Experiment results | `D:\ResearchAI_Data\Experiment_Results\` | Large outputs |
| Model checkpoints | `D:\ResearchAI_Data\Model_Checkpoints\` | Trained weights |
| ResearchAI workspace | `C:\ResearchAI\` | Code, docs, knowledge |
