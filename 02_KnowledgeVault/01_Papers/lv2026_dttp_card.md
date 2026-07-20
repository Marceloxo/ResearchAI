---
title: "DTPP: An efficient depthwise separable TCN for seismic phase picking"
authors: [Shuai Lv, Yuxiang Peng]
year: 2026
venue: ""
task: [Seismic Phase Picking]
method: [Depthwise Separable TCN, Dilated Convolution, DeepLabV3+ inspired encoder-decoder]
dataset: [STEAD, GEEDataset V1.0]
code_available: Not Checked
importance: medium
reading_status: deep-read
tags: [seismic-phase-picking, depthwise-separable, tcn, dilated-convolution, steadi-geedataset]
created: 2026-07-10
---

# Basic Information / 基本信息

- **Title**: DTPP: An efficient depthwise separable TCN for seismic phase picking
- **Authors**: Shuai Lv, Yuxiang Peng
- **Year**: 2026
- **Venue**: ""
- **Task**: Seismic Phase Picking (P and S wave arrival time detection)
- **Method**: Depthwise Separable Temporal Convolutional Network (TCN) with dilated convolution and ASPP module, inspired by DeepLabV3+ architecture
- **Dataset**: STEAD (training), GEEDataset V1.0 (evaluation, 84,782 samples after excluding STEAD overlap)
- **Code**: Not Checked — paper states "will be made available upon publication"

# Research Problem / 研究问题

Balancing picking accuracy with computational efficiency for real-time seismic monitoring. Existing models face a trade-off: Transformer-based models (e.g., SeisLM at 87M params) have high accuracy but slow inference; classical CNNs (e.g., PhaseNet) have limited receptive fields that struggle with long-range P-S wave dependencies.

# Main Contribution / 主要贡献

Proposes DTPP, a lightweight seismic phase picking network (0.25M params, 0.98 MB) that achieves state-of-the-art P-wave F1 (0.878) and highest average P/S F1 (0.714) on GEEDataset V1.0, while maintaining ~3ms single-sample inference time suitable for real-time deployment.

# Method Overview / 方法概述

1. **Encoder-Decoder architecture** with Stem Block, SeismicBackbone (6 ETB modules), SeismicASPP, and Decoder.
2. **ETB (Efficient TCN Block)** combines depthwise separable convolution and dilated convolution with residual connections for exponential receptive field growth.
3. **SeismicASPP** adapts Atrous Spatial Pyramid Pooling for 1-D seismic waveforms with dilation rates [6, 12, 18] tuned to typical P-S wave intervals.
4. **Skip connections** from Encoder3 preserve phase boundary detail in the decoder.

# Dataset and Evaluation / 数据集与评估

- **Training**: STEAD dataset (~1.05M waveforms, 2613 stations, 8:1:1 split)
- **Evaluation**: GEEDataset V1.0 (92,219 samples, 84,782 after removing STEAD overlap)
- **Baselines**: PhaseNet, EQTransformer, LPPN, SeisT, PickerXL, SeisLM
- **Metrics**: Precision/Recall/F1 at 0.1s tolerance, error statistics (μ, σ, MAE) at 0.5s range, inference speed, parameter count
- **Ablation**: Replaced ETB→CNN, ASPP→CNN, removed skip connections — all caused performance drops

# Why This Paper Matters / 为什么关注这篇论文

Directly relevant to seismic phase picking research. DTPP demonstrates that a well-designed lightweight CNN architecture can outperform larger Transformer models on the accuracy-efficiency frontier. The depthwise separable + dilated convolution combination with ASPP adapted for 1-D seismic signals offers transferable design patterns. The comprehensive evaluation on a global cross-dataset benchmark (GEEDataset V1.0) strengthens the validity of claims.

# Limitations / 局限性

- S-wave F1 (0.551) lags behind LPPN (0.582) and PickerXL (0.563)
- Tested only on epicentral distances ≤ 100 km; performance at greater distances unverified
- No validation on continuous seismic waveform data (only pre-segmented events)
- Code not yet available; reproducibility cannot be fully assessed
- Model may not generalize well to atypical seismic signals or extreme noise environments

# Reproducibility Status / 可复现性状态

## Code Availability

**Status**: [ ] Available [ ] Not Found Yet [x] Confirmed Missing [ ] Not Checked

**URL**: N/A — paper states code will be available upon publication

## Data Status / 数据可用性

- [x] **Public dataset available** — freely downloadable
- [ ] **Restricted dataset** — requires application or license
- [ ] **Private dataset** — not publicly accessible
- [ ] **Unknown** — paper does not specify

**Dataset Link**: 
- STEAD: https://github.com/smousavi05/STEAD
- GEEDataset V1.0 results: https://prismax.opencompass.org.cn/domainlb

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [x] High [ ] Medium [ ] Low

**Reason**: Both training (STEAD) and evaluation (GEEDataset V1.0) datasets are publicly available. Architecture is well-described with detailed hyperparameters, dilation rates, and training settings (AdamW, LR=1e-3, batch=1024, 200 epochs, V100 GPUs). Model size (0.25M) is small, making reproduction computationally inexpensive.

**Notes / 备注**: Code pending publication may delay immediate reproduction. Architecture details are sufficiently complete to implement from scratch.

# My Decision / 我的决定

- [x] Read deeply / 精读
- [ ] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason / 理由**: Decision Framework score 11/15 — Direct relevance (3), High novelty (3), Comprehensive experiments (3), Public datasets (2). This paper introduces a novel lightweight architecture that directly competes with existing phase picking methods on both accuracy and efficiency metrics. Recommended for Level 2 Deep Read.

# Related Knowledge / 相关知识链接

- Task: [[Seismic Phase Picking]]
- Method: [[Depthwise Separable Convolution]], [[Temporal Convolutional Network]], [[Dilated Convolution]], [[ASPP]]
- Dataset: [[STEAD]], [[GEEDataset V1.0]]
