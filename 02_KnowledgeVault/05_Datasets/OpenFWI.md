---
dataset_name: "OpenFWI"
domain: "Seismic"
size: "Multiple models"
modality: "Seismic reflection data"
task: ["Full Waveform Inversion"]
official_link: "https://openfwi.github.io/OpenFWI/"
related_papers: ["Abraham et al. (2020)"]
tags: [seismic, fwI, inversion]
source_type: public_dataset
created: 2026-07-08
---

# Dataset Overview / 数据集概述

OpenFWI is an open benchmark dataset for Full Waveform Inversion (FWI) in seismic exploration. It provides multiple synthetic models with varying complexity for training and evaluating FWI algorithms.

- **Source / 来源**: OpenFWI Consortium
- **Purpose / 目的**: Benchmark for FWI algorithm development and comparison
- **License / 许可**: Open benchmark

# Data Format / 数据格式

- **File Format / 文件格式**: Synthetic seismic data with velocity models
- **Task / 任务**: Velocity model estimation from seismic recordings

# Dataset Scale / 数据规模

| Split | Count | Description |
|---|---|---|
| Models / 模型 | Multiple | Varying geological complexity |

# Usage / 使用方式

- **Data Location / 数据位置**: `/home/lco/ResearchAI_Data/datasets\OpenFWI`

# Related Papers / 相关论文

- [[Paper - ]] — Abraham et al. (2020): OpenFWI benchmark description

# Limitations / 局限性

- Synthetic data only — does not capture real acquisition effects
- Focuses on inversion, not segmentation

## Tasks Using This Dataset / 使用该数据集的任务

- Full Waveform Inversion — OpenFWI benchmark (no dedicated task node yet)
