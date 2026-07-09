# 06_Experiments — Experiment Interpretation

## Purpose

Experiment records from a knowledge perspective — what was done, why, and what was learned. This is the interpretive layer on top of raw experiment logs stored in `05_Experiments/`.

## Contents

- Experiment interpretation notes (e.g., `Exp - UNet Baseline on Thebe`).
- Hypothesis tested and rationale.
- Key results summary (quantitative and qualitative).
- Interpretation and takeaways.
- Links to the raw experiment directory in `05_Experiments/`.
- Ideas for follow-up experiments.

## Difference from `05_Experiments/`

- `05_Experiments/` (workspace level): Raw experiment artifacts — code configs, logs, figures. Machine-readable.
- `06_Experiments/` (vault level): Human and AI-readable interpretations. Knowledge, not artifacts.

## Relationship to Other Directories

- Links to raw experiment records in `05_Experiments/` (external to vault).
- Tests hypotheses from `07_Ideas/`.
- Validates methods from `03_Methods/` on tasks from `04_Tasks/`.
- Uses datasets from `05_Datasets/`.
- Provides evidence for claims in `08_Writing/`.

## AI Agent Usage

1. After running an experiment, create an interpretation note here even if the experiment failed.
2. Always include "what to try next" — this feeds directly into `07_Ideas/`.
3. Link experiments to the exact method and dataset used.
4. Generate summary tables comparing experiment results for the same task.
