# Zotero Setup Guide

## Overview

This guide defines how to set up Zotero for ResearchAI integration.

---

## Required Software

### Zotero

**Purpose**: Reference management database. Stores paper metadata, PDFs, tags, and collections.

**Installation**: Download from [zotero.org](https://www.zotero.org/)

**Role in ResearchAI**: Single source of truth for bibliographic metadata and PDFs.

### Better BibTeX (BBT)

**Purpose**: Zotero plugin that auto-generates and exports BibTeX citation keys.

**Installation**: Install from within Zotero -> Tools -> Add-ons -> Search "Better BibTeX"

**Role in ResearchAI**: Bridges Zotero metadata to ResearchAI's literature system via BibTeX export.

---

## Zotero Workflow Configuration

See `Zotero_Workflow_Configuration.md` for full collection design, tag taxonomy, and Zotero↔ResearchAI mapping.

### Quick Reference

**Collections** (manage reading status):
```
ResearchAI/
├── 00_Inbox/        → status: inbox
├── 01_Screening/    → status: screened
├── 02_Reading/      → status: deep_read
├── 03_Deep_Read/    → status: deep_read (completed)
├── 04_Core/         → status: deep_read (core paper)
└── Archive/         → status: archived
```

**Tags** (classify knowledge domain):
- Domain: `#seismic`, `#earthquake`, `#medical`
- Task: `#phase-picking`, `#segmentation`, `#denoising`
- Method: `#cnn`, `#transformer`, `#unet`, `#diffusion`
- Status: `#to-read`, `#deep-read`, `#reproduced`, `#key-paper`

---

## Metadata Rules

### Fields Managed by Zotero

| Field | Source | Notes |
|---|---|---|
| `title` | Zotero title field | Authoritative |
| `authors` | Zotero creators | Authoritative |
| `year` | Zotero date | Authoritative |
| `journal` | Zotero publication title | Authoritative |
| `DOI` | Zotero DOI field | Authoritative |
| `citationKey` | Better BibTeX auto-generated | `auth.lower + year + shorttitle(2)` format |
| `itemKey` | Zotero internal | Immutable once assigned |

### Fields Managed by ResearchAI

| Field | Source | Notes |
|---|---|---|
| `paper_id` | ResearchAI convention | `YYYY_FirstAuthor_ShortTitle` |
| `reading_status` | Literature Card decision | Deep Read / Keep / Ignore |
| `importance` | Researcher assessment | High / Medium / Low |
| `knowledge_status` | Vault extraction progress | See Literature Index |

---

## Citation Key Naming

### Current Configuration

Better BibTeX citation key format: `auth.lower + year + shorttitle(2)`

Example: `mont24lit` (not `monteiro2024literature`)

**Do not change this setting.** The actual format differs from the originally designed `authorYEARkeyword` format, but both are BibTeX-compatible and the Literature Index records whatever key Zotero generates.

### Important Distinction

| Identifier | Format | Example | Purpose |
|---|---|---|---|
| Paper ID | `YYYY_FirstAuthor_ShortTitle` | `2024_Monteiro_LiteratureReview` | File organization |
| Citation Key | `auth.lower + year + shorttitle(2)` | `mont24lit` | Academic citations |

**They are different identifiers for the same paper.** The Literature Index maps between them.

---

## Export Rules

### Better BibTeX Configuration

| Setting | Value |
|---|---|
| Export format | BibTeX |
| Auto-export | Enabled |
| Export target | `C:\ResearchAI\01_Literature\04_Literature_Index\bibliography.bib` |
| Update on change | Yes |

### Export Behavior

- BibTeX is **auto-updated** when papers are added/modified in Zotero
- Only papers with `#done` or `#key-paper` tags are included in exports
- Citation keys follow the actual Better BibTeX format (not Paper ID format)

---

## ResearchAI Mapping

### Data Flow

```
Zotero (metadata, PDFs, tags)
    -> Better BibTeX export
bibliography.bib -> Literature Index (zotero_key, doi, citation_status)
    -> MinerU processing -> Processed Markdown -> Literature Card
    -> KnowledgeVault (structured notes, wikilinks)
    -> Writing (citations from Zotero BibTeX)
```

### Mapping Table

| Zotero Entity | ResearchAI Location | Purpose |
|---|---|---|
| Collection | `01_Literature/04_Literature_Index/Literature_Index.md` | Status tracking |
| Tags | `01_Literature/04_Literature_Index/Literature_Index.md` | Classification |
| BibTeX | `01_Literature/04_Literature_Index/bibliography.bib` | Citation source |
| Item Key | `01_Literature/04_Literature_Index/Literature_Index.md` | Bidirectional lookup |

---

## Current Status

**Partially configured.** Zotero is installed and Better BibTeX is configured. Collections and tags need to be created. See `Zotero_Workflow_Configuration.md` for the full configuration checklist.
