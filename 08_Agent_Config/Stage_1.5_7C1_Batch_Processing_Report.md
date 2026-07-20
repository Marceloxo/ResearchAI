
---

# APPENDIX A: C:\ResearchAI\ Directory Listing

Compact tree of workspace directory. Excludes .obsidian/, __pycache__/, .git/ for token efficiency.

## Root Files
- AGENT_BOOTSTRAP.md (project bootstrap)
- PROJECT_STATUS.md (stage tracking)
- README.md (project design)
- research_config.yaml (data paths)

## Directory Tree

`
C:\ResearchAI\
├── .agents/                          [AI agent skills]
├── 00_Inbox/
│   └── README.md
├── 01_Literature/
│   ├── Citation_Management.md
│   ├── Literature_Intake_Template.md
│   ├── Paper_ID_Rules.md
│   ├── Processed_Markdown_Template.md
│   ├── README.md
│   ├── 00_Inbox/
│   │   └── README.md
│   ├── 01_PDFs/                     [DEPRECATED — placeholder]
│   │   └── README.md
│   ├── 02_MinerU_Output/            [DEPRECATED — placeholder]
│   │   └── README.md
│   ├── 03_Processed_Markdown/       [DEPRECATED — placeholder]
│   │   └── README.md
│   ├── 04_Literature_Index/
│   │   ├── Literature_Index.md
│   │   └── README.md
│   ├── Markdown/                    [DEPRECATED — empty]
│   ├── PDFs/                        [DEPRECATED — empty]
│   └── References/
│       └── bibliography.bib
├── 02_KnowledgeVault/
│   ├── README.md
│   ├── Vault_README.md
│   ├── 00_Meta/                     [Navigation: MOCs, indexes, maps]
│   │   ├── Dataset_Map.md
│   │   ├── Deep_Learning_Map.md
│   │   ├── Experiment_Index.md
│   │   ├── Home.md
│   │   ├── Idea_Index.md
│   │   ├── Linking_Rules.md
│   │   ├── Method_Map.md
│   │   ├── Paper_Index.md           [← UPDATE AFTER BATCH]
│   │   ├── README.md
│   │   ├── Research_Map.md
│   │   ├── Seismic_AI_Map.md
│   │   ├── Tag_System.md
│   │   └── Writing_System.md
│   ├── 01_Papers/                   [Literature Cards, Notes, Surveys]
│   │   ├── abdallah2024_inasar_vit_card.md          [NEW — BATCH-001]
│   │   ├── bandara2022_changeformer_card.md         [NEW — BATCH-001]
│   │   ├── chai2020_using_card.md
│   │   ├── chai2020_using_note.md
│   │   ├── chen2022_rs_transformer_cd_survey.md     [NEW — BATCH-001]
│   │   ├── fang2022_snunet_cd_card.md               [NEW — BATCH-001]
│   │   ├── ghorman2022_landslide4sense_card.md      [NEW — BATCH-001]
│   │   ├── le2023_landslide_unet_card.md            [NEW — BATCH-001]
│   │   ├── liu2020_ridgecrest_card.md
│   │   ├── liu2020_ridgecrest_note.md
│   │   ├── liu2025_insar_deformation_survey.md      [NEW — BATCH-001]
│   │   ├── monteiro2024_deep_learning_card.md
│   │   ├── monteiro2024_deep_learning_survey.md
│   │   ├── mousavi2020_eqtransformer_card.md
│   │   ├── mousavi2020_eqtransformer_note.md
│   │   ├── mousavi2023_machine_learning_card.md
│   │   ├── mousavi2023_machine_learning_survey.md
│   │   ├── README.md
│   │   ├── sener2024_landslidesegnet_card.md        [NEW — BATCH-001]
│   │   ├── weber2020_disaster_damage_fusion_card.md [NEW — BATCH-001]
│   │   ├── yadav2025_hybrid_transformer_landslide_card.md [NEW — BATCH-001]
│   │   ├── zhang2020_ds_ifn_cd_card.md              [NEW — BATCH-001]
│   │   ├── zhu2018_phasenet_card.md
│   │   └── zhu2018_phasenet_note.md
│   ├── 02_Topics/
│   │   ├── README.md
│   │   └── Seismic AI.md
│   ├── 03_Methods/                  [Algorithm/method descriptions]
│   │   ├── Attention Mechanism.md
│   │   ├── CNN.md
│   │   ├── PhaseNet.md
│   │   ├── README.md
│   │   ├── Transfer Learning.md
│   │   ├── Transformer.md
│   │   ├── U-Net.md
│   │   └── Vision Transformer.md
│   ├── 04_Tasks/                    [Task definitions]
│   │   ├── Fault Segmentation.md
│   │   ├── README.md
│   │   ├── Seismic Image Segmentation.md
│   │   └── Seismic Phase Picking.md
│   ├── 05_Datasets/                 [Dataset registries]
│   │   ├── EGS Collab SURF.md
│   │   ├── F3 Netherlands.md
│   │   ├── Marmousi.md
│   │   ├── OpenFWI.md
│   │   ├── Parihaka.md
│   │   ├── Penobscot.md
│   │   ├── README.md
│   │   ├── SEAM.md
│   │   ├── SEG Salt.md
│   │   └── Thebe.md
│   ├── 06_Experiments/
│   │   ├── exp_chai2020_phase_picking.md
│   │   └── README.md
│   ├── 07_Ideas/
│   │   └── README.md
│   ├── 08_Writing/
│   │   └── README.md
│   ├── 09_Paper_Logic/              [Argument Mining analysis]
│   │   ├── chai2020_paper_logic.md              [DEPRECATED]
│   │   ├── chai2020_using_logic.md
│   │   └── README.md
│   ├── HumanRead_AgentIgnore/       [Human-readable docs, ignored by agents]
│   │   ├── current_v1.0.md
│   │   ├── current_v2.0.md
│   │   ├── current_v2.0_中文介绍.md
│   │   ├── GPT推荐研究方向.md
│   │   └── 未命名.md
│   └── Templates/                   [10 templates + README]
│       ├── Dataset_Template.md
│       ├── Experiment_Template.md
│       ├── Idea_Template.md
│       ├── Literature_Card_Template.md
│       ├── Method_Template.md
│       ├── Paper_Logic_Template.md
│       ├── Paper_Template.md
│       ├── README.md
│       ├── Survey_Template.md
│       ├── Task_Template.md
│       └── Writing_Template.md
├── 03_Projects/
│   └── README.md
├── 04_Tools/
│   ├── Data_Storage_Architecture.md
│   ├── README.md
│   └── Zotero/
│       ├── metadata_mapping.md
│       ├── README.md
│       ├── Zotero_Deployment_Record.md
│       ├── Zotero_Setup_Guide.md
│       ├── Zotero_Storage_Strategy.md
│       └── Zotero_Workflow_Configuration.md
├── 05_Experiments/
│   └── README.md
├── 06_Writing/
│   └── README.md
├── 07_Research_Ideas/
│   └── README.md
└── 08_Agent_Config/                 [Agent instructions, rules, workflows]
    ├── ADR_Zotero_PDF_Centered_Architecture.md
    ├── Batch_Processing_Guideline.md
    ├── Batch_Processing_Log.md
    ├── Current_State_Check.md
    ├── Data_Migration_Plan.md
    ├── Literature_Intake_Workflow.md
    ├── Literature_Processing_Strategy.md
    ├── Markdown_Processing_Workflow.md
    ├── MinerU_Cleaning_Rules.md
    ├── MinerU_Workflow_Status.md
    ├── MinerU_Zotero_Mapping.md        [← UPDATED: +11 rows]
    ├── Missing_Data_Report.md
    ├── Paper_Card_Guideline.md
    ├── Paper_File_Naming_Rules.md
    ├── Paper_Logic_Guideline.md
    ├── Paper_Processing_Decision_Framework.md
    ├── README.md
    ├── ResearchAI_Data_Flow_Architecture.md
    ├── ResearchAI_Design_Principles.md
    ├── Single_Paper_End_to_End_Test.md
    ├── Stage_1.4A_Test_Report.md
    ├── Stage_1.4C3_2_Zotero_Status_Report.md
    ├── Stage_1.4C3_3_Zotero_Storage_Confirmation.md
    ├── Stage_1.5_2_Closed_Loop_Validation_Report.md
    ├── Stage_1.5_6B_Real_Paper_Stress_Test.md
    ├── Stage_1.5_6D1_Architecture_Verification_Report.md
    ├── Stage_1.5_6F_Architecture_Audit_Report.md
    ├── Stage_1.5_6F1_Architecture_Cleanup_Report.md
    ├── Stage_1.5_7A_Preparation_Report.md
    ├── Stage_1.5_7B_Architecture_Freeze_Audit_Report.md
    ├── Stage_1.5_7B_Freeze_Confirmation.md
    ├── Stage_1.5_Single_Paper_Validation_Protocol.md
    ├── Stage_1.5_7C1_Batch_Processing_Report.md  [NEW — this file]
    ├── Stress_Test_Execution_Log.md
    ├── Workspace_Cleanup_Plan.md
    ├── Zotero_Integration_Design.md
    └── Zotero_Test_Plan.md
`

## File Counts

| Directory | Files | Notes |
|---|---|---|
| 00_Inbox/ | 1 | README.md placeholder |
| 01_Literature/ | 9 + 5 deprecated dirs | 5 deprecated dirs are empty placeholders |
| 02_KnowledgeVault/00_Meta/ | 13 | Navigation layer |
| 02_KnowledgeVault/01_Papers/ | 24 | 17 papers + 7 templates/README |
| 02_KnowledgeVault/02_Topics/ | 2 | 1 topic + README |
| 02_KnowledgeVault/03_Methods/ | 8 | 7 methods + README |
| 02_KnowledgeVault/04_Tasks/ | 4 | 3 tasks + README |
| 02_KnowledgeVault/05_Datasets/ | 10 | 9 datasets + README |
| 02_KnowledgeVault/06_Experiments/ | 2 | 1 experiment + README |
| 02_KnowledgeVault/07_Ideas/ | 1 | README only |
| 02_KnowledgeVault/08_Writing/ | 1 | README only |
| 02_KnowledgeVault/09_Paper_Logic/ | 3 | 2 logics + README |
| 02_KnowledgeVault/Templates/ | 11 | 10 templates + README |
| 03_Projects/ | 1 | README only |
| 04_Tools/ | 8 | Zotero scripts + docs |
| 05_Experiments/ | 1 | README only |
| 06_Writing/ | 1 | README only |
| 07_Research_Ideas/ | 1 | README only |
| 08_Agent_Config/ | 36 | Agent rules, configs, reports |

---

# APPENDIX A: C:\ResearchAI\ Directory Listing

Compact tree of workspace directory. Excludes .obsidian/, __pycache__/, .git/ for token efficiency.

## Root Files
- AGENT_BOOTSTRAP.md (project bootstrap)
- PROJECT_STATUS.md (stage tracking)
- README.md (project design)
- research_config.yaml (data paths)

## Directory Tree

`
C:\ResearchAI\
├── .agents/                          [AI agent skills]
├── 00_Inbox/
│   └── README.md
├── 01_Literature/
│   ├── Citation_Management.md
│   ├── Literature_Intake_Template.md
│   ├── Paper_ID_Rules.md
│   ├── Processed_Markdown_Template.md
│   ├── README.md
│   ├── 00_Inbox/
│   │   └── README.md
│   ├── 01_PDFs/                     [DEPRECATED — placeholder]
│   │   └── README.md
│   ├── 02_MinerU_Output/            [DEPRECATED — placeholder]
│   │   └── README.md
│   ├── 03_Processed_Markdown/       [DEPRECATED — placeholder]
│   │   └── README.md
│   ├── 04_Literature_Index/
│   │   ├── Literature_Index.md
│   │   └── README.md
│   ├── Markdown/                    [DEPRECATED — empty]
│   ├── PDFs/                        [DEPRECATED — empty]
│   └── References/
│       └── bibliography.bib
├── 02_KnowledgeVault/
│   ├── README.md
│   ├── Vault_README.md
│   ├── 00_Meta/                     [Navigation: MOCs, indexes, maps]
│   │   ├── Dataset_Map.md
│   │   ├── Deep_Learning_Map.md
│   │   ├── Experiment_Index.md
│   │   ├── Home.md
│   │   ├── Idea_Index.md
│   │   ├── Linking_Rules.md
│   │   ├── Method_Map.md
│   │   ├── Paper_Index.md           [← UPDATE AFTER BATCH]
│   │   ├── README.md
│   │   ├── Research_Map.md
│   │   ├── Seismic_AI_Map.md
│   │   ├── Tag_System.md
│   │   └── Writing_System.md
│   ├── 01_Papers/                   [Literature Cards, Notes, Surveys]
│   │   ├── abdallah2024_inasar_vit_card.md          [NEW — BATCH-001]
│   │   ├── bandara2022_changeformer_card.md         [NEW — BATCH-001]
│   │   ├── chai2020_using_card.md
│   │   ├── chai2020_using_note.md
│   │   ├── chen2022_rs_transformer_cd_survey.md     [NEW — BATCH-001]
│   │   ├── fang2022_snunet_cd_card.md               [NEW — BATCH-001]
│   │   ├── ghorman2022_landslide4sense_card.md      [NEW — BATCH-001]
│   │   ├── le2023_landslide_unet_card.md            [NEW — BATCH-001]
│   │   ├── liu2020_ridgecrest_card.md
│   │   ├── liu2020_ridgecrest_note.md
│   │   ├── liu2025_insar_deformation_survey.md      [NEW — BATCH-001]
│   │   ├── monteiro2024_deep_learning_card.md
│   │   ├── monteiro2024_deep_learning_survey.md
│   │   ├── mousavi2020_eqtransformer_card.md
│   │   ├── mousavi2020_eqtransformer_note.md
│   │   ├── mousavi2023_machine_learning_card.md
│   │   ├── mousavi2023_machine_learning_survey.md
│   │   ├── README.md
│   │   ├── sener2024_landslidesegnet_card.md        [NEW — BATCH-001]
│   │   ├── weber2020_disaster_damage_fusion_card.md [NEW — BATCH-001]
│   │   ├── yadav2025_hybrid_transformer_landslide_card.md [NEW — BATCH-001]
│   │   ├── zhang2020_ds_ifn_cd_card.md              [NEW — BATCH-001]
│   │   ├── zhu2018_phasenet_card.md
│   │   └── zhu2018_phasenet_note.md
│   ├── 02_Topics/
│   │   ├── README.md
│   │   └── Seismic AI.md
│   ├── 03_Methods/                  [Algorithm/method descriptions]
│   │   ├── Attention Mechanism.md
│   │   ├── CNN.md
│   │   ├── PhaseNet.md
│   │   ├── README.md
│   │   ├── Transfer Learning.md
│   │   ├── Transformer.md
│   │   ├── U-Net.md
│   │   └── Vision Transformer.md
│   ├── 04_Tasks/                    [Task definitions]
│   │   ├── Fault Segmentation.md
│   │   ├── README.md
│   │   ├── Seismic Image Segmentation.md
│   │   └── Seismic Phase Picking.md
│   ├── 05_Datasets/                 [Dataset registries]
│   │   ├── EGS Collab SURF.md
│   │   ├── F3 Netherlands.md
│   │   ├── Marmousi.md
│   │   ├── OpenFWI.md
│   │   ├── Parihaka.md
│   │   ├── Penobscot.md
│   │   ├── README.md
│   │   ├── SEAM.md
│   │   ├── SEG Salt.md
│   │   └── Thebe.md
│   ├── 06_Experiments/
│   │   ├── exp_chai2020_phase_picking.md
│   │   └── README.md
│   ├── 07_Ideas/
│   │   └── README.md
│   ├── 08_Writing/
│   │   └── README.md
│   ├── 09_Paper_Logic/              [Argument Mining analysis]
│   │   ├── chai2020_paper_logic.md              [DEPRECATED]
│   │   ├── chai2020_using_logic.md
│   │   └── README.md
│   ├── HumanRead_AgentIgnore/       [Human-readable docs, ignored by agents]
│   │   ├── current_v1.0.md
│   │   ├── current_v2.0.md
│   │   ├── current_v2.0_中文介绍.md
│   │   ├── GPT推荐研究方向.md
│   │   └── 未命名.md
│   └── Templates/                   [10 templates + README]
│       ├── Dataset_Template.md
│       ├── Experiment_Template.md
│       ├── Idea_Template.md
│       ├── Literature_Card_Template.md
│       ├── Method_Template.md
│       ├── Paper_Logic_Template.md
│       ├── Paper_Template.md
│       ├── README.md
│       ├── Survey_Template.md
│       ├── Task_Template.md
│       └── Writing_Template.md
├── 03_Projects/
│   └── README.md
├── 04_Tools/
│   ├── Data_Storage_Architecture.md
│   ├── README.md
│   └── Zotero/
│       ├── metadata_mapping.md
│       ├── README.md
│       ├── Zotero_Deployment_Record.md
│       ├── Zotero_Setup_Guide.md
│       ├── Zotero_Storage_Strategy.md
│       └── Zotero_Workflow_Configuration.md
├── 05_Experiments/
│   └── README.md
├── 06_Writing/
│   └── README.md
├── 07_Research_Ideas/
│   └── README.md
└── 08_Agent_Config/                 [Agent rules, configs, workflows]
    ├── ADR_Zotero_PDF_Centered_Architecture.md
    ├── Batch_Processing_Guideline.md
    ├── Batch_Processing_Log.md
    ├── Current_State_Check.md
    ├── Data_Migration_Plan.md
    ├── Literature_Intake_Workflow.md
    ├── Literature_Processing_Strategy.md
    ├── Markdown_Processing_Workflow.md
    ├── MinerU_Cleaning_Rules.md
    ├── MinerU_Workflow_Status.md
    ├── MinerU_Zotero_Mapping.md        [← UPDATED: +11 rows]
    ├── Missing_Data_Report.md
    ├── Paper_Card_Guideline.md
    ├── Paper_File_Naming_Rules.md
    ├── Paper_Logic_Guideline.md
    ├── Paper_Processing_Decision_Framework.md
    ├── README.md
    ├── ResearchAI_Data_Flow_Architecture.md
    ├── ResearchAI_Design_Principles.md
    ├── Single_Paper_End_to_End_Test.md
    ├── Stage_1.4A_Test_Report.md
    ├── Stage_1.4C3_2_Zotero_Status_Report.md
    ├── Stage_1.4C3_3_Zotero_Storage_Confirmation.md
    ├── Stage_1.5_2_Closed_Loop_Validation_Report.md
    ├── Stage_1.5_6B_Real_Paper_Stress_Test.md
    ├── Stage_1.5_6D1_Architecture_Verification_Report.md
    ├── Stage_1.5_6F_Architecture_Audit_Report.md
    ├── Stage_1.5_6F1_Architecture_Cleanup_Report.md
    ├── Stage_1.5_7A_Preparation_Report.md
    ├── Stage_1.5_7B_Architecture_Freeze_Audit_Report.md
    ├── Stage_1.5_7B_Freeze_Confirmation.md
    ├── Stage_1.5_Single_Paper_Validation_Protocol.md
    ├── Stage_1.5_7C1_Batch_Processing_Report.md  [NEW — this file]
    ├── Stress_Test_Execution_Log.md
    ├── Workspace_Cleanup_Plan.md
    ├── Zotero_Integration_Design.md
    └── Zotero_Test_Plan.md
`

## File Counts

| Directory | Files | Notes |
|---|---|---|
| 00_Inbox/ | 1 | README.md placeholder |
| 01_Literature/ | 9 + 5 deprecated dirs | 5 deprecated dirs are empty placeholders |
| 02_KnowledgeVault/00_Meta/ | 13 | Navigation layer |
| 02_KnowledgeVault/01_Papers/ | 24 | 17 papers + README |
| 02_KnowledgeVault/02_Topics/ | 2 | 1 topic + README |
| 02_KnowledgeVault/03_Methods/ | 8 | 7 methods + README |
| 02_KnowledgeVault/04_Tasks/ | 4 | 3 tasks + README |
| 02_KnowledgeVault/05_Datasets/ | 10 | 9 datasets + README |
| 02_KnowledgeVault/06_Experiments/ | 2 | 1 experiment + README |
| 02_KnowledgeVault/07_Ideas/ | 1 | README only |
| 02_KnowledgeVault/08_Writing/ | 1 | README only |
| 02_KnowledgeVault/09_Paper_Logic/ | 3 | 2 logics + README |
| 02_KnowledgeVault/Templates/ | 11 | 10 templates + README |
| 03_Projects/ | 1 | README only |
| 04_Tools/ | 8 | Zotero scripts + docs |
| 05_Experiments/ | 1 | README only |
| 06_Writing/ | 1 | README only |
| 07_Research_Ideas/ | 1 | README only |
| 08_Agent_Config/ | 36 | Agent rules, configs, reports |

---

# APPENDIX A: C:\ResearchAI\ Directory Listing

Compact tree of workspace directory. Excludes .obsidian/, __pycache__/, .git/ for token efficiency.

## Root Files
- AGENT_BOOTSTRAP.md (project bootstrap)
- PROJECT_STATUS.md (stage tracking)
- README.md (project design)
- research_config.yaml (data paths)

## Directory Tree

`
C:\ResearchAI\
├── .agents/                          [AI agent skills]
├── 00_Inbox/
│   └── README.md
├── 01_Literature/
│   ├── Citation_Management.md
│   ├── Literature_Intake_Template.md
│   ├── Paper_ID_Rules.md
│   ├── Processed_Markdown_Template.md
│   ├── README.md
│   ├── 00_Inbox/
│   │   └── README.md
│   ├── 01_PDFs/                     [DEPRECATED — placeholder]
│   │   └── README.md
│   ├── 02_MinerU_Output/            [DEPRECATED — placeholder]
│   │   └── README.md
│   ├── 03_Processed_Markdown/       [DEPRECATED — placeholder]
│   │   └── README.md
│   ├── 04_Literature_Index/
│   │   ├── Literature_Index.md
│   │   └── README.md
│   ├── Markdown/                    [DEPRECATED — empty]
│   ├── PDFs/                        [DEPRECATED — empty]
│   └── References/
│       └── bibliography.bib
├── 02_KnowledgeVault/
│   ├── README.md
│   ├── Vault_README.md
│   ├── 00_Meta/                     [Navigation: MOCs, indexes, maps]
│   │   ├── Dataset_Map.md
│   │   ├── Deep_Learning_Map.md
│   │   ├── Experiment_Index.md
│   │   ├── Home.md
│   │   ├── Idea_Index.md
│   │   ├── Linking_Rules.md
│   │   ├── Method_Map.md
│   │   ├── Paper_Index.md           [← UPDATE AFTER BATCH]
│   │   ├── README.md
│   │   ├── Research_Map.md
│   │   ├── Seismic_AI_Map.md
│   │   ├── Tag_System.md
│   │   └── Writing_System.md
│   ├── 01_Papers/                   [Literature Cards, Notes, Surveys]
│   │   ├── abdallah2024_inasar_vit_card.md          [NEW — BATCH-001]
│   │   ├── bandara2022_changeformer_card.md         [NEW — BATCH-001]
│   │   ├── chai2020_using_card.md
│   │   ├── chai2020_using_note.md
│   │   ├── chen2022_rs_transformer_cd_survey.md     [NEW — BATCH-001]
│   │   ├── fang2022_snunet_cd_card.md               [NEW — BATCH-001]
│   │   ├── ghorman2022_landslide4sense_card.md      [NEW — BATCH-001]
│   │   ├── le2023_landslide_unet_card.md            [NEW — BATCH-001]
│   │   ├── liu2020_ridgecrest_card.md
│   │   ├── liu2020_ridgecrest_note.md
│   │   ├── liu2025_insar_deformation_survey.md      [NEW — BATCH-001]
│   │   ├── monteiro2024_deep_learning_card.md
│   │   ├── monteiro2024_deep_learning_survey.md
│   │   ├── mousavi2020_eqtransformer_card.md
│   │   ├── mousavi2020_eqtransformer_note.md
│   │   ├── mousavi2023_machine_learning_card.md
│   │   ├── mousavi2023_machine_learning_survey.md
│   │   ├── README.md
│   │   ├── sener2024_landslidesegnet_card.md        [NEW — BATCH-001]
│   │   ├── weber2020_disaster_damage_fusion_card.md [NEW — BATCH-001]
│   │   ├── yadav2025_hybrid_transformer_landslide_card.md [NEW — BATCH-001]
│   │   ├── zhang2020_ds_ifn_cd_card.md              [NEW — BATCH-001]
│   │   ├── zhu2018_phasenet_card.md
│   │   └── zhu2018_phasenet_note.md
│   ├── 02_Topics/
│   │   ├── README.md
│   │   └── Seismic AI.md
│   ├── 03_Methods/                  [Algorithm/method descriptions]
│   │   ├── Attention Mechanism.md
│   │   ├── CNN.md
│   │   ├── PhaseNet.md
│   │   ├── README.md
│   │   ├── Transfer Learning.md
│   │   ├── Transformer.md
│   │   ├── U-Net.md
│   │   └── Vision Transformer.md
│   ├── 04_Tasks/                    [Task definitions]
│   │   ├── Fault Segmentation.md
│   │   ├── README.md
│   │   ├── Seismic Image Segmentation.md
│   │   └── Seismic Phase Picking.md
│   ├── 05_Datasets/                 [Dataset registries]
│   │   ├── EGS Collab SURF.md
│   │   ├── F3 Netherlands.md
│   │   ├── Marmousi.md
│   │   ├── OpenFWI.md
│   │   ├── Parihaka.md
│   │   ├── Penobscot.md
│   │   ├── README.md
│   │   ├── SEAM.md
│   │   ├── SEG Salt.md
│   │   └── Thebe.md
│   ├── 06_Experiments/
│   │   ├── exp_chai2020_phase_picking.md
│   │   └── README.md
│   ├── 07_Ideas/
│   │   └── README.md
│   ├── 08_Writing/
│   │   └── README.md
│   ├── 09_Paper_Logic/              [Argument Mining analysis]
│   │   ├── chai2020_paper_logic.md              [DEPRECATED]
│   │   ├── chai2020_using_logic.md
│   │   └── README.md
│   ├── HumanRead_AgentIgnore/       [Human-readable docs, ignored by agents]
│   │   ├── current_v1.0.md
│   │   ├── current_v2.0.md
│   │   ├── current_v2.0_中文介绍.md
│   │   ├── GPT推荐研究方向.md
│   │   └── 未命名.md
│   └── Templates/                   [10 templates + README]
│       ├── Dataset_Template.md
│       ├── Experiment_Template.md
│       ├── Idea_Template.md
│       ├── Literature_Card_Template.md
│       ├── Method_Template.md
│       ├── Paper_Logic_Template.md
│       ├── Paper_Template.md
│       ├── README.md
│       ├── Survey_Template.md
│       ├── Task_Template.md
│       └── Writing_Template.md
├── 03_Projects/
│   └── README.md
├── 04_Tools/
│   ├── Data_Storage_Architecture.md
│   ├── README.md
│   └── Zotero/
│       ├── metadata_mapping.md
│       ├── README.md
│       ├── Zotero_Deployment_Record.md
│       ├── Zotero_Setup_Guide.md
│       ├── Zotero_Storage_Strategy.md
│       └── Zotero_Workflow_Configuration.md
├── 05_Experiments/
│   └── README.md
├── 06_Writing/
│   └── README.md
├── 07_Research_Ideas/
│   └── README.md
└── 08_Agent_Config/                 [Agent rules, configs, workflows]
    ├── ADR_Zotero_PDF_Centered_Architecture.md
    ├── Batch_Processing_Guideline.md
    ├── Batch_Processing_Log.md
    ├── Current_State_Check.md
    ├── Data_Migration_Plan.md
    ├── Literature_Intake_Workflow.md
    ├── Literature_Processing_Strategy.md
    ├── Markdown_Processing_Workflow.md
    ├── MinerU_Cleaning_Rules.md
    ├── MinerU_Workflow_Status.md
    ├── MinerU_Zotero_Mapping.md        [← UPDATED: +11 rows]
    ├── Missing_Data_Report.md
    ├── Paper_Card_Guideline.md
    ├── Paper_File_Naming_Rules.md
    ├── Paper_Logic_Guideline.md
    ├── Paper_Processing_Decision_Framework.md
    ├── README.md
    ├── ResearchAI_Data_Flow_Architecture.md
    ├── ResearchAI_Design_Principles.md
    ├── Single_Paper_End_to_End_Test.md
    ├── Stage_1.4A_Test_Report.md
    ├── Stage_1.4C3_2_Zotero_Status_Report.md
    ├── Stage_1.4C3_3_Zotero_Storage_Confirmation.md
    ├── Stage_1.5_2_Closed_Loop_Validation_Report.md
    ├── Stage_1.5_6B_Real_Paper_Stress_Test.md
    ├── Stage_1.5_6D1_Architecture_Verification_Report.md
    ├── Stage_1.5_6F_Architecture_Audit_Report.md
    ├── Stage_1.5_6F1_Architecture_Cleanup_Report.md
    ├── Stage_1.5_7A_Preparation_Report.md
    ├── Stage_1.5_7B_Architecture_Freeze_Audit_Report.md
    ├── Stage_1.5_7B_Freeze_Confirmation.md
    ├── Stage_1.5_Single_Paper_Validation_Protocol.md
    ├── Stage_1.5_7C1_Batch_Processing_Report.md  [NEW — this file]
    ├── Stress_Test_Execution_Log.md
    ├── Workspace_Cleanup_Plan.md
    ├── Zotero_Integration_Design.md
    └── Zotero_Test_Plan.md
`

## File Counts

| Directory | Files | Notes |
|---|---|---|
| 00_Inbox/ | 1 | README.md placeholder |
| 01_Literature/ | 9 + 5 deprecated dirs | 5 deprecated dirs are empty placeholders |
| 02_KnowledgeVault/00_Meta/ | 13 | Navigation layer |
| 02_KnowledgeVault/01_Papers/ | 24 | 17 papers + README |
| 02_KnowledgeVault/02_Topics/ | 2 | 1 topic + README |
| 02_KnowledgeVault/03_Methods/ | 8 | 7 methods + README |
| 02_KnowledgeVault/04_Tasks/ | 4 | 3 tasks + README |
| 02_KnowledgeVault/05_Datasets/ | 10 | 9 datasets + README |
| 02_KnowledgeVault/06_Experiments/ | 2 | 1 experiment + README |
| 02_KnowledgeVault/07_Ideas/ | 1 | README only |
| 02_KnowledgeVault/08_Writing/ | 1 | README only |
| 02_KnowledgeVault/09_Paper_Logic/ | 3 | 2 logics + README |
| 02_KnowledgeVault/Templates/ | 11 | 10 templates + README |
| 03_Projects/ | 1 | README only |
| 04_Tools/ | 8 | Zotero scripts + docs |
| 05_Experiments/ | 1 | README only |
| 06_Writing/ | 1 | README only |
| 07_Research_Ideas/ | 1 | README only |
| 08_Agent_Config/ | 36 | Agent rules, configs, reports |

---

# APPENDIX B: D:\ResearchAI_Data\ Directory Listing

Data layer. Zotero storage, MinerU output, datasets, experiments, model checkpoints.

## Directory Tree

`
D:\ResearchAI_Data\
├── Datasets/                          [0 files — empty, awaiting data]
├── Experiment_Results/                [0 files — empty, awaiting experiments]
├── locate/                            [2 files — utility]
├── Model_Checkpoints/                 [0 files — empty, awaiting models]
├── Paper/
│   └── MinerU_md/                     [25 folders — raw PDF→MD extraction]
│       ├── 2312.16717v1.pdf-02e09c3b-9eb7-431d-bd0a-4f99cd221909/  [Le 2023 — arXiv]
│       ├── Abdallah 等 - 2024 - Automated deformation...pdf-bd0d85e1-11ee-4b4a-a728-75290aff88d2/  [NEW BATCH]
│       ├── annurev-earth-071822-100323.pdf-9a70ce64-31d0-4383-8119-1f6ca9fbc69a/  [Mousavi 2023]
│       ├── Bandara和Patel - 2022 - A Transformer...pdf-4e820481-75e7-467b-9869-1ef40db602f0/  [NEW BATCH]
│       ├── chai2020.pdf-a31f1ca0-679c-4ffc-9af2-56fde3f21605/  [Chai 2020]
│       ├── Chen 等 - 2022 - Remote Sensing...pdf-0650cfba-bb66-485f-ba67-ecd029175725/  [NEW BATCH]
│       ├── Ding 等 - 2023 - High-resolution...pdf-e3bf5ec2-65f9-4757-8ce8-9e7831c981b1/
│       ├── Fang 等 - 2022 - SNUNet-CD...pdf-a5830dbe-84a4-4114-82c4-55c059653c61/  [NEW BATCH]
│       ├── Ghorbanzadeh 等 - 2022 - Landslide4Sense...pdf-a4cfc830-4943-46b6-859d-0e71ebba8701/  [NEW BATCH]
│       ├── Literature-review-on-deep-learning...pdf-cb8637d0-3d99-4095-b574-428cb2308196/  [Monteiro 2024]
│       ├── Liu 等 - 2025 - Deep Learning...pdf-133bbcc3-4f87-419f-874a-d394a1997d35/  [NEW BATCH]
│       ├── liu2020.pdf-de81d3ee-26c7-4d08-a1a8-0e945a65544c/  [Liu 2020]
│       ├── McBrearty和Beroza - 2023 - Earthquake Phase...pdf-de0530a4-5811-488a-9651-8f9a7671e8c0/
│       ├── mousavi2020.pdf-1e8cf44d-14b9-4217-8b73-5bd9f30165a3/  [Mousavi 2020]
│       ├── park2020.pdf-5f7aa978-8ce1-4053-a175-20d3715d529c/
│       ├── ross2020.pdf-319a04d4-c4bf-47b6-aeb8-ce3654d84eb3/
│       ├── Si 等 - 2024 - An all-in-one...pdf-8a6e77c2-4a0-498b-b86e-e5069eef9275/
│       ├── tsr-2021001.1.pdf-bd06980f-c9f3-4fa4-aeab-d0f6d6a33fb5/
│       ├── Weber和Kan - 2020 - BUILDING DISASTER...pdf-fb3486e9-b17d-4152-b954-91b4bd452655/  [NEW BATCH]
│       ├── Yadav 等 - 2025 - Hybrid lightweight...pdf-d50f131c-b377-4460-8a5c-9913a8278147/  [NEW BATCH]
│       ├── Zhang 等 - 2020 - A deeply supervised...pdf-6dbf493f-afab-431d-8a0a-352fa28ae2ff/  [NEW BATCH]
│       ├── Zhou 等 - 2021 - A high-resolution...pdf-a188feb1-2973-4fa4-b707-b97aa174eae2/
│       ├── Zhou 等 - 2022 - Seismological Characterization...pdf-155cbe33-2dc5-4af7-9930-ec0d6d69bc80/
│       ├── zhu2018.pdf-b5963bad-6896-4b64-b218-3f9b5a4c92be/  [Zhu 2018]
│       ├── Şener和Ergen - 2024 - LandslideSegNet...pdf-68ed30b6-e754-4338-8fd0-ce60a5bcf092/  [NEW BATCH]
│       └── 硕士毕业论文初稿v11.docx-d3dce535-857f-4a20-8401-3b5214b26fb4/  [Non-paper: Chinese thesis]
├── storage/                           [0 files — empty alias]
├── translators/                       [745 files — Zotero translation plugins]
├── Zotero/                            [830 files — PDFs, metadata, config]
│   ├── storage/                       [17 item dirs, 17 PDFs]
│   │   ├── 2U6E8WAQ/ -> zhu2018.pdf (PhaseNet)
│   │   ├── 2XQFZKZN/ -> bandara2022.pdf (ChangeFormer) [NEW BATCH]
│   │   ├── 2ZVY52Y6/ -> McBrearty 2023
│   │   ├── 3ZLDQRA3/ -> yadav2025.pdf [NEW BATCH]
│   │   ├── 46C4TYYR/ -> chen2022.pdf [NEW BATCH]
│   │   ├── 6VTKJ8W2/ -> fang2022.pdf [NEW BATCH]
│   │   ├── 76SW77W3/ -> abdallah2024.pdf [NEW BATCH]
│   │   ├── 94NARCAD/ -> Ross 2020
│   │   ├── 9W23DNVG/ -> chai2020.pdf
│   │   ├── AJINC2AY/ -> weber2020.pdf [NEW BATCH]
│   │   ├── J2ML7W6A/ -> Wang 2023
│   │   ├── JEIK5MKZ/ -> Tan 2021
│   │   ├── JXS7GPZW/ -> liu2025.pdf [NEW BATCH]
│   │   ├── K9XWQTIL/ -> liu2020.pdf
│   │   ├── LDQ9IIMY/ -> Si 2024
│   │   ├── LM3S7TX8/ -> Zhou 2021
│   │   ├── M8TB5AYY/ -> mousavi2023.pdf
│   │   ├── NCKCP6BS/ -> le2023.pdf (arXiv:2312.16717) [NEW BATCH]
│   │   ├── PKGESHPH/ -> Zhou 2022
│   │   ├── QKMKLG2N/ -> mousavi2020.pdf
│   │   ├── RDXHK4FQ/ -> Ding 2023
│   │   ├── RRC82BEC/ -> ghorman2022.pdf [NEW BATCH]
│   │   ├── SGUIYBB2/ -> monteiro2024.pdf
│   │   ├── SNZGPVWJ/ -> ggae049.pdf
│   │   ├── UJ95QNW9/ -> sener2024.pdf [NEW BATCH]
│   │   ├── UL36XRSA/ -> zhang2020.pdf [NEW BATCH]
│   │   └── VPZLHRS4/ -> park2020.pdf
│   └── zotero.sqlite                  [Bibliographic metadata]
└── Zotero_Attachments/                [0 files — empty]
`

## Summary

| Component | Count | Notes |
|---|---|---|
| Zotero PDFs | 26 | 17 in item dirs + 9 flat PDFs |
| MinerU folders | 25 | 15 with valid papers + 10 new batch |
| Processed papers (KV) | 17 | 6 pre-batch + 11 in this batch |
| Unprocessed MinerU | 14 | Have MinerU output, no KV files |
| Empty data dirs | 3 | Datasets, Experiment_Results, Model_Checkpoints |

## New Batch Papers in MinerU (marked [NEW BATCH])

All 11 papers from this batch have verified MinerU output folders with full.md files.
Their Item Keys are confirmed in Zotero storage.
Their KnowledgeVault cards are created in 02_KnowledgeVault/01_Papers/.
