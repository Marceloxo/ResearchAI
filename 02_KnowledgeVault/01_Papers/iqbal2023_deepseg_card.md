---
title: "DeepSeg: Deep Segmental Denoising Neural Network for Seismic Data"
authors: [Naveed Iqbal]
year: 2023
venue: "IEEE Transactions on Geoscience and Remote Sensing"
task: [Seismic Denoising]
method: [Deep Convolutional Neural Network, STDCT, U-Net-like Architecture]
dataset: [Synthetic Seismic Data, Real Passive Seismic Data]
code_available: Not Found Yet
importance: High
reading_status: to_read
tags: [seismic, denoising, deep-learning, cnn, passive-seismic]
created: 2026-07-20
---

# Basic Information / 基本信息

- **Title**: DeepSeg: Deep Segmental Denoising Neural Network for Seismic Data
- **Authors**: Naveed Iqbal
- **Year**: 2023
- **Venue**: IEEE Transactions on Geoscience and Remote Sensing
- **Task**: 地震数据去噪 (Seismic Denoising)
- **Method**: 深度卷积神经网络 + 短时DCT变换 + 编码器-解码器架构
- **Dataset**: 合成地震数据 + 真实被动地震数据
- **Code**: Not Found Yet

# Research Problem / 研究问题

地震信号在采集过程中受到各种噪声污染（环境噪声、仪器噪声、人为噪声等），传统滤波方法在噪声与信号频带重叠时性能急剧下降。现有深度学习方法需要大量训练数据且依赖掩码函数，性能受限。如何设计一种高效的去噪方法，能够在极低信噪比环境下有效去噪，同时仅使用合成数据训练即可泛化到真实数据？

# Main Contribution / 主要贡献

提出DeepSeg — 一种基于时频域分段的深度卷积神经网络去噪框架。核心创新：(1) 使用短时离散余弦变换(STDCT)将一维地震信号转换为二维时频表示，然后在时频域进行分段处理；(2) 利用过去、当前、未来共15个连续STDCT片段预测当前干净片段，类似于数字信号处理中的滤波器设计；(3) 网络仅使用合成数据训练，无需真实数据，即可泛化到真实地震数据。

# Method Overview / 方法概述

DeepSeg采用类似U-Net的编码器-解码器架构：12个卷积层 + 转置卷积层 + 最后的全连接层。输入15个含噪STDCT片段（128样本窗口，90%重叠），输出一个干净的中间片段。使用L2损失函数优化。卷积核3×3，滤波器数量从8到512递增再递减。使用LeakyReLU激活和批归一化。

# Dataset and Evaluation / 数据集与评估

**训练数据**: 合成波形 + 合成地震图，添加各种类型噪声（相关噪声、不相关噪声）。**测试数据**: 未见过的新合成数据 + 真实被动地震数据。**评估指标**: SNR改善。与现有深度去噪方法对比，DeepSeg在训练数据量更少的情况下取得更好的SNR提升。

# Why This Paper Matters / 为什么关注这篇论文

地震去噪是地震数据预处理的关键步骤。DeepSeg的分段式时频域去噪策略对RTX 4070友好（网络结构简洁），其仅用合成数据训练即可泛化的特性对标注数据稀缺的地震领域非常有价值。思路可迁移到地震相分割、断层检测等任务的预处理环节。

# Limitations / 局限性

(1) 仅在被动地震数据上验证，主动地震数据效果未知；(2) 使用矩形窗（90%重叠）可能引入边界伪影；(3) 未与传统方法（如小波变换、曲波变换）进行全面对比；(4) 网络深度和滤波器数量的选择依据经验确定，缺乏理论解释。

# Reproducibility Status / 可复现性状态

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: <!-- Only fill when Status = Available -->

## Data Status / 数据可用性

- [ ] **Public dataset available** — freely downloadable
- [ ] **Restricted dataset** — requires application or license
- [ ] **Private dataset** — not publicly accessible
- [x] **Unknown** — paper does not specify

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [ ] High [x] Medium [ ] Low

**Reason**: 网络结构描述清晰（层数、滤波器数量、核大小等），但训练超参数、数据生成细节不够完整，需要自行实现。

# My Decision / 我的决定

- [x] Read deeply / 精读
- [ ] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason**: 地震去噪是基础预处理任务，其分段式策略和合成数据训练方法对资源受限的RTX 4070场景具有实际参考价值。

# Related Knowledge / 相关知识链接

- Task: [[Seismic Denoising]]
- Method: [[Deep Convolutional Neural Network]]
- Method: [[U-Net]]

## Zotero

- **Zotero Item Key (Attachment)**: SMX9BMYC
- **Zotero Item Key (Parent)**: 6REQ57LL
- **Status**: Level 1 Card Created
