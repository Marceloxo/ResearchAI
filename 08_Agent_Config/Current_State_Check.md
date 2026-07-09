# Current ResearchAI State

## Completed

- Stage 0 — Workspace Initialization
- Stage 1.1 — Obsidian KnowledgeVault Initialization
- Stage 1.2 — Obsidian Note Templates
- Stage 1.3 — Navigation & Knowledge Graph Design
- Stage 1.4A — First Paper End-to-End Validation
- Stage 1.4A.1 — Agent Bootstrap & Workflow Optimization
- Stage 1.4B-0 — Literature Intake System Design
- Stage 1.4B-1 — Processed Markdown Pipeline Design
- Stage 1.4C-0 through 1.4C-3.4 — Zotero integration and PDF architecture
- Stage 1.5-0 through 1.5-5 — Single paper validation, Paper Logic upgrade
- Stage 1.5-6A — Paper Processing Decision Framework
- Stage 1.5-6A.1 — Reproducibility Metadata System
- Stage 1.5-6A.2 — Reproducibility Status Upgrade (graded code status)
- Stage 1.5-6B — Real Paper Stress Test Protocol
- Stage 1.5-6B.1 — Stress Test Execution Tracking System
- **Stage 1.5-6C — Architecture Refactoring**
  - Paper file naming rules defined
  - Reproducibility tracking upgraded to graded status
  - Paper Card vs Paper Note roles clarified
  - Workspace cleanup plan created (no action needed)
  - Context recovery rule added

## Current Stage

**Stage 1.5-6C completed.** System is ready for Stage 1.5-6B stress test execution.

## Known Issues

### 1. Historical Test Report Paths
The Stage_1.4A_Test_Report.md contains historical execution paths from the actual test run. These are **execution logs**, not configuration references, and are intentionally preserved as-is.

### 2. Manual Wikilinks
All knowledge graph links are created manually. No automatic backlink or cross-reference generation.

### 3. Deprecated 01_Literature Subdirectories
Five subdirectories in 01_Literature/ are deprecated but physically retained as empty placeholders:
- Markdown/, PDFs/, 01_PDFs/, 02_MinerU_Output/, 03_Processed_Markdown/
- See 01_Literature/README.md for details

### 4. Unused MinerU Outputs
4 papers have MinerU output on D: but are not yet in KnowledgeVault:
- liu2020.pdf
- park2020.pdf
- tsr-2021001.1.pdf
- zhu2018.pdf (PhaseNet original)

### 5. Zotero Collections/Tags
Zotero is installed and Better BibTeX configured, but collections and tags need manual setup in the Zotero UI before papers can be properly categorized.

## Next Actions

1. **Researcher**: Create Zotero collections (ResearchAI/00_Inbox through Archive) and assign tags per Zotero_Workflow_Configuration.md
2. **Researcher**: Select 4 stress test papers (one per category A/B/C/D)
3. **Agent**: Execute stress test protocol per Stage_1.5_6B_Real_Paper_Stress_Test.md
4. **Agent**: Fill in Stress_Test_Execution_Log.md for each paper

**Architecture is now frozen.** Do not redesign directory structure, naming conventions, or data flow after this stage.

