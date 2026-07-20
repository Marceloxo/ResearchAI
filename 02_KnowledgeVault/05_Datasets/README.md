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
- Actual data files stored in `/home/lco/ResearchAI_Data/datasets\` (external to vault).
- Preprocessing tools in `04_Tools/` (external to vault).

## AI Agent Usage

1. When encountering a new dataset in a paper, create a dataset note here.
2. Always record the data format and loading instructions for reproducibility.
3. Link dataset notes to all papers and experiments that use them.
4. Note any preprocessing steps applied to the dataset before use.

## Knowledge Node Files

- [[EGS Collab SURF]] — Enhanced Geothermal System monitoring dataset
- [[F3 Netherlands]] — Standard seismic facies segmentation benchmark
- [[Marmousi]] — Complex velocity model synthetic benchmark
- [[Northern California Seismic Network]] — ~3M relocated events; GENIE/PLAN benchmark
- [[OpenFWI]] — Full waveform inversion benchmark
- [[Parihaka]] — 3D seismic survey for FWI testing
- [[Penobscot]] — Canadian seismic survey for facies segmentation
- [[SEAM]] — Seal Beach Advanced Modeling benchmark
- [[SEG Salt]] — Salt body segmentation benchmark
- [[Thebe]] — Fault detection benchmark
- [[Japan Hi-net]] — 700+ station dense network; PhaseNet/PLAN benchmark
