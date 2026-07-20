
# Stage 7 — ResearchAI System Audit & Consistency Review

## Background

You are now taking over an existing long-term research infrastructure project named ResearchAI.

This project has gone through multiple construction stages:

Stage 0
Workspace Initialization

- ResearchAI directory structure
- Git initialization
- Basic configuration
- Agent workspace

Stage 1
Knowledge Infrastructure Construction

- Obsidian KnowledgeVault
- Templates
- Meta indexes
- Paper Index
- Research maps

Stage 1.5
Agent Workflow System

- Skill system
- Paper intake workflow
- Deep Read workflow
- Batch processing
- Zotero integration
- MinerU pipeline
- Encoding governance
- Workflow automation

Stage 2
Literature Intelligence

- Large-scale paper processing
- Literature cards
- Paper notes
- Paper logic extraction
- Knowledge graph construction
- Research gap discovery

Stage 3
Research Direction Formation

- Seismic AI Research Map
- Method nodes
- Dataset nodes
- Task nodes
- Idea nodes
- Experiment planning

Stage 4
Experiment System

- Dataset management
- Baseline reproduction
- Model development
- Experiment tracking
- Result analysis

Stage 5
Paper Production

- Writing pipeline
- Draft generation
- Revision workflow
- Reference management
- Submission preparation


Later stages focused on KnowledgeVault refinement:

Stage 6.x
KnowledgeVault Quality Improvement

Including:

- Method/task/dataset node creation
- Schema consistency audit
- Wikilink integrity
- Encoding repair
- Dataset-task connectivity
- Knowledge graph refinement


## Important Context

The project was migrated from Windows to Ubuntu.

During migration, potential issues may have appeared:

- .codex configuration differences
- Codex session migration
- Skill migration
- Plugin differences
- MCP configuration differences
- Path changes
- Trust configuration changes
- Encoding conversion problems
- Git configuration changes
- Line ending differences
- File permission differences
- Environment differences


## Current Mission

DO NOT execute any modification.

This is a READ-ONLY audit.

Your task is to reconstruct the actual current state of ResearchAI and produce a comprehensive audit report.

The goal is to identify:

1. What the project actually is now
2. Whether the implementation still matches the original design goals
3. Whether previous agent executions introduced inconsistencies
4. Whether Windows→Ubuntu migration introduced hidden problems
5. What should be fixed before continuing future stages


---

# Audit Scope

## Part 1 — Project Architecture Reconstruction

Inspect:

- Repository structure
- Main directories
- README files
- Agent configuration files
- Stage documents
- Templates
- Meta files


Answer:

1. What is the current ResearchAI architecture?
2. Does the current directory structure match the intended architecture?
3. Are there obsolete directories/files?
4. Are there missing expected components?
5. Are there duplicated or conflicting components?


---

# Part 2 — Stage Progress Verification

Inspect:

```

08_Agent_Config/

```

Review:

- Stage documents
- Completion reports
- Audit reports
- Proposal documents


Construct:

| Stage | Intended Goal | Current Status | Evidence |
|---|---|---|---|

Determine:

- Which stages are truly completed?
- Which stages only have reports but incomplete execution?
- Which stages have conflicts between report and filesystem?


Pay special attention to:

- Stage 6.5.x
- Stage 6.6.x
- Stage 6.7


Verify reports against actual files.


---

# Part 3 — KnowledgeVault Schema Audit

Inspect:

```

02_KnowledgeVault/

```

Check:

## Methods

```

03_Methods/

```

Verify:

- YAML frontmatter consistency
- Naming conventions
- Template compliance
- Related Tasks links
- Related Papers links
- Duplicate nodes
- Missing nodes


## Tasks

```

04_Tasks/

```

Verify:

- YAML consistency
- Method links
- Dataset links
- Benchmark sections
- Missing relationships


## Datasets

```

05_Datasets/

```

Verify:

- source_type
- Tasks Using This Dataset
- Related Papers
- Dataset provenance


## Meta

```

00_Meta/

```

Verify:

- Index consistency
- Broken links
- Intentional placeholders
- Encoding issues


---

# Part 4 — Knowledge Graph Integrity

Perform a graph-level analysis.

Check:

- Broken wikilinks
- Orphan nodes
- Duplicate concepts
- Naming conflicts
- Case sensitivity issues

Especially check:

Examples:

```

Segformer vs SegFormer
U-Segformer-Hyper vs U-SegFormer-Hyper

```

Look for similar hidden problems.


Classify:

- Real errors
- Intentional navigation placeholders
- Acceptable design choices


---

# Part 5 — Agent Workflow System Audit

Inspect:

```

08_Agent_Config/

```

and related files.

Analyze:

- Are workflows still valid?
- Are skills correctly referenced?
- Are templates synchronized?
- Are prompts outdated?
- Are stage instructions contradictory?


Check for:

- Old paths
- Windows-specific paths
- Deprecated commands
- Missing MCP references
- Broken skill references


---

# Part 6 — Windows → Ubuntu Migration Audit

This section is critical.

Inspect:

## Codex

Check:

```

~/.codex/

```

and project configuration.

Analyze:

- config.toml
- projects
- sessions
- skills
- plugins
- memories
- MCP configuration


Identify:

- Missing migrated data
- Incorrect paths
- Windows leftovers
- Linux incompatibilities


---

## Git

Check:

- remote
- user identity
- line endings
- ignored files
- repository status


Look for:

- unnecessary massive diffs
- permission changes
- executable-bit changes
- encoding changes


---

## Encoding

Scan:

- UTF-8 BOM
- GBK corruption
- CRLF/LF inconsistency


Especially:

- Chinese text
- Markdown files
- YAML


---

# Part 7 — Documentation vs Reality Check

Compare:

Documentation:

```

Stage documents
README files
Templates
Reports

```

against:

Actual filesystem.

Find:

- completed according to report but missing in reality
- existing but undocumented files
- outdated instructions
- conflicting specifications


---

# Part 8 — Research Direction Consistency

Review:

- Seismic_AI_Map
- Method_Map
- Dataset_Map
- Task_Map if exists


Determine:

Does the current KnowledgeVault still support the original research goal:

"Deep Learning + Computer Vision/Image Processing + Seismic AI"

Check whether:

- nodes are balanced
- too much effort shifted into seismology
- computer vision/deep learning side is sufficient
- future paper exploration is supported


---

# Part 9 — Future Development Recommendation

After audit, propose:

## Immediate fixes

(high priority)

## Optional improvements

(medium priority)

## Future Stage roadmap

(low priority)


Do NOT execute fixes.

Only recommend.


---

# Final Deliverable

Create:

```

08_Agent_Config/Stage_7_System_Audit_Report.md

```

Report structure:

```

# Stage 7 — ResearchAI System Audit Report

## 1. Executive Summary

## 2. Current Architecture

## 3. Stage Completion Verification

## 4. KnowledgeVault Status

## 5. Knowledge Graph Analysis

## 6. Agent Workflow Status

## 7. Windows→Ubuntu Migration Audit

## 8. Documentation vs Reality

## 9. Critical Issues

## 10. Recommended Next Steps

## 11. Future Stage Proposal

```

Rules:

- READ ONLY
- No file modification except creating the final report
- Do not repair anything
- Do not create new nodes
- Do not assume previous reports are correct
- Verify against filesystem
- Provide evidence paths for every important conclusion


The final report will be reviewed externally before any further execution.
```


