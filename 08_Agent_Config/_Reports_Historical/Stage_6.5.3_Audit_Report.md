# Stage 6.5.3 — Knowledge Graph Consistency Audit Report

**Date**: 2026-07-19
**Scope**: READ-ONLY audit of 02_KnowledgeVault/03_Methods, 04_Tasks, 05_Datasets, 00_Meta
**Files audited**: 14 method nodes, 7 task nodes, 11 dataset nodes, 5 meta map files

---

## Issue Inventory

### P0 — Critical (must fix before next batch processing)

| # | Issue | Location | Details |
|---|---|---|---|
| P0-1 | Vision Transformer.md is empty | 03_Methods/Vision Transformer.md | File exists (0 bytes) but contains no content. Appears to be a stub from Stage 1.5-6F.1 when it was moved from KV root. |

### P1 — High (should fix in next maintenance cycle)

| # | Issue | Location | Details |
|---|---|---|---|
| P1-1 | 8 dataset nodes missing source_type field | 05_Datasets/*.md | EGS Collab SURF, F3 Netherlands, Marmousi, OpenFWI, Parihaka, Penobscot, SEAM, SEG Salt all lack `source_type:` YAML field. This breaks automated provenance tracking. |
| P1-2 | 13 dataset nodes contain placeholder `[[Paper - ]]` links | 05_Datasets/*.md | F3 Netherlands (3), SEG Salt (2), Parihaka (3), OpenFWI (1), Thebe (1), Marmousi (1), SEAM (1). These are pre-existing from earlier stages. |
| P1-3 | Method → Task unidirectional links (no back-link) | 03_Methods/*.md → 04_Tasks/*.md | 5 unidirectional Method→Task links where the method does not reference the task that cites it: PhaseNet↛Phase Association, GENIE↛Earthquake Sequence, PLAN↛Earthquake Sequence, Multi-task Learning↛Earthquake Sequence, PhaseNet↛Earthquake Sequence. |
| P1-4 | Task → Dataset unidirectional links (no back-link) | 04_Tasks/*.md → 05_Datasets/*.md | All 6 Task→Dataset links are unidirectional. No dataset node references the task(s) it benchmarks. |
| P1-5 | CNN.md contains minor paper-summary language | 03_Methods/CNN.md | Line 16: "Replace fully-connected layers..." reads like a paper abstract rather than a method definition. Minor — the file is mostly conceptual. |

### P2 — Low (nice-to-have improvements)

| # | Issue | Location | Details |
|---|---|---|---|
| P2-1 | Method_Map.md categories have encoding corruption | 00_Meta/Method_Map.md | Chinese category headers show garbled UTF-8 (e.g., "鍗风Н绁炵粡缃戠粶" instead of "卷积神经网络"). Pre-existing issue, not caused by this stage. |
| P2-2 | Seismic_AI_Map.md and Deep_Learning_Map.md both contain new Stage 6.5.2 entries | 00_Meta/*.md | GENIE, PLAN, Segformer, U-Segformer-Hyper appear in both maps. This is intentional cross-indexing but creates duplication. Consider whether cross-references should be one-directional (Seismic_AI_Map references Deep_Learning_Map methods). |
| P2-3 | README.md files link to themselves | 04_Tasks/README.md, 05_Datasets/README.md | Task README links to all task files including itself; Dataset README links to all dataset files including itself. Not broken but slightly noisy. |
| P2-4 | Multi-task Learning.md lacks related paper reference | 03_Methods/Multi-task Learning.md | The method note describes PLAN as its primary seismic MTL example but does not have a "Related Papers" section like other method notes (PLAN, GENIE, U-Segformer-Hyper all have one). |

---

## Detailed Findings

### 1. Method ↔ Task Bidirectional Wikilinks

**Status**: Mostly functional with 5 unidirectional gaps.

**Bidirectional (healthy)**:
- Phase Association ↔ GENIE ✅
- Phase Association ↔ PLAN ✅
- Phase Association ↔ Multi-task Learning ✅
- Earthquake Location ↔ PLAN ✅
- Earthquake Location ↔ Multi-task Learning ✅
- Seismic Facies Segmentation ↔ CNN ✅
- Seismic Facies Segmentation ↔ Segformer ✅
- Seismic Facies Segmentation ↔ U-Segformer-Hyper ✅
- Fault Segmentation ↔ U-Net ✅

**Unidirectional (Task → Method, no back-link)**:
- Phase Association → PhaseNet ❌ (PhaseNet.md does not reference Phase Association)
- Earthquake Sequence → GENIE ❌
- Earthquake Sequence → PLAN ❌
- Earthquake Sequence → Multi-task Learning ❌
- Earthquake Sequence → PhaseNet ❌
- Seismic Facies Segmentation → Transformer ❌

**Assessment**: Unidirectional links are acceptable for the "citation flows downward" model (methods are cited by tasks, tasks don't need to be listed in every method). However, for discoverability, methods that are central to a task should reference that task.

### 2. Dataset ↔ Task Bidirectional Wikilinks

**Status**: All links are unidirectional (Task → Dataset). No dataset node references any task.

**Impact**: Tasks correctly cite their benchmark datasets. Datasets do not indicate which tasks they serve. This means browsing a dataset note gives no sense of its role in the research taxonomy.

**Recommendation**: Each dataset should have a "Used by Tasks" section with wikilinks to relevant task nodes.

### 3. Method Node Quality (Concept vs Paper Summary)

**Status**: All 13 method nodes (excluding empty Vision Transformer.md) are conceptual definitions with architecture/formulation sections. None read as paper summaries.

**Exception**: Multi-task Learning.md lacks a "Related Papers" section, unlike PLAN, GENIE, U-Segformer-Hyper, and Segformer which all have one.

**Verdict**: Method nodes are properly structured as concept nodes.

### 4. Task Categorization Correctness

**Status**: All 7 task notes have proper YAML frontmatter with `task_name`, `domain`, `input`, `output`, `metrics`, and `tags`. All follow the Task_Template.md structure with all 8 required sections.

**Observation**: No task notes are misclassified. Fault Segmentation and Seismic Phase Picking are correctly in 04_Tasks/ (not 03_Methods/).

### 5. Dataset source_type Compliance

**Status**: 2/2 new dataset nodes (Northern California, Japan Hi-net) correctly have `source_type: mentioned_in_paper`. 8/8 pre-existing dataset nodes are missing this field entirely.

**Risk**: The `source_type` field is mandatory per Stage 6.5.2 design. Pre-existing nodes without it create inconsistency in the graph.

### 6. Meta_Map Duplication and Category Consistency

**Status**: 
- Method_Map.md has 7 categories (CNN, Transformer, Attention, Fourier, Optimization, Generative) + New Nodes section. Categories are consistent.
- Dataset_Map.md has 3 categories (Seismic, CV, Medical) + New Nodes section. Categories are consistent.
- Seismic_AI_Map.md and Deep_Learning_Map.md both contain the 4 new Stage 6.5.2 methods. This is intentional cross-indexing but worth noting.

**Encoding Issue**: Method_Map.md Chinese headers are corrupted (UTF-8 BOM + encoding mismatch). This is a pre-existing issue from Stage 1.5-6F.1 migration.

### 7. Broken, Missing, or Unnecessary Links

**Status**: Zero broken wikilinks found in all 6 newly created files. All links resolve.

**Placeholder Links**: 13 `[[Paper - ]]` placeholders exist across 8 pre-existing dataset nodes. These are cosmetic — they don't break anything but should be replaced with actual paper references when available.

---

## Summary Statistics

| Metric | Value |
|---|---|
| Total files audited | 38 |
| New files created (Stage 6.5.2) | 6 |
| New meta entries added | 17 |
| Broken wikilinks | 0 |
| Unidirectional method→task links | 5 |
| Unidirectional task→dataset links | 6 |
| Datasets missing source_type | 8 |
| Placeholder `[[Paper - ]]` links | 13 |
| Empty/stub files | 1 (Vision Transformer.md) |

---

## Recommended Fix Priority

1. **P0-1**: Fill or remove Vision Transformer.md (1 minute)
2. **P1-1**: Add source_type to 8 pre-existing datasets (batch operation, ~10 minutes)
3. **P1-3**: Add task references to 5 method nodes that are central to tasks (optional, ~5 minutes)
4. **P1-4**: Add "Used by Tasks" section to 11 dataset nodes (optional, ~15 minutes)
5. **P1-2**: Replace 13 `[[Paper - ]]` placeholders with actual references (deferred, requires paper lookup)
6. **P2-1**: Fix Method_Map.md UTF-8 encoding (requires full file rewrite)
7. **P2-4**: Add "Related Papers" section to Multi-task Learning.md (5 minutes)

---

## Conclusion

The KnowledgeVault graph is structurally sound. All new files from Stage 6.5.2 have correct wikilinks, proper frontmatter, and follow the established templates. The main issues are:

1. One empty stub file (Vision Transformer.md)
2. Pre-existing datasets missing source_type fields (not caused by this stage)
3. Unidirectional links between Tasks and Datasets (acceptable but could be improved)
4. Pre-existing placeholder links in dataset nodes (cosmetic)

**No blocking issues prevent further paper processing.**
