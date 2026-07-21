---
title: "TopSUMseg: A Topology-Aware Swin Transformer-Mamba Framework for 3D Seismic Fault Image Segmentation"
authors: [Ran Chen, Jingyang Deng, Zeren Zhang, Ruohua Shi, Jinwen Ma]
year: 2025
venue: "arXiv preprint"
task: [Seismic Fault Segmentation]
method: [Swin Transformer, Mamba, Global-Local Attention, Topology-Aware Structural Constraint]
dataset: [Thebe Dataset]
code_available: Not Found Yet
importance: High
reading_status: to_read
tags: [seismic, fault-segmentation, swin-transformer, mamba, hybrid-architecture, 3d-segmentation, topology]
created: 2026-07-20
---

# Basic Information / 基本信息

- **Title**: TopSUMseg: A Topology-Aware Swin Transformer-Mamba Framework for 3D Seismic Fault Image Segmentation
- **Authors**: Ran Chen, Jingyang Deng, Zeren Zhang, Ruohua Shi, Jinwen Ma
- **Year**: 2025
- **Venue**: arXiv (Peking University)
- **Task**: 3D地震断层图像分割
- **Method**: Swin Transformer + Mamba + Global-Local Attention + Topology-Aware Structural Constraint
- **Dataset**: Thebe（最大公开3D地震数据集）
- **Code**: Not Found Yet

# Research Problem / 研究问题

现有3D地震断层分割方法面临两个挑战：(1) 单一架构的局限：CNN局部感受野有限，Transformer计算量太大且依赖大规模预训练，Mamba序列化处理破坏空间结构；(2) 断层目标的特殊性：断层呈细长连续结构、空间分布不均匀、信号弱且边界模糊。如何设计一个混合架构，既能高效建模局部细节和长程依赖，又能保持断层结构的拓扑连续性？

# Main Contribution / 主要贡献

提出TopSUMseg — 首个将Mamba架构应用于地震图像分割的混合框架。核心创新：(1) 混合编码器：早期用Swin Transformer提取局部特征，中间用改进的Mamba模块（含GLA）建模长程依赖，后期再用Swin Transformer整合全局语义；(2) Global-Local Attention (GLA)模块：增强Mamba在3D空间中的空间关系建模能力；(3) Topology-Aware Structural Constraint (TASC)：在感知特征空间提供拓扑结构级监督，增强断层连续性并抑制噪声。在Thebe数据集上达到SOTA（OIS=0.879, ODS=0.875），且参数量更少。

# Method Overview / 方法概述

U型编码器-解码器架构。编码器分为4个阶段：Stage 1（Swin Transformer提取局部特征）→ Stage 2-3（G-Mamba模块，即Mamba+GLA）→ Stage 4（Swin Transformer整合全局语义）。解码器通过上采样逐步恢复分辨率。GLA模块并行提取局部空间特征和全局通道注意力。TASC约束在感知特征空间中对齐预测与真实结构的拓扑关系。

# Dataset and Evaluation / 数据集与评估

**数据集**: Thebe — 目前最大公开3D地震数据集（An et al., 2023），包含真实3D地震数据及断层标注。**评估指标**: OIS (Optimal Image Scale), ODS (Optimal Dataset Scale)。**结果**: OIS=0.879, ODS=0.875，超越现有SOTA预训练模型。**消融实验**: 验证了GLA、TASC、混合编码器各组件有效。

# Why This Paper Matters / 为什么关注这篇论文

(1) 首次将Mamba引入地震分割，开辟了新的研究方向；(2) Swin Transformer + Mamba的混合架构在参数量和性能之间取得良好平衡，对RTX 4070等有限硬件具有实际意义；(3) TASC拓扑约束的思想可迁移到其他地震图像分割任务；(4) 使用Thebe数据集（公开可获取），便于复现和对比。

# Limitations / 局限性

(1) 代码和预训练模型未公开，复现有难度；(2) 仅在Thebe单一数据集上验证，泛化性待确认；(3) Mamba+Swin混合架构的推理效率分析不够详细；(4) 与基于预训练的方法（如FaultSeg Swin-UNETR）相比，计算量优势的量化分析不足。

# Reproducibility Status / 可复现性状态

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [ ] High [x] Medium [ ] Low

**Reason**: 方法描述详细（公式、架构图），Thebe数据集公开可用，但无开源代码，需要自行实现。

# My Decision / 我的决定

- [x] Read deeply / 精读
- [ ] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason**: SOTA方法，混合架构思路新颖，对RTX 4070友好，值得深入研究其可迁移的组件。

# Related Knowledge / 相关知识链接

- Task: [[Seismic Fault Segmentation]]
- Method: [[Swin Transformer]]
- Method: [[Mamba]]
- Dataset: [[Thebe Dataset]]

## Zotero

- **Zotero Item Key (Attachment)**: M29ILMXG
- **Zotero Item Key (Parent)**: 4NEI9ULI
- **Status**: Level 1 Card Created
