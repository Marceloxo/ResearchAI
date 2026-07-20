# Task: Execute Stage 7.1 — Research Gap Discovery

You are continuing the ResearchAI project.

Current system status:

Completed:

- Stage 0 — Workspace Initialization
- Stage 1 — Knowledge Infrastructure Construction
- Stage 1.5 — Agent Workflow System
- Stage 2 — Literature Intelligence Pipeline (foundation)
- Stage 3 — Knowledge Graph Construction (first version)
- Stage 6.5.x — Knowledge Node Extraction and Graph Enhancement
- Stage 6.6.x — Schema Audit and Repair
- Stage 6.7 — Connectivity Enhancement

Current KnowledgeVault status:

- Obsidian KnowledgeVault is operational
- Method / Task / Dataset / Paper nodes exist
- Wikilink graph has been validated
- YAML schema has been repaired
- Meta maps are functional
- No major structural repair is required

Important constraints:

1. DO NOT modify files immediately.
2. First perform READ-ONLY analysis.
3. Do not fabricate missing papers, methods, datasets, or research gaps.
4. Preserve existing KnowledgeVault schema.
5. Do not modify:
   - 01_Papers/
   - Templates/
   - Agent configuration files
   unless explicitly approved.
6. All proposed modifications require approval first.

---

# Stage 7.1 Objective

Transition ResearchAI from:

"knowledge organization"

to:

"research intelligence".

The goal is to discover potential research gaps from the existing knowledge graph.

---

# Phase A — Read Current Context

First inspect:

## Agent documents

08_Agent_Config/

Read:

- Stage_6.6_Audit_Report.md
- Stage_6.6.1_Completion_Report.md
- Stage_6.6.2_Audit_Report.md
- Stage_6.7_Completion_Report.md

## Knowledge structure

Inspect:

02_KnowledgeVault/

Especially:

- 00_Meta/
- 03_Methods/
- 04_Tasks/
- 05_Datasets/

Understand:

- existing methods
- existing tasks
- existing datasets
- existing relationships


---

# Phase B — Knowledge Graph Analysis

Perform READ-ONLY analysis.

Build the following matrices:

## 1. Method × Task Matrix

Example:

| Method | Task | Evidence |
|---|---|---|
| PhaseNet | Phase Picking | paper/task link |
| GENIE | Phase Association | paper/task link |
| SegFormer | Seismic Facies Segmentation | task link |


Identify:

- over-explored combinations
- under-explored combinations
- missing connections


---

## 2. Task × Dataset Matrix

Analyze:

- which tasks have strong benchmarks
- which tasks lack datasets
- which datasets are under-utilized


---

## 3. Method Evolution Analysis

Analyze:

Example:

CNN
 ↓
Transformer
 ↓
Hybrid CNN-Transformer
 ↓
Foundation Model


Find:

- mature areas
- emerging areas
- possible gaps


---

# Phase C — Research Gap Extraction

Generate candidate gaps.

Each gap must contain:

## Gap Template

```markdown
## Research Gap

### Problem

Existing limitation.

### Current Solutions

Existing methods.

### Limitation

Why current methods are insufficient.

### Opportunity

Possible research direction.

### Related Nodes

Methods:
Tasks:
Datasets:
Papers:
````

---

# Phase D — Seismic AI + Deep Learning Perspective

Focus on intersection:

Deep Learning
+
Computer Vision
+
Seismic Applications

Prioritize:

* segmentation
* representation learning
* Transformer
* lightweight models
* domain adaptation
* self-supervised learning
* foundation models
* multi-modal learning

Avoid:

* purely geological problems
* problems requiring extensive domain expertise without AI contribution

---

# Phase E — Deliverable

Create:

08_Agent_Config/

Stage_7.1_Research_Gap_Report.md

The report should contain:

1. Current Knowledge Graph Status

2. Method-Task-Dataset Analysis

3. Identified Research Gaps

4. Candidate Research Directions

5. Recommended Next Steps

---

# Important

This stage is ANALYSIS ONLY.

Do NOT:

* create new KnowledgeVault nodes
* modify existing markdown files
* update Meta maps
* edit templates

After completing the report:

STOP.

Wait for explicit approval before any implementation stage.

```


