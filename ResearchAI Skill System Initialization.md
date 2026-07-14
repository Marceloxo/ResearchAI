

# ResearchAI Skill System Initialization

## Context

ResearchAI architecture has completed Stage 1.5-7C batch processing validation and Stage 1.5-7B architecture freeze.

The current architecture is frozen:

Zotero → MinerU → KnowledgeVault

Frozen principles:
- Zotero is the source of truth for papers.
- MinerU is a transient parsing layer.
- KnowledgeVault is the permanent knowledge layer.
- No architecture redesign is allowed.
- Existing templates and directory structures must not be changed without explicit approval.

The purpose of this task is to introduce a Skill system that formalizes existing workflows into reusable Agent procedures.

This is an infrastructure extension, NOT an architecture modification.

---

# Objective

Create the initial ResearchAI Skill framework.

The Skill system should allow future Codex sessions to execute standardized workflows through commands like:

```

/SKILL Paper Intake

76SW77W3

```

or:

```

/SKILL Deep Read

76SW77W3

```

The Skill system follows a human-confirmation workflow.

---

# Permission Model

IMPORTANT:

All Skills must follow:

## Semi-Automatic Mode (Mode B)

Workflow:

1. Agent analyzes request.
2. Agent generates execution plan.
3. Agent shows:

Example:

```

Execution Plan:

Input:  
Zotero Item Key: 76SW77W3

Detected:  
PDF:  
xxx.pdf

MinerU:  
xxx/full.md

Will create:  
02_KnowledgeVault/01_Papers/  
abdallah2024_inasar_vit_note.md

Will modify:  
Paper_Index.md  
MinerU_Zotero_Mapping.md

Waiting for confirmation.

```

4. User confirms.
5. Agent performs modifications.

No Skill may silently modify KnowledgeVault.

---

# Create Directory

Create:

```

C:\ResearchAI\08_Agent_Config\Skills\

```

Structure:

```

Skills/

├── README.md

├── 01_Literature/  
│  
│ ├── SKILL_Paper_Intake.md  
│ ├── SKILL_Paper_Deep_Read.md  
│ ├── SKILL_Paper_Batch_Process.md  
│ └── SKILL_Paper_Update.md  
│  
├── 02_Knowledge/  
│  
│ ├── SKILL_Knowledge_Node_Check.md  
│ └── SKILL_Research_Map_Update.md  
│  
├── 03_Writing/  
│  
│ └── SKILL_Literature_Synthesis.md  
│  
└── 04_System/

```
└── SKILL_Architecture_Audit.md
```

```

Do NOT create additional Skills at this stage.

---

# Required Skill Files

Create the following 8 Skills.

---

# 1. SKILL_Paper_Intake.md

Purpose:

Handle newly imported papers.

Input:

```

Zotero Item Key

```

Example:

```

76SW77W3

```

Workflow:

1. Verify Zotero storage:

```

D:\ResearchAI_Data\Zotero\storage{ItemKey}

```

2. Locate PDF.

3. Locate corresponding MinerU output:

```

D:\ResearchAI_Data\Paper\MinerU_md\

```

4. Verify:

```

full.md

```

exists.

5. Check:

```

MinerU_Zotero_Mapping.md

```

6. Check duplicates:

- Paper_Index.md
- 01_Papers/

7. Decide processing level:

Level 1:
Literature Card

Level 2:
Paper Note

Level 3:
Research Insight

8. Generate execution plan.

Must not modify before confirmation.

---

# 2. SKILL_Paper_Deep_Read.md

Purpose:

Generate technical Paper Note.

Input:

```

Zotero Item Key

```

Workflow:

Read:

```

MinerU/full.md

```

Generate:

```

02_KnowledgeVault/01_Papers/  
{author}{year}_{keyword}_note.md

```

Use existing Paper_Template.md.

Required analysis:

- Problem
- Motivation
- Contribution
- Architecture
- Method details
- Training strategy
- Loss function
- Results
- Ablation
- Limitations
- Transferability to seismic AI
- Reproducibility

No fabricated information.

Unknown information:

```

Not Found Yet

```

---

# 3. SKILL_Paper_Batch_Process.md

Purpose:

Batch processing.

Input:

Multiple Zotero Item Keys.

Execute:

For each paper:

```

Zotero verification

↓

Mapping verification

↓

Duplicate check

↓

Processing decision

↓

Literature Card

↓

Optional Deep Read

↓

Index update

↓

Log update

```

Must follow:

```

Batch_Processing_Guideline.md

```

---

# 4. SKILL_Paper_Update.md

Purpose:

Update existing papers.

Examples:

- New GitHub repository found
- Citation update
- Dataset update
- Additional information

Before modification:

Show:

```

Existing file:  
xxx.md

Modification:  
xxx section

Reason:  
xxx

```

Wait confirmation.

---

# 5. SKILL_Knowledge_Node_Check.md

Purpose:

Prevent unnecessary knowledge node creation.

Input:

New concept.

Example:

```

ChangeFormer

```

Output:

Recommendation only.

Possible results:

```

Reuse Existing Node

Create New Node

Wait for More Evidence

```

Never automatically create nodes.

Criteria:

- Appears in multiple papers
- Relevance to seismic AI
- Transfer value
- Concept maturity

---

# 6. SKILL_Research_Map_Update.md

Purpose:

Maintain:

```

00_Meta/  
Research_Map.md

Deep_Learning_Map.md

Seismic_AI_Map.md

```

Before modification:

Generate preview.

Wait confirmation.

---

# 7. SKILL_Literature_Synthesis.md

Purpose:

Generate writing materials.

Input:

Topic.

Example:

```

Transformer in Seismic AI

```

Read:

```

KnowledgeVault

```

Generate:

```

08_Writing/

```

content.

Structure:

- Historical evolution
- Current methods
- Comparison
- Research gaps
- Future directions
- References

Do not create final manuscript automatically.

---

# 8. SKILL_Architecture_Audit.md

Purpose:

Periodic system audit.

Check:

- Broken wikilinks
- Naming convention
- Zotero mapping
- Duplicate papers
- Template compliance
- Directory integrity

Read-only by default.

Generate audit report only.

---

# Create Human Documentation

Create:

```

C:\ResearchAI\08_Agent_Config\ResearchAI_Skill_Guide_CN.md

```

Language:

Chinese.

Purpose:

Human-readable manual.

Include:

## 1. Skill System Introduction

Explain:

- Why Skills exist
- Relationship with Agent
- Relationship with frozen architecture


## 2. Skill Invocation

Examples:

### New Paper

```

/SKILL Paper Intake

76SW77W3

```


### Deep Read

```

/SKILL Deep Read

76SW77W3

```


### Batch

```

/SKILL Batch Process

76SW77W3  
6VTKJ8W2

```


## 3. Workflow Diagram

Include:

```

Research Asset

↓

Skill Router

↓

Verification

↓

Execution Plan

↓

Human Confirmation

↓

KnowledgeVault Update

```


## 4. Skill List

Explain every Skill:

- Purpose
- Input
- Output
- When to use


## 5. Usage Examples

Include examples:

- Adding new paper
- Deep reading important paper
- Updating old paper
- Creating literature synthesis
- Running architecture audit


---

# Modify Existing Files

Only update:

## AGENT_BOOTSTRAP.md

Add Quick Reference entry:

```

ResearchAI_Skill_Guide_CN.md

```

and:

```

Skills/

```

Do NOT modify existing rules.

Do NOT modify:

- Templates
- KnowledgeVault
- Data architecture
- Batch rules

---

# Validation Required

After completion report:

1. Created files list

2. Modified files list

3. Confirm:

- No architecture changes
- No KnowledgeVault content changed
- No templates changed
- Skill permission model is Mode B
- Existing frozen rules remain unchanged

Create:

```

Stage_1.5_8A_Skill_System_Initialization_Report.md

```

under:

```

08_Agent_Config/

```

---

# Important

This task creates the Skill framework only.

Do NOT process any papers.

Do NOT create Literature Cards.

Do NOT create Paper Notes.

Do NOT modify existing research content.