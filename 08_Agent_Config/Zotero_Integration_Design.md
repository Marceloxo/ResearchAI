# Zotero Integration Design

## Purpose

This document defines how Zotero integrates with ResearchAI as the reference management layer.

### Zotero's Responsibility

Zotero manages:
- **Metadata**: title, authors, year, DOI, journal, volume, issue, pages
- **PDF files**: original paper PDFs, organized by collection
- **Citations**: BibTeX, RIS, CSL-JSON exports for reference formatting
- **Tags**: Zotero tags for classification and filtering
- **Attachments**: supplementary files, notes, highlights

### ResearchAI's Responsibility

ResearchAI manages:
- **Literature understanding**: paper analysis, screening, deep reading
- **Knowledge extraction**: methods, tasks, datasets, ideas
- **Experiment management**: test plans, results, interpretations
- **Writing assistance**: manuscript drafting, citation insertion

Zotero is the **reference database**. ResearchAI is the **research workspace**.

---

## System Architecture

```
+-----------------------------------------------------------------------+
|                    ResearchAI Workspace                                |
|                                                                        |
|  01_Literature/                                                       |
|  +-- 00_Inbox/          <- PDFs arrive here                           |
|  +-- 01_PDFs/           <- Archived PDFs                              |
|  +-- 02_MinerU_Output/  <- Raw MinerU parsing                         |
|  +-- 03_Processed_Markdown/ <- Cleaned for AI                          |
|  +-- 04_Literature_Index/ <- Master tracker                           |
|                                                                        |
|  02_KnowledgeVault/                                                  |
|  +-- 01_Papers/         <- Reading notes                              |
|  +-- 03_Methods/        <- Algorithm knowledge                         |
|  +-- 04_Tasks/          <- Problem definitions                         |
|  +-- 05_Datasets/       <- Dataset documentation                       |
|  +-- 07_Ideas/          <- Research ideas                              |
|                                                                        |
|  06_Writing/                                                         |
|  +-- Manuscripts <- cite from Zotero                                  |
+-----------------------------------------------------------------------+
                            |
                            v
+-----------------------------------------------------------------------+
|                            Zotero                                      |
|                                                                        |
|  Collections -> 01_Literature/00_Inbox/                                |
|  PDFs -> 01_Literature/01_PDFs/                                        |
|  Better BibTeX -> BibTeX export for writing                            |
|  Tags -> Literature_Index.md status tracking                           |
+-----------------------------------------------------------------------+
```

### Data Flow

1. **Import**: PDFs are imported into Zotero collections (e.g., "Seismic AI", "To Read")
2. **Sync**: Zotero exports metadata via Better BibTeX to `01_Literature/04_Literature_Index/`
3. **Process**: Papers flow through MinerU -> Processed Markdown -> KnowledgeVault
4. **Cite**: Writing in `06_Writing/` pulls citations from Zotero via BibTeX

---

## Metadata Ownership

### Owned by Zotero

These fields are **authoritative in Zotero** and should be sourced from there:

| Field | Source |
|---|---|
| title | Zotero title |
| authors | Zotero creators |
| year | Zotero date |
| DOI | Zotero DOI field |
| journal/conference | Zotero publication title |
| volume, issue, pages | Zotero fields |
| BibTeX key | Better BibTeX auto-generated |
| Zotero item key | Unique identifier |

### Owned by ResearchAI

These fields are **generated within ResearchAI**:

| Field | Source |
|---|---|
| reading_notes | KnowledgeVault paper notes |
| methods_extracted | 03_Methods/ notes |
| ideas_generated | 07_Ideas/ notes |
| experiments_run | 06_Experiments/ notes |
| paper_type | Determined during screening |
| importance_rating | Assigned by researcher |
| reading_decision | Deep Read / Keep / Ignore |

### Shared Fields

| Field | Source | Sync Direction |
|---|---|---|
| tags | Both | Zotero -> ResearchAI (classification) |
| status | ResearchAI -> Zotero | Reading status sync |
| paper_id | ResearchAI only | Local convention |

---

## Paper Identity Mapping

### Three Independent Identifiers

Each paper has **three independent identifiers** (see Principle 4 in ResearchAI_Design_Principles.md):

| System | Identifier | Format | Example |
|---|---|---|---|
| Zotero | Item Key | 6-char alphanumeric | `ABCDE123` |
| ResearchAI | Paper ID | `YYYY_FirstAuthor_ShortTitle` | `2023_Monteiro_DeepLearningSeismicSegmentation` |
| Better BibTeX | Citation Key | `authorYEARkeyword` | `monteiro2023deeplearning` |

### Mapping Strategy

The mapping is maintained in `01_Literature/04_Literature_Index/Literature_Index.md`:

| Paper ID | Zotero Key | Citation Key | Zotero Collection |
|---|---|---|---|
| 2023_Monteiro_... | ABCDE123 | monteiro2023deeplearning | Seismic AI/To Read |

### Consistency Rules

1. **Zotero key is immutable** — once assigned, never changed.
2. **Paper ID is ResearchAI-local** — can be reformatted without affecting Zotero.
3. **Citation Key is BBT-managed** — follows `authorYEARkeyword` convention, independent of Paper ID.
4. **All three IDs must coexist** in the Literature Index for bidirectional lookup.
5. **Paper ID and Citation Key are NOT required to match** — they follow different naming conventions.

---

## Future Workflow

### Integrated Pipeline

```
PDF arrives
    -> Import to Zotero (add to collection, assign tags)
    -> Export metadata via Better BibTeX -> Literature Index update
    -> MinerU processing -> 02_MinerU_Output/
    -> Clean -> 03_Processed_Markdown/
    -> Level 1 Screening -> Literature Card
    -> Level 2 Deep Read -> Paper Note + Methods + Tasks + Datasets
    -> Level 3 Research -> Experiment + Idea + Writing
    -> Citation inserted from Zotero BibTeX
```

### Zotero Collections (Proposed)

| Collection | Purpose |
|---|---|
| `To Read` | Papers awaiting screening |
| `Reading` | Papers currently being analyzed |
| `Done` | Papers fully processed |
| `Archived` | Papers kept for reference, not active |
| `Seismic AI` | Domain-specific sub-collection |
| `Methods` | Papers focused on method development |

### Zotero Tags (Proposed)

| Tag | Meaning |
|---|---|
| `#to-read` | Pending screening |
| `#reading` | Currently being read |
| `#done` | Screening and deep read completed |
| `#key-paper` | Exceptionally important |
| `#survey` | Review/survey paper |
| `#benchmark` | Benchmark/evaluation paper |
| `#seismic-ai` | Domain tag |
| `#segmentation` | Task tag |

---

## Better BibTeX Configuration

When Better BibTeX plugin is installed in Zotero:

### Citation Key Format

Recommended format for academic citations:

```
authorYEARkeyword
```

Example: `monteiro2023deeplearning`

**Note**: This is different from the ResearchAI Paper ID format (`2023_Monteiro_DeepLearningSeismicSegmentation`). They serve different purposes and follow different conventions.

### Auto-export Settings

- Export on save: enabled
- Export format: BibTeX
- Export to: `C:\ResearchAI\01_Literature\04_Literature_Index\bibliography.bib`
- Sync interval: manual (not automatic yet)

---

## Current Status

**Not yet implemented.**

This is a design document. Actual integration requires:
1. Installing Zotero
2. Installing Better BibTeX plugin
3. Configuring collections and tags
4. Setting up BibTeX export path
5. Validating the Paper ID <-> Zotero Key mapping

This will be done in a future stage after the core pipeline is validated with 3-5 papers.
