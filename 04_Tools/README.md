# 04_Tools — Reusable Scripts and Utilities

## Purpose

Shared scripts and utilities used across multiple ResearchAI projects.

This directory is for **tools**, not **projects**. If code is specific to a single research project, it belongs in `03_Projects/`. If it is used by multiple projects or workflows, it belongs here.

---

## Tool Categories

### External Tool Integration

Scripts and configurations for integrating external tools:

- **Zotero**: BibTeX export scripts, collection management, metadata sync
- **MinerU**: CLI wrapper scripts, batch processing automation
- **Obsidian**: Plugin configurations, vault management scripts
- **Dataview**: Query templates for automated paper indices

### Data Processing

Utilities for transforming and preparing data:

- Format converters (PDF → Markdown, SEGY → NumPy)
- Data preprocessing pipelines
- Image extraction and organization
- Citation format conversion

### Visualization

Shared plotting and visualization utilities:

- Standard figure styles and color schemes
- Seismic data visualization helpers
- Experiment result plotting templates
- Comparison chart generators

### Automation

Scripts for repetitive tasks:

- File organization and cleanup
- Literature Index auto-updates
- Backup and sync scripts
- Quality check automation

---

## Guidelines

1. **Project-specific code goes in `03_Projects/`**, not here.
2. **Each tool should have its own directory** with a README explaining usage.
3. **Avoid duplicating code** — if a utility already exists here, reuse it.
4. **Document dependencies** — list required packages and installation steps.
5. **Keep tools lightweight** — this is a research workspace, not a software product.

---

## Relationship to Other Directories

- Used by `03_Projects/` (projects import shared utilities)
- Supports `05_Experiments/` (visualization and analysis tools)
- Assists `01_Literature/` (format conversion, batch processing)
- Configured by `08_Agent_Config/` (tool setup and automation)
