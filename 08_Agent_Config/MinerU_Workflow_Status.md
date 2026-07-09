---
tags: [meta, tool-config]
created: 2026-07-08
---

# MinerU Workflow Status

## Current Status / 当前状态

MinerU is used via **Desktop GUI Version**. No CLI automation is configured yet.

## Current MinerU Mode / 当前MinerU模式

Desktop GUI Version — manual one-by-one PDF processing.

## Current Workflow / 当前工作流

```
PDF (from 01_Literature/PDFs/ or 00_Inbox/)
    ↓
MinerU Desktop GUI → Manual Export
    ↓
Output saved to manual export directory
    ↓
Files manually moved to D:\ResearchAI_Data\Literature\MinerU_Output\
    ↓
AI agent reads full.md for processing
```

## Current Limitation / 当前限制

- **Not CLI mode**: Each PDF must be processed manually through the GUI.
- **No batch processing**: Cannot process multiple PDFs in one command.
- **Manual file management**: Output files must be manually organized.
- **Pipeline gap**: No automated trigger from Inbox → MinerU → KnowledgeVault.

## Future Upgrade Plan / 未来升级计划

### Target: MinerU CLI

Switch to MinerU CLI (`magic-pdf` or `mineru` command) to enable:

1. **Batch PDF processing**: Process entire folders of PDFs with one command.
2. **Automatic pipeline**: Watch folder → auto-process → output to standard location.
3. **Integration with ResearchAI**: Agent can invoke MinerU CLI directly.

### CLI Configuration Reference

```bash
# Example: batch process all PDFs in a directory
mineru -p /path/to/pdf/folder -o /path/to/output

# Or with magic-pdf
magic-pdf -p /path/to/pdf/folder -o /path/to/output
```

### Target Output Path

```
D:\ResearchAI_Data\Literature\MinerU_Output\{{paper_name}}\
    ├── full.md
    ├── origin.pdf
    └── images/
```

## Current Phase Strategy / 当前阶段策略

Stage 1.4A is a **validation phase**, not an automation phase. The goal is to:

1. Verify that the template system works with real paper content.
2. Validate the Literature Card → Paper Note → Knowledge Node workflow.
3. Document the current manual MinerU workflow for future automation.

Automation will come in a later stage when the knowledge pipeline is proven.
