---
title: "AttentionFaultFormer: An attention-enhanced 3D CNN & transformer model for seismic fault detection"
authors: [Jing Wang, Siteng Ma, Yue Liu, Ruihai Dong]
year: 2025
venue: "Computers & Geosciences (or similar — full venue not specified in MinerU frontmatter)"
task: [Fault Detection]
method: [AttentionFaultFormer, 3D CNN-ViT Hybrid, Swin Transformer, CBAM, Multi-Axis Striped Convolution Attention]
dataset: [FaultSeg3D, F3, Kerry3D, Thebe]
code_available: Not Found Yet
importance: High
reading_status: Screening Complete
tags: [fault-detection, vision-transformer, cnn-vit-hybrid, attention-mechanism, seismic-interpretation]
created: 2026-07-20
---

# Basic Information / 基本信息

- **Title**: AttentionFaultFormer: An attention-enhanced 3D CNN & transformer model for seismic fault detection
- **Authors**: Jing Wang, Siteng Ma, Yue Liu, Ruihai Dong
- **Year**: 2025
- **Venue**: 未在MinerU前文中明确标识（推测为 Computers & Geosciences 或类似期刊）
- **Task**: 地震断层检测 (Fault Detection)
- **Method**: AttentionFaultFormer — 3D CNN & ViT混合模型，包含Swin Transformer编码器、残差卷积解码器、AttentionSkip（CBAM增强跳跃连接）和MASCA（多轴条形卷积注意力模块）
- **Dataset**: FaultSeg3D（合成数据），F3、Kerry3D、Thebe（野外数据）
- **Code**: 未找到

# Research Problem / 研究问题

论文试图解决3D Vision Transformer（ViT）在断层检测中面临的三个核心挑战：(1) 断层在三维地震体中极度稀疏，导致类别严重不平衡；(2) ViT的全局注意力机制可能过度关注非断层像素，忽略断层本身的特征；(3) 3D ViT模型计算资源消耗巨大。此外，现有CNN模型主要关注局部特征，难以准确刻画长距离延伸的连续断层。

# Main Contribution / 主要贡献

1. 设计了**AttentionFaultFormer**，一个新颖的三阶段CNN & Transformer混合模型，以Swin Transformer块为编码器、残差卷积块为解码器，专门用于断层检测任务。
2. 提出了**AttentionSkip** — 一种注意力增强的跳跃连接，集成CBAM（通道和空间注意力机制），增强模型对断层特征的关注。
3. 基于断层几何特征（延伸性），设计了**MASCA（多轴条形卷积注意力）模块**，沿三个坐标轴使用大尺度条形卷积提取长距离特征，提升对连续长断层的检测能力。
4. 在FaultSeg3D上预训练，迁移到F3、Kerry3D和Thebe三个野外地震数据集，与UNet3D、VNet3D、Swin UNETR、VT-UNet等SOTA模型对比，证明模型预测的断层更连续、更具可解释性。

# Method Overview / 方法概述

AttentionFaultFormer采用**U形架构**，包含三个阶段的下采样：

1. **3D Swin Transformer编码器**：输入三维地震体，通过PatchEmbed（5×5×5卷积）分割为3D tokens，经三个级联阶段处理，每个阶段包含多个Swin Transformer块（W-MSA和SW-MSA交替）和PatchMerging下采样层。
2. **AttentionSkip（注意力增强跳跃连接）**：由3×3×3卷积层、CBAM（Convolutional Block Attention Module）和BatchNorm3d组成，在通道和空间两个维度上自适应关注断层相关特征。
3. **MASCA模块**：利用1×1×N、1×N×1、N×1×1三种方向的条形卷积，结合两种核大小（7和11），沿三个轴提取长条形特征，仅插入浅层跳跃连接以增强对长延伸断层特征的关注。
4. **残差卷积解码器**：由三个ResBlock组成，采用最近邻上采样和跳跃连接融合。

损失函数为BCELoss、DiceLoss和FocalLoss的加权组合（权重0.4:0.2:0.4），应对断层类别不平衡问题。

# Dataset and Evaluation / 数据集与评估

**训练数据集**：
- **FaultSeg3D**：合成数据集，128×128×128，200个训练样本，分割为96×96×96的小体积（最终400训练/30验证/10测试）

**迁移测试数据集**：
- **F3**：荷兰北海区块，512×384×128
- **Kerry3D**：新西兰野外数据，287×735×1252
- **Thebe**：最大公开标注野外数据集，703×3174×1537，标注>20m垂直位移的断层

**评估指标**：Accuracy、Precision、Recall、F1 Score

**对比模型**：UNet3D、VNet3D（CNN模型）；VT-UNet、Swin UNETR（ViT模型）

**关键结果**：
- FaultSeg3D上：F1=78.77%（第二，仅次于UNet3D的78.93%），但优于两个ViT模型
- 模型参数量仅9.62M，远低于VNet3D（45.59M）和Swin UNETR（61.41M）
- Thebe数据集上（微调后）：Accuracy=93.43%，Recall=54.06%，F1=55.98%（均为最高）
- 消融实验表明Swin Transformer提供更强的泛化能力，MASCA提升断层连续性

# Why This Paper Matters / 为什么关注这篇论文

本文是**专门为3D地震断层检测设计的CNN-ViT混合模型**，具有以下价值：
1. 针对断层几何特征（延伸性）设计了MASCA模块，思路新颖
2. 模型参数量仅9.62M，在RTX 4070（12GB）上具有可行性
3. 在三个野外数据集上验证了迁移学习能力，具有实际应用价值
4. 与当前研究热点（ViT在地震中的应用）高度相关

# Limitations / 局限性

1. 在FaultSeg3D合成数据集上，UNet3D的F1反而更高（78.93% vs 78.77%），说明ViT在纯合成数据上优势不明显
2. 推理时间较长（95.87ms），是UNet3D（33.31ms）的近3倍，实时性受限
3. 仅使用一个合成数据集（FaultSeg3D）进行预训练，泛化能力验证有限
4. 消融实验显示去除Swin Transformer块后F1反而提升3.4%，说明ViT编码器对断层检测的贡献存在争议
5. 数据不可用声明为"Data will be made available on request"，代码未公开

# Reproducibility Status / 可复现性状态

> Literature Card: lightweight screening. Paper Note / Paper Logic: deep analysis.

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: <!-- Only fill when Status = Available -->

## Data Status / 数据可用性

- [ ] **Public dataset available** — freely downloadable
- [ ] **Restricted dataset** — requires application or license
- [ ] **Private dataset** — not publicly accessible
- [x] **Unknown** — paper does not specify

**Dataset Link**: <!-- URL to dataset download or access page -->

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [ ] High [x] Medium [ ] Low

**Reason**: 模型架构描述详细，使用公开数据集FaultSeg3D、F3、Kerry3D、Thebe，但代码未公开，需要从零实现。参数量较小（9.62M），在RTX 4070上理论上可复现。

**Notes / 备注**:

# My Decision / 我的决定

- [x] Read deeply / 精读
- [ ] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason / 理由**: 端到端CNN-ViT混合模型，9.62M参数量适合RTX 4070，MASCA模块设计有创新性，与当前断层检测研究方向高度相关。

# Related Knowledge / 相关知识链接

- Task: [[Fault Detection]]
- Method: [[AttentionFaultFormer]]
- Dataset: [[FaultSeg3D]]

## Zotero

**Zotero Item Key**: 8U23DIYR (att), parent: 6YBBCNWE