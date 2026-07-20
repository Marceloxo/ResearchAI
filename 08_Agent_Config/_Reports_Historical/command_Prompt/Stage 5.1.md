# Task: Stage 5.1 — MinerU CLI Migration Validation

You are working inside the ResearchAI workspace.

Workspace:

/home/lco/ResearchAI

External data:

/home/lco/ResearchAI_Data


## Mission

Implement and validate the first migration step from MinerU Desktop workflow to Linux-native MinerU CLI workflow.

The goal is NOT to redesign ResearchAI.

The goal is to verify that:

Zotero storage PDF
        ↓
MinerU CLI 3.4.4
        ↓
normalized full.md
        ↓
Agent-readable literature pipeline

works correctly.


---

# IMPORTANT ARCHITECTURE RULES

Before doing anything:

Read:

1. AGENTS.md
2. PROJECT_STATUS.md
3. README.md
4. research_config.yaml
5. 08_Agent_Config/Migration/Stage_5_MinerU_Linux_Architecture_Design.md
6. 08_Agent_Config/ADR_Zotero_PDF_Centered_Architecture.md


These documents define the architecture contract.


Do NOT:

- redesign directory structure
- modify Zotero architecture
- modify Obsidian vault structure
- rewrite Agent skills
- delete existing MinerU outputs
- migrate old MinerU Desktop files


This is a controlled migration stage.


---

# Current Environment

Verified:

Conda environment:

mineru


MinerU:

mineru, version 3.4.4


Command:

mineru


Zotero PDF source:

/home/lco/ResearchAI_Data/Zotero/storage/


MinerU output:

/home/lco/ResearchAI_Data/Paper/MinerU_md/


---

# Stage 5.1 Objective

Use ONE existing Zotero paper to validate the complete pipeline.

Use:

Zotero Item Key:

9W23DNVG


PDF:

/home/lco/ResearchAI_Data/Zotero/storage/9W23DNVG/


Paper:

Chai et al. 2020
Using a Deep Neural Network and Transfer Learning to Bridge Scales for Seismic Phase Picking


---

# Step 1 — Inspect Current State

Before processing:

Check:

1. PDF exists
2. Zotero storage structure
3. Existing MinerU output
4. Whether this paper has already been processed


Do not overwrite existing outputs.


Report:

- PDF path
- existing MinerU folder
- current format
- whether reprocessing is needed


---

# Step 2 — Run MinerU CLI Test

Create a temporary test output directory:

/home/lco/ResearchAI_Data/Paper/MinerU_test/


Do NOT write directly into the production MinerU_md directory yet.


Run MinerU using the recommended default:

Backend:

pipeline


Method:

txt


Language:

auto or English-compatible


Disable proxy environment variables before execution:

env -u http_proxy \
    -u https_proxy \
    -u HTTP_PROXY \
    -u HTTPS_PROXY \
    -u ALL_PROXY \
    -u all_proxy


Example:

mineru \
-p <pdf_path> \
-o <test_output>


---

# Step 3 — Analyze CLI Output

Inspect generated structure.


Determine:

- Is full.md generated?
- Is markdown quality acceptable?
- Are images generated?
- Are image references valid?
- Are JSON metadata files generated?


Compare with previous MinerU Desktop assumptions:

Expected:

paper_folder/

├── full.md
├── images/
├── *_content_list.json
├── *_model.json
└── *_origin.pdf


If output differs:

DO NOT modify Agent skills.

Instead document the difference.


---

# Step 4 — Implement Minimal Normalization Layer

If needed, create:

/home/lco/ResearchAI/04_Tools/mineru/


with:

normalize_mineru_output.py


Purpose:

Convert MinerU output variants into a stable Agent input format.


Required behavior:

Input:

Any MinerU output folder


Output:

A folder containing:

full.md

images/

metadata


Supported cases:

Case A:

full.md already exists

→ verify only


Case B:

hybrid_auto/*.md exists

→ copy markdown to full.md


Case C:

other markdown filename exists

→ rename/copy to full.md


Do NOT modify original markdown content.


Create log:

.normalization.log


---

# Step 5 — Design Future Automation (DO NOT IMPLEMENT YET)

Create a design note only:

08_Agent_Config/Migration/Stage_5.1_MinerU_CLI_Test_Report.md


Include:

1. Test environment
2. Command used
3. Output structure
4. Compatibility analysis
5. Problems found
6. Recommendation for Stage 5.2


Do NOT implement:

- Zotero database watcher
- cron
- systemd
- batch processing

Those belong to later stages.


---

# Step 6 — Validation Checklist

The stage is successful only if:

[ ] MinerU CLI can parse Zotero PDF

[ ] Output markdown can be located reliably

[ ] Agent can consume normalized full.md

[ ] Existing ResearchAI architecture remains unchanged

[ ] No existing knowledge files modified

[ ] No old MinerU outputs deleted


---

# Final Response Requirements

After execution, provide:

## Summary

- Files created
- Files modified
- Commands executed


## Validation Result

Table:

| Item | Result |
|---|---|
| Zotero PDF access | PASS/FAIL |
| MinerU CLI execution | PASS/FAIL |
| Markdown generation | PASS/FAIL |
| Image extraction | PASS/FAIL |
| Agent compatibility | PASS/FAIL |


## Recommendation

State whether Stage 5.2 should proceed.

Do not continue to Stage 5.2 automatically.
Wait for approval.
