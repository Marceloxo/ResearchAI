---
title: "TopSUMseg: A Topology-Aware Swin Transformer-Mamba Framework for 3D Seismic Fault Image Segmentation"
authors: [Ran Chen, Jingyang Deng, Zeren Zhang, Ruohua Shi, Jinwen Ma]
year: 2025
venue: "arXiv preprint"
task: [Seismic Fault Segmentation]
methods: [Swin Transformer, Mamba, Global-Local Attention, Topology-Aware Structural Constraint]
datasets: [Thebe Dataset]
metrics: [OIS, ODS]
code: "Not Found Yet"
importance: High
status: to_read
paper_type: research_article
tags: [seismic, fault-segmentation, swin-transformer, mamba, hybrid-architecture, 3d-segmentation, topology]
created: 2026-07-20
---

# Paper Type / 论文类型

Type: research_article — 提出Swin Transformer + Mamba混合架构用于3D地震断层分割

# One Sentence Summary / 一句话总结

提出TopSUMseg，首个将Mamba架构引入地震分割的Swin Transformer-Mamba混合框架，通过Global-Local Attention和Topology-Aware Structural Constraint在Thebe数据集上达到SOTA（OIS=0.879, ODS=0.875），且参数量更少。

# Research Background / 研究问题

3D地震断层分割面临两个核心挑战：(1) 单一架构局限 — CNN局部感受野小，Transformer计算复杂度高且依赖预训练，Mamba序列化处理破坏空间结构；(2) 断层目标特殊性 — 细长连续结构、空间分布不均匀、信号弱且边界模糊。现有方法难以同时高效建模局部细节和长程依赖。

# Problem Definition / 问题定义

- **Input / 输入**: 3D地震体数据 X ∈ R^(C×D×H×W)
- **Output / 输出**: 3D分割掩码，标记断层位置

# Motivation / 研究动机

现有单架构模型无法同时兼顾局部特征提取和长程依赖建模。Swin Transformer擅长局部特征但全局建模受限，Mamba线性复杂度适合长序列但破坏空间结构。将两者互补整合，加上拓扑感知约束，有望突破现有性能瓶颈。

# Main Contributions / 主要贡献

1. 首个将Mamba架构应用于地震图像分割，提出Swin Transformer-Mamba混合编码器
2. 提出Global-Local Attention (GLA)模块增强Mamba在3D空间中的关系建模能力
3. 提出Topology-Aware Structural Constraint (TASC)在感知特征空间提供拓扑结构级监督
4. 在Thebe数据集上达到SOTA，参数量更少，无需大规模预训练

# Method / 方法

## Overall Framework / 整体框架

U型编码器-解码器架构。编码器4阶段：Stage 1（Swin Transformer）→ Stage 2-3（G-Mamba = Mamba + GLA）→ Stage 4（Swin Transformer）。解码器通过上采样逐步恢复分辨率。

## Key Modules / 关键模块

### Module 1: 混合编码器
- Stage 1: Swin Transformer块（W-MSA + SW-MSA），提取局部特征并编码相对位置
- Stage 2-3: G-Mamba模块（Mamba + GLA），线性复杂度长程建模
- Stage 4: Swin Transformer块，整合多尺度特征

### Module 2: Global-Local Attention (GLA)
并行提取局部空间特征和全局通道注意力，增强Mamba在3D空间中的特征表示能力。

### Module 3: Topology-Aware Structural Constraint (TASC)
在感知特征空间中约束预测与真实结构的拓扑一致性，促进断层连续性，抑制噪声敏感性。

## Mathematical Formulation / 数学表述

Swin Transformer注意力：
$$\text{Attention}(Q,K,V) = \text{SoftMax}\left(\frac{QK^T}{\sqrt{d_k}} + B\right)V$$

B为相对位置编码矩阵。Mamba使用选择性扫描机制（S6），计算复杂度O(n)。

# Dataset / 数据集

| Dataset | Size | Modality | Description |
|---------|------|----------|-------------|
| Thebe | 公开 | 3D地震体数据 | 最大公开3D地震断层分割数据集（An et al., 2023） |

# Experimental Setup / 实验设置

从头训练（scratch），无需大规模预训练。评估指标：OIS (Optimal Image Scale), ODS (Optimal Dataset Scale)。对比方法包括基于预训练的SOTA模型。

# Results / 实验结果

| Method | OIS | ODS |
|--------|:---:|:---:|
| TopSUMseg (Ours) | 0.879 | 0.875 |
| SOTA pre-trained models | 低于TopSUMseg | 低于TopSUMseg |

TopSUMseg在参数量更少的情况下，超越所有基于预训练的SOTA模型。

# Ablation Study / 消融实验

1. GLA模块有效性：移除GLA后人脸下降
2. TASC约束有效性：加入TASC后ODS和OIS提升
3. 混合编码器设计：验证各阶段组件选择合理

# Limitation / 局限性

1. 代码和预训练模型未公开，复现困难
2. 仅在Thebe单一数据集上验证
3. Mamba+Swin混合架构的推理效率分析不够详细
4. 与预训练方法的计算量对比缺乏量化分析

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

1. **Mamba + Transformer混合架构**：对RTX 4070友好，线性复杂度适合大尺寸3D数据
2. **拓扑感知约束（TASC）**：可迁移到其他地震图像分割任务（如相分割、盐体分割）
3. **GLA模块**：增强Mamba空间建模能力的通用设计

## Potential Improvements / 潜在改进方向

1. 在RTX 4070上测试推理速度和显存占用
2. 探索更轻量级的Mamba变体
3. 将TASC扩展到其他地震分割任务

# Reproducibility Analysis / 复现性分析

**Code Status**: [ ] Confirmed Available [ ] Confirmed Missing [x] Not Found Yet [ ] Not Checked

**Overall Difficulty**: [ ] Easy [ ] Moderate [x] Hard [ ] Impossible

**RTX 4070 Compatibility**: [x] May struggle — 3D Swin Transformer + Mamba，需测试

# Related Notes / 相关笔记

- Task: [[Seismic Fault Segmentation]]
- Method: [[Swin Transformer]]
- Method: [[Mamba]]
- Dataset: [[Thebe Dataset]]

## Zotero
- **Zotero Item Key (Attachment)**: M29ILMXG
- **Zotero Item Key (Parent)**: 4NEI9ULI
- **Status**: Level 2 Note Created
