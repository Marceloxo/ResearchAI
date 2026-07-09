# ResearchAI Workspace — Directory Tree v1.0

> Generated for AI Agent context. Structured for readability, not raw `dir /s` output.
> Two roots: **C:\ResearchAI** (knowledge workspace) and **D:\ResearchAI_Data** (external data layer).

---

## Root: C:\ResearchAI (Knowledge Workspace)

```
C:\ResearchAI\
├── AGENT_BOOTSTRAP.md              # Agent startup guide, project identity, rules
├── PROJECT_STATUS.md               # Stage tracking, completed tasks
├── README.md                       # Overall project design
├── research_config.yaml            # Data path configuration
├── .git\                           # Git repository (ignore in tree listing)
├── .agents\                        # Agent skills (ignore)
│
├── 00_Inbox\
│   └── README.md
│
├── 01_Literature\                  # Literature management
│   ├── README.md
│   ├── Paper_ID_Rules.md           # Paper identifier naming conventions
│   ├── Literature_Intake_Template.md
│   ├── Citation_Management.md      # Citation rules
│   ├── Markdown\                   # Raw markdown files
│   ├── PDFs\                       # PDF files (if any stored here)
│   ├── References\
│   │   └── bibliography.bib        # BibTeX bibliography
│   ├── 00_Inbox\
│   │   └── README.md
│   ├── 01_PDFs\
│   │   └── README.md
│   ├── 02_MinerU_Output\
│   │   └── README.md
│   ├── 03_Processed_Markdown\
│   │   └── README.md
│   └── 04_Literature_Index\
│       ├── README.md
│       └── Literature_Index.md     # Master paper tracker
│
├── 02_KnowledgeVault\              # Obsidian vault — intellectual memory
│   ├── README.md
│   ├── Vault_README.md             # Vault conventions, bilingual design, link rules
│   ├── Vision Transformer.md       # Method note (top-level, non-standard)
│   ├── .obsidian\                  # Obsidian app config (5 files)
│   │   ├── app.json
│   │   ├── appearance.json
│   │   ├── core-plugins.json
│   │   ├── graph.json
│   │   └── workspace.json
│   │
│   ├── 00_Meta\                    # Navigation layer — MOCs, indexes, maps
│   │   ├── README.md
│   │   ├── Home.md                 # Vault home page
│   │   ├── Research_Map.md         # Top-level research map
│   │   ├── Seismic_AI_Map.md       # Seismic AI direction entry
│   │   ├── Deep_Learning_Map.md    # Deep learning methods entry
│   │   ├── Method_Map.md           # Method index
│   │   ├── Dataset_Map.md          # Dataset index
│   │   ├── Paper_Index.md          # Paper index
│   │   ├── Idea_Index.md           # Idea index
│   │   ├── Experiment_Index.md     # Experiment index
│   │   ├── Writing_System.md       # Writing system entry
│   │   ├── Tag_System.md           # Tag naming conventions
│   │   └── Linking_Rules.md        # Wikilink relationship rules
│   │
│   ├── 01_Papers\                  # Paper-level notes
│   │   ├── README.md
│   │   ├── chai2020_phase_picking_Card.md           # Literature Card
│   │   ├── chai2020_using_deep_neural_network_transfer_learning.md  # Paper Note
│   │   ├── Literature-review-on-deep-learning-for-segmentation-of-seismic-images.md  # Survey Paper Note
│   │   └── Literature-review-on-deep-learning-for-segmentation-of-seismic-images_Card.md  # Survey Literature Card
│   │
│   ├── 02_Topics\                  # Research topics
│   │   ├── README.md
│   │   └── Seismic AI.md
│   │
│   ├── 03_Methods\                 # Method/algorithm notes
│   │   ├── README.md
│   │   ├── CNN.md
│   │   ├── U-Net.md
│   │   ├── Transformer.md
│   │   ├── Attention Mechanism.md
│   │   ├── PhaseNet.md
│   │   └── Transfer Learning.md
│   │
│   ├── 04_Tasks\                   # Task definition notes
│   │   ├── README.md
│   │   ├── Fault Segmentation.md
│   │   ├── Seismic Image Segmentation.md
│   │   └── Seismic Phase Picking.md
│   │
│   ├── 05_Datasets\                # Dataset registry notes
│   │   ├── README.md
│   │   ├── EGS Collab SURF.md
│   │   ├── F3 Netherlands.md
│   │   ├── Marmousi.md
│   │   ├── OpenFWI.md
│   │   ├── Parihaka.md
│   │   ├── Penobscot.md
│   │   ├── SEAM.md
│   │   ├── SEG Salt.md
│   │   └── Thebe.md
│   │
│   ├── 06_Experiments\             # Experiment notes
│   │   ├── README.md
│   │   └── exp_chai2020_phase_picking.md
│   │
│   ├── 07_Ideas\                   # Research ideas
│   │   └── README.md
│   │
│   ├── 08_Writing\                 # Manuscript planning
│   │   └── README.md
│   │
│   ├── 09_Paper_Logic\             # Argument Mining paper logic
│   │   ├── README.md
│   │   ├── chai2020_paper_logic.md                  # v1 (old format, preserved)
│   │   └── chai2020_paper_logic_argument_mining.md  # v2 (Argument Mining format)
│   │
│   └── Templates\                  # Obsidian note templates
│       ├── README.md
│       ├── Literature_Card_Template.md
│       ├── Paper_Template.md
│       ├── Survey_Template.md
│       ├── Method_Template.md
│       ├── Task_Template.md
│       ├── Dataset_Template.md
│       ├── Experiment_Template.md
│       ├── Idea_Template.md
│       ├── Writing_Template.md
│       └── Paper_Logic_Template.md
│
├── 03_Projects\
│   └── README.md
│
├── 04_Tools\                       # External tool integration
│   ├── README.md
│   ├── Data_Storage_Architecture.md
│   └── Zotero\
│       ├── README.md
│       ├── Zotero_Deployment_Record.md
│       ├── Zotero_Setup_Guide.md
│       ├── Zotero_Storage_Strategy.md
│       ├── Zotero_Workflow_Configuration.md
│       └── metadata_mapping.md
│
├── 05_Experiments\
│   └── README.md
│
├── 06_Writing\
│   └── README.md
│
├── 07_Research_Ideas\
│   └── README.md
│
└── 08_Agent_Config\                # AI agent configuration and reports
    ├── README.md
    ├── ADR_Zotero_PDF_Centered_Architecture.md    # ADR-001: PDF architecture decision
    ├── Current_State_Check.md                     # Current status snapshot
    ├── Data_Migration_Plan.md
    ├── Literature_Intake_Workflow.md
    ├── Literature_Processing_Strategy.md           # 3-level processing strategy
    ├── Markdown_Processing_Workflow.md
    ├── MinerU_Cleaning_Rules.md
    ├── MinerU_Workflow_Status.md
    ├── Missing_Data_Report.md
    ├── Paper_Logic_Guideline.md                   # Mandatory agent rule
    ├── Paper_Processing_Decision_Framework.md      # Decision framework
    ├── ResearchAI_Design_Principles.md             # 10 design principles
    ├── Single_Paper_End_to_End_Test.md             # Test plan
    ├── Stage_1.4A_Test_Report.md
    ├── Stage_1.5_2_Closed_Loop_Validation_Report.md
    ├── Stage_1.5_6B_Real_Paper_Stress_Test.md      # Stress test protocol
    ├── Stage_1.5_Single_Paper_Validation_Protocol.md
    ├── Stress_Test_Execution_Log.md                # Per-paper execution log
    ├── Zotero_Integration_Design.md
    └── Zotero_Test_Plan.md
```

**Summary**: 108 markdown files, 5 obsidian config files. ~30KB total.

---

## Root: D:\ResearchAI_Data (External Data Layer)

> Large files only. Knowledge workspace stays on C:.

```
D:\ResearchAI_Data\
├── README.md
│
├── Zotero\                          # Zotero data directory
│   ├── zotero.sqlite                # Bibliographic metadata database
│   ├── zotero.sqlite.bak            # Backup
│   │
│   ├── storage\                     # PDF files (7 papers)
│   │   ├── 2U6E8WAQ\
│   │   │   ├── .zotero-ft-cache
│   │   │   └── Zhu和Beroza - 2018 - PhaseNet...pdf
│   │   ├── 9W23DNVG\
│   │   │   ├── .zotero-ft-cache
│   │   │   └── Chai 等 - 2020 - Using a Deep Neural Network...pdf
│   │   ├── JEIK5MKZ\
│   │   │   ├── .zotero-ft-cache
│   │   │   └── Tan 等 - 2021 - Machine-Learning-Based...pdf
│   │   ├── K9XWQTIL\
│   │   │   ├── .zotero-ft-cache
│   │   │   └── Liu 等 - 2020 - Rapid Characterization...pdf
│   │   ├── QKMKLG2N\
│   │   │   ├── .zotero-ft-cache
│   │   │   └── Mousavi 等 - 2020 - Earthquake transformer...pdf
│   │   ├── SGUIYBB2\
│   │   │   ├── .zotero-ft-cache
│   │   │   └── Monteiro 等 - 2024 - Literature review...pdf
│   │   └── VPZLHRS4\
│   │       ├── .zotero-ft-cache
│   │       └── Park 等 - 2020 - Machine-Learning-Based...pdf
│   │
│   ├── styles\                      # CSL citation styles (15 files)
│   │   ├── apa.csl
│   │   ├── nature.csl
│   │   ├── ieee.csl
│   │   └── ... (12 more)
│   │
│   ├── translators\                 # Zotero translators (745 files — omitted)
│   │   # Standard Zotero installation files, not research data
│   │
│   └── better-bibtex\
│       └── read-only.json
│
├── Zotero_Attachments\              # Linked attachment base directory
│   # (empty or placeholder)
│
├── Paper\
│   └── MinerU_md\                   # MinerU Desktop output (processed PDFs)
│       ├── chai2020.pdf-<uuid>\     # Chai 2020 — research article
│       │   ├── full.md              # Extracted markdown
│       │   ├── layout.json          # Layout analysis
│       │   ├── block_list.json      # Block-level structure
│       │   ├── *_content_list.json  # Content list (2 files)
│       │   ├── *_model.json         # Model predictions
│       │   ├── *_origin.pdf         # Original PDF
│       │   ├── MinerU_markdown_*.md # Alternative output
│       │   └── images\              # Extracted figures (19 files)
│       │
│       ├── Literature-review-on-deep-learning-for-the-segmentation-of-seismic-images.pdf-<uuid>\  # Monteiro 2024 — survey
│       │   ├── full.md
│       │   ├── layout.json
│       │   ├── block_list.json
│       │   ├── *_content_list.json (2 files)
│       │   ├── *_model.json
│       │   ├── *_origin.pdf
│       │   ├── MinerU_markdown_*.md
│       │   └── images\              # Extracted figures (28 files)
│       │
│       ├── liu2020.pdf-<uuid>\      # Liu 2020 — processed but not in vault
│       │   ├── full.md + supporting files (8 files)
│       │   └── images\ (9 files)
│       │
│       ├── park2020.pdf-<uuid>\     # Park 2020 — processed but not in vault
│       │   ├── full.md + supporting files (8 files)
│       │   └── images\ (9 files)
│       │
│       ├── tsr-2021001.1.pdf-<uuid>\ # TSR paper — processed but not in vault
│       │   ├── full.md + supporting files (8 files)
│       │   └── images\ (11 files)
│       │
│       └── zhu2018.pdf-<uuid>\      # Zhu 2018 (PhaseNet original) — processed but not in vault
│           ├── full.md + supporting files (7 files)
│           └── images\ (46 files)
│
├── Datasets\                        # Research datasets (empty — to be populated)
├── Experiment_Results\              # Experiment output (empty — to be populated)
├── Model_Checkpoints\               # Trained model weights (empty — to be populated)
└── locate\                          # Non-research utility files
    ├── engines.json
    └── Google Scholar.ico
```

**Summary**: 7 PDFs in Zotero storage, 5 papers processed by MinerU (2 in vault, 3 waiting). 745 Zotero translator files omitted (standard installation).

---

## Key Relationships

```
C:\ResearchAI                              D:\ResearchAI_Data
──────────────                             ──────────────────
02_KnowledgeVault/01_Papers/    ←───  references  ──→  Zotero/storage/*.pdf
02_KnowledgeVault/03_Methods/   ←───  cites       ──→  MinerU_md/*/full.md
02_KnowledgeVault/05_Datasets/  ←───  benchmarks  ──→  Zotero metadata
08_Agent_Config/*               ←───  config      ──→  research_config.yaml
01_Literature/*                 ←───  workflow    ──→  MinerU_md/ (input)

MinerU input:  Zotero/storage/*.pdf
MinerU output: D:\ResearchAI_Data\Paper\MinerU_md\*/full.md
AI reads:      MinerU_md full.md → creates KnowledgeVault notes
```

## Unprocessed MinerU Outputs (in D: but NOT yet in KnowledgeVault)

| Paper | MinerU Path | Vault Status |
|---|---|---|
| liu2020.pdf | MinerU_md/liu2020.pdf-*/full.md | Not processed |
| park2020.pdf | MinerU_md/park2020.pdf-*/full.md | Not processed |
| tsr-2021001.1.pdf | MinerU_md/tsr-2021001.1.pdf-*/full.md | Not processed |
| zhu2018.pdf (PhaseNet original) | MinerU_md/zhu2018.pdf-*/full.md | Not processed |

## Zotero Papers (in storage but NOT yet processed by MinerU)

None — all 7 Zotero PDFs have MinerU output.
