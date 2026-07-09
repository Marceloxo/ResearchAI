# Paper File Naming Rules

## Purpose

Define consistent, human-readable file naming for papers in the KnowledgeVault. This ensures agents can locate, deduplicate, and cross-reference paper notes reliably.

## Naming Convention

```
{author_lower}{year}_{title_first_keyword}_{type}.md
```

### Components

| Component | Rule | Example |
|---|---|---|
| `author_lower` | First author's last name, lowercase | `chai` |
| `year` | Publication year, 4 digits | `2020` |
| `title_first_keyword` | First meaningful keyword from the paper title, lowercase, underscores | `transfer_learning` |
| `type` | Note type identifier | `card`, `note`, `logic` |

### Examples

| Paper | File Name |
|---|---|
| Chai 2020, "Using a Deep Neural Network and Transfer Learning to Bridge Scales for Seismic Phase Picking" | `chai2020_transfer_learning_card.md` |
| Same paper, Paper Note | `chai2020_transfer_learning_note.md` |
| Same paper, Paper Logic | `chai2020_transfer_learning_logic.md` |
| Monteiro 2024, "Literature review on deep learning for the segmentation of seismic images" | `monteiro2024_deep_learning_card.md` |
| Same paper, Paper Note | `monteiro2024_deep_learning_note.md` |
| Same paper, Survey Note | `monteiro2024_deep_learning_survey.md` |
| Zhu & Beroza 2018, "PhaseNet" | `zhu2018_phasenet_card.md` |

## Collision Resolution

If two papers produce the same filename (same author, same year, same first keyword):

1. Add the **second meaningful keyword** from the title.
2. If still colliding, add a short distinguishing descriptor.

**Example collision:**
- Paper A: "Deep Learning for Fault Segmentation in Seismic Images"
- Paper B: "Deep Learning for Salt Body Segmentation in Seismic Images"

Both would initially map to `{author}{year}_deep_learning_{type}`.
Resolved:
- `{author}{year}_deep_learning_fault_{type}`
- `{author}{year}_deep_learning_salt_{type}`

## Rules

1. **Never use meaningless numbers** 鈥?no `paper1.md`, `doc_v2.md`, or UUID-based names.
2. **Always lowercase** 鈥?filenames must be case-insensitive friendly.
3. **Use underscores, not hyphens** 鈥?consistent separator.
4. **Human readable** 鈥?an agent or researcher should understand the filename without opening the file.
5. **Type suffix is mandatory** 鈥?`_card`, `_note`, `_survey`, `_logic` distinguish note types for the same paper.

## Three Independent Identifiers

Paper filename, Paper ID, and Citation Key are **completely independent**. Never confuse them.

| Identifier | Example | Where Used |
|---|---|---|
| **Filename** | chai2020_using_card.md | KnowledgeVault file system |
| **Paper ID** | 2020_Chai_SeismicPhasePicking | Internal tracking, Literature Index |
| **Citation Key** | chai2020using | Zotero/BibTeX, manuscript citations |

**Rule:** Filename is NOT Paper ID. Filename is NOT Citation Key. They are three separate identifiers.

---

## Identifier Separation

Three identifiers serve different purposes and are NOT interchangeable:

| Identifier | System | Example | Purpose |
|---|---|---|---|
| **Paper ID** (ResearchAI file name) | `02_KnowledgeVault/01_Papers/` | `chai2020_transfer_learning_note.md` | File organization, human readability |
| **Zotero Citation Key** | Better BibTeX | `chai2020using` | Academic citation in manuscripts |
| **Zotero Item Key** | Zotero internal | `9W23DNVG` | Immutable reference within Zotero |

**Rule:** These three are related but NOT required to match. The Literature Index maintains the mapping.

## Migration Note

Existing paper files in the vault use the old naming convention. Do NOT rename them during this stage. The new rules apply to all **new** papers created after Stage 1.5-6C.

