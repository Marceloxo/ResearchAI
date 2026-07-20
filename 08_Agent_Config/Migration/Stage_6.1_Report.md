# Stage 6.1 Report — Extend Paper Processing Registry for Agent State

**Date**: 2026-07-18
**Status**: COMPLETE
**Author**: scan_registry.py automated generation

---

## Objective

Extend the Paper Processing Registry (Paper_Processing_State.yaml) with an `agent_state` field
to track KnowledgeVault processing progress for each paper, enabling AI agents to determine
which papers need further processing.

## Changes Made

### 1. Schema Extension: `agent_state` Field

Added `agent_state` dict to every paper entry in the registry with 4 fields:

| Field | Maps To | Description |
|---|---|---|
| `literature_card` | `_card.md` files | Level 1 literature screening |
| `deep_read` | `_note.md` files | Level 2 deep analysis |
| `method_extraction` | `_method.md` files | Level 2 method documentation |
| `obsidian_note` | `_logic.md` files | Level 3 argument mining |

Each field uses one of three states:
- **PENDING** — not yet started
- **IN_PROGRESS** — currently being processed
- **COMPLETE** — file exists in KnowledgeVault

### 2. Updated `scan_registry.py`

New functions added:

- **`extract_title_from_kv_file(filepath)`** — Extracts paper title from KnowledgeVault files,
  handling both YAML frontmatter (with BOM stripping) and `# Title:` fallback format.

- **`scan_knowledgevault()`** — Scans `02_KnowledgeVault/01_Papers/` for all card/note/method/logic/survey files,
  extracts titles and maps note types to agent_state fields.

- **`build_kv_to_paper_mapping(kv_files, zotero_papers)`** — Matches KnowledgeVault files to Zotero papers
  using a multi-strategy title matching algorithm:
  1. Exact match on cleaned titles
  2. Substring match (either direction)
  3. Keyword overlap scored by ratio (overlap / max(word_counts)) — prefers papers with higher title similarity

- **`assign_agent_state(state_map, paper_agent_state)`** — Assigns agent_state to each paper entry.

- **`compute_agent_summary(state_map)`** — Computes aggregate counts for agent_state fields.

- **`_strip_bom(text)`** / **`_clean_title(t)`** — Utility functions for BOM handling and title normalization.

### 3. Generated Registry

Updated [Paper_Processing_State.yaml](/home/lco/ResearchAI/08_Agent_Config/Paper_Processing_State.yaml) with:
- `agent_state` field on all 33 paper entries
- `agent_state` summary in the top-level summary section

## Results

### Agent State Summary

| Field | Complete | In Progress | Pending |
|---|---|---|---|
| `literature_card` | 11 | 0 | 22 |
| `deep_read` | 7 | 0 | 26 |
| `method_extraction` | 0 | 0 | 33 |
| `obsidian_note` | 0 | 0 | 33 |

### Breakdown

- **18 papers** have at least one KnowledgeVault file (18 with card, 7 with note)
- **6 papers** have no PDF in Zotero (MINERU_PENDING)
- **9 papers** have PDFs but no KnowledgeVault files yet

### Matched Papers

| Zotero Key | Title | literature_card | deep_read |
|---|---|---|---|
| 3HB6LAR9 | LandslideSegNet: an effective deep learning network for landslide segm | COMPLETE | PENDING |
| 5L2QLL47 | Using a Deep Neural Network and Transfer Learning to Bridge Scales for | PENDING | COMPLETE |
| 6HWKP8EC | A deeply supervised image fusion network for change detection in high  | PENDING | COMPLETE |
| 79AR33SX | BUILDING DISASTER DAMAGE ASSESSMENT IN SATELLITE IMAGERY WITH MULTI-TE | COMPLETE | PENDING |
| CY43XIQN | Automated deformation detection and interpretation using InSAR data an | PENDING | COMPLETE |
| FAA4JYRC | Rapid Characterization of the July 2019 Ridgecrest, California, Earthq | PENDING | COMPLETE |
| FGFVQ8EP | Landslide Detection and Segmentation Using Remote Sensing Images and D | PENDING | COMPLETE |
| JCKZQTYW | DTPP:An efficient depthwise separable TCN for seismic phase picking | COMPLETE | PENDING |
| JM2US4DM | Deep Learning for Automatic Detection of Volcanic and Earthquake-Relat | COMPLETE | PENDING |
| LY282M9N | Remote Sensing Image Change Detection With Transformers | COMPLETE | PENDING |
| N7UP2CZT | A Transformer-Based Siamese Network for Change Detection | PENDING | COMPLETE |
| SQT45NJU | Hybrid lightweight transformer for efficient landslide change detectio | COMPLETE | PENDING |
| TSQGFMA2 | SNUNet-CD: A Densely Connected Siamese Network for Change Detection of | PENDING | COMPLETE |
| VSG3K538 | PhaseNet: A Deep-Neural-Network-Based Seismic Arrival Time Picking Met | COMPLETE | PENDING |
| XYZBCLGH | Machine Learning in Earthquake Seismology | COMPLETE | PENDING |
| YQDJU2Y6 | Landslide4Sense: Reference Benchmark Data and Deep Learning Models for | COMPLETE | PENDING |
| YUB9FY6Q | Literature review on deep learning for the segmentation of seismic ima | COMPLETE | PENDING |
| ZN6HHVJ7 | Earthquake transformer—an attentive deep-learning model for simultaneo | COMPLETE | PENDING |

### Unmatched Papers (All PENDING)

| Zotero Key | Reason |
|---|---|
| FL6TSZPA | No PDF in Zotero |
| H9LQNVTM | No PDF in Zotero |
| II3UGDYS | No PDF in Zotero |
| PW86NPCG | No PDF in Zotero |
| YW7ADGN9 | No PDF in Zotero |
| YXFR9DZT | No PDF in Zotero |
| 43PF2JMB | PDF exists, no KV files |
| 5JGQ7YTL | PDF exists, no KV files |
| 7JZTDVB3 | PDF exists, no KV files |
| 89DCUBSH | PDF exists, no KV files |
| 8PQBD3RU | PDF exists, no KV files |
| D98KRK3B | PDF exists, no KV files |
| KGC7EEQX | PDF exists, no KV files |
| RIGVWYL3 | PDF exists, no KV files |
| VDGWT3R3 | PDF exists, no KV files |

## Design Decisions

### 1. Title Matching Algorithm

Used a 3-tier approach to handle title inconsistencies between Zotero and KnowledgeVault:
- Zotero titles may contain em-dashes (em-dash) that become joined words after cleaning
- KV files may have truncated titles or different punctuation
- Keyword overlap ratio scoring prevents false positives from generic terms like "earthquake"

### 2. Survey Files mapped to literature_card

Survey papers (e.g., `*_survey.md`) are mapped to `literature_card` since they serve
as Level 1 screening equivalents for broad-topic reviews.

### 3. BOM Handling

KnowledgeVault files created on Windows may have UTF-8 BOM prefix.
The `extract_title_from_kv_file()` function strips BOM before regex matching.

### 4. Fallback: # Title: Format

Some KV files use `# Title:` markdown format instead of YAML frontmatter.
The extractor tries YAML first, then falls back to hash-title format.

## File Inventory

| File | Action |
|---|---|
| [scan_registry.py](/home/lco/ResearchAI/04_Tools/mineru/scan_registry.py) | **Modified** — Added KnowledgeVault scanning and agent_state logic |
| [Paper_Processing_State.yaml](/home/lco/ResearchAI/08_Agent_Config/Paper_Processing_State.yaml) | **Regenerated** — Now includes agent_state on all 33 papers |
| [Stage_6.1_Report.md](/home/lco/ResearchAI/08_Agent_Config/Migration/Stage_6.1_Report.md) | **Created** — This file |

## Backward Compatibility

- All existing fields preserved (paper_key, att_key, title, mineru_state, etc.)
- New `agent_state` field is additive — does not modify any existing data
- Registry version remains 1.0 (schema extension, not breaking change)
- `scan_registry.py` retains all existing CLI options (--report, --filter)

## Rollback

To rollback to pre-Stage-6.1 state:
1. Restore `scan_registry.py` from backup: `cp scan_registry.py.bak scan_registry.py`
2. Regenerate registry: `python scan_registry.py`
3. The backup is at [scan_registry.py.bak](/home/lco/ResearchAI/04_Tools/mineru/scan_registry.py.bak)

## Next Steps

1. **KnowledgeVault processing** — Process the 9 papers with PDFs but no KV files
2. **Agent bootstrap integration** — Use agent_state to guide AI agents on which papers to process next
3. **IN_PROGRESS state** — Implement workflow for marking papers as being actively processed
4. **Batch automation** — Integrate scan_registry.py into the paper processing pipeline for automatic updates
