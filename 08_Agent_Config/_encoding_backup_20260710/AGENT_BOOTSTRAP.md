# ResearchAI Agent Bootstrap

## Project Identity

ResearchAI is a long-term AI-assisted scientific research workspace.

It is designed to support the complete research lifecycle:

```
Literature Acquisition
  éˆ?Paper Understanding
  éˆ?Knowledge Organization
  éˆ?Research Gap Discovery
  éˆ?Model Development
  éˆ?Experiment Management
  éˆ?Result Analysis
  éˆ?Scientific Writing
```

The system is designed for both human researchers and AI agents (Codex, Claude Code, Gemini CLI, etc.) to understand, maintain, and extend the research workflow.

**Primary focus**: Deep Learning + Computer Vision + Earth Science (Seismic AI)

**Future scope**: Medical imaging, remote sensing, industrial computer vision, general deep learning research.

---

## Current Research Direction

### Current Focus: Seismic AI

Applying deep learning and computer vision to seismic data processing and interpretation.

### Main Interests

- Seismic image processing
- Seismic image segmentation (fault, facies, salt body)
- Deep learning based methods (CNN, Transformer, GAN, Attention)
- Lightweight computer vision models (hardware-constrained: RTX4070)

### Future Extension

Other computer vision related research in geoscience domains.

---

## Hardware Constraints

### Local GPU: RTX 4070

**Implications:**

- Prefer lightweight models and efficient architectures
- Favor 2D approaches over heavy 3D when possible
- Optimize for reproducibility with limited VRAM (12GB)

**Avoid:**

- Unnecessary large-scale models
- Heavy 3D architectures without justification
- Training from scratch on large datasets

---

## Current Pipeline Status

| Stage | Status |
|---|---|
| Stage 0 éˆ?Workspace Initialization | é‰?Completed |
| Stage 1.1 éˆ?Obsidian KnowledgeVault Init | é‰?Completed |
| Stage 1.2 éˆ?Obsidian Note Templates | é‰?Completed |
| Stage 1.3 éˆ?Navigation & Knowledge Graph | é‰?Completed |
| Stage 1.4A éˆ?First Paper Validation | é‰?Completed |
| Stage 1.4A.1 éˆ?Agent Bootstrap | é‰?Completed |
| Stage 1.4B-0 éˆ?Literature Intake System | é‰?Completed |
| Stage 1.4B-1 éˆ?Processed Markdown Pipeline | é‰?Completed |
| Stage 1.4C-0 éˆ?Zotero Integration Design | é‰?Completed |
| Stage 1.4C-1 éˆ?Zotero Deployment Prep | é‰?Completed |
| Stage 1.4C-1.1 éˆ?Design Principles & ID Fix | é‰?Completed |
| Stage 1.4C-2 éˆ?Zotero Test Plan | é‰?Completed |
| Stage 1.4C-3 éˆ?Zotero Readiness | é‰?Completed |
| Stage 1.4C-3.1 éˆ?Data Path Sync | é‰?Completed |
| Stage 1.4C-3.2 éˆ?Zotero Status Sync | é‰?Completed |
| Stage 1.4C-3.3 éˆ?Storage Confirmation | é‰?Completed |
| **Stage 1.4C-3.4 éˆ?PDF Architecture Redesign** | é¦ƒæ”§ Current |
| Stage 1.4B éˆ?Survey Template & Data Setup | éˆ?Next |

---

## Directory Map

| Directory | Purpose |
|---|---|
| `00_Inbox/` | Temporary input area éˆ?new papers, notes, unprocessed files |
| `01_Literature/` | Literature management éˆ?MinerU output, processed markdown, index |
| `02_KnowledgeVault/` | Obsidian knowledge base éˆ?the intellectual memory of the project |
| `03_Projects/` | Research implementation éˆ?DL code, training scripts, configs |
| `04_Tools/` | Reusable scripts éˆ?preprocessing, conversion, visualization |
| `05_Experiments/` | Experiment tracking éˆ?configs, results, figures |
| `06_Writing/` | Scientific writing éˆ?drafts, manuscripts, proposals |
| `07_Research_Ideas/` | Idea management éˆ?gaps, hypotheses, future directions |
| `08_Agent_Config/` | AI agent config éˆ?instructions, skills, templates, workflows |

---

## Agent Startup Procedure

**Every AI Agent must follow this procedure on first interaction:**

1. **Read `AGENT_BOOTSTRAP.md`** éˆ?understand project identity, constraints, and status.
2. **Read `PROJECT_STATUS.md`** éˆ?understand completed stages and next planned work.
3. **Read `README.md`** éˆ?understand overall project design and principles.
4. **Read the current task document** éˆ?understand what you are being asked to do.

**After startup, before any action:**

- Check `02_KnowledgeVault/Vault_README.md` for vault conventions.
- Check `08_Agent_Config/Literature_Processing_Strategy.md` for paper processing rules.
- Check `08_Agent_Config/Current_State_Check.md` for current status snapshot.
- Check `08_Agent_Config/ResearchAI_Data_Flow_Architecture.md` for architecture reference.

---

### 6. Follow Paper Processing Decision Framework

Agents must not perform deep analysis automatically. Paper processing depth must follow Paper Processing Decision Framework (08_Agent_Config/Paper_Processing_Decision_Framework.md).

Every paper MUST go through Level 1 screening. Levels 2 and 3 require explicit criteria to be met. Never skip screening. Never auto-promote a paper to Argument Mining Paper Logic without trigger conditions being satisfied.


### 7. Evaluate Reproducibility Status

Agents must evaluate reproducibility status for every paper processed. This is NOT the same as checking whether code exists. Reproducibility requires evaluating ALL of: code availability, dataset accessibility, checkpoint availability, preprocessing scripts, hyperparameter completeness, environment specifications, and hardware requirements.

Agents must distinguish between "code exists" and "paper is reproducible." A paper with public code but missing checkpoints, undefined random seeds, or proprietary data is NOT reproducible.

**Code Status must use one of four graded values:**
- **Confirmed Available** â€?verified the repository exists and is reachable
- **Confirmed Missing** â€?full-text verification confirms no code is provided
- **Not Found Yet** â€?paper mentions code but URL not located in full text
- **Not Checked** â€?agent has not verified (requires human follow-up)

**Critical rule**: Agents must NOT mark code as "Unavailable" or "Missing" unless full-text verification confirms absence. The default when code is not explicitly mentioned is "Not Found Yet," not "Missing."

These evaluations are mandatory in:
- Literature Cards (Level 1): Initial assessment using paper text, record evidence location
- Paper Notes (Level 2): Verify against actual repositories, record verification method
- Paper Logic (Level 3): Deep analysis of whether experimental claims are reproducible

Never skip reproducibility evaluation. Never conflate code availability with reproducibility.

### 8. Context Recovery After Compression

After any context window compression or thread reset, agents MUST restore project context in this order:

1. Read PROJECT_STATUS.md â€?understand completed stages and current position.
2. Read Current_State_Check.md â€?understand known issues and next actions.
3. Read ResearchAI_Design_Principles.md â€?remember permanent architectural decisions.
4. Read relevant ADR documents (e.g., ADR_Zotero_PDF_Centered_Architecture.md) â€?remember why specific architecture choices were made.

**Critical:** Do NOT redesign or restructure completed architecture after context compression. The system has already been designed through extensive iteration. Trust the existing structure. If a question arises about why something was done a certain way, check the ADR documents first.

**Never:** Re-run stages that are already completed. Never recreate templates that already exist. Never redesign directories that are already established.

### 9. Zotero-First Literature Entry

**Zotero is the only entry point for papers entering ResearchAI KnowledgeVault.**

Before any paper can be processed through MinerU and KnowledgeVault, it MUST first be imported into Zotero. This is a hard rule, not a recommendation.

**Mandatory workflow:**

1. PDF acquired â†?Import into Zotero (creates bibliographic record)
2. Zotero metadata verified (title, authors, year, venue, DOI, citation key)
3. PDF stored in Zotero storage directory
4. MinerU reads PDF from Zotero storage
5. KnowledgeVault notes generated from MinerU output

**If Zotero record is missing:**

STOP processing. Respond with: "Paper is not registered in Zotero. Import into Zotero before KnowledgeVault processing."

**Rationale:** Zotero owns bibliographic truth (ADR-001). All metadata, citations, and PDFs flow through Zotero. MinerU is only a PDF extraction tool â€?it does not own any paper asset.

**Agent enforcement:** Before creating any KnowledgeVault note, verify the corresponding Zotero item exists. Check the Zotero database or Zotero item key field in the paper's metadata. If no Zotero record exists, halt and request Zotero import.

### 10. Existing KnowledgeVault Verification

Before creating any new paper file (Literature Card, Paper Note, or Paper Logic), agents MUST verify the paper does not already exist in the KnowledgeVault.

Check in order:
1. MinerU_Zotero_Mapping.md ¡ª search by Zotero Item Key and Paper ID.
| `08_Agent_Config/ResearchAI_Skill_Guide_CN.md` | Skill system user guide (Chinese) |
| `08_Agent_Config/Skills/` | Skill framework directory ¡ª standardized agent procedures |
2. Paper_Index.md ¡ª search by filename pattern.
3. 02_KnowledgeVault/01_Papers/ ¡ª search for matching {author}{year}_* files.

If a match is found: STOP creation. Update the existing file if needed. Do not create duplicates.

This rule prevents redundant notes and ensures KnowledgeVault integrity during batch processing.

## Critical Research Rules

### 1. Do Not Modify Directory Architecture Without Approval

The directory structure in `README.md` is a design contract. Changes require explicit user approval.

### 2. Do Not Fabricate

Never fabricate:

- Experiments that were not run
- Datasets that were not used
- Results that were not obtained
- Citations that do not exist

If you are unsure about a fact, state the uncertainty explicitly.

### 3. Distinguish Dataset Provenance

Always distinguish between:

- **Mentioned in paper** éˆ?a dataset the paper references but did not personally use
- **Personally used** éˆ?a dataset the paper actually ran experiments on
- **Benchmark target** éˆ?a dataset used as a standard evaluation target

This distinction is critical for avoiding hallucinated claims about what has been done.

### 4. Prefer Knowledge Compression

Do not store unnecessary raw text inside KnowledgeVault.

- Store structured summaries, not full paper reproductions
- Store key insights, not every paragraph
- Link to external sources (PDFs, code repos) instead of duplicating content

### 5. Maintain Obsidian Wikilinks

All internal knowledge connections use `[[wikilink]]` syntax. Every note should link to related notes. This is the backbone of the knowledge graph.

---

## Knowledge Processing Strategy

Future papers are processed through three levels:

### Level 1: Literature Screening

- **Input**: MinerU markdown (full.md)
- **Output**: Literature Card
- **Purpose**: Rapid classification of 50-100 papers
- **Token cost**: Low
- **Decision**: Deep Read / Keep Reference / Ignore

### Level 2: Deep Analysis

- **Input**: Selected papers from Level 1
- **Output**: Paper Note + Method + Task + Dataset
- **Purpose**: Full understanding of important papers
- **Token cost**: Medium
- **Scope**: Only for papers marked "Deep Read"

### Level 3: Research Development

- **Input**: Core papers from Level 2
- **Output**: Experiment + Idea + Writing
- **Purpose**: Turn knowledge into research output
- **Token cost**: High
- **Scope**: Only for papers that inspire active research

---

## External Data Paths

### Zotero (Single Source of Truth for PDFs)

- **Zotero data directory**: `D:\ResearchAI_Data\`
  - `storage/` éˆ?PDF files (MinerU reads from here)
  - `zotero.sqlite` éˆ?bibliographic metadata
- **ADR-001**: Zotero-centered PDF architecture. All PDFs managed by Zotero.

### Other Data

- **MinerU output**: `D:\ResearchAI_Data\Paper\MinerU_md\`
- **Datasets**: `D:\ResearchAI_Data\Datasets\`
- **Experiment results**: `D:\ResearchAI_Data\Experiment_Results\`
- **Model checkpoints**: `D:\ResearchAI_Data\Model_Checkpoints\`
- **Config**: `research_config.yaml`

Always check `research_config.yaml` for current data paths before assuming file locations.

---

## Quick Reference

| File | Purpose |
|---|---|
| `README.md` | Project design and directory structure |
| `PROJECT_STATUS.md` | Stage tracking and task completion |
| `research_config.yaml` | Workspace and data path configuration |
| `02_KnowledgeVault/Vault_README.md` | Vault conventions (bilingual, links, tags, naming) |
| `02_KnowledgeVault/Templates/README.md` | Template selection guide |
| `08_Agent_Config/Literature_Processing_Strategy.md` | Paper processing strategy |
| `08_Agent_Config/Current_State_Check.md` | Current status snapshot |
| `08_Agent_Config/MinerU_Workflow_Status.md` | MinerU workflow documentation |
| `08_Agent_Config/Missing_Data_Report.md` | Missing data path documentation |
| `08_Agent_Config/Stage_1.4A_Test_Report.md` | First paper validation report |
| `08_Agent_Config/Zotero_Integration_Design.md` | Zotero architecture design |
| `08_Agent_Config/Single_Paper_End_to_End_Test.md` | Single paper test plan |
| `08_Agent_Config/ADR_Zotero_PDF_Centered_Architecture.md` | ADR-001: PDF architecture decision |
| `04_Tools/Data_Storage_Architecture.md` | SSD vs external drive allocation |
| `04_Tools/Zotero/Zotero_Storage_Strategy.md` | Zotero storage configuration |
| `08_Agent_Config/Paper_Processing_Decision_Framework.md` | 3-level processing strategy with enforcement rules |
| `08_Agent_Config/Paper_File_Naming_Rules.md` | Filename conventions and identifier separation |
| `08_Agent_Config/Paper_Card_Guideline.md` | Card vs Note vs Logic roles |
| `08_Agent_Config/Paper_Logic_Guideline.md` | Mandatory Argument Mining standard |
| `08_Agent_Config/ResearchAI_Data_Flow_Architecture.md` | **Definitive architecture reference** â€?three layers, data flow, explicit rules |
| `08_Agent_Config/Batch_Processing_Guideline.md` | Batch processing workflow, Zotero-first rules, duplicate prevention |
| `08_Agent_Config/MinerU_Zotero_Mapping.md` | Paper source-to-knowledge traceability registry |
