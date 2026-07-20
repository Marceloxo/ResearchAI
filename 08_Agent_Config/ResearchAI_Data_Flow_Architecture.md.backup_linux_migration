# ResearchAI Data Flow Architecture

> This document is the definitive reference for the ResearchAI architecture.
> After context compression, agents MUST read this document to understand the system.
> Do NOT redesign the architecture — trust this document.

---

## Three-Layer Architecture

ResearchAI has exactly three layers. Nothing more, nothing less.

| Layer | System | Responsibility | Location |
|---|---|---|---|
| **Layer 1: Source** | Zotero | PDF storage, metadata, citation management | `D:\ResearchAI_Data\Zotero\` |
| **Layer 2: Processing** | MinerU | PDF → Markdown + Figures | `D:\ResearchAI_Data\Paper\MinerU_md\` |
| **Layer 3: Knowledge** | KnowledgeVault | Structured understanding, notes, links | `C:\ResearchAI\02_KnowledgeVault\` |

---

## Data Flow Diagram

```
Zotero (Layer 1: Source)
    │
    ├── PDFs in D:\ResearchAI_Data\Zotero\storage\
    ├── Metadata in D:\ResearchAI_Data\Zotero\zotero.sqlite
    └── Citation Keys via Better BibTeX
        │
        ▼
MinerU Desktop (Layer 2: Processing)
    │
    ├── Reads PDF from Zotero storage/
    ├── Outputs full.md + images + layout files
    └── Output stored in D:\ResearchAI_Data\Paper\MinerU_md\
        │
        ▼
AI Agent Analysis
    │
    ├── Reads Processed Markdown (full.md)
    ├── Applies Paper Processing Decision Framework
    ├── Creates KnowledgeVault notes
    └── Links via [[wikilinks]]
        │
        ▼
KnowledgeVault (Layer 3: Knowledge)
    │
    ├── 01_Papers/ — Literature Cards, Paper Notes
    ├── 02_Topics/ — Research topic definitions
    ├── 03_Methods/ — Algorithm/method descriptions
    ├── 04_Tasks/ — Task definitions
    ├── 05_Datasets/ — Dataset registries
    ├── 06_Experiments/ — Experiment interpretations
    ├── 07_Ideas/ — Research ideas
    ├── 08_Writing/ — Manuscript planning
    ├── 09_Paper_Logic/ — Argument Mining analysis
    ├── Templates/ — Note templates
    └── 00_Meta/ — Navigation layer (MOCs, indexes)
```

---

## Explicit Rules

These rules are **permanent**. Do not violate them regardless of context compression or agent reset.

### Rule 1: Never Duplicate PDFs Outside Zotero

Zotero is the **sole owner** of all paper PDFs.

- No PDFs in `C:\ResearchAI\`
- No separate `Origin_pdf/` directory
- No copies in `01_Literature/PDFs/` or `01_Literature/01_PDFs/` (both deprecated)
- MinerU reads directly from Zotero storage

### Rule 2: Never Treat MinerU Output as Final Knowledge

MinerU output (`full.md`, `layout.json`, images) is **raw material**, not knowledge.

- MinerU output lives on D: drive (`D:\ResearchAI_Data\Paper\MinerU_md\`)
- It is transient — serves analysis, not archival
- Knowledge lives in `02_KnowledgeVault/`
- Raw data never enters the KnowledgeVault

### Rule 3: Never Store Processed Knowledge Inside Literature Directory

The `01_Literature/` directory is for intake materials only.

- Knowledge notes belong in `02_KnowledgeVault/`
- Paper notes, method notes, dataset notes — all in Vault
- `01_Literature/` subdirectories `Markdown/`, `PDFs/`, `01_PDFs/`, `02_MinerU_Output/`, `03_Processed_Markdown/` are **deprecated**

### Rule 4: Zotero Citation Key Is Independent From Filename

Three identifiers serve different purposes:

| Identifier | System | Example | Purpose |
|---|---|---|---|
| **Filename** | KnowledgeVault | `chai2020_using_note.md` | File organization |
| **Citation Key** | Better BibTeX | `chai2020using` | Manuscript citations |
| **Item Key** | Zotero internal | `9W23DNVG` | Immutable reference |

These are related but NOT required to match.

---

## Directory Responsibilities

| Directory | Owner | Contents |
|---|---|---|
| `D:\ResearchAI_Data\Zotero\` | Zotero | PDFs, metadata, citation styles |
| `D:\ResearchAI_Data\Paper\MinerU_md\` | MinerU | Raw markdown output |
| `C:\ResearchAI\01_Literature\` | Deprecated intake layer | Only `00_Inbox/`, `04_Literature_Index/`, `References/` are active |
| `C:\ResearchAI\02_KnowledgeVault\` | KnowledgeVault | All structured knowledge |
| `C:\ResearchAI\08_Agent_Config\` | Agent config | Rules, templates, workflows |
| `C:\ResearchAI\04_Tools\` | Tool integration | Zotero setup, data architecture |

---

## Why This Architecture

1. **Single source of truth** for PDFs (Zotero)
2. **Separation of concerns**: source → processing → knowledge
3. **Lean workspace**: C: drive stays under ~100MB for Git
4. **Tool independence**: MinerU can be replaced, Zotero can be replaced, but the three-layer structure endures
5. **Traceability**: every knowledge note traces back to a source PDF via the pipeline

---

## References

- `08_Agent_Config/ADR_Zotero_PDF_Centered_Architecture.md` — ADR-001: why Zotero owns PDFs
- `08_Agent_Config/ResearchAI_Design_Principles.md` — 10 permanent design principles
- `08_Agent_Config/Paper_Processing_Decision_Framework.md` — 3-level processing strategy
- `08_Agent_Config/Paper_File_Naming_Rules.md` — filename conventions
- `08_Agent_Config/Paper_Card_Guideline.md` — Card vs Note vs Logic roles
