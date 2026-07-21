---
title: "FaultEdgeFormer: an edge enhanced transformer model for 3D seismic fault detection"
authors: [Xi Di, Yang Liu, Suoliang Chang, Wenbin Tian, Jiangtao Ma, Zilong Dong]
year: 2026
venue: "待确认"
task: [3D Seismic Fault Detection]
method: [Edge-Enhanced Transformer, Trainable Sobel Convolution, Improved Swin Transformer, Parallel Multiscale Fusion]
dataset: [Synthetic 3D Seismic, F3 Netherlands, Kerry New Zealand]
code_available: Not Found Yet
importance: High
reading_status: to_read
tags: []
created: 2026-07-20
---

# Basic Information / 基本信息

- **Title**: FaultEdgeFormer: an edge enhanced transformer model for 3D seismic fault detection
- **Authors**: Xi Di, Yang Liu, Suoliang Chang, Wenbin Tian, Jiangtao Ma, Zilong Dong
- **Year**: 2026
- **Venue**: 待确认
- **Task**: 3D地震断层检测（3D Seismic Fault Detection）
- **Method**: 边缘增强Transformer（可训练Sobel卷积 + 改进Swin Transformer + 并行多尺度融合）
- **Dataset**: 合成三维地震数据、F3 Netherlands野外数据、Kerry New Zealand野外数据
- **Code**: Not Found Yet

# Research Problem / 研究问题

现有基于CNN的断层检测方法面临两个关键挑战：
1. **CNN核随机初始化问题**：卷积核从随机权重开始优化，限制了网络在早期训练阶段聚焦于断层相关特征的能力。
2. **局部感受野限制**：CNN受限于固定核大小和有限的感受野，无法学习全局上下文信息，导致长距离断层检测不连续。

# Main Contribution / 主要贡献

提出FaultEdgeFormer——一种边缘增强的Transformer架构，用于三维地震断层检测，核心创新点包括：

1. **可训练Sobel卷积（Trainable Sobel Convolution）**：首次将3D多方向Sobel算子作为网络第一层，通过可学习的缩放因子γ自适应调整边缘增强强度，使网络在训练初期就聚焦于断层边缘特征。
2. **改进Swin Transformer块**：在W-MSA中引入卷积投影（Convolutional Projection），在MLP中引入深度可分离卷积（Depthwise Convolution），在保持Transformer全局建模能力的同时引入CNN的局部归纳偏置。
3. **并行多尺度融合（Parallel Multiscale Fusion）**：不同于U-Net的串行下采样，采用并行多分辨率流结构，在整个网络中保持高分辨率表示，减少断层边缘信息丢失。

# Method Overview / 方法概述

FaultEdgeFormer采用五阶段四分辨率架构：

- **Stage 1**：可训练Sobel卷积（9个3×3×3多方向核）→ 标准卷积 → 下采样
- **Stage 2**：瓶颈层 → 双分辨率流（高分辨率9通道 + 低分辨率18通道）
- **Stage 3-4**：改进Swin Transformer块（窗口大小7×7×7，头数[1,2,4]）+ 多尺度融合交换单元（上采样/下采样）
- **Stage 5**：上采样 → 1×1×1卷积 → Sigmoid输出断层概率

**可训练Sobel卷积**：3个正交梯度核（x, y, z轴）+ 6个非正交梯度核（xy, xz, yz平面45°/135°方向），每个核乘以可学习因子γ（初始化为1），通过反向传播优化。

**改进Swin Transformer**：将标准线性投影替换为3×3×3卷积投影（QKV生成），在MLP两个线性层之间插入3×3×3深度可分离卷积。

# Dataset and Evaluation / 数据集与评估

**训练数据**：采用Wu et al. (2019, 2020)的工作流生成600对128×128×128合成地震数据（500训练/50验证/100测试）。主频30-50Hz Ricker子波，SNR 5-25dB，包含正断层、逆断层、平行断层、相交断层等多种类型。数据增强：随机旋转、翻转、裁剪至96×96×96。

**损失函数**：平衡交叉熵损失（BCE，α由正负样本比确定）。消融实验也测试了Dice Loss和Tversky Loss（α=0.3, β=0.7）。

**评估指标**：Accuracy, Precision, Recall, F1, IoU（阈值0.5二值化）。

**基线方法**：CNN方法（FaultSeg3D, Fault-Net, FaultEdge-Net）、Transformer方法（UNETR, Swin UNETR）、消融变体（v1/v2/v3）。

**野外数据**：F3 Netherlands（多方向断层，Y形断层）和Kerry New Zealand（浅层高发育断层，相邻断层对）。

**关键结果**（合成测试集）：
- FaultEdgeFormer: F1=76.57%, IoU=62.37%（显著优于Fault-Net F1=62.59%, IoU=45.85%）
- 噪声鲁棒性：SNR从20dB降至5dB，F1从75.90%降至62.82%
- 模型复杂度：参数量1.34M，FLOPs 29.56G（96³输入），推理时间134.26ms

# Why This Paper Matters / 为什么关注这篇论文

1. **创新地将传统图像处理算子（Sobel）与深度学习结合**：可训练Sobel卷积为CNN-Transformer混合架构提供了新的先验知识注入方式，思路新颖且简洁有效。
2. **系统改进了Swin Transformer的局部感知能力**：在W-MSA和MLP中引入卷积操作，实验证明W-MSA中的卷积投影贡献更大，两者结合最优。
3. **轻量级模型**：参数量仅1.34M，适合RTX 4070（12GB VRAM）等有限硬件资源，具备实际部署潜力。
4. **与本研究方向高度相关**：地震断层检测是ResearchAI的核心研究方向，该论文提出的边缘增强+Transformer混合思路可直接参考。

# Limitations / 局限性

1. **仅探索了监督学习**：未涉及半监督（Dou et al. 2024）或自监督方法，而半监督/自监督已成为断层检测的前沿方向。
2. **训练数据仅为合成数据**：未包含野外数据训练，论文指出加入野外数据训练对实际应用泛化至关重要。
3. **推理速度较慢**：虽然参数量少（1.34M），但推理时间（134.26ms/96³）远高于CNN方法（Fault-Net 12.98ms），高分辨率分支重复应用Transformer是主要原因。
4. **高Recall低Precision问题**：BCE Loss倾向于过分割，虽然Dice/Tversky Loss可缓解但非论文重点。
5. **Sobel核方向覆盖有限**：仅9个方向，论文指出更复杂的Gabor滤波器可能更有效。

# Reproducibility Status / 可复现性状态

> Literature Card: lightweight screening. Paper Note / Paper Logic: deep analysis.

## Code Availability

**Status**: [ ] Available [X] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: <!-- Only fill when Status = Available -->

## Data Status / 数据可用性

- [ ] **Public dataset available** — freely downloadable
- [ ] **Restricted dataset** — requires application or license
- [X] **Private dataset** — not publicly accessible
- [ ] **Unknown** — paper does not specify

**Dataset Link**: 合成数据需通过作者请求获取（"The data that support the findings of this study can be obtained from the corresponding author upon request."）

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [ ] High [X] Medium [ ] Low

**Reason**: 模型架构描述详细（含伪代码Algorithm 1），超参数完整（Adam, lr=0.0001, 100 epochs, batch size=1），但合成数据生成代码未公开，需自行实现Wu et al.工作流。野外数据（F3和Kerry）可公开获取。

**Notes / 备注**: 论文未提及代码仓库，数据需向通讯作者申请。

# My Decision / 我的决定

- [X] Read deeply / 精读
- [ ] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason / 理由**: 该论文提出的可训练Sobel卷积+改进Swin Transformer思路对地震断层检测具有重要参考价值，模型轻量（1.34M参数）适合RTX 4070硬件条件。建议进入Level 2 Paper Note分析，重点关注架构复现和消融实验结果。

# Related Knowledge / 相关知识链接

- Task: [[3D Seismic Fault Detection]]
- Method: [[Edge-Enhanced Transformer]]
- Dataset: [[F3 Netherlands]], [[Kerry New Zealand]]

## Zotero

- **Item Key**: MVSQQ8TY (att)
- **Parent Item Key**: CR6P58ZY
- **Type**: Research Article