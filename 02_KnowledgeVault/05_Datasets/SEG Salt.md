---
dataset_name: "SEG Salt Body Benchmark"
domain: "Seismic"
size: "3D volume"
modality: "Seismic reflection data"
task: ["Salt Body Segmentation"]
official_link: "https://wiki.seg.org/wiki/Phantom_model_for_salt_structures"
related_papers: ["Shi et al. (2019)", "Kaggle TGS Salt Challenge"]
tags: [seismic, salt-segmentation, benchmark]
source_type: public_dataset
created: 2026-07-08
---

# Dataset Overview / 数据集概述

The SEG Salt Body Benchmark is a classic dataset for salt dome and salt body identification in seismic data. Salt structures are critical for hydrocarbon exploration as they trap petroleum reservoirs.

- **Source / 来源**: SEG Open Data
- **Purpose / 目的**: Salt body identification and delineation
- **License / 许可**: Open data (SEG Wiki)

# Data Format / 数据格式

- **File Format / 文件格式**: SEGY
- **Task / 任务**: Binary segmentation (salt vs. non-salt)

# Dataset Scale / 数据规模

| Split | Count | Description |
|---|---|---|
| Classes / 类别 | 2 | Salt / Non-salt |

# Usage / 使用方式

- **Loading / 加载**: Standard SEGY reader
- **Data Location / 数据位置**: `/home/lco/ResearchAI_Data/datasets\SEG Salt`

# Benchmark Results / 基准结果

| Method | Metric | Year |
|---|---|---|
| SaltSeg (CNN) | — | 2019 |

# Related Papers / 相关论文

- [[Paper - ]] — Shi et al. (2019): SaltSeg using deep CNN
- [[Paper - ]] — Kaggle TGS Salt Identification Challenge

# Limitations / 局限性

- Binary task only (salt vs. non-salt), less complex than facies segmentation
- Limited published comparisons on this dataset

## Tasks Using This Dataset / 使用该数据集的任务
- [[Seismic Facies Segmentation]] — Salt body segmentation benchmark
- [[Seismic Image Segmentation]] — Kaggle competition dataset
