# 04_Tasks — Research Task Definitions

## Purpose

Formal definitions of research tasks — the problems that methods aim to solve. Each note defines a task, its input/output specification, evaluation metrics, benchmarks, and state-of-the-art results.

## Contents

- Task definition notes (e.g., `Task - 3D Seismic Fault Segmentation`).
- Problem formulation (input, output, constraints).
- Standard evaluation metrics (with formulas).
- Benchmark datasets and leaderboard results.
- Links to relevant methods that address the task.

## Relationship to Other Directories

- Grounded in paper notes from `01_Papers/`.
- Organized under topics in `02_Topics/`.
- References methods in `03_Methods/`.
- References datasets in `05_Datasets/`.
- Drives experiment design in `06_Experiments/`.
- Informs research gap identification in `07_Ideas/`.

## AI Agent Usage

1. When defining a new project, first check whether the task is already defined here.
2. Keep the SOTA (state-of-the-art) leaderboard up to date.
3. Use task notes to identify which metrics are standard for evaluation.
4. Link new experiments to their parent task for traceability.

## Knowledge Node Files

- [[Phase Association]] — Assigning phase picks to common earthquake sources
- [[Earthquake Location]] — Hypocenter and origin time prediction from multi-station data
- [[Seismic Facies Segmentation]] — Pixel-wise lithological classification of seismic images
- [[Earthquake Sequence Analysis]] — Foreshock-mainshock-aftershock cascades and causal relationships
- [[Fault Segmentation]] — Thin-structure detection in seismic images
- [[Seismic Image Segmentation]] — General seismic image segmentation tasks
- [[Seismic Phase Picking]] — P/S wave arrival time detection from waveforms
