# 03_Projects

## Purpose

Research implementation projects — the executable code behind research ideas.

## What Goes Here

Each subdirectory is a self-contained research project containing:

- Deep learning model source code
- Training and evaluation scripts
- Configuration files
- Project-specific documentation

Example structure:

```
SeismicFaultSegmentation/
  ├── README.md
  ├── src/
  ├── configs/
  ├── scripts/
  └── requirements.txt
```

## Projects Are Self-Contained

Each project should be independently understandable and runnable. Avoid cross-project code dependencies unless they live in `04_Tools/`.

## Relationship to Other Directories

- Implements ideas from `07_Research_Ideas/`
- Runs experiments tracked in `05_Experiments/`
- May use shared utilities from `04_Tools/`
- Produces results that feed into `02_KnowledgeVault/` and `06_Writing/`
