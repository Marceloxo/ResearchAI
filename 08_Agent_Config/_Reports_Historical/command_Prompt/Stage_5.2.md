# Task: Stage 5.2 — Build Production MinerU CLI Processing Pipeline

You are continuing the ResearchAI MinerU Linux migration.

Stage 5.1 has been completed successfully.

Read first:

1. AGENTS.md
2. PROJECT_STATUS.md
3. README.md
4. research_config.yaml
5. 08_Agent_Config/Migration/Stage_5_MinerU_Linux_Architecture_Design.md
6. 08_Agent_Config/Migration/Stage_5.1_MinerU_CLI_Test_Report.md


---

# Objective

Convert the validated single-paper MinerU CLI workflow into a reproducible production pipeline.

The target architecture:

Zotero
  |
  | PDF attachment
  ↓
Zotero storage/{ItemKey}/
  |
  ↓
MinerU CLI 3.4.4
  |
  ↓
Normalization Layer
  |
  ↓
MinerU_md/{paper}/full.md
  |
  ↓
Agent Literature Processing


---

# Architecture Constraints

DO NOT:

- change Zotero architecture
- move PDFs
- modify Obsidian vault structure
- delete existing MinerU Desktop outputs
- rewrite Agent skills
- process all existing papers yet


Only add tools required for MinerU automation.


---

# Step 1 — Inspect Existing Tools

Review:

/home/lco/ResearchAI/04_Tools/mineru/

Current expected files:

normalize_mineru_output.py


Determine whether the structure is suitable.

If necessary create:

04_Tools/mineru/
    process_paper.py
    batch_process.py
    README.md


---

# Step 2 — Implement Single Paper Processor

Create:

04_Tools/mineru/process_paper.py


Requirements:

Input:

Zotero Item Key


Example:

python process_paper.py 9W23DNVG


The script must:

1. Query Zotero storage directory:

/home/lco/ResearchAI_Data/Zotero/storage/{ItemKey}


2. Find PDF attachment


3. Check whether MinerU output already exists


4. If output exists:

print:

"Already processed, skipping"


5. Otherwise run:

mineru


with:

backend:
pipeline


method:
txt


Before execution remove proxy variables:

http_proxy
https_proxy
HTTP_PROXY
HTTPS_PROXY
ALL_PROXY
all_proxy


6. Run normalization automatically


7. Verify:

full.md exists


8. Return status.


---

# Step 3 — Implement Batch Processor

Create:

04_Tools/mineru/batch_process.py


Purpose:

Find Zotero papers requiring MinerU processing.


Use:

/home/lco/ResearchAI_Data/Zotero/zotero.sqlite


Read:

- paper item key
- title
- attachment path


For each paper:

Check:

/home/lco/ResearchAI_Data/Paper/MinerU_md/


If normalized full.md exists:

SKIP


Otherwise:

PROCESS


Do not actually process all papers by default.


Default behavior:

DRY RUN


Example:

python batch_process.py


Output:

PROCESS:
key title


SKIP:
key title


Add argument:

--execute


Only with:

python batch_process.py --execute


should MinerU actually run.


---

# Step 4 — Naming Strategy

Keep existing architecture.


Output:

ResearchAI_Data/Paper/MinerU_md/


Each paper folder should contain:

full.md
images/


Do not introduce new directory layers.


---

# Step 5 — Logging

Create:

ResearchAI_Data/Paper/MinerU_logs/


Each run generates:

YYYY-MM-DD_batch.log


Record:

- Zotero key
- title
- PDF path
- start time
- end time
- success/failure
- error message


---

# Step 6 — Testing

Do NOT run all papers.

Test only:

3 papers:

1.
9W23DNVG

2.
one existing paper with tables

3.
one existing paper with many figures


Validate:

- markdown generation
- image extraction
- normalization
- skip mechanism


---

# Step 7 — Documentation

Create:

08_Agent_Config/Migration/Stage_5.2_MinerU_Production_Pipeline_Report.md


Include:

1. architecture
2. files created
3. commands
4. test results
5. known limitations
6. recommendation for Stage 5.3


---

# Final Response

Return:

## Created files

## Modified files

## Test results

Table:

| Component | Result |
|---|---|
| Zotero query | PASS/FAIL |
| PDF detection | PASS/FAIL |
| MinerU execution | PASS/FAIL |
| Normalization | PASS/FAIL |
| Skip mechanism | PASS/FAIL |
| Logging | PASS/FAIL |


Do not continue to Stage 5.3 automatically.
Wait for approval.
