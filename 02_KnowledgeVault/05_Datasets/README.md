# 05_Datasets — Dataset Documentation

## Purpose

Central registry of datasets used or referenced in research. Each note documents a dataset's origin, characteristics, format, and typical usage.

## Contents

- Dataset description notes (e.g., `Dataset - Thebe Fault Benchmark`).
- Data statistics (size, dimensions, class distribution).
- Data format and loading instructions.
- Licensing and attribution information.
- Known issues or biases.
- Links to papers that introduced or used the dataset.

## Relationship to Other Directories

- Referenced by paper notes in `01_Papers/`.
- Linked from task notes in `04_Tasks/` as benchmarks.
- Used by experiments in `06_Experiments/`.
- Actual data files stored in `D:\ResearchAI_Data\datasets\` (external to vault).
- Preprocessing tools in `04_Tools/` (external to vault).

## AI Agent Usage

1. When encountering a new dataset in a paper, create a dataset note here.
2. Always record the data format and loading instructions for reproducibility.
3. Link dataset notes to all papers and experiments that use them.
4. Note any preprocessing steps applied to the dataset before use.
