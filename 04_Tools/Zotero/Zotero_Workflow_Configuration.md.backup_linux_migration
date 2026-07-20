# Zotero Workflow Configuration

## Purpose

Define Zotero's collection structure, tag taxonomy, and mapping to ResearchAI's Literature Index. This is a configuration document — execute when installing Zotero.

---

## 1. Collections

Collections manage **reading status**, not research topics.

```
ResearchAI/
├── 00_Inbox/           # Papers awaiting initial screening
├── 01_Screening/       # Papers undergoing Level 1 screening
├── 02_Reading/         # Papers undergoing Level 2 deep reading
├── 03_Deep_Read/       # Papers with completed deep reading
├── 04_Core/            # Papers that inspired active research
└── Archive/            # Papers kept for reference only
```

### Collection Semantics

| Collection | ResearchAI Status | Action |
|---|---|---|
| `00_Inbox` | `inbox` | Assign Paper ID, begin Level 1 screening |
| `01_Screening` | `screened` | Literature Card created, decision made |
| `02_Reading` | `deep_read` | Paper Note + Methods/Tasks/Datasets extracted |
| `03_Deep_Read` | `done` | Full knowledge extraction complete |
| `04_Core` | `done` + `key-paper` | Papers that inspired experiments/projects |
| `Archive` | `archived` | Kept for reference, no active research |

### Moving Papers Between Collections

A paper moves through collections as its processing status changes:

```
00_Inbox → 01_Screening → 02_Reading → 03_Deep_Read → 04_Core
                                                    ↓
                                              (or) Archive
```

---

## 2. Tags

Tags classify by **knowledge domain**, not reading status.

### Tag Categories

#### Domain Tags

| Tag | Meaning |
|---|---|
| `#seismic` | Seismic data processing |
| `#earthquake` | Earthquake-related research |
| `#medical` | Medical imaging |
| `#remote-sensing` | Remote sensing |

#### Task Tags

| Tag | Meaning |
|---|---|
| `#phase-picking` | Seismic phase picking |
| `#segmentation` | Image segmentation |
| `#denoising` | Noise removal |
| `#classification` | Classification tasks |
| `#inversion` | Geophysical inversion |

#### Method Tags

| Tag | Meaning |
|---|---|
| `#cnn` | Convolutional neural networks |
| `#transformer` | Transformer architectures |
| `#unet` | U-Net and variants |
| `#diffusion` | Diffusion models |
| `#attention` | Attention mechanisms |
| `#gan` | Generative adversarial networks |

#### Status Tags

| Tag | Meaning |
|---|---|
| `#to-read` | Not yet read |
| `#deep-read` | Currently being deeply read |
| `#reproduced` | Code reproduced |
| `#key-paper` | Exceptionally important |

### Tag Design Principles

1. **Flat hierarchy**: No nested tags. Use atomic tags.
2. **Hyphen-separated**: `#phase-picking`, not `#phase_picking` or `#PhasePicking`.
3. **One meaning per tag**: Don't combine domain+task into one tag.
4. **Minimal set**: Start with essential tags. Add new ones only when clearly needed.

---

## 3. Zotero ↔ ResearchAI Mapping

### Collection → Processing Status

| Zotero Collection | Literature Index Status |
|---|---|
| `00_Inbox` | `inbox` |
| `01_Screening` | `screened` |
| `02_Reading` | `deep_read` |
| `03_Deep_Read` | `deep_read` (completed) |
| `04_Core` | `deep_read` (core paper) |
| `Archive` | `archived` |

### Tags → Knowledge Status

| Zotero Tags | KnowledgeVault Status |
|---|---|
| `#to-read` | `not_processed` |
| `#deep-read` | `literature_card` or `paper_note` |
| `#reproduced` | `methods_extracted`, `datasets_extracted` |
| `#key-paper` | All knowledge statuses |

### Literature Index Row

Each paper in the Literature Index maps to one Zotero entry:

| Literature Index Field | Zotero Source |
|---|---|
| `paper_id` | ResearchAI convention |
| `zotero_key` | Zotero item key |
| `citation_key` | Better BibTeX citation key |
| `doi` | Zotero DOI field |
| `status` | Corresponds to Zotero collection |
| `knowledge_status` | Derived from Zotero tags |

---

## 4. BibTeX Export Configuration

| Setting | Value |
|---|---|
| Auto-export | Enabled |
| Export format | BibTeX |
| Export target | `C:\ResearchAI\01_Literature\04_Literature_Index\bibliography.bib` |
| Include only tagged papers | `#done` or `#key-paper` |

---

## 5. Execution Checklist

- [ ] Create collections: `00_Inbox`, `01_Screening`, `02_Reading`, `03_Deep_Read`, `04_Core`, `Archive`
- [ ] Assign initial tags to test papers
- [ ] Configure BibTeX export target
- [ ] Import Phase 1 paper (`2024_Monteiro_LiteratureReview`) into `00_Inbox`
- [ ] Import Phase 2 paper (`2020_Chai_SeismicPhasePicking`) into `00_Inbox`
- [ ] Verify Literature Index row creation for each paper
