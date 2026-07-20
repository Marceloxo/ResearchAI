# Stage 5.3: MinerU-Agent Integration and Output Stabilization

You are working inside:

/home/lco/ResearchAI

Read before modifying anything:

1. 08_Agent_Config/Migration/Stage_5_MinerU_Linux_Architecture_Design.md
2. 08_Agent_Config/Migration/Stage_5.1_MinerU_CLI_Test_Report.md
3. 08_Agent_Config/Migration/Stage_5.2_MinerU_Production_Pipeline_Report.md
4. 08_Agent_Config/ResearchAI_Design_Principles.md
5. Existing literature processing skills:
   - .codex/skills/researchai/references/literature/paper_intake.md
   - .codex/skills/researchai/references/literature/paper_deep_read.md
   - .codex/skills/researchai/references/literature/paper_batch_process.md


## Objective

Integrate the validated MinerU Linux pipeline into the Agent workflow.

Do NOT redesign the architecture.

Do NOT change:
- Zotero structure
- ResearchAI_Data directory structure
- KnowledgeVault structure
- Existing templates

Only update interfaces between MinerU output and Agent skills.


---

# Task 1: Normalize Existing MinerU Outputs

Locate:

/home/lco/ResearchAI_Data/Paper/MinerU_md/


Identify all folders.

For every folder:

Run:

python /home/lco/ResearchAI/04_Tools/mineru/normalize_mineru_output.py <folder>


Expected final state:

Every processed paper folder must contain:

<folder>/
├── full.md
├── images/
└── MinerU metadata files


The following formats must be normalized:

A:
full.md already exists
→ verify only

B:
hybrid_auto/*.md
→ create root full.md

C:
txt/*.md
→ create root full.md


Do not delete:
- original txt/
- original hybrid_auto/
- JSON metadata
- images


Generate report:

08_Agent_Config/Migration/Stage_5.3_Normalization_Report.md


Report must include:

- number of folders scanned
- number normalized
- number already compatible
- failed cases
- remaining format inconsistencies


---

# Task 2: Update Agent Literature Skills

Modify only if necessary.

Target:

.codex/skills/researchai/references/literature/


Update:

paper_intake.md
paper_deep_read.md
paper_batch_process.md


Required changes:


## Add MinerU input contract

The Agent must assume:

Input:

/home/lco/ResearchAI_Data/Paper/MinerU_md/{paper_folder}/


Canonical file:

full.md


Images:

images/


Do NOT directly read:

- txt/*.md
- hybrid_auto/*.md


because normalization layer already handles conversion.


---

# Add processing flow description:


The official pipeline is:

Zotero
 ↓
MinerU CLI
 ↓
normalize_mineru_output.py
 ↓
full.md
 ↓
Agent reading
 ↓
KnowledgeVault


The Agent must not call MinerU itself.

The Agent only consumes normalized output.


---

# Task 3: Add Validation Script

Create:

04_Tools/mineru/validate_mineru_output.py


Purpose:

Check whether MinerU folders are Agent-compatible.


Requirements:

Input:

optional:
path


Default:

/home/lco/ResearchAI_Data/Paper/MinerU_md/


Checks:


For every paper folder:


PASS if:

- full.md exists
- images directory exists
- all markdown image references resolve


FAIL if:

- missing full.md
- missing images
- broken image references


Output:

terminal summary:

Example:


MinerU Validation Report

Total papers:
27

Compatible:
27

Failed:
0


Also save:

MinerU_validation_report.md


under:

08_Agent_Config/Migration/


---

# Task 4: Update MinerU README

Modify:

04_Tools/mineru/README.md


Add:

## Agent Integration

Explain:

MinerU output is not directly consumed.

Required sequence:

1. process_paper.py
2. normalize_mineru_output.py
3. validate_mineru_output.py
4. Agent literature skills


Explain that:

full.md is the stable interface contract.


---

# Task 5: Test End-to-End Workflow


Select one new paper.

Run:

1.
process_paper.py


2.
normalize_mineru_output.py


3.
validate_mineru_output.py


Then simulate Agent reading:

- locate full.md
- locate images
- confirm paths


Do NOT create KnowledgeVault notes yet.


Only validate interface.


---

# Constraints

Before modification:

Create backups:

*.backup_stage5.3


Do not modify:

- Zotero files
- bibliography.bib
- KnowledgeVault existing notes
- templates


Keep all changes reversible.


---

# Final Deliverables


Create:

1.
08_Agent_Config/Migration/Stage_5.3_Normalization_Report.md


2.
04_Tools/mineru/validate_mineru_output.py


3.
Updated:

04_Tools/mineru/README.md

and only necessary Agent skill files.


Final response must contain:

- files created
- files modified
- tests executed
- validation result
- recommendation for Stage 5.4


Do not proceed to Stage 5.4 automatically.
