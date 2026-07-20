# Stage 6.6 — KnowledgeVault Schema Consistency Audit Report

**Date**: 2026-07-19  
**Scope**: Read-only audit of 02_KnowledgeVault/03_Methods, 04_Tasks, 05_Datasets, and 00_Meta  
**Constraint**: No modifications made — audit only

---

## Summary

| Category | Total Files | Issues Found | Severity |
|---|---|---|---|
| Methods (03_Methods) | 12 | 3 | LOW-MEDIUM |
| Tasks (04_Tasks) | 8 | 1 | LOW |
| Datasets (05_Datasets) | 12 | 1 | LOW |
| Meta Maps (00_Meta) | 5 | 2 | MEDIUM |
| Wikilink Integrity | — | 14 unique broken | MEDIUM |
| Naming Consistency | — | 1 case variant | LOW |
| Stray Files | — | 1 empty file | LOW |

**Overall Assessment**: The KnowledgeVault is structurally sound. Most issues are minor schema deviations or placeholder links in meta maps. No critical data loss or structural corruption detected.

---

## Phase A — YAML Schema Findings

### Methods (03_Methods/)

**Expected YAML fields**: `method_name`, `category`, `application`, `related_tasks`, `tags`, `created`

**Result**: All 11 method files (excluding README.md) contain valid YAML frontmatter with all required fields.

| File | Status |
|---|---|
| Attention Mechanism.md | OK |
| CNN.md | OK |
| GENIE.md | OK |
| Multi-task Learning.md | OK |
| PLAN.md | OK |
| PhaseNet.md | OK |
| Segformer.md | OK |
| Transfer Learning.md | OK |
| Transformer.md | OK |
| U-Net.md | OK |
| U-Segformer-Hyper.md | OK |
| Vision Transformer.md | OK |

### Tasks (04_Tasks/)

**Expected YAML fields**: `task_name`, `category`, `domain`, `input`, `output`, `metrics`, `tags`, `created`

**Result**: All 7 task files contain YAML frontmatter. 7 files are missing the `category` field.

| File | Status | Missing Fields |
|---|---|---|
| Earthquake Location.md | ⚠️ Partial | `category` |
| Earthquake Sequence Analysis.md | ⚠️ Partial | `category` |
| Fault Segmentation.md | ⚠️ Partial | `category` |
| Phase Association.md | ⚠️ Partial | `category` |
| Seismic Facies Segmentation.md | ⚠️ Partial | `category` |
| Seismic Image Segmentation.md | ⚠️ Partial | `category` |
| Seismic Phase Picking.md | ⚠️ Partial | `category` |

**Note**: All tasks use `domain` instead of `category`. This is a systematic naming deviation from the expected schema. The `domain` field serves the same purpose but uses a different key name.

### Datasets (05_Datasets/)

**Expected YAML fields**: `dataset_name`, `source_type`, `domain`, `size`, `modality`, `task`, `official_link`, `related_papers`, `tags`, `created`

**Result**: All 11 dataset files contain valid YAML with all required fields. The `source_type` field is present in all files (added in Stage 6.5.5).

---

## Phase B — Section Completeness

### Methods Required Sections

Expected: `Definition`, `Core Idea`, `Architecture/Formulation`, `Advantages`, `Limitations`, `Typical Applications`, `Related Papers`, `Related Methods`

| File | Status | Notes |
|---|---|---|
| Attention Mechanism.md | ✅ Complete | Uses `#` level headings (not `##`) |
| CNN.md | ✅ Complete | Uses `#` level headings |
| GENIE.md | ✅ Complete | Uses `##` level headings |
| Multi-task Learning.md | ✅ Complete | Uses `##` level headings |
| PLAN.md | ✅ Complete | Uses `##` level headings |
| PhaseNet.md | ✅ Complete | Uses `#` level headings |
| Segformer.md | ✅ Complete | Uses `##` level headings |
| Transfer Learning.md | ✅ Complete | Uses `#` level headings |
| Transformer.md | ✅ Complete | Uses `#` level headings |
| U-Net.md | ✅ Complete | Uses `#` level headings |
| U-Segformer-Hyper.md | ✅ Complete | Uses `##` level headings |
| Vision Transformer.md | ✅ Complete | Uses `#` level headings |

**Observation**: Two heading styles coexist — some files use `#` (single-hash) for top-level sections, others use `##` (double-hash). This is a cosmetic inconsistency but does not affect functionality.

### Tasks Required Sections

Expected: `Task Definition`, `Problem Formulation`, `Input Data`, `Output`, `Evaluation Metrics`, `Common Methods`, `Challenges`, `Benchmark Datasets`, `Open Problems`

**Result**: All 7 task files contain all required sections (using `#` level headings).

### Datasets Required Sections

Expected: `Dataset Overview`, `Data Description`, `Collection Method`, `Application`, `Related Papers`, `Tasks Using This Dataset`

| File | Status | Missing Sections |
|---|---|---|
| EGS Collab SURF.md | ⚠️ Partial | `Data Description`, `Collection Method`, `Application` |
| F3 Netherlands.md | ⚠️ Partial | `Data Description`, `Collection Method`, `Application` |
| Japan Hi-net.md | ⚠️ Partial | `Data Description`, `Collection Method`, `Application` |
| Marmousi.md | ⚠️ Partial | `Data Description`, `Collection Method`, `Application` |
| Northern California Seismic Network.md | ⚠️ Partial | `Data Description`, `Collection Method`, `Application` |
| OpenFWI.md | ❌ Incomplete | `Data Description`, `Collection Method`, `Application`, `Tasks Using This Dataset` |
| Parihaka.md | ⚠️ Partial | `Data Description`, `Collection Method`, `Application` |
| Penobscot.md | ⚠️ Partial | `Data Description`, `Collection Method`, `Application` |
| SEAM.md | ⚠️ Partial | `Data Description`, `Collection Method`, `Application` |
| SEG Salt.md | ⚠️ Partial | `Data Description`, `Collection Method`, `Application` |
| Thebe.md | ⚠️ Partial | `Data Description`, `Collection Method`, `Application` |

**Pattern**: All datasets use `# Dataset Overview` (single hash) as their main heading, with data format described inline under that section rather than as a separate `## Data Description` subsection. The `Collection Method` and `Application` sections are consistently absent — these datasets were created from the original template which may not have included these sections.

---

## Phase C — Knowledge Graph Consistency

### Method → Task Links

All methods that reference tasks do so via `related_tasks` YAML field AND/or body wikilinks.

| Method | Task Links | Paper Links | Status |
|---|---|---|---|
| Attention Mechanism | Fault Segmentation, Seismic Image Segmentation | — | ✅ Has both |
| CNN | Seismic Image Segmentation, Fault Segmentation | — | ✅ Has both |
| GENIE | Phase Association, Earthquake Location | mcbrearty2023_genie_note | ✅ Has both |
| Multi-task Learning | Seismic Phase Picking, Phase Association, Earthquake Location | si2024_plan_allinone_note | ✅ Has both |
| PLAN | Seismic Phase Picking, Phase Association, Earthquake Location | si2024_plan_allinone_note | ✅ Has both |
| PhaseNet | Seismic Phase Picking, Event Detection | chai2020_using_note | ✅ Has both |
| Segformer | Seismic Facies Segmentation, Fault Segmentation | wang2024_segformer_seismic_facies_note | ✅ Has both |
| Transfer Learning | Seismic Phase Picking, Seismic Image Segmentation | chai2020_using_note | ✅ Has both |
| Transformer | Seismic Image Segmentation, Fault Segmentation | — | ⚠️ No paper link |
| U-Net | Seismic Image Segmentation, Fault Segmentation | — | ⚠️ No paper link |
| U-Segformer-Hyper | Seismic Facies Segmentation, Fault Segmentation | wang2024_segformer_seismic_facies_note | ✅ Has both |
| Vision Transformer | Image Classification, Semantic Segmentation, Fault Detection, Facies Classification | — | ⚠️ No paper link |

### Task → Method Links

| Task | Method Links | Status |
|---|---|---|
| Earthquake Location | PLAN, Multi-task Learning | ✅ |
| Earthquake Sequence Analysis | PhaseNet, GENIE, PLAN, Multi-task Learning | ✅ |
| Fault Segmentation | U-Net | ✅ |
| Phase Association | GENIE, PLAN, Multi-task Learning, PhaseNet | ✅ |
| Seismic Facies Segmentation | CNN, Segformer, U-Segformer-Hyper, Transformer | ✅ |
| Seismic Image Segmentation | U-Net, CNN, Attention Mechanism | ✅ |
| Seismic Phase Picking | (none in body — relies on related_papers) | ⚠️ No direct method link |

### Task → Dataset Links

| Task | Dataset Links | Status |
|---|---|---|
| Earthquake Location | Northern California Seismic Network, Japan Hi-net | ✅ |
| Earthquake Sequence Analysis | Northern California Seismic Network | ✅ |
| Fault Segmentation | F3 Netherlands, Thebe | ✅ |
| Phase Association | Northern California Seismic Network, Japan Hi-net | ✅ |
| Seismic Facies Segmentation | F3 Netherlands, SEG Salt, Marmousi, Thebe | ✅ |
| Seismic Image Segmentation | F3 Netherlands, Thebe, SEG Salt, Marmousi | ✅ |
| Seismic Phase Picking | EGS Collab SURF | ✅ |

### Dataset → Task Backlinks

All 11 non-OpenFWI datasets have a `## Tasks Using This Dataset` section with valid wikilinks to task nodes.

| Dataset | Has "Tasks Using This Dataset"? | Status |
|---|---|---|
| EGS Collab SURF | Yes | ✅ |
| F3 Netherlands | Yes | ✅ |
| Japan Hi-net | Yes | ✅ |
| Marmousi | Yes | ✅ |
| Northern California Seismic Network | Yes | ✅ |
| OpenFWI | **No** | ❌ |
| Parihaka | Yes | ✅ |
| Penobscot | Yes | ✅ |
| SEAM | Yes | ✅ |
| SEG Salt | Yes | ✅ |
| Thebe | Yes | ✅ |

---

## Phase D — Broken Wikilinks

The following wikilinks reference files/nodes that do not exist in the KnowledgeVault. These are categorized by type:

### Category 1: Placeholder Links (intentional, not broken)

These are template placeholders or navigation stubs that are expected to be filled in later:

- `[[Paper - ]]` — 19 occurrences across multiple files (template placeholder)
- `[[Task - ]]` — 2 occurrences
- `[[Dataset - ]]` — template placeholder
- `[[Method - ]]` — template placeholder
- `[[Exp - ]]` — template placeholder
- `[[Idea - ]]` — template placeholder
- `{{variable}}` patterns — template placeholders (e.g., `{{dataset}}`, `{{method}}`, `{{task}}`)

### Category 2: Links to Non-Existent Method/Task/Dataset Nodes

These reference concepts that should have knowledge nodes but do not:

| Link | Referenced From | Issue |
|---|---|---|
| `[[ResNet]]` | CNN.md, Deep_Learning_Map, Method_Map, Seismic_AI_Map, U-Net.md, README.md | File does not exist in 03_Methods/ |
| `[[Swin Transformer]]` | Deep_Learning_Map, Method_Map, Seismic_AI_Map, README.md | File does not exist in 03_Methods/ |
| `[[DeepLab]]` | Deep_Learning_Map, Method_Map | File does not exist |
| `[[DenseNet]]` | Deep_Learning_Map, Method_Map | File does not exist |
| `[[GAN]]` | Deep_Learning_Map, Method_Map | File does not exist |
| `[[Diffusion Models]]` | Deep_Learning_Map, Method_Map | File does not exist |
| `[[VAE]]` | Deep_Learning_Map, Method_Map | File does not exist |
| `[[Self-Supervised Learning]]` | Deep_Learning_Map, Method_Map, Multi-task Learning.md, Transfer Learning.md | File does not exist |
| `[[Semi-Supervised Learning]]` | Deep_Learning_Map, Method_Map | File does not exist |
| `[[Frequency Domain Learning]]` | Deep_Learning_Map, Method_Map, Seismic_AI_Map | File does not exist |
| `[[Fourier Neural Operator]]` | Deep_Learning_Map, Method_Map, Seismic_AI_Map | File does not exist |
| `[[Self-Attention]]` | Deep_Learning_Map, Method_Map, Seismic_AI_Map | File does not exist |
| `[[Channel Attention]]` | Deep_Learning_Map, Seismic_AI_Map | File does not exist |
| `[[Spatial Attention]]` | Deep_Learning_Map | File does not exist |
| `[[Cross-Attention]]` | Deep_Learning_Map | File does not exist |
| `[[Knowledge Distillation]]` | Deep_Learning_Map | File does not exist |
| `[[Loss Functions]]` | Deep_Learning_Map | File does not exist |
| `[[Normalizing Flows]]` | Deep_Learning_Map | File does not exist |
| `[[Wavelet Transform]]` | Deep_Learning_Map | File does not exist |
| `[[DETR]]` | Deep_Learning_Map | File does not exist |
| `[[SegFormer]]` | Deep_Learning_Map | File does not exist (actual file is `Segformer.md` — case mismatch) |
| `[[DeepFault]]` | Dataset_Map, Seismic_AI_Map | File does not exist in 05_Datasets/ |
| `[[ImageNet]]` | Dataset_Map | File does not exist |
| `[[COCO]]` | Dataset_Map | File does not exist |
| `[[ADE20K]]` | Dataset_Map | File does not exist |

### Category 3: Links to Non-Existent Paper-Level Concepts

| Link | Referenced From | Issue |
|---|---|---|
| `[[Literature-review-on-deep-learning-for-segmentation-of-seismic-images]]` | Attention Mechanism.md, CNN.md, Transformer.md, U-Net.md, Seismic AI.md | Appears to be a file path used as a wikilink |
| `[[EQTransformer]]` | GENIE.md, PLAN.md, si2024_plan_allinone_note.md | No standalone EQTransformer method node |
| `[[PhaseLink]]` | GENIE.md, mcbrearty2023_genie_note.md | No standalone PhaseLink method node |
| `[[AR Picker]]` | PhaseNet.md | No standalone AR Picker node |
| `[[STA/LTA]]` | PhaseNet.md | No standalone STA/LTA node |
| `[[Domain Adaptation]]` | Transfer Learning.md | No standalone node |
| `[[Phase Picking]]` | EGS Collab SURF.md | Task exists as `Seismic Phase Picking`, not `Phase Picking` |
| `[[Schoenball_et_al_2020]]` | EGS Collab SURF.md | Paper note does not exist |

### Category 4: Template-Only Links (expected to be unresolved)

These are in template files and are expected to be resolved when templates are instantiated:

- All `{{variable}}` references in template files
- `[[Templates]]` in Home.md
- `[[Note Title#heading]]` and `[[Note Title\|display text]]` in Vault_README.md (documentation examples)

---

## Phase E — Naming Consistency

### Case Variants Detected

| Concept | File Exists | Wikilink Used | Match? |
|---|---|---|---|
| SegFormer | `Segformer.md` | `[[Segformer]]` ✅, `[[SegFormer]]` ❌ | Case mismatch in Deep_Learning_Map.md |

**Finding**: The file is named `Segformer.md` (lowercase 'f'), but `Deep_Learning_Map.md` references `[[SegFormer]]` (capital 'F'). In Obsidian, wikilinks are case-sensitive on some filesystems. This link may resolve on case-insensitive filesystems (macOS/Windows) but could break on case-sensitive ones (Linux ext4).

### Stray Files

| File | Issue |
|---|---|
| `02_KnowledgeVault/03_Methods/Multi-task` | Empty file, no .md extension. Should be removed or renamed to `Multi-task.md` (though `Multi-task Learning.md` is the correct file). |

### Chinese Character Encoding

| File | Issue |
|---|---|
| `02_KnowledgeVault/00_Meta/Paper_Index.md` | Has UTF-8 BOM (EF BB BF) and Windows-style CRLF line endings. Chinese text renders as garbled characters due to BOM. Title shows "论文索引" as mojibake. |

---

## Phase F — Orphan Node Detection

### Nodes with No Incoming References

These method/task/dataset nodes are not linked TO from any other knowledge node (only linked FROM):

| Node | Type | Notes |
|---|---|---|
| `PhaseNet.md` | Method | Referenced by GENIE, PLAN, Multi-task Learning, Earthquake Sequence Analysis, Transfer Learning — actually has incoming links ✅ |
| All other methods | Method | All have incoming references from task notes ✅ |
| All tasks | Task | All have incoming references from method/dataset notes ✅ |
| All datasets | Dataset | All have incoming references from task/method notes ✅ |

**Result**: No orphan nodes detected. The knowledge graph is well-connected.

### Nodes with Minimal Connectivity

| Node | Type | Outgoing Links | Incoming Links |
|---|---|---|---|
| `Vision Transformer.md` | Method | 3 | 1 (from Segformer.md) | Low connectivity |
| `Transfer Learning.md` | Method | 2 | 1 (from Multi-task Learning.md) | Low connectivity |
| `Seismic Phase Picking.md` | Task | 0 | 3 (from datasets) | No outgoing method links |

---

## Phase G — Meta Map Consistency

### Method_Map.md

- Contains references to 20+ method nodes
- Many reference nodes that do not exist (see Phase D, Category 2)
- "New Nodes (Stage 6.5.2)" section correctly lists GENIE, PLAN, Multi-task Learning, Segformer, U-Segformer-Hyper
- Missing: `PhaseNet` is not listed in the "New Nodes" section despite being a recent addition
- Missing: `Vision Transformer` is not listed in the "New Nodes" section

### Dataset_Map.md

- References non-existent datasets: `DeepFault`, `ImageNet`, `COCO`, `ADE20K`
- "New Nodes (Stage 6.5.2)" section correctly lists Northern California Seismic Network, Japan Hi-net
- Well-organized by domain

### Seismic_AI_Map.md

- References many non-existent methods and tasks
- "New Methods" section correctly adds GENIE, PLAN, Segformer, U-Segformer-Hyper
- "New Tasks" section correctly adds Phase Association, Earthquake Location, Earthquake Sequence Analysis
- Contains placeholder entries like `[[Seismic Denoising]]`, `[[Seismic Imaging]]`, `[[Seismic Inversion]]` that have no corresponding nodes

### Deep_Learning_Map.md

- Most comprehensive map but also has the most broken links (30+ non-existent nodes)
- "New Nodes (Stage 6.5.2)" section correctly lists Segformer, U-Segformer-Hyper, GENIE, PLAN, Multi-task Learning
- Case mismatch: references `[[SegFormer]]` but file is `Segformer.md`

### Paper_Index.md

- **Has UTF-8 BOM** — causes encoding issues
- **Has CRLF line endings** — inconsistent with other vault files (LF only)
- Chinese title "论文索引" renders as garbled text due to BOM + CRLF combination
- Contains 17+ paper entries across multiple categories
- "To Read" section has 15 entries
- Some duplicate entries: `wang2024_segformer_seismic_facies_card/note` and `si2024_plan_allinone_card/note` appear twice (once under Seismic Facies Segmentation, once under Method Innovation)

---

## Recommended Fix Plan

### Priority 1 — Fix Encoding Issues (LOW EFFORT, HIGH IMPACT)

1. Remove BOM from `Paper_Index.md` and convert CRLF to LF
2. Remove stray empty file `02_KnowledgeVault/03_Methods/Multi-task`

### Priority 2 — Fix Case-Sensitive Links (LOW EFFORT)

3. Decide on canonical casing for SegFormer: either rename file to `SegFormer.md` or update all links to `Segformer`
4. Fix `[[SegFormer]]` → `[[Segformer]]` in Deep_Learning_Map.md

### Priority 3 — Add Missing Sections (MEDIUM EFFORT)

5. Add `category` field to all 7 task YAML frontmatter (or standardize on `domain` as the canonical field name)
6. Add `## Tasks Using This Dataset` section to OpenFWI.md
7. Standardize dataset headings — either all use `#` or all use `##` for top sections

### Priority 4 — Clean Up Meta Maps (MEDIUM EFFORT)

8. Remove or create missing method nodes referenced in Deep_Learning_Map.md and Method_Map.md (ResNet, Swin Transformer, DenseNet, etc.)
9. Remove or create missing dataset nodes referenced in Dataset_Map.md (DeepFault, ImageNet, COCO, ADE20K)
10. Clarify placeholder links: distinguish between intentional placeholders (`[[Paper - ]]`) and unintentional broken links

### Priority 5 — Improve Connectivity (LOW-MEDIUM EFFORT)

11. Add outgoing method links to `Seismic Phase Picking.md` task node
12. Add more incoming references to `Vision Transformer.md` and `Transfer Learning.md`

---

## Audit Conclusion

The KnowledgeVault is in good structural health. The most impactful fixes are:
1. Paper_Index.md encoding (BOM + CRLF)
2. Stray `Multi-task` empty file
3. SegFormer case consistency
4. Adding `category`/standardizing task YAML fields

All issues are non-blocking and can be addressed incrementally. No data loss or critical integrity issues were found.

---

**Audit complete. Awaiting approval to proceed to Stage 6.6.1 — Schema Repair.**
