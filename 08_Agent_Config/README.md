# 08_Agent_Config

## Purpose

AI agent configuration — instructions, skills, templates, and workflow definitions for AI agents working within ResearchAI.

## What Goes Here

- Agent instruction files (system prompts, task descriptions)
- Skill definitions for research-specific workflows
- Templates for common research tasks (paper analysis, experiment setup, etc.)
- Workflow definitions that span multiple directories

## Agent Compatibility

Future AI agents should read this folder before performing any research task. The configurations here define how agents should interact with the rest of the ResearchAI system.

## Relationship to Other Directories

- Governs how agents operate across all other directories
- Defines workflows that connect `01_Literature/` → `02_KnowledgeVault/` → `03_Projects/` → `05_Experiments/` → `06_Writing/`
- Ensures consistent agent behavior regardless of which AI agent (Codex, Claude Code, etc.) is operating
