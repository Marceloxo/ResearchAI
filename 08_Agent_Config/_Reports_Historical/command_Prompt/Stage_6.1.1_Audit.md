
# Task: Generate ResearchAI Project Architecture Audit Report

You are performing a complete architecture audit after Windows → Ubuntu migration.

DO NOT modify any files.

Your task:
Generate a comprehensive markdown report describing the current state of the ResearchAI project.

Output file:

08_Agent_Config/Migration/ResearchAI_Current_Architecture_Audit.md


The report should help another AI agent understand the entire project structure and make future architectural decisions.

---

## 1. Project Root Overview

Analyze:

/home/lco/ResearchAI/

Provide:

- absolute path
- directory tree (important directories only)
- purpose of each top-level directory
- whether the directory is active / deprecated / unclear


Example:

```

ResearchAI/
├── 01_Literature
├── 02_KnowledgeVault
├── 03_Templates
├── 04_Tools
├── 08_Agent_Config
└── ...

```


For each:

| Directory | Purpose | Status | Notes |
|---|---|---|---|


---

## 2. Data Layer Analysis

Analyze:

/home/lco/ResearchAI_Data/


Report:

### Zotero

- database location
- attachment location
- storage structure
- relation between paper key and attachment key


### MinerU

Analyze:

MinerU_md/

Report:

- folder count
- naming convention
- output structure
- compatibility with Agent contract:

Required:

```

paper_folder/
├── full.md
└── images/

```


### Registry

Analyze:

08_Agent_Config/Paper_Processing_State.yaml


Report:

- schema version
- fields
- current statistics
- dependency relationships


---

## 3. KnowledgeVault Architecture

Analyze:

02_KnowledgeVault/


Identify:

- directory tree
- note categories
- templates
- naming convention


Especially report:

```

_card.md
_note.md
_method.md
_logic.md
_survey.md

```


For each:

- purpose
- current count
- connection with registry agent_state


---

## 4. Agent System Analysis

Analyze:

08_Agent_Config/


Report:

Tree:

```

08_Agent_Config/
├── Skills
├── Migration
├── Templates
└── Registry

```


Identify:

### Existing skills

For every SKILL file:

Provide:

| Skill | Purpose | Dependencies | Status |


Analyze:

- Are skills discoverable by Codex?
- Are paths correct after Ubuntu migration?
- Any broken references?


---

## 5. Tooling Layer Analysis

Analyze:

04_Tools/


Especially:

```

04_Tools/mineru/

```


Report:

All scripts:

| Script | Function | Input | Output | Used by |


Include:

- normalize_mineru_output.py
- process_paper.py
- batch_process.py
- validate_mineru_output.py
- scan_registry.py


Analyze:

- dependency order
- whether scripts form a complete pipeline


---

## 6. End-to-End Pipeline Diagram

Generate current real workflow:

Example:

```

Zotero
|
| scan_registry.py
↓
Paper_Processing_State.yaml
|
| batch_process.py
↓
MinerU
|
| normalize
↓
full.md
|
| Agent
↓
KnowledgeVault
|
| scan_registry.py
↓
agent_state

```


Mark:

- completed components
- missing components
- manual intervention points


---

## 7. Migration Audit

Compare:

Before migration (Windows)

vs

Current Ubuntu


Check:

- hardcoded paths
- absolute paths
- environment assumptions
- Windows-specific dependencies


Search for:

```

C:
D:
Users
AppData

```


Report any remaining.


---

## 8. Broken / Risk Items

Create a section:

## Architecture Risks


Classify:

HIGH:
- breaks workflow

MEDIUM:
- future maintenance issue

LOW:
- cosmetic


Examples:

- duplicated configuration
- undocumented scripts
- missing dependency
- inconsistent naming


---

## 9. Recommended Next Stage

Based on current architecture:

Recommend:

Stage 6.2+

Include:

- priority
- reason
- expected impact


Do NOT implement anything.

Only analyze.


---

## 10. Final Summary

Provide:

Current maturity assessment:

Choose:

- Prototype
- Functional pipeline
- Production-ready research assistant
- Autonomous research system


Explain why.


---

Important:

DO NOT modify existing files.

Only create:

08_Agent_Config/Migration/ResearchAI_Current_Architecture_Audit.md

```


