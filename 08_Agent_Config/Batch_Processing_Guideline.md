# Batch Processing Guideline

> **Purpose**: Define the batch processing workflow for ResearchAI paper ingestion.
> **Scope**: This guideline governs how papers move through the pipeline in batch mode.
> **Constraint**: Architecture is frozen. Do not modify directory structure, templates, or processing framework.

---

## 1. Batch Processing Overall Workflow

```
Zotero (Layer 1: Source)
    →PDF Verification (Zotero storage exists, readable)
    →MinerU Output Verification (full.md exists, parseable)
    →Level 1 Screening (Literature Card created)
    →Decision Framework (Ignore / Keep Reference / Deep Read)
    →Literature Card (saved to 02_KnowledgeVault/01_Papers/)
    →(Optional) Paper Note (Level 2 —only if Deep Read)
    →Knowledge Node linking (Methods, Tasks, Datasets, Ideas)
    →(Optional) Paper Logic (Level 3 —only if Argument Mining triggers met)
```

Each step must complete successfully before proceeding to the next. If any step fails, the paper is flagged for **Human Review** and processing stops.

---

## 2. Zotero-First Enforcement

**Rule**: Every paper MUST be registered in Zotero before any KnowledgeVault processing begins.

### Mandatory Pre-conditions

1. **PDF must exist in Zotero storage** (`D:\ResearchAI_Data\Zotero\storage\`)
2. **Zotero Item Key must be recorded** —this is the paper's immutable identity
3. **Better BibTeX citation key must be resolved** —used for manuscript citations
4. **Metadata verified** —title, authors, year, venue, DOI match expected values

### Enforcement

- If no Zotero record exists: **STOP**. Flag for human researcher to import.
- If PDF is missing from Zotero storage: **STOP**. Flag for human researcher.
- If Zotero Item Key cannot be determined: **STOP**. Flag for human researcher.
- No MinerU processing or KnowledgeVault notes are created until Zotero verification passes.

### Exception Handling

The Mousavi 2023 paper was processed without Zotero import (detected in Stage 1.5-6E.1). Its Literature Card was corrected to show Zotero status as "Not Imported". This paper must be imported before any Level 2 or Level 3 processing.

---

## 3. Processing Level Decision

Processing depth follows the **Paper Processing Decision Framework** (`Paper_Processing_Decision_Framework.md`).

### Level 1 —Literature Card (Screening)

**Applied to**: All papers. Non-optional.

**Input**: MinerU `full.md` output.
**Output**: Literature Card in `02_KnowledgeVault/01_Papers/`.
**Decision**: Ignore / Keep Reference / Deep Read.

### Level 2 —Paper Note (Deep Analysis)

**Applied to**: Papers marked "Deep Read" at Level 1.
**Input**: Literature Card + MinerU `full.md`.
**Output**: Paper Note in `02_KnowledgeVault/01_Papers/`, plus optional Method/Task/Dataset nodes.
**Decision**: Full understanding, reproducibility analysis, transferable ideas.

### Level 3 —Argument Mining Paper Logic

**Applied to**: Papers meeting ALL Level 3 trigger conditions:
1. Directly influences own research direction
2. Contains novel architecture or design
3. SOTA benchmark paper
4. Highly cited foundational paper

**Input**: Paper Note from Level 2.
**Output**: Paper Logic in `02_KnowledgeVault/09_Paper_Logic/`.

### Batch Processing Rule

In batch mode:
- **All papers** go through Level 1.
- **Only Deep Read papers** proceed to Level 2.
- **Only Level 3 trigger papers** proceed to Level 3.
- Agents MUST NOT auto-promote beyond Level 1 without explicit decision framework criteria.

---

## 4. Knowledge Node Creation Rules

### Principle: Reuse First

Before creating any new knowledge node (Method, Task, Dataset, Topic, Idea), the agent MUST search existing nodes for equivalent or closely related concepts.

### Conditions for Creating a New Node

A new node is created ONLY when ALL of the following are true:

1. **Reuse Value**: The concept appears in or relates to multiple papers (not just one isolated paper).
2. **Necessity**: Understanding the paper requires this concept as a distinct reference point.
3. **Stability**: The concept is a stable research term (not a paper-specific phrasing or temporary label).

### Prohibited Behaviors

- **DO NOT** create a new node for every paper.
- **DO NOT** create nodes for paper-specific experiment names or temporary labels.
- **DO NOT** create duplicate nodes with slightly different names (e.g., "Vision Transformer" vs "ViT" vs "Transformer for Vision").
- **DO NOT** create nodes that exist only as mentions without substantive discussion.

### Search Procedure

Before creating a new Method/Task/Dataset node:
1. List existing nodes in the target directory (`03_Methods/`, `04_Tasks/`, `05_Datasets/`).
2. Search file contents for keyword matches.
3. If a closely related node exists, add a wikilink to it instead of creating a new one.
4. If uncertain, flag for human review.

---

## 5. Duplicate Prevention Rules

### What to Check Before Creating Any Node

| Entity Type | Check Against |
|---|---|
| **Method** | Existing methods in `03_Methods/` —compare architecture, purpose, domain |
| **Task** | Existing tasks in `04_Tasks/` —compare input/output formulation |
| **Dataset** | Existing datasets in `05_Datasets/` —compare source, format, scale |
| **Idea** | Existing ideas in `07_Ideas/` —compare hypothesis, approach, feasibility |

### Duplicate Detection Strategy

1. **Exact name match**: Check if the proposed node name already exists.
2. **Synonym match**: Check for common abbreviations and full names (e.g., "CNN" vs "Convolutional Neural Network").
3. **Semantic match**: If the new node describes the same concept as an existing one (even with different naming), reuse the existing node.
4. **Cross-directory check**: Some concepts may be in unexpected directories. Check broadly before creating.

### Resolution

- If duplicate detected: Add wikilink to existing node. Log the detection in the processing table.
- If near-duplicate (related but distinct): Create new node, but add cross-links to the related existing node.

---

## 5.5 Mapping Registry Requirement

Every processed paper must have a verified entry in MinerU_Zotero_Mapping.md before KnowledgeVault creation.

**Rule**: Before creating any Literature Card, Paper Note, or Paper Logic, the agent MUST:
1. Verify the paper's row exists in MinerU_Zotero_Mapping.md.
2. Confirm Zotero Item Key, PDF Filename, and MinerU Output Folder are correct.
3. If no row exists, create one with status PENDING_ZOTERO or PENDING_MINERU as appropriate.
4. Update the row's KnowledgeVault Files and Status after processing completes.

This rule prevents source-to-knowledge traceability loss during batch processing.


## 5.6 Processing Gate — Existing KnowledgeVault Check

Before creating any Literature Card, Paper Note, or Paper Logic, the agent MUST verify the paper does not already exist in the KnowledgeVault.

**Check three sources in order:**

1. **MinerU_Zotero_Mapping.md** — Has this paper already been processed? Check Zotero Item Key and Paper ID columns.
2. **Paper_Index.md** — Is this paper listed in the vault index? Check filename patterns.
3. **01_Papers/ directory** — Does a file with the same Paper ID pattern exist? Check {author}{year}_{keyword}_{type}.md naming convention.

**Duplicate detection criteria (ANY match = duplicate):**

| Check | What to match |
|---|---|
| Zotero Item Key | Exact match in MinerU_Zotero_Mapping.md |
| Paper ID | Same author-year-keyword prefix (e.g., chai2020_using) |
| Filename pattern | Any file in 01_Papers/ matching {author}{year}_*_{card,note,logic,survey,card}.md |

**If duplicate detected:**

- STOP file creation immediately.
- Check the existing file's status and processing level.
- If the existing file is incomplete (e.g., Card exists but Note does not), append missing content.
- Do NOT create a duplicate note — update the existing file instead.
- Log the duplicate detection in Batch_Processing_Log.md under "Duplicate Detections".

**Gate enforcement:** This check is mandatory for every paper in batch processing. Skipping it risks KnowledgeVault duplication.
## 6. Human Review Checkpoints

During batch processing, the following situations require **human researcher confirmation** before proceeding:

| Checkpoint | Condition | Action |
|---|---|---|
| **Zotero Missing** | Paper has no Zotero record | Stop. Request human to import PDF and metadata to Zotero. |
| **MinerU Output Missing** | No `full.md` found for the paper | Stop. Request human to run MinerU on the PDF. |
| **Paper Type Uncertain** | Cannot determine if Survey / Research Article / Benchmark | Flag. Ask human to classify. |
| **Level 2 Decision Disputed** | Borderline case: Keep Reference vs Deep Read | Flag. Ask human to decide processing depth. |
| **New Knowledge Node** | Agent believes a new node should be created | Flag. Human confirms node necessity and naming. |
| **Level 3 Trigger** | Paper meets Level 3 criteria | Flag. Human confirms Argument Mining is warranted. |
| **Reproducibility Blocker** | Critical missing component identified | Flag. Human decides if this is acceptable for the paper's value. |
| **Template Ambiguity** | Paper type doesn't match existing template well | Flag. Human selects or approves custom approach. |

### Batch Mode Behavior

- Collect all flags during processing.
- Present a consolidated review list to the human after the batch completes.
- Do NOT stop the entire batch for a single flag unless the Zotero or MinerU pre-condition fails.

---

## Quick Reference

| Document | Purpose |
|---|---|
| `Paper_Processing_Decision_Framework.md` | 3-level processing strategy, decision tree, scoring rubric |
| `Paper_Card_Guideline.md` | Literature Card role and content rules |
| `Paper_Logic_Guideline.md` | Argument Mining Paper Logic mandatory standard |
| `Paper_File_Naming_Rules.md` | Filename conventions and identifier separation |
| `ResearchAI_Data_Flow_Architecture.md` | Three-layer architecture reference |
| `Stress_Test_Execution_Log.md` | Batch processing execution log |
