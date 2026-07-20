---
title: "Earthquake transformer: an attentive deep-learning model for simultaneous earthquake detection and phase picking"
authors: [Mousavi, Ellsworth, Zhu, Chuang, Beroza]
year: 2020
venue: "Nature Communications"
task: [Earthquake Detection, Seismic Phase Picking]
method: [EQTransformer, Attention, LSTM, CNN]
dataset: [STEAD]
code_available: https://github.com/smousavi05/EQTransformer
importance: high
reading_status: done
tags: [eqtransformer, attention, cnn, lstm, earthquake-detection, phase-picking, mousavi]
created: 2026-07-09
---

# Basic Information / 基本信息

- **Title**: Earthquake transformer: an attentive deep-learning model for simultaneous earthquake detection and phase picking
- **Authors**: S. Mostafa Mousavi, William L. Ellsworth, Weiqiang Zhu, Lindsay Y. Chuang, Gregory C. Beroza
- **Year**: 2020
- **Venue**: Nature Communications, Vol. 11, Article 3546
- **Task**: Simultaneous earthquake detection + P/S phase picking
- **Method**: EQTransformer (hierarchical attention + very deep encoder + multi-task decoders)
- **Dataset**: STEAD (STanford EArthquake Dataset) — 1M earthquake + 300K noise waveforms
- **Code**: https://github.com/smousavi05/EQTransformer

# Research Problem / 研究问题

> 地震检测与震相拾波是两个紧密相关的任务，但以往方法分别处理。EQTransformer用层次注意力机制同时完成检测和拾波，利用全局上下文信息和局部震相特征提升性能。

# Main Contribution / 主要贡献

> 提出EQTransformer — 一个56层的非常深编码器+三个解码器（检测/P拾波/S拾波）的多任务网络。引入层次注意力机制（全局检测注意力 + 局部震相注意力），在STEAD测试集上超越所有对比方法，并在日本鸟取连续数据上检测到2倍于人工的事件。

# Method Overview / 方法概述

> 非常深编码器（残差CNN + BiLSTM + NiN + 全局注意力）→ 三个独立解码器（检测/P拾波/S拾波）。局部注意力在拾波解码器开头进一步聚焦震相特征。Dropout用于不确定性估计。

# Dataset and Evaluation / 数据集与评估

- **STEAD**: 1M地震+300K噪声波形，~450K地震，地理分布多样，最大震级M2.5
- **测试**: 日本鸟取5周连续数据（2000事件）
- **评估**: F1 score, Precision, Recall, 残差统计
- **基线**: PhaseNet, GPD, PpkNet, Yews, DetNet, CRED, STA/LTA, Kurtosis, Filter-Picker, AIC

# Why This Paper Matters / 为什么关注这篇论文

> EQTransformer是继PhaseNet之后的又一里程碑。它首次将注意力机制引入地震检测/拾波，提出了多任务同时学习的范式。其层次注意力设计启发了后续Transformer在地震学中的应用。代码和数据完全开源，促进了领域发展。Mousavi团队后续又发表了Annual Review综述，形成了从方法→综述的完整影响力链。

# Limitations / 局限性

> 训练数据主要来自北美地区，域外泛化性需验证。模型需要1分钟窗口（6000样本），计算复杂度较高。未测试多事件在同一窗口内的性能（尽管增强数据有所帮助）。不确定性估计基于MC Dropout，可能不够精确。

# Reproducibility Status / 可复现性状态

> Literature Card: lightweight screening. Paper Note / Paper Logic: deep analysis.

## Code Availability

**Status**: [x] Available [ ] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: https://github.com/smousavi05/EQTransformer

## Data Status / 数据状态

- [x] **Public dataset available** — freely downloadable
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

**Dataset Link**: https://github.com/smousavi05/STEAD (STEAD), http://www.hinet.bosai.go.jp (HiNet)

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [x] High [ ] Medium [ ] Low

**Reason**: 代码开源，数据集公开，架构描述详细，训练超参数完整（Adam, lr变化, dropout=0.1）。

**Notes / 备注**:
- 训练耗时约89小时（4×Tesla-V100 GPU）
- 代码+数据+模型均可获取
- 不确定性估计使用MC Dropout

## Zotero

**Status**: Imported
**Item Key**: QKMKLG2N

# My Decision / 我的决定

- [x] Read deeply / 精读
- [ ] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason / 理由**: EQTransformer是地震AI领域的经典方法论文，引入了层次注意力机制和多任务学习范式。其架构设计（非常深编码器+多解码器+层次注意力）对地震图像分割有直接启发。代码和数据完全开源，复现性强。

# Related Knowledge / 相关知识链接

- Task: [[Seismic Phase Picking]]
- Method: [[PhaseNet]], [[Transformer]], [[Attention Mechanism]], [[CNN]], [[U-Net]]
- Dataset: [[EGS Collab SURF]]
