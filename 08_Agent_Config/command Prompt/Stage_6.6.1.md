
# Continue ResearchAI KnowledgeVault Pipeline

## Current Context

We are continuing the ResearchAI KnowledgeVault maintenance pipeline.

Previous completed stages:

- Stage 6.5.2 — Knowledge Node Extraction Implementation
  - Created new Method / Task / Dataset nodes
  - Updated Meta maps and Paper Index
  - Verified wikilinks

- Stage 6.5.4 — Foundational Method Completion
  - Completed `03_Methods/Vision Transformer.md`

- Stage 6.5.5 — KnowledgeVault Quality Improvement
  - Fixed `Method_Map.md` UTF-8 encoding corruption
  - Added `source_type: public_dataset` to 9 dataset nodes
  - Added "Tasks Using This Dataset" backlinks to dataset nodes
  - Verified no Paper Notes or Templates were modified

- Stage 6.6 — KnowledgeVault Schema Consistency Audit
  - Completed READ-ONLY audit
  - Report generated:
    `08_Agent_Config/Stage_6.6_Audit_Report.md`
  - No files modified during audit

---

# Current Status

Stage 6.6 audit is complete.

The audit report identified schema consistency issues.

The next stage is:

# Stage 6.6.1 — Schema Repair

Before modifying anything:

1. Read:
```

08_Agent_Config/Stage_6.6_Audit_Report.md

```

2. Read relevant templates:
```

08_Agent_Config/Templates/

```

3. Inspect current filesystem state.

4. Generate a READ-ONLY execution proposal first.

Do NOT modify files until the repair plan is reviewed and approved.

---

# Known Stage 6.6 Findings

Priority issues identified:

## P0/P1

1. Task YAML schema inconsistency

Finding:
- 7 task files use `domain:` instead of expected `category:`

Need:
- Determine whether to migrate all tasks to `category`
- Check Task_Template.md before proposing changes


2. Dataset schema incompleteness

Finding:
- 10/11 dataset notes lack:

```

Data Description
Collection Method
Application

```

Need:
- Compare with Dataset_Template.md
- Propose standardized insertion


3. Dataset backlink inconsistency

Finding:
- OpenFWI.md missing:

```

Tasks Using This Dataset

```

Need:
- Verify whether applicable before adding


4. Segformer filename mismatch

Finding:

Actual file:
```

03_Methods/Segformer.md

```

Some references:
```

[[SegFormer]]

```

Need:
- Fix case mismatch according to Obsidian wikilink rules


5. Encoding normalization

Finding:

```

00_Meta/Paper_Index.md

```

contains:
- UTF-8 BOM
- CRLF line endings

Need:
- Normalize encoding only
- Do not alter content


6. Stray file

Finding:

```

03_Methods/Multi-task

```

(no extension)

Need:
- Inspect content
- Decide whether remove or merge


7. Broken meta-map references

Approximately 20 legitimate unresolved links:

Examples:
```

[[ResNet]]
[[Swin Transformer]]
...

```

Need:
- Separate:
  - missing foundational nodes that should exist
  - intentional references that should remain plain text

Do NOT create placeholder nodes without justification.

---

# Execution Rules

Follow ResearchAI pipeline principles:

## Immutable

Never modify:

```

01_Papers/
08_Agent_Config/Templates/

```

unless explicitly requested.

## No fabrication

Do not create:
- fake paper nodes
- fake method nodes
- fake datasets

Only create nodes when they represent real reusable knowledge entities.

## Minimal modification

Prefer:
- schema repair
- encoding correction
- backlink completion

Avoid:
- rewriting existing knowledge content
- unnecessary restructuring

---

# First Action

Start with:

"Stage 6.6.1 — Schema Repair Proposal"

Only produce:

1. Audit summary
2. Proposed modifications
3. Files affected
4. Risk assessment
5. Execution order

No file modifications yet.

Wait for approval.


