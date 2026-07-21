---
title: "3D-FaultSeg-UNet: 3D Fault Segmentation in Seismic Data Using Bi-stream U-Net"
authors: [Thi Dinh Van-Ha, Nguyen Thanh-An]
year: 2022
venue: "ICISN 2022, Springer"
task: [Seismic Fault Segmentation]
methods: [3D Bi-stream U-Net, 3D Convolutional Neural Network]
datasets: [3D Synthetic Seismic Dataset]
metrics: [Accuracy]
code: "Not Found Yet"
importance: Medium
status: to_read
paper_type: research_article
tags: [seismic, fault-segmentation, 3d-cnn, u-net, dual-stream]
created: 2026-07-20
---

# Paper Type / 论文类型

Type: research_article — 提出3D双流U-Net用于地震断层分割

# One Sentence Summary / 一句话总结

提出3D Bi-stream U-Net，通过两个独立并行分支提取互补特征，在合成3D地震数据上达到96.79%的断层分割准确率。

# Research Background / 研究背景

地震断层分割是结构解释的关键步骤，传统上依靠人工标注，效率低且主观性强。3D卷积神经网络（如3D U-Net）在自动断层分割中取得进展，但单一网络流对断层这种稀疏、不连续结构的特征表达能力有限。

# Problem Definition / 问题定义

- **Input / 输入**: 3D地震图像体数据
- **Output / 输出**: 3D二值掩码（断层位置=1，非断层=0）

# Motivation / 研究动机

单一网络流提取的特征可能不够丰富，尤其在断层边界模糊、空间分布不均匀的情况下。双流网络通过两个独立分支从不同角度学习特征表示，在瓶颈层融合互补信息，有望提升分割性能。

# Main Contributions / 主要贡献

1. 提出3D Bi-stream U-Net — 双流3D卷积神经网络用于端到端断层分割
2. 结合U-Net跳跃连接和ResNet残差连接的思想，控制信息流动
3. 在合成3D地震数据上验证，测试集准确率96.79%，优于现有方法

# Method / 方法

## Overall Framework / 整体框架

输入3D地震图像 → 双流并行编码器（Branch 1和Branch 2分别提取特征）→ 瓶颈层拼接 → 上采样解码器（含跳跃连接）→ Sigmoid输出分割掩码

## Key Modules / 关键模块

### Module 1: 双流编码器
每个分支5组3D卷积层+3D最大池化层：
- 第1组: 2×Conv3D(8, 3×3×3) + MaxPooling
- 第2组: 2×Conv3D(16, 3×3×3) + MaxPooling
- 第3组: 2×Conv3D(32, 3×3×3) + MaxPooling
- 第4组: 2×Conv3D(64, 3×3×3) + Dropout(0.5) + MaxPooling
- 第5组: 2×Conv3D(128, 3×3×3) + Dropout(0.5)

### Module 2: 上采样解码器
UpSampling3D(2×2×2) → 拼接两个分支对应层特征 → Conv3D → 逐步恢复分辨率 → 最终Conv3D(1, 1×1×1) + Sigmoid

# Dataset / 数据集

| Dataset | Size | Modality | Description |
|---------|------|----------|-------------|
| 3D Synthetic Seismic Data | 未公开 | 3D体数据 | 来自Wu et al. FaultSeg3D的合成数据 |

# Experimental Setup / 实验设置

使用数据增强（旋转、翻转）。优化器和超参数未详细说明。评估指标：准确率（Accuracy）。

# Results / 实验结果

| Dataset | Accuracy |
|---------|----------|
| Training Set | 97.31% |
| Test Set | 96.79% |

优于现有方法，但对比方法未详细说明。

# Limitation / 局限性

1. 仅在合成数据上验证，真实数据泛化能力未知
2. 仅使用Accuracy作为评估指标，缺少IoU/Dice等分割标准指标
3. 未提供充分的消融实验证明双流优于单流
4. 数据集未公开，无法复现和公平对比
5. 与SOTA方法（如FaultSeg3D）的详细对比不足

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

1. **双流并行设计**：简单有效的特征增强策略，可迁移到其他3D分割任务
2. **跳跃连接**：融合编码器和解码器特征，保留空间细节

## Potential Improvements / 潜在改进方向

1. 使用更丰富的评估指标（IoU, Dice, F1-score）
2. 在公开数据集（如Thebe）上验证
3. 添加注意力机制引导双流关注不同特征

# Reproducibility Analysis / 复现性分析

**Code Status**: [ ] Confirmed Available [ ] Confirmed Missing [x] Not Found Yet [ ] Not Checked

**Overall Difficulty**: [ ] Easy [x] Moderate [ ] Hard [ ] Impossible

**RTX 4070 Compatibility**: [x] Runs fine — 3D卷积，参数量适中

# Related Notes / 相关笔记

- Task: [[Seismic Fault Segmentation]]
- Method: [[U-Net]]
- Method: [[3D Convolutional Neural Network]]

## Zotero
- **Zotero Item Key (Attachment)**: EHKI6VXW
- **Zotero Item Key (Parent)**: FCLVNZWZ
- **Status**: Level 2 Note Created
