---
title: "PhaseNet: a deep-neural-network-based seismic arrival-time picking method"
authors: [Zhu, Beroza]
year: 2019
venue: "Geophysical Journal International"
task: [Seismic Phase Picking]
methods: [PhaseNet, U-Net, CNN]
datasets: [NCEDC]
metrics: [Precision, Recall, F1 Score, Residual Mean/Std]
code: "https://github.com/weiqiangzhu/PhaseNet"
importance: high
status: done
paper_type: research_article
tags: [phasenet, cnn, phase-picking, deep-learning, zhu-beroza]
created: 2026-07-09
---

# Paper Type / 论文类型

Type: research_article

# One Sentence Summary / 一句话总结

PhaseNet将U-Net改造为1D CNN，直接从未滤波三分量波形预测P/S/噪声概率分布，在779K条NCEDC数据上训练，F1分数远超传统AR拾波器。

# Research Background / 研究背景

地震监测依赖精确的震相拾波。人工拾波劳动密集且引入主观偏差；传统自动拾波器(STA/LTA, AR-AIC)依赖人工设计的特征和阈值，精度不及人类专家。深度学习在图像分割领域取得突破，但直接应用于1D地震时间序列需要架构调整。

# Problem Definition / 问题定义

- **Input / 输入**: 3-component seismograms, 30s long, 100Hz sampled (3×3001 data points)
- **Output / 输出**: P wave, S wave, and noise probability distributions (3×3001)

# Motivation / 研究动机

1. 传统方法依赖手工特征(方差、偏度、峰度)，需要精细的数据预处理(带通滤波、阈值设定)
2. 不同分析师对同一信号的拾波存在主观差异
3. S波拾波特别困难(被P尾波污染)
4. 深度学习在图像分割上成功，但需要适配1D时间序列

# Main Contributions / 主要贡献

1. **提出PhaseNet架构**: 将2D U-Net改为1D CNN，保留skip connection，适配地震波形时间序列
2. **软标签训练策略**: 用高斯分布掩码代替硬标注，减少人工拾波误差的影响(std=0.1s)
3. **无需预处理**: 直接使用未滤波原始波形，模型自动学习噪声特征
4. **大规模验证**: 在779K条波形上训练，覆盖多种仪器类型和SNR范围

# Method / 方法

## Overall Framework / 整体框架

PhaseNet = Modified U-Net for 1D Time Series

```
Input (3×3001) → Down-sampling (4 stages) → Bottleneck → Up-sampling (4 stages) → Output (3×3001)
                    ↓ conv, stride=4                    ↑ deconv, factor=4
                    ↓ skip connection                   ↑ skip connection
```

## Key Modules / 关键模块

### Module 1: 1D Convolutional Encoder/Decoder

- **Conv kernel size**: 7 data points
- **Down-sampling stride**: 4 (each stage reduces length to 1/4)
- **Up-sampling**: Deconvolution (Noh et al. 2015), expands by factor of 4
- **Padding**: Front and back padding to maintain sequence length
- **Activation**: ReLU

### Module 2: Skip Connections

- Concatenate encoder output directly to decoder input at each stage
- Improves convergence (Ronneberger et al. 2015; Li et al. 2017)
- Preserves fine-grained temporal information lost in down-sampling

### Module 3: Soft Label Masking

- Manual picks → Gaussian distribution (mean=arrival_time, std=0.1s)
- Prob(noise) = 1 - Prob(P) - Prob(S)
- Reduces influence of annotation uncertainty
- Accelerates convergence

### Module 4: Probability Output

- Softmax normalization over 3 classes (noise, P, S)
- $q_i(x) = e^{z_i(x)} / \sum_{k=1}^{3} e^{z_k(x)}$
- Loss: Cross-entropy $H(p,q) = -\sum_i \sum_x p_i(x) \log q_i(x)$
- Peak probability > 0.5 → positive pick
- Arrival time = peak location

## Mathematical Formulation / 数学表述

**Architecture**: Modified U-Net, 1D convolution instead of 2D

**Loss**: Cross-entropy between true probability distribution and predicted distribution

**Prediction**: $argmax_x q_i(x)$ for each class i ∈ {noise, P, S}

# Dataset / 数据集

| Dataset | Size | Modality | Description |
|---|---|---|---|
| NCEDC | 779,514 waveforms | 3-component seismograms (30s, 100Hz) | Northern California Earthquake Data Center, 30yr of data, 234K earthquakes, 889 stations |

**Split**: Train 623,054 / Val 77,866 / Test 78,592 (stratified by station)

**Instrument diversity**: Broadband, short-period, accelerometer, various orientations

**SNR range**: Wide distribution (Fig. 3 in paper)

# Experimental Setup / 实验设置

- **Baseline**: AR Picker (ObsPy) — bandpass filtered 0.1-40Hz
- **Threshold**: Peak probability > 0.5 → positive pick
- **True positive**: Residual Δt < 0.1s
- **Evaluation metrics**: Precision, Recall, F1, Mean residual, Std residual
- **No preprocessing**: Raw unfiltered waveforms (contrast with AR picker which requires bandpass)

# Results / 实验结果

| Metric | PhaseNet P | PhaseNet S | AR Picker P | AR Picker S |
|---|---|---|---|---|
| Precision | 0.939 | 0.853 | 0.558 | 0.195 |
| Recall | 0.857 | 0.755 | 0.558 | 0.144 |
| F1 Score | 0.896 | 0.801 | 0.558 | 0.165 |
| Mean Resid. (ms) | 2.068 | 3.311 | 11.647 | 27.496 |
| Std Resid. (ms) | 51.530 | 82.858 | 83.991 | 181.027 |

**Key findings:**
- PhaseNet S-wave F1 is **4.8×** higher than AR picker (0.801 vs 0.165)
- PhaseNet P-wave F1 is **1.6×** higher (0.896 vs 0.558)
- Robust across all instrument types without parameter tuning
- F1 > 0.9 (P) and > 0.8 (S) when log10(SNR) > 0.5
- PCA of deepest layer weights shows clear P/S/noise separation

# Ablation Study / 消融实验

- **Skip connection analysis**: Model trained without skip connection → PCA shows less separable features
- **Instrument robustness**: Same model works across all instrument types (Fig. 7)
- **SNR robustness**: Performance degrades gracefully with lower SNR (Fig. 8)
- **Probability threshold**: Setting threshold at 0.5 works well; tuning has minimal effect

# Limitation / 局限性

> 论文自己承认的局限 + 你看到的局限

**Author-admitted:**
- Model trained on detected earthquakes; continuous-data detection needs different training set
- PCA only on deepest layer (limited interpretability)
- No comparison with other DL methods (PhaseNet was the first of its kind)

**Agent-identified:**
- Only tested on Northern California data — domain generalizability unknown
- No hyperparameter sensitivity analysis (kernel size, stride, depth)
- No discussion of computational cost or inference speed
- Random seed not specified
- No requirements.txt or environment specification

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

1. **U-Net → 1D CNN transformation**: The architecture modification (2D conv → 1D conv) is directly applicable to seismic image segmentation. U-Net is already the standard for image segmentation; PhaseNet shows it works for 1D time series too.
2. **Soft labeling with Gaussian masks**: Instead of hard annotations, use probabilistic labels. This is valuable when ground truth has uncertainty (analyst picks are inherently imprecise).
3. **No preprocessing advantage**: Training on raw waveforms means the model learns noise robustness. For seismic images, this translates to not needing to pre-filter/seismic-data before feeding to CNN.
4. **Skip connections for temporal localization**: Essential for preserving fine-grained timing information in time series — equally important for pixel-level seismic image segmentation.

## Potential Improvements / 潜在改进方向

1. **Multi-region training**: Train on multiple seismic networks (not just NCEDC) to improve domain generalization
2. **Continuous data detection**: Extend PhaseNet to detect earthquakes on continuous streams (currently only tested on known events)
3. **Attention mechanisms**: Add attention to U-Net skip connections (similar to Attention U-Net in images)
4. **Lightweight variant**: Reduce channels/depth for RTX 4070 deployment
5. **Self-supervised pre-training**: Pre-train on unlabeled data (like BERT for NLP) before fine-tuning on labeled picks

# Reproducibility Analysis / 复现性分析

## Official Implementation Verification / 官方实现验证

> Paper Note inherits basic code status from Literature Card, then adds deep analysis.

- **Code Status**: [x] Available [ ] Not Found Yet [ ] Confirmed Missing [ ] Not Checked
- **Official URL**: https://github.com/weiqiangzhu/PhaseNet
- **Framework**: PyTorch
- **Checkpoint / Pre-trained Weights**: [ ] Available [ ] Not mentioned [ ] Not applicable
- **Last Repository Update**: <!-- unknown -->
- **Code Quality Indicators**: <!-- stars, forks, issues responsiveness, documentation quality -->

## Missing Reproduction Components / 缺失的复现组件

> 即使代码公开，也可能缺少某些关键组件导致无法复现。逐项评估。

| Component | Available? | Source Location | Notes |
|---|---|---|---|
| Source Code | [x] Yes [ ] No [ ] Partial | GitHub repo | PyTorch implementation |
| Dataset Access | [x] Public [ ] Restricted [ ] Private | NCEDC (ncedc.org) | Free download, registration may be needed |
| Pre-trained Checkpoint | [ ] Yes [ ] No [ ] N/A | Not mentioned in paper | |
| Preprocessing Scripts | [x] Fully Listed [ ] Partially [ ] Missing | Sec 2 Data section | Normalization (mean removal, std division) |
| Hyperparameters | [x] Fully Listed [ ] Partially [ ] Missing | Architecture, conv=7, stride=4, softmax | But: learning rate, batch size, optimizer NOT specified |
| Environment Specs | [ ] requirements.txt [ ] Docker [ ] Not specified | Not mentioned | CUDA/Python versions unknown |
| Random Seeds | [ ] Specified [ ] Not specified | Not mentioned | |
| Train/Val/Test Split | [x] Defined [ ] Undefined | 623K/78K/79K stratified by station | Ratio ≈ 80/10/10 |
| Data Augmentation | [ ] Described [ ] Vaguely [ ] Not described | Not mentioned | |

## Reproduction Difficulty Assessment / 复现难度评估

- **Overall Difficulty**: [x] Easy [ ] Moderate [ ] Hard [ ] Impossible
- **Estimated Effort**: <!-- 1-2 weeks for a skilled researcher -->
- **Hardware Requirements**: <!-- CNN on 1D data, minimal VRAM -->
- **Key Barriers**: Learning rate and batch size not specified; no random seed; no environment file
- **Workaround Options**: Use standard DL hyperparameters (lr=0.001, Adam); set seed manually
- **RTX 4070 Compatibility**: [x] Runs fine [ ] May struggle [ ] Won't fit in VRAM
- **Gap Between Code Existence and Reproducibility**: Code is available and architecture is clear, but training hyperparameters (lr, batch size, optimizer settings) are NOT specified. This means exact reproduction of results is difficult, though architectural reproduction is straightforward.

# Related Notes / 相关笔记

- Method: [[PhaseNet]], [[U-Net]], [[CNN]]
- Task: [[Seismic Phase Picking]]
- Dataset: [[EGS Collab SURF]]
