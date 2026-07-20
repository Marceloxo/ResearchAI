---
dataset_name: "Penobscot 3D Dataset"
domain: "Seismic"
size: "3D volume"
modality: "Seismic reflection data"
task: ["Facies Segmentation"]
official_link: "https://wiki.seg.org/wiki/Dictionary:Penobscot_3D_dataset"
related_papers: ["Baroni et al. (2018)", "Baroni et al. (2019)"]
tags: [seismic, facies-segmentation, benchmark]
source_type: public_dataset
created: 2026-07-08
---

# Dataset Overview / 数据集概述

The Penobscot 3D dataset is a Canadian offshore seismic survey with a detailed facies interpretation released by Baroni et al. It is one of the publicly available datasets with ground-truth annotations for seismic facies classification.

- **Source / 来源**: SEG Wiki Open Data + Baroni et al. interpretation
- **Purpose / 目的**: Seismic facies segmentation benchmark
- **License / 许可**: Creative Commons Attribution

# Data Format / 数据格式

- **File Format / 文件格式**: SEGY
- **Annotation / 标注**: Provided by Baroni et al. (2018, 2019)

# Dataset Scale / 数据规模

| Split | Count | Description |
|---|---|---|
| Classes / 类别 | Multiple | Facies classes as interpreted by Baroni et al. |

# Usage / 使用方式

- **Loading / 加载**: Standard SEGY reader
- **Preprocessing / 预处理**: Normalization, patch extraction
- **Data Location / 数据位置**: `D:\ResearchAI_Data\datasets\Penobscot`

# Related Papers / 相关论文

- [[Paper - ]] — Baroni et al. (2018, 2019): Released interpretation and analysis

# Limitations / 局限性

- Less widely used than F3 Netherlands or Parihaka
- Limited number of published comparative studies

## Tasks Using This Dataset / 使用该数据集的任务
- [[Seismic Facies Segmentation]] — Canadian offshore; CC-BY interpretation by Baroni et al.
