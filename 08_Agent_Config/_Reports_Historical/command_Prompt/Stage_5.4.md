
# Stage 5.4: MinerU Production Batch Processing

## Objective

Execute the first production batch processing of all remaining Zotero papers that do not yet have Agent-compatible MinerU output.

The goal is NOT to redesign the pipeline.

The goal is to validate that the established production workflow can scale from test papers to the complete Zotero library.

---

## Current Verified State

Stage 5.1:
- MinerU CLI 3.4.4 validated
- pipeline backend + txt method validated
- output normalized successfully

Stage 5.2:
- process_paper.py works
- batch_process.py works
- Zotero paper key / attachment key resolution works
- logging works

Stage 5.3:
- All existing MinerU folders are Agent-compatible
- Every valid paper folder contains:
  - full.md
  - images/
  - resolved markdown image references

Current stable contract:

MinerU output:
```

/home/lco/ResearchAI_Data/Paper/MinerU_md/{paper_folder}/
├── full.md
└── images/

```

Agent only consumes:
```

full.md
images/

```

Do not change this contract.

---

# Scope

Process ONLY Zotero papers that satisfy:

1. PDF exists in:

```

/home/lco/ResearchAI_Data/Zotero/storage/{attachment_key}/

```

2. No existing valid MinerU output:

```

/home/lco/ResearchAI_Data/Paper/MinerU_md/{paper_folder}/full.md

````

3. Paper is a valid research document.

Skip:

- existing processed papers
- missing PDFs
- non-paper attachments
- docx files
- notes
- snapshots
- Zotero metadata items

---

# Step 1: Dry Run

Before execution:

Run:

```bash
python 04_Tools/mineru/batch_process.py
````

without --execute.

Generate a report:

```
08_Agent_Config/Migration/Stage_5.4_Batch_Dry_Run_Report.md
```

Report must include:

* total Zotero papers
* already processed count
* pending processing count
* skipped count
* missing PDF count
* list of pending papers:

Format:

| Zotero Key | Title | Attachment Key | PDF Path |
| ---------- | ----- | -------------- | -------- |

STOP after dry run.

Wait for approval before actual execution.

---

# Step 2: Production Execution (after approval)

Execute:

```bash
python 04_Tools/mineru/batch_process.py --execute
```

Requirements:

* Process sequentially
* Do NOT parallelize
* Do NOT use VLM backend
* Do NOT change MinerU backend

Use:

```
backend:
pipeline

method:
txt

language:
ch

formula:
true

table:
true
```

Proxy handling must remain:

```
env -u http_proxy \
-u https_proxy \
-u HTTP_PROXY \
-u HTTPS_PROXY \
-u ALL_PROXY \
-u all_proxy
```

---

# Step 3: After Processing

Run validation:

```bash
python 04_Tools/mineru/validate_mineru_output.py --report
```

Verify:

Every processed folder has:

```
full.md
images/
```

Every markdown image reference resolves.

---

# Step 4: Generate Production Report

Create:

```
08_Agent_Config/Migration/Stage_5.4_MinerU_Production_Batch_Report.md
```

Include:

## Processing Summary

| Metric                | Count |
| --------------------- | ----- |
| Zotero papers scanned |       |
| Already processed     |       |
| Newly processed       |       |
| Failed                |       |
| Skipped               |       |

## Performance Statistics

For each processed paper:

| Paper | Pages | Time | Images | Markdown Size |
| ----- | ----- | ---- | ------ | ------------- |

## Validation Results

Include:

* full.md validation
* image validation
* markdown reference validation
* agent compatibility

## Failure Analysis

For failures:

Include:

* Zotero key
* PDF path
* Error message
* Recommended action

---

# Safety Constraints

DO NOT:

* modify Zotero database
* modify Obsidian vault
* modify KnowledgeVault templates
* modify Agent skills
* rename existing MinerU folders
* delete old MinerU outputs
* change directory architecture

Only create:

```
MinerU_md/
MinerU_logs/
Migration reports
```

---

# Completion Criteria

Stage 5.4 is complete only when:

1. All valid Zotero PDFs have MinerU output
2. All outputs pass validator
3. No duplicate processing occurred
4. Logs exist for every processed paper
5. Production report is generated

After completion, summarize:

* files created
* files modified
* papers processed
* failures
* validation result



