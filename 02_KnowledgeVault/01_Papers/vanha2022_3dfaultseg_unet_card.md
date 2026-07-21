---
title: "3D-FaultSeg-UNet: 3D Fault Segmentation in Seismic Data Using Bi-stream U-Net"
authors: [Thi Dinh Van-Ha, Nguyen Thanh-An]
year: 2022
venue: "Intelligent Systems and Networks (ICISN 2022)"
task: [Seismic Fault Segmentation]
method: [3D Bi-stream U-Net, 3D Convolutional Neural Network]
dataset: [3D Synthetic Seismic Dataset]
code_available: Not Found Yet
importance: Medium
reading_status: to_read
tags: [seismic, fault-segmentation, 3d-cnn, u-net, deep-learning]
created: 2026-07-20
---

# Basic Information / 基本信息

- **Title**: 3D-FaultSeg-UNet: 3D Fault Segmentation in Seismic Data Using Bi-stream U-Net
- **Authors**: Thi Dinh Van-Ha, Nguyen Thanh-An
- **Year**: 2022
- **Venue**: ICISN 2022 (Springer)
- **Task**: 地震断层分割 (3D Seismic Fault Segmentation)
- **Method**: 3D双流U-Net (3D Bi-stream U-Net)
- **Dataset**: 3D合成地震数据集
- **Code**: Not Found Yet

# Research Problem / 研究问题

传统断层解释依赖人工标注，效率低且主观性强。现有深度学习方法使用单一网络流提取特征，对断层这种稀疏、不连续结构的特征表达能力有限。如何设计一个3D端到端网络，能够从不同视角提取互补特征，提高断层分割精度？

# Main Contribution / 主要贡献

提出3D Bi-stream U-Net — 一个双流3D卷积神经网络用于地震断层分割。核心创新：(1) 两个独立的并行分支（Branch 1和Branch 2）对同一输入3D地震图像提取不同特征，然后在瓶颈层拼接融合；(2) 结合U-Net的跳跃连接思想和ResNet的残差连接；(3) 在合成数据上训练，在测试集上达到96.79%的准确率。

# Method Overview / 方法概述

网络架构：两个独立分支，每个分支包含5组3D卷积层+3D最大池化层（卷积核3×3×3，滤波器数从8到128递增），后两个组添加Dropout(0.5)。两个分支的输出在瓶颈层拼接后，通过上采样流（UpSampling3D + 跳跃连接融合两个分支的特征）逐步恢复分辨率，最终通过Sigmoid输出分割掩码。

# Dataset and Evaluation / 数据集与评估

**数据集**: 3D合成地震数据（来自Wu et al. FaultSeg3D）。使用数据增强（旋转、翻转）。**评估指标**: 准确率（Accuracy）。训练集准确率97.31%，测试集准确率96.79%，优于现有方法。

# Why This Paper Matters / 为什么关注这篇论文

双流架构思路简单但有效，两个分支隐式学习互补特征。对RTX 4070（12GB显存）来说，3D卷积网络的计算量需要评估，但双流设计可作为一种轻量级改进思路。该工作为断层分割提供了一个简洁的基线模型。

# Limitations / 局限性

(1) 仅在合成数据上验证，在真实地震数据上的泛化能力未知；(2) 仅使用准确率作为评估指标，缺少IoU、Dice系数等分割任务标准指标；(3) 双流设计增加了参数量，但未提供充分的消融实验证明双流优于单流；(4) 数据集较小，且未公开；(5) 未与SOTA方法（如FaultSeg3D）进行详细对比。

# Reproducibility Status / 可复现性状态

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [ ] High [x] Medium [ ] Low

**Reason**: 网络结构描述详细（表1和表2），但缺少训练超参数、数据预处理细节。

# My Decision / 我的决定

- [ ] Read deeply / 精读
- [x] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason**: 双流U-Net思路简洁，但论文较为初步（会议短文），缺乏充分的实验验证和与SOTA方法的对比，作为参考基线保留即可。

# Related Knowledge / 相关知识链接

- Task: [[Seismic Fault Segmentation]]
- Method: [[U-Net]]
- Method: [[3D Convolutional Neural Network]]

## Zotero

- **Zotero Item Key (Attachment)**: EHKI6VXW
- **Zotero Item Key (Parent)**: FCLVNZWZ
- **Status**: Level 1 Card Created
