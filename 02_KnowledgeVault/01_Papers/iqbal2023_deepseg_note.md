---
title: "DeepSeg: Deep Segmental Denoising Neural Network for Seismic Data"
authors: [Naveed Iqbal]
year: 2023
venue: "IEEE Transactions on Geoscience and Remote Sensing"
task: [Seismic Denoising]
methods: [Deep Convolutional Neural Network, STDCT, U-Net-like Architecture]
datasets: [Synthetic Seismic Data, Real Passive Seismic Data]
metrics: [SNR Improvement]
code: "Not Found Yet"
importance: High
status: to_read
paper_type: research_article
tags: [seismic, denoising, deep-learning, cnn, passive-seismic, time-frequency]
created: 2026-07-20
---

# Paper Type / 论文类型

Type: research_article — 提出新的地震去噪方法DeepSeg

# One Sentence Summary / 一句话总结

提出基于STDCT时频域分段和深度卷积神经网络的去噪框架DeepSeg，仅用合成数据训练即可在真实数据上有效去噪，在极低信噪比环境下仍能显著提升SNR。

# Research Background / 研究背景

地震信号在采集过程中受到各种噪声污染（环境噪声、仪器噪声、人为活动噪声等）。传统带通滤波和谱滤波方法在噪声与信号频带重叠时性能急剧下降。时频域阈值方法（小波变换、曲波变换等）依赖于最优阈值函数的选择，难以同时实现有效去噪和信号保持。现有深度学习方法需要大量训练数据，且通常依赖掩码函数，性能受限。

# Problem Definition / 问题定义

- **Input / 输入**: 含噪地震信号的一维波形（经STDCT变换后的15个连续时频域片段，每个片段128个样本，90%重叠）
- **Output / 输出**: 干净的中间时频域片段，经逆变换恢复为时域去噪信号

# Motivation / 研究动机

现有去噪方法在噪声与信号频带重叠时效果差；深度学习方法虽然表现好但需要大量标注训练数据。本文希望：(1) 仅在合成数据上训练即可泛化到真实数据；(2) 在极低SNR环境下仍能有效去噪；(3) 片段式策略减少训练数据需求。

# Main Contributions / 主要贡献

1. 提出DeepSeg — 基于STDCT时频域分段和深度CNN的去噪框架，将一维去噪问题转化为二维时频域学习问题
2. 创新性地使用过去-当前-未来多个连续STDCT片段（15个）预测当前干净片段，类似数字滤波器设计思路
3. 仅使用合成数据训练，无需真实数据，即可有效泛化到真实地震数据

# Method / 方法

## Overall Framework / 整体框架

输入一维含噪地震信号 → STDCT变换（128样本窗口，90%重叠）→ 取15个连续STDCT片段 → 深度CNN → 输出干净中间片段 → 逆STDCT → 时域去噪信号

## Key Modules / 关键模块

### Module 1: STDCT变换
使用离散余弦变换（DCT-IV）替代STFT，避免复数运算，使网络仅处理实数。窗口大小N=128，重叠率90%。

### Module 2: 深度卷积神经网络
编码器-解码器架构（类U-Net）：12个卷积层 + 转置卷积层 + 最后的全连接层（128神经元）。卷积核3×3，滤波器数从8到512。使用LeakyReLU激活函数和批归一化（BN）。跳跃连接用于连接编码器和解码器对应层。

## Mathematical Formulation / 数学表述

噪声模型：Y = X + N，其中Y是含噪时频表示，X是干净信号，N是噪声。

优化目标：使用L2损失，利用过去⌊Δ/2⌋、当前、未来⌊Δ/2⌋共Δ=15个连续片段预测当前干净片段：

$$\min \sum_{n=1}^{T} \left\| \mathbf{X}_n - f(\mathbf{Y}_{n-\lfloor\Delta/2\rfloor}, \dots, \mathbf{Y}_{n+\lfloor\Delta/2\rfloor}) \right\|_2^2$$

# Dataset / 数据集

| Dataset | Size | Modality | Description |
|---------|------|----------|-------------|
| Synthetic Waveforms | 合成生成 | 一维波形 | 使用合成波形+各种噪声类型（相关噪声、不相关噪声） |
| Synthetic Earthquake Seismograms | 合成生成 | 一维波形 | 合成地震图，用于训练和测试 |
| Real Passive Seismic Data | 未公开 | 一维波形 | 真实被动地震数据，仅用于测试泛化性 |

# Experimental Setup / 实验设置

训练数据全部为合成数据。网络使用15个输入片段预测1个输出片段。对比方法：基于深度学习的掩码式去噪方法。评估指标：SNR改善。

# Results / 实验结果

DeepSeg在训练数据量更少的情况下，在合成和真实数据上均取得比现有深度去噪方法更好的SNR提升。在极低SNR环境下仍能有效去噪，对信号形态改变最小。可处理多种噪声类型（相关色噪声、不相关噪声等）。

# Ablation Study / 消融实验

论文通过敏感性分析确定Δ=15为最优值，但未提供详细的消融实验验证各组件贡献。

# Limitation / 局限性

1. 仅在被动地震数据上验证，主动地震数据效果未知
2. 使用矩形窗（90%重叠）可能引入边界伪影
3. 网络深度和滤波器数量选择依据经验确定
4. 未与传统方法（小波、曲波变换）进行全面对比
5. 合成数据与真实数据之间的域差异未定量分析

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

1. **片段式处理策略**：将一维信号分段转换为二维时频表示，可迁移到地震相分割、断层检测等任务的预处理
2. **仅用合成数据训练**：对标注数据稀缺的地震领域极具价值，可减少对真实标注数据的依赖
3. **滤波器设计思想**：利用过去-当前-未来片段预测当前值的思路类似于数字信号处理，可应用于其他时序任务

## Potential Improvements / 潜在改进方向

1. 使用更先进的时频变换（如Synchrosqueezing Transform）替代STDCT
2. 引入注意力机制增强对关键时频区域的关注
3. 在合成数据生成中引入更真实的噪声模型（如实际仪器噪声特征）
4. 在RTX 4070上验证推理速度和显存占用

# Reproducibility Analysis / 复现性分析

## Official Implementation Verification / 官方实现验证

**Code Status**: [ ] Confirmed Available [ ] Confirmed Missing [x] Not Found Yet [ ] Not Checked

**Repository URL**: 未找到

## Missing Reproduction Components / 缺失的复现组件

| Component | Available? | Notes |
|-----------|-----------|-------|
| Source Code | [ ] No | 未公开 |
| Dataset Access | [ ] Restricted | 合成数据生成方式描述但不完整 |
| Hyperparameters | [ ] Partially | 网络结构参数给出，但训练超参数不完整 |
| Random Seeds | [ ] Not specified | 未指定 |

## Reproduction Difficulty Assessment / 复现难度评估

- **Overall Difficulty**: [ ] Easy [x] Moderate [ ] Hard [ ] Impossible
- **RTX 4070 Compatibility**: [x] Runs fine — 网络结构简洁，参数量适中

# Related Notes / 相关笔记

- Task: [[Seismic Denoising]]
- Method: [[Deep Convolutional Neural Network]]
- Method: [[U-Net]]

## Zotero
- **Zotero Item Key (Attachment)**: SMX9BMYC
- **Zotero Item Key (Parent)**: 6REQ57LL
- **Status**: Level 2 Note Created
