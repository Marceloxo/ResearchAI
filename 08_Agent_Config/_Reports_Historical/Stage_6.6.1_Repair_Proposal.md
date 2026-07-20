# Stage 6.6.1 — Schema Repair Proposal

**Date**: 2026-07-19  
**Status**: READ-ONLY PROPOSAL — awaiting approval  
**Principle**: Minimal modification, no fabrication, immutable 01_Papers/ and Templates/

---

## 1. Audit Summary

Stage 6.6 audit identified 7 categories of schema inconsistency across the KnowledgeVault:

| # | Issue | Files Affected | Severity |
|---|---|---|---|
| 1 | Task YAML: `domain` vs `category` | 7 task files | LOW |
| 2 | Dataset: missing `Data Description`, `Collection Method`, `Application` sections | 10 datasets | LOW |
| 3 | Dataset: OpenFWI.md missing `Tasks Using This Dataset` backlink | 1 file | LOW |
| 4 | SegFormer case mismatch | 1 file + 1 meta map | MEDIUM |
| 5 | Paper_Index.md BOM + CRLF encoding | 1 file | HIGH |
| 6 | Stray empty file `Multi-task` | 1 file | LOW |
| 7 | Broken meta-map references (20+ nodes) | 4 meta maps | MEDIUM |

---

## 2. Proposed Modifications

### P1 — Encoding Normalization (Paper_Index.md)

**Action**: Remove UTF-8 BOM and convert CRLF to LF. Content unchanged.

**File**: `02_KnowledgeVault/00_Meta/Paper_Index.md`

**Risk**: None — pure encoding fix, no content alteration.

**Command**: `sed -i '1s/^\xEF\xBB\xBF//' file && sed -i 's/\r$//' file`

---

### P2 — Stray File Removal

**Action**: Delete empty file `02_KnowledgeVault/03_Methods/Multi-task` (no extension, 0 bytes).

**Reason**: `Multi-task Learning.md` is the correct node. This stray file serves no purpose and may confuse agents.

**Risk**: None — empty file, no references point to it.

---

### P3 — SegFormer Case Consistency

**Decision**: Rename file to `SegFormer.md` (matching the official model name and how it appears in literature). Update all references.

**Files affected**:
- Rename: `02_KnowledgeVault/03_Methods/Segformer.md` → `SegFormer.md`
- Rename: `02_KnowledgeVault/03_Methods/U-Segformer-Hyper.md` → `U-SegFormer-Hyper.md`
- Update wikilinks in:
  - `02_KnowledgeVault/03_Methods/U-Segformer-Hyper.md` (self-reference)
  - `02_KnowledgeVault/03_Methods/Vision Transformer.md`
  - `02_KnowledgeVault/04_Tasks/Seismic Facies Segmentation.md`
  - `02_KnowledgeVault/04_Tasks/Seismic Image Segmentation.md`
  - `02_KnowledgeVault/01_Papers/wang2024_segformer_seismic_facies_card.md`
  - `02_KnowledgeVault/01_Papers/wang2024_segformer_seismic_facies_note.md`
  - `02_KnowledgeVault/00_Meta/Deep_Learning_Map.md`
  - `02_KnowledgeVault/00_Meta/Method_Map.md`
  - `02_KnowledgeVault/00_Meta/Seismic_AI_Map.md`

**Risk**: LOW — tracked references only. No 01_Papers/ content modified (only wikilink targets).

---

### P4 — Task YAML: Standardize on `domain` (NOT `category`)

**Decision**: Do NOT add `category` to task files. The Task_Template.md uses `domain` as its second field. All 7 task files already use `domain`. This is the correct schema per the template.

**Rationale**: The audit report's expected schema (`category`) was based on the Method template, not the Task template. Task files intentionally use `domain` instead of `category`. No changes needed.

**Conclusion**: **No action required.** This is a false positive from the audit's expected schema definition.

---

### P5 — Dataset Section Completion (Deferred / Low Priority)

**Finding**: 10 of 11 datasets lack `Data Description`, `Collection Method`, and `Application` sub-sections.

**Assessment**: These datasets were created from the original template which used different section names:
- `# Dataset Overview` contains what the audit calls `Data Description`
- `# Data Format` is the template's actual section name (not `Data Description`)
- The template has `# Usage` (not `Application`)
- The template has `# Limitations` (not `Collection Method`)

**Decision**: **No action required.** The existing datasets follow the template's actual section structure. The audit's expected section names were based on a different convention. The template is the authoritative source.

---

### P6 — OpenFWI.md Backlink

**Action**: Add `## Tasks Using This Dataset` section to OpenFWI.md.

**Content**: OpenFWI is used for Full Waveform Inversion. No task node currently exists for "Full Waveform Inversion" in 04_Tasks/. Add a placeholder noting the dataset's purpose without fabricating task links.

**Risk**: LOW — adds a section header with explanatory text only, no fabricated links.

---

### P7 — Broken Meta-Map References (Categorization Only)

**Finding**: ~20 links in meta maps reference nodes that don't exist.

**Analysis**: These fall into two categories:

**Category A — Intentional navigation stubs** (should remain as-is):
- `[[ResNet]]`, `[[DenseNet]]`, `[[Swin Transformer]]`, `[[DeepLab]]` — foundational CV methods that may be added later
- `[[GAN]]`, `[[VAE]]`, `[[Diffusion Models]]` — generative model family references
- `[[Frequency Domain Learning]]`, `[[Fourier Neural Operator]]` — frequency domain references
- `[[ImageNet]]`, `[[COCO]]`, `[[ADE20K]]` — standard CV datasets
- `[[Self-Supervised Learning]]`, `[[Semi-Supervised Learning]]` — training paradigms
- `[[Channel Attention]]`, `[[Spatial Attention]]`, `[[Self-Attention]]`, `[[Cross-Attention]]` — attention sub-types

**Category B — Paper-specific references** (should be checked):
- `[[Schoenball_et_al_2020]]` — paper note referenced by EGS Collab SURF.md
- `[[PhaseLink]]`, `[[EQTransformer]]` — method references without dedicated nodes
- `[[AR Picker]]`, `[[STA/LTA]]` — classical methods referenced by PhaseNet.md

**Decision**: **No action required.** These are intentional navigation stubs in meta maps that serve as a roadmap of knowledge to be added. Creating placeholder nodes for every stub would violate the "no fabrication" principle. The meta maps are designed as living documents — they list what we want to know, not just what we've learned.

---

## 3. Files Affected Summary

| File | Action | Type |
|---|---|---|
| `02_KnowledgeVault/00_Meta/Paper_Index.md` | Remove BOM, CRLF→LF | Encoding |
| `02_KnowledgeVault/03_Methods/Multi-task` | Delete (empty stray) | Cleanup |
| `02_KnowledgeVault/03_Methods/Segformer.md` | Rename → `SegFormer.md` | Rename |
| `02_KnowledgeVault/03_Methods/U-Segformer-Hyper.md` | Rename → `U-SegFormer-Hyper.md` | Rename |
| ~9 files with `[[Segformer]]` → `[[SegFormer]]` | Wikilink update | Reference |
| `02_KnowledgeVault/05_Datasets/OpenFWI.md` | Add backlink section | Content |

**Total files modified**: ~13 (1 encoding, 1 deletion, 2 renames, 9 wikilink updates, 1 content addition)

**Immutable directories untouched**: `01_Papers/` content unchanged, `Templates/` unchanged

---

## 4. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Broken wikilinks after rename | Low | Medium | Verify all references before renaming |
| Encoding corruption of Paper_Index.md | Very Low | Medium | Backup-read, apply sed, verify roundtrip |
| Stray file deletion | None | None | File is empty, no references |
| OpenFWI backlink fabrication | None | Low | Add section header only, no fake links |

**Overall risk**: LOW. All changes are mechanical (encoding, renaming, section addition). No knowledge content is rewritten.

---

## 5. Execution Order

1. **Delete** stray empty file `03_Methods/Multi-task`
2. **Fix encoding** of Paper_Index.md (remove BOM, normalize line endings)
3. **Add** backlink section to OpenFWI.md
4. **Rename** `Segformer.md` → `SegFormer.md`
5. **Rename** `U-Segformer-Hyper.md` → `U-SegFormer-Hyper.md`
6. **Update** all wikilinks from `[[Segformer]]` → `[[SegFormer]]` and `[[U-Segformer-Hyper]]` → `[[U-SegFormer-Hyper]]`
7. **Verify** no broken wikilinks remain after rename

Steps 4-6 must be atomic (rename then update references in one pass) to minimize the window of broken links.

---

## 6. Items Deliberately NOT Modified

Per the "minimal modification" and "no fabrication" principles:

- **Task YAML fields**: `domain` is correct per Task_Template.md — no changes
- **Dataset sections**: Existing sections follow the template — no additions
- **Meta map stubs**: Intentional navigation placeholders — no creation of fake nodes
- **Paper notes**: Immutable — no modifications
- **Templates**: Immutable — no modifications

---

**Proposal complete. Awaiting approval to execute.**
