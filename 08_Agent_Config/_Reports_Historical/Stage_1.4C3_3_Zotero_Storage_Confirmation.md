# Stage 1.4C-3.3 Zotero Storage Confirmation Report

## Date

2026-07-09

## Purpose

Confirm the actual Zotero storage architecture and document it in ResearchAI's system documentation. No migration or configuration changes were made.

---

## Current Storage Architecture

### Confirmed (No Change Needed)

| Component | Location | Status |
|---|---|---|
| Zotero database | `C:\Users\DZ\Zotero\` | ✅ Confirmed |
| Zotero Linked Attachment Base Directory | `D:\ResearchAI_Data\Zotero_Attachments\` | ✅ Confirmed |

### ResearchAI Data Layer

| Component | Location | Status |
|---|---|---|
| ResearchAI paper PDFs | `D:\ResearchAI_Data\Paper\Origin_pdf\` | ✅ Confirmed |
| MinerU output | `D:\ResearchAI_Data\Paper\MinerU_md\` | ✅ Confirmed |
| Datasets | `D:\ResearchAI_Data\Datasets\` | ✅ Confirmed |
| Experiment results | `D:\ResearchAI_Data\Experiment_Results\` | ✅ Confirmed |
| Model checkpoints | `D:\ResearchAI_Data\Model_Checkpoints\` | ✅ Confirmed |

---

## Why Two PDF Locations?

There are **two** PDF locations on the D: drive. They serve different purposes:

### 1. `D:\ResearchAI_Data\Zotero_Attachments\`

- **Managed by**: Zotero
- **Mechanism**: Linked Attachment Base Directory (symlinks in Zotero DB)
- **Purpose**: Papers that have been imported into Zotero for reference management
- **Access**: Through Zotero interface, not directly in ResearchAI

### 2. `D:\ResearchAI_Data\Paper\Origin_pdf\`

- **Managed by**: ResearchAI literature intake system
- **Mechanism**: Direct file storage
- **Purpose**: Papers in the ResearchAI processing pipeline (MinerU input, literature screening)
- **Access**: Through ResearchAI directories (`01_Literature/`)

### Overlap

A paper may exist in **both** locations if:
- It has been imported to Zotero (for reference management)
- AND it is being processed through the ResearchAI pipeline (for knowledge extraction)

This is normal and expected. The two systems are complementary, not redundant.

---

## Why This Design Is Correct

### Separation of Concerns

| System | Owns | Manages |
|---|---|---|
| **Zotero** | Bibliographic metadata, PDF references | Collections, tags, BibTeX, citation keys |
| **ResearchAI** | Knowledge extraction, experiment tracking | Literature cards, paper notes, methods, tasks |

### Drive Separation

| Drive | Purpose | Components |
|---|---|---|
| **SSD (C:)** | Fast access, active work | Zotero DB, ResearchAI workspace |
| **Large Disk (D:)** | High capacity, large files | PDFs, datasets, models, checkpoints |

### Git-Friendly

No PDFs or large files are stored in `C:\ResearchAI\`. The Git repository stays under ~100MB.

---

## Files Updated

| File | Change |
|---|---|
| `Zotero_Storage_Strategy.md` | Confirmed attachment path; clarified two-PDF-location design |
| `D:\ResearchAI_Data\README.md` | Added Zotero_Attachments section |
| `Current_State_Check.md` | Removed "attachment storage pending" status |

---

## No Changes Made

- No Zotero configuration was modified
- No PDF files were moved
- No files were deleted
- No citation key format was changed
- No KnowledgeVault structure was altered

This stage was purely a **confirmation and documentation** exercise.
