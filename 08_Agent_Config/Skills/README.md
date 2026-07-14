# ResearchAI Skills Directory

This directory contains the ResearchAI Skill framework — standardized, reusable agent procedures for executing frozen workflows.

## Structure

| Directory | Purpose |
|---|---|
| `01_Literature/` | Paper intake, deep read, batch processing, update workflows |
| `02_Knowledge/` | Knowledge node management, research map maintenance |
| `03_Writing/` | Literature synthesis, writing material generation |
| `04_System/` | Architecture audit, system health checks |

## Permission Model

All Skills operate in **Semi-Automatic Mode (Mode B)**:

1. Agent analyzes the request
2. Agent generates an execution plan
3. Agent presents the plan for human confirmation
4. Upon confirmation, agent executes
5. No Skill may silently modify KnowledgeVault

## Usage

Skills are invoked through agent commands. Refer to `../ResearchAI_Skill_Guide_CN.md` for the complete Chinese-language guide with examples.

## Relationship to Architecture

Skills are an **infrastructure extension**, not an architecture modification. They formalize existing frozen workflows but do not change:
- Directory structure
- Templates
- Processing framework
- Data flow architecture
- Naming conventions

The frozen architecture (Zotero → MinerU → KnowledgeVault) remains unchanged.
