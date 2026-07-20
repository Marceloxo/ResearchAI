# Stage 6.4.1 — MinerU Path Architecture Correction and Verification Report

**Date**: 2026-07-18
**Author**: Codex Agent
**Source Task**: Stage_6.3.2.md

---

## Architectural Statement

**Zotero/storage is the authoritative PDF source. MinerU_md is the authoritative Markdown output.**

- **PDF Source**: `/home/lco/ResearchAI_Data/Zotero/storage/<ZoteroKey>/*.pdf`
- **Markdown Output**: `/home/lco/ResearchAI_Data/Paper/MinerU_md/<paper>/full.md`
- **Deprecated Path**: `/home/lco/ResearchAI_Data/Paper/Origin_pdf` — DO NOT USE

---

## Verification Results

### 1. Wang 2023 — Seismic Facies Segmentation via Segformer

| Field | Status | Details |
|---|---|---|
| Zotero PDF | VERIFIED | `/home/lco/ResearchAI_Data/Zotero/storage/J2ML7W6A/Wang 等 - 2023 - Seismic Facies Segmentation via a Segformer-Based Specific Encoder–Decoder–Hypercolumns Scheme.pdf` (5.2 MB) |
| MinerU full.md | VERIFIED | `Seismic Facies Segmentation via a Segformer-Based...-8PQBD3RU/full.md` (343 lines) |
| KnowledgeVault Card | EXISTS | `wang2024_segformer_seismic_facies_card.md` |
| KnowledgeVault Note | MISSING | No `*_note.md` file found |
| KnowledgeVault Logic | MISSING | No `*_logic.md` file found |
| MinerU_Zotero_Mapping | MISSING | No entry found in mapping table |
| Zotero Item Key in Card | MISSING | Card does not contain Item Key field |

### 2. McBrearty 2023 — GENIE GNN Phase Association

| Field | Status | Details |
|---|---|---|
| Zotero PDF | VERIFIED | `/home/lco/ResearchAI_Data/Zotero/storage/2ZVY52Y6/McBrearty和Beroza - 2023 - Earthquake Phase Association with Graph Neural Networks.pdf` (13.4 MB) |
| MinerU full.md | VERIFIED | `McBrearty和Beroza - 2023 - Earthquake Phase Association...-de0530a4.../full.md` (573 lines) |
| KnowledgeVault Card | EXISTS | `mcbrearty2023_genie_card.md` |
| KnowledgeVault Note | MISSING | No `*_note.md` file found |
| KnowledgeVault Logic | MISSING | No `*_logic.md` file found |
| MinerU_Zotero_Mapping | PARTIAL | Row exists (line 104) but status is "To verify" — no Item Key recorded |
| Zotero Item Key in Card | MISSING | Card does not contain Item Key field |

---

## Findings Summary

### Path Architecture — CONFIRMED CORRECT

Both papers confirm the pipeline:
1. PDF stored in `Zotero/storage/<ZoteroKey>/` — **both verified**
2. MinerU extracts to `Paper/MinerU_md/<folder>/full.md` — **both verified**
3. KnowledgeVault cards exist but are incomplete — **see Issues below**

### Issues Identified

1. **No KnowledgeVault Notes created** — Both papers have only Literature Cards (Level 1). No Deep Read Notes (Level 2) or Paper Logics (Level 3) exist.
2. **No Zotero Item Keys recorded in cards** — Neither card contains a Zotero Item Key field, breaking traceability.
3. **Wang 2023 missing from MinerU_Zotero_Mapping.md** — No entry exists at all.
4. **McBrearty 2023 in mapping has no Item Key** — Row exists but status is "To verify" and no Item Key is recorded.
5. **Wang card year mismatch** — Card records year as 2024 (IEEE TGRS), but PDF filename references 2023. The paper was likely published online in 2023 and in print in 2024.

---

## MinerU Processing Plan

**No MinerU processing needed.** Both papers already have:
- Source PDF in Zotero storage (verified)
- MinerU output `full.md` (verified)

Per Stage 6.3.2.md constraints: *"Do NOT create Deep Read Notes yet."*

---

## Constraints Compliance

- [x] Did NOT modify templates
- [x] Did NOT create skills
- [x] Did NOT modify historical reports
- [x] Did NOT use Origin_pdf path
- [x] Did NOT create Deep Read Notes

---

## Conclusion

Both papers have complete PDF source (Zotero storage) and MinerU output (full.md). The pipeline path architecture is confirmed correct. However, both papers have incomplete KnowledgeVault entries — missing Zotero Item Keys, missing Notes, and incomplete mapping registry entries.

**Status**: MinerU path verification PASSED. KnowledgeVault completeness requires follow-up.
