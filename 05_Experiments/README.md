# 05_Experiments

## Purpose

Experiment tracking system — a structured record of every experiment run.

## What Goes Here

Each experiment lives in its own subdirectory following this template:

```
experiment_name/
  ├── README.md       # Experiment description, hypothesis, and conclusions
  ├── config.yaml     # Hyperparameters and run configuration
  ├── results.json    # Quantitative results and metrics
  └── figures/        # Plots, visualizations, and output images
```

## AI Agent Compatibility

Experiment records must be understandable by AI agents. Every experiment README should include:

- What was tested and why
- Configuration used
- Key results (quantitative and qualitative)
- Interpretation and next steps

## Relationship to Other Directories

- Runs code from `03_Projects/`
- Tests hypotheses from `07_Research_Ideas/`
- Feeds results into `02_KnowledgeVault/`
- Provides evidence for `06_Writing/`
