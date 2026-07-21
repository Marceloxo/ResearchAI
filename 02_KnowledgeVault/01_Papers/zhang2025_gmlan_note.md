---
title: "GMLAN: Grouped-Residual and Multi-Scale Large-Kernel Attention Network for Seismic Image Super-Resolution"
authors: [Zhang et al.]
year: 2025
venue: "Journal"
task: [Seismic Image Super-Resolution]
methods: [Grouped Residual Learning, Large-Kernel Attention, Multi-Scale Feature Fusion]
datasets: [Seismic Dataset]
metrics: [PSNR, SSIM, RMSE]
code: "Not Found Yet"
importance: High
status: to_read
paper_type: research_article
tags: [seismic, super-resolution, attention, grouped-residual, large-kernel]
created: 2026-07-20
---

# Paper Type / 论文类型

Type: research_article — 提出分组残差大核注意力网络用于地震图像超分辨率

# One Sentence Summary / 一句话总结

提出GMLAN，通过分组残差学习和多尺度大核注意力机制，在保持计算效率的同时提升地震图像超分辨率重建质量。

# Research Background / 研究背景

地震图像分辨率对后续解释任务（断层检测、相分割）至关重要。超分辨率技术可从低分辨率数据重建高分辨率图像，但现有方法在保持纹理细节和结构连续性方面存在不足。

# Main Contributions / 主要贡献

1. 分组残差学习策略减少参数量同时保持表示能力
2. 多尺度大核注意力机制捕获不同尺度的空间依赖
3. 在多个地震数据集上取得SOTA超分辨率结果

# Method / 方法

## Overall Framework / 整体框架

输入低分辨率地震图像 → 分组残差模块提取特征 → 多尺度大核注意力模块增强表示 → 上采样重建 → 高分辨率输出

# Results / 实验结果

在PSNR、SSIM、RMSE等指标上优于现有超分辨率方法。

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

1. 分组残差设计对RTX 4070友好，可在有限显存下使用更大模型
2. 大核注意力可迁移到其他地震图像恢复任务
3. 超分辨率作为预处理步骤可提升下游分割任务性能

# Reproducibility Analysis / 复现性分析

**Code Status**: [ ] Confirmed Available [ ] Confirmed Missing [x] Not Found Yet [ ] Not Checked

**Overall Difficulty**: [ ] Easy [x] Moderate [ ] Hard [ ] Impossible

**RTX 4070 Compatibility**: [x] Runs fine — 分组残差设计减少显存需求

# Related Notes / 相关笔记

- Task: [[Seismic Super-Resolution]]
- Method: [[Large-Kernel Attention]]

## Zotero
- **Zotero Item Key (Attachment)**: J4M25UH8
- **Zotero Item Key (Parent)**: 6JT5ZPGC
- **Status**: Level 2 Note Created
