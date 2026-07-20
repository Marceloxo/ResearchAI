# Stage 5.4 — Batch Dry Run Report

> **Generated**: 2026-07-17
> **Mode**: Dry Run (no execution)
> **Script**: `04_Tools/mineru/batch_process.py`
> **Status**: AWAITING APPROVAL

---

## Summary

| Metric | Count |
| --- | --- |
| Total Zotero papers with PDFs | 27 |
| Already processed (MinerU output exists) | 20 |
| Pending processing | 7 |
| Missing PDFs | 0 |
| Skipped (non-paper attachments) | 0 |

**Verdict**: All 7 pending papers have valid, unique PDFs in Zotero storage. No missing PDFs. No duplicates detected. Ready for production execution pending approval.

---

## Pending Papers Detail

| # | Zotero Key | Title | Attachment Key | PDF Exists |
| --- | --- | --- | --- | --- |
| 1 | XYZBCLGH | Machine Learning in Earthquake Seismology (Mousavi & Beroza 2023) | M8TB5AYY | Yes |
| 2 | KGC7EEQX | 3D fault architecture controls the dynamism of earthquake swarms (Ross et al.) | 94NARCAD | Yes |
| 3 | ZN6HHVJ7 | Earthquake transformer—an attentive deep-learning model (Mousavi et al. 2020) | QKMKLG2N | Yes |
| 4 | 43PF2JMB | Machine-Learning-Based High-Resolution Earthquake Catalog (Tan et al. 2021) | JEIK5MKZ | Yes |
| 5 | D98KRK3B | Machine-Learning-Based Analysis of Guy-Greenbrier Earthquakes (Park et al. 2020) | VPZLHRS4 | Yes |
| 6 | FAA4JYRC | Rapid Characterization of the Ridgecrest Sequence (Liu et al. 2020) | K9XWQTIL | Yes |
| 7 | VSG3K538 | PhaseNet: A Deep-Neural-Network-Based Seismic Arrival Time Picking (Zhu & Beroza 2018) | 2U6E8WAQ | Yes |

---

## Already Processed Papers (20)

| Zotero Key | Title | Attachment Key | MinerU Folder |
| --- | --- | --- | --- |
| JCKZQTYW | DTPP (Lv & Peng 2026) | IATKSLBG | Lv和Peng - 2026 - DTPP... |
| CY43XIQN | InSAR ViT model (Abdallah et al. 2024) | 76SW77W3 | Abdallah 等 - 2024... |
| JM2US4DM | InSAR Deformation DL (Liu et al. 2025) | JXS7GPZW | Liu 等 - 2025... |
| FGFVQ8EP | Landslide UNet (Le et al. 2023) | NCKCP6BS | 2312.16717v1.pdf... |
| LY282M9N | RS Change Detection (Chen et al. 2022) | 46C4TYYR | Chen 等 - 2022... |
| TSQGFMA2 | SNUNet-CD (Fang et al. 2022) | 6VTKJ8W2 | Fang 等 - 2022... |
| 6HWKP8EC | DS-IFN Change Detection (Zhang et al. 2020) | UL36XRSA | Zhang 等 - 2020... |
| YQDJU2Y6 | Landslide4Sense (Ghorbanzadeh et al. 2022) | RRC82BEC | Ghorbanzadeh 等 - 2022... |
| 3HB6LAR9 | LandslideSegNet (Senar & Ergen 2024) | UJ95QNW9 | Senar和Ergen - 2024... |
| SQT45NJU | Hybrid Transformer Landslide (Yadav et al. 2025) | 3ZLDQRA3 | Yadav 等 - 2025... |
| 79AR33SX | Disaster Damage Fusion (Weber & Kan 2020) | AJINC2AY | Weber和Kan - 2020... |
| N7UP2CZT | ChangeFormer (Bandara & Patel 2022) | 2XQFZKZN | Bandara和Patel - 2022... |
| 7JZTDVB3 | All-in-one seismic phase (Si et al. 2024) | LDQ9IIMY | Si 等 - 2024... |
| 89DCUBSH | Kahramanmaras seismicity (Ding et al. 2023) | RDXHK4FQ | Ding 等 - 2023... |
| RIGVWYL3 | Yangbi Foreshock 2022 (Zhou et al. 2022) | LM3S7TX8 | Zhou 等 - 2022... |
| 5JGQ7YTL | Yangbi Catalog 2021 (Zhou et al. 2021) | LDQ9IIMY | Zhou 等 - 2021... |
| VDGWT3R3 | EQA GNN (McBrearty & Beroza 2023) | PKGESHPH | McBrearty和Beroza - 2023... |
| 8PQBD3RU | Seismic Facies Segmentation | 2ZVY52Y6 | Seismic Facies Segmentation... |
| YUB9FY6Q | Seismic Image Segmentation Review (Monteiro 2024) | SGUIYBB2 | Literature review on deep learning... |
| 5L2QLL47 | Chai 2020 Transfer Learning | 9W23DNVG | Chai 等 - 2020... |

---

## Duplicate Analysis

**Result: No duplicates detected.**

Verified via direct SQL query against Zotero database. Each of the 7 pending papers has a **unique attachment key** that does not conflict with any already-processed paper:

| Pending Key | Att Key | Title | Conflicts with existing? |
| --- | --- | --- | --- |
| XYZBCLGH | M8TB5AYY | Machine Learning in Earthquake Seismology | No — unique PDF |
| KGC7EEQX | 94NARCAD | 3D fault architecture controls swarm dynamism | No — unique PDF |
| ZN6HHVJ7 | QKMKLG2N | Earthquake transformer (Mousavi 2020) | No — unique PDF |
| 43PF2JMB | JEIK5MKZ | High-Res Earthquake Catalog (Tan 2021) | No — unique PDF |
| D98KRK3B | VPZLHRS4 | Guy-Greenbrier Earthquakes (Park 2020) | No — unique PDF |
| FAA4JYRC | K9XWQTIL | Ridgecrest Sequence (Liu 2020) | No — unique PDF |
| VSG3K538 | 2U6E8WAQ | PhaseNet (Zhu & Beroza 2018) | No — unique PDF |

> **Note**: Earlier preliminary analysis suggested possible duplicates due to attachment key overlap in a different query path. After rigorous verification using the exact `get_zotero_papers()` SQL query, all 7 papers confirmed as unique with distinct attachment keys and PDFs.

---

## Execution Plan (Pending Approval)

If approved, the batch processor will:
1. Process all 7 pending papers sequentially
2. Use MinerU CLI with: `pipeline backend + txt method + ch language + formula + table`
3. Run normalization on each output
4. Log results to `MinerU_logs/`
5. Create folders at `MinerU_md/{pdf_basename}-{paper_key}/`

Expected output folders:
```
MinerU_md/
  Mousavi和Beroza - 2023 - Machine Learning in Earthquake Seismology.pdf-XYZBCLGH/
  Ross 等 - 3D fault architecture controls the dynamism of earthquake swarms.pdf-KGC7EEQX/
  Mousavi 等 - 2020 - Earthquake transformer...pdf-ZN6HHVJ7/
  Tan 等 - 2021 - Machine-Learning-Based...pdf-43PF2JMB/
  Park 等 - 2020 - Machine-Learning-Based Analysis...pdf-D98KRK3B/
  Liu 等 - 2020 - Rapid Characterization...pdf-FAA4JYRC/
  Zhu和Beroza - 2018 - PhaseNet...pdf-VSG3K538/
```

---

## Safety Constraints (per Stage 5.4.md)

- [x] Will NOT modify Zotero database
- [x] Will NOT modify Obsidian vault
- [x] Will NOT modify KnowledgeVault templates
- [x] Will NOT modify Agent skills
- [x] Will NOT rename existing MinerU folders
- [x] Will NOT delete old MinerU outputs
- [x] Will NOT change directory architecture
- [x] Will process sequentially (no parallelization)
- [x] Will NOT use VLM backend
- [x] Will strip proxy env vars before execution

---

## STOP — Awaiting Approval

Per Stage 5.4.md Step 1: "STOP after dry run. Wait for approval before actual execution."

**To proceed**, respond with approval to execute `python 04_Tools/mineru/batch_process.py --execute`.
