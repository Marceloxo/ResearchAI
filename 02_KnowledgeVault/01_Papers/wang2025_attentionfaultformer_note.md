---
title: "AttentionFaultFormer: An Attention-Enhanced 3D CNN & Transformer Model for Seismic Fault Detection"
authors: [Wang et al.]
year: 2025
venue: "Journal"
task: [Seismic Fault Detection]
methods: [3D CNN, Transformer, Attention Mechanism, Hybrid Architecture]
datasets: [Thebe, Synthetic Seismic Data]
metrics: [OIS, ODS, IoU, F1]
code: "Not Found Yet"
importance: High
status: to_read
paper_type: research_article
tags: [seismic, fault-detection, 3d-cnn, transformer, attention, hybrid]
created: 2026-07-20
---

# Paper Type / 论文类型

Type: research_article — 提出3D CNN + Transformer混合注意力模型用于地震断层检测

# One Sentence Summary / 一句话总结

提出AttentionFaultFormer，结合3D CNN的局部特征提取能力和Transformer的全局上下文建模能力，通过注意力增强机制在多个地震数据集上实现高精度断层检测。

# Research Background / 研究背景

地震断层检测是油气勘探和地质结构解释的关键步骤。3D CNN擅长局部特征提取但感受野有限，Transformer能建模长程依赖但计算量大。如何有效融合两者优势是当前研究热点。

# Problem Definition / 问题定义

- **Input / 输入**: 3D地震体数据
- **Output / 输出**: 3D断层检测结果（分割掩码或概率图）

# Main Contributions / 主要贡献

1. 提出3D CNN + Transformer混合架构，结合局部和全局特征
2. 注意力增强模块提升对弱断层信号的敏感度
3. 在多个数据集上验证，包括最大公开数据集Thebe

# Method / 方法

## Overall Framework / 整体框架

3D CNN编码器提取局部特征 → Transformer模块建模全局依赖 → 注意力融合模块整合多尺度特征 → 解码器输出检测结果

# Results / 实验结果

在Thebe数据集上取得有竞争力的结果，与SOTA方法（如FaultSeg Swin-UNETR）可比。

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

1. CNN+Transformer混合架构对RTX 4070友好
2. 注意力增强思想可迁移到其他地震分割任务

# Reproducibility Analysis / 复现性分析

**Code Status**: [ ] Confirmed Available [ ] Confirmed Missing [x] Not Found Yet [ ] Not Checked

**Overall Difficulty**: [ ] Easy [ ] Moderate [x] Hard [ ] Impossible

**RTX 4070 Compatibility**: [x] May struggle — 3D Transformer需评估显存

# Related Notes / 相关笔记

- Task: [[Seismic Fault Detection]]
- Method: [[3D CNN]]
- Method: [[Transformer]]

## Zotero
- **Zotero Item Key (Attachment)**: 8U23DIYR
- **Zotero Item Key (Parent)**: 6YBBCNWE
- **Status**: Level 2 Note Created
