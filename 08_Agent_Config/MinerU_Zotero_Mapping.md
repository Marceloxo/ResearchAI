# MinerU 鈫?Zotero 鈫?KnowledgeVault Mapping

> **Purpose**: Trace every processed paper from its Zotero source through MinerU output to KnowledgeVault notes.
> **Maintained by**: Agent during batch processing.
> **Updated**: After each paper completes the pipeline.
> **Constraint**: Do not redesign this file's structure. Append rows as new papers are processed.

---

## Why This File Exists

During batch processing, it is critical to maintain a single-source traceability registry that connects:

1. **Zotero Item Key** 鈥?the immutable identity of the paper in the Zotero database
2. **PDF Filename** 鈥?the actual file stored in Zotero `storage/`
3. **MinerU Output Folder** 鈥?the extracted markdown directory on D: drive
4. **KnowledgeVault Files** 鈥?the notes created in `02_KnowledgeVault/01_Papers/`
5. **Processing Status** 鈥?whether the paper has been screened, deep-read, or argument-mined

Without this mapping, large-scale batch processing risks:
- Processing the same paper twice under different names
- Losing track of which papers have been imported to Zotero
- Creating orphaned KnowledgeVault files with no source traceability
- Mixing up papers with similar titles or authors

---

## Zotero-First Workflow Reference

```
Step 0: Verify paper exists in Zotero (Item Key confirmed)
Step 1: Verify PDF in Zotero storage/ (PDF Filename confirmed)
Step 2: Run MinerU on PDF 鈫?verify full.md in MinerU_md/ (MinerU Folder confirmed)
Step 3: Process through Decision Framework (Level 1 鈫?Level 2 鈫?Level 3)
Step 4: Create KnowledgeVault files (KV Files confirmed)
Step 5: Update this mapping file with all verified fields
Step 6: Set Status to PROCESSED
```

**Rule**: Every processed paper must have a verified entry in this file before KnowledgeVault creation is considered complete.

---

## Mapping Table

| Paper ID | Zotero Item Key | PDF Filename | MinerU Output Folder | KnowledgeVault Files | Status |
|---|---|---|---|---|---|
| chai2020_using | 9W23DNVG | chai2020.pdf | chai2020.pdf-a31f1ca0-679c-4ffc-9af2-56fde3f21605 | chai2020_using_card.md, chai2020_using_note.md | PROCESSED |
| zhu2018_phasenet | 2U6E8WAQ | zhu2018.pdf | zhu2018.pdf-b5963bad-6896-4b64-b218-3f9b5a4c92be | zhu2018_phasenet_card.md, zhu2018_phasenet_note.md | PROCESSED |
| monteiro2024_deep_learning | SGUIYBB2 | Literature-review-on-deep-learning-for-the-segmentation-of-seismic-images.pdf | Literature-review-on-deep-learning-for-the-segmentation-of-seismic-images.pdf-cb8637d0-3d99-4095-b574-428cb2308196 | monteiro2024_deep_learning_card.md, monteiro2024_deep_learning_survey.md | PROCESSED |
| mousavi2023_machine_learning | M8TB5AYY | annurev-earth-071822-100323.pdf | annurev-earth-071822-100323.pdf-9a70ce64-31d0-4383-8119-1f6ca9fbc69a | mousavi2023_machine_learning_card.md, mousavi2023_machine_learning_survey.md | PROCESSED |
| mousavi2020_eqtransformer | QKMKLG2N | mousavi2020.pdf | mousavi2020.pdf-1e8cf44d-14b9-4217-8b73-5bd9f30165a3 | mousavi2020_eqtransformer_card.md, mousavi2020_eqtransformer_note.md | PROCESSED |
| liu2020_ridgecrest | K9XWQTIL | liu2020.pdf | liu2020.pdf-de81d3ee-26c7-4d08-a1a8-0e945a65544c | liu2020_ridgecrest_card.md, liu2020_ridgecrest_note.md | PROCESSED |

---

| abdallah2024_inasar_vit | 76SW77W3 | Abdallah 等 - 2024 - Automated deformation...pdf | Abdallah 等 - 2024 - ...pdf-bd0d85e1... | abdallah2024_inasar_vit_card.md, abdallah2024_inasar_vit_note.md | C1 |
| liu2025_insar_deformation | JXS7GPZW | Liu 等 - 2025 - Deep Learning...pdf | Liu 等 - 2025 - ...pdf-133bbcc3... | liu2025_insar_deformation_survey.md | A |
| chen2022_rs_transformer_cd | 46C4TYYR | Chen 等 - 2022 - Remote Sensing...pdf | Chen 等 - 2022 - ...pdf-0650cfba... | chen2022_rs_transformer_cd_survey.md | A |
| fang2022_snunet_cd | 6VTKJ8W2 | Fang 等 - 2022 - SNUNet-CD...pdf | Fang 等 - 2022 - ...pdf-a5830dbe... | fang2022_snunet_cd_card.md, fang2022_snunet_cd_note.md | C2 |
| zhang2020_ds_ifn_cd | UL36XRSA | Zhang 等 - 2020 - A deeply supervised...pdf | Zhang 等 - 2020 - ...pdf-6dbf493f... | zhang2020_ds_ifn_cd_card.md | C2 |
| ghorman2022_landslide4sense | RRC82BEC | Ghorbanzadeh 等 - 2022 - Landslide4Sense...pdf | Ghorbanzadeh 等 - 2022 - ...pdf-a4cfc830... | ghorman2022_landslide4sense_card.md | C1 |
| le2023_landslide_unet | NCKCP6BS | 2312.16717v1.pdf | 2312.16717v1.pdf-02e09c3b... | le2023_landslide_unet_card.md, le2023_landslide_unet_note.md | C1 |
| sener2024_landslidesegnet | UJ95QNW9 | ?ener和Ergen - 2024 - LandslideSegNet...pdf | ?ener和Ergen - 2024 - ...pdf-68ed30b6... | sener2024_landslidesegnet_card.md | C2 |
| yadav2025_hybrid_transformer | 3ZLDQRA3 | Yadav 等 - 2025 - Hybrid lightweight...pdf | Yadav 等 - 2025 - ...pdf-d50f131c... | yadav2025_hybrid_transformer_landslide_card.md, yadav2025_hybrid_transformer_landslide_note.md | C2 |
| weber2020_disaster_damage_fusion | AJINC2AY | Weber和Kan - 2020 - BUILDING DISASTER...pdf | Weber和Kan - 2020 - ...pdf-fb3486e9... | weber2020_disaster_damage_fusion_card.md | C1 |
| bandara2022_changeformer | 2XQFZKZN | Bandara和Patel - 2022 - A Transformer...pdf | Bandara和Patel - 2022 - ...pdf-4e820481... | bandara2022_changeformer_card.md, bandara2022_changeformer_note.md | C2 |
| lv2026_dttp | IATKSLBG | Lv和Peng - 2026 - DTPP...pdf | Lv和Peng - 2026 - ...pdf-6ec18a94... | lv2026_dttp_card.md | LEVEL_1_DONE |

## Status Definitions

| Status | Meaning |
|---|---|
| **PENDING_ZOTERO** | Paper has MinerU output but no verified Zotero record |
| **PENDING_MINERU** | Paper is in Zotero but MinerU has not been run |
| **LEVEL_1_DONE** | Literature Card created, awaiting Level 2 decision |
| **LEVEL_2_DONE** | Paper Note created, awaiting Level 3 decision |
| **LEVEL_3_DONE** | Paper Logic created (Argument Mining complete) |
| **PROCESSED** | Full pipeline complete (Level 1 + Level 2 or Level 3) |
| **FLAGGED** | Requires human review (see Manual Notes column) |
| **IGNORED** | Level 1 decision: paper not relevant, no further processing |

---

## Unprocessed Papers in MinerU Output

The following papers have MinerU output but are **not yet in this mapping** (not processed through KnowledgeVault):

| MinerU Output Folder | Estimated Paper | Zotero Status |
|---|---|---|
| park2020.pdf-5f7aa978-8ce1-4053-a175-20d3715d529c | park2020 (Guy-Greenbrier earthquake) | To verify |
| tsr-2021001.1.pdf-bd06980f-c9f3-4fa4-aeab-d0f6d6a33fb5 | TSR paper | To verify |
| Ross 2020 (seismic) | ross2020.pdf-319a04d4-c4bf-47b6-aeb8-ce3654d84eb3 | To verify |
| Ding et al. 2023 | Ding 绛?- 2023 - High-resolution... | To verify |
| McBrearty & Beroza 2023 | McBrearty鍜孊eroza - 2023 - Earthquake Phase Association... | To verify |
| Si et al. 2024 | Si 绛?- 2024 - An all-in-one seismic phase picking... | To verify |
| Zhou et al. 2021 | Zhou 绛?- 2021 - A high-resolution seismic catalog... | To verify |
| Zhou et al. 2022 | Zhou 绛?- 2022 - Seismological Characterization... | To verify |

> **Note**: These papers should be verified against Zotero storage/ before any batch processing begins.

---

## Maintenance Rules

1. **Append only**: Never delete or modify existing rows. Add new rows at the bottom.
2. **Verify before writing**: Confirm Zotero Item Key matches the actual Zotero database before recording.
3. **Update status sequentially**: A paper's status should only advance through the pipeline stages in order.
4. **Flag inconsistencies**: If a paper's MinerU folder cannot be matched to a Zotero PDF, mark as FLAGGED.
5. **Cross-check before batch**: Before running any batch, verify all rows in the "Unprocessed Papers" table against Zotero.


