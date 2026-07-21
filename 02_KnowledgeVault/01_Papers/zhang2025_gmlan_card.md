---
title: "GMLAN: Grouped-residual and multi-scale large-kernel attention network for seismic image super-resolution"
authors: [Anxin Zhang, Zhenbo Guo, Shiqi Dong, Zhiqi Wei]
year: 2025
venue: "Journal of Seismic Exploration (or similar — Special Issue on Advanced AI for Seismic Exploration)"
task: [Seismic Super-Resolution]
method: [GMLAN, Grouped-Residual Learning, Multi-Scale Large-Kernel Attention, Sub-Pixel Convolution]
dataset: [Synthetic seismic images (2000 pairs), F3 Netherlands, Kerry New Zealand, Volve North Sea]
code_available: Not Found Yet
importance: High
reading_status: Screening Complete
tags: [super-resolution, seismic-image-processing, attention-mechanism, grouped-residual, large-kernel-attention]
created: 2026-07-20
---

# Basic Information / 基本信息

- **Title**: GMLAN: Grouped-residual and multi-scale large-kernel attention network for seismic image super-resolution
- **Authors**: Anxin Zhang, Zhenbo Guo, Shiqi Dong, Zhiqi Wei
- **Year**: 2025
- **Venue**: 未在MinerU前文中明确标识（Special Issue: Advanced Artificial Intelligence Theories and Methods for Seismic Exploration）
- **Task**: 地震图像超分辨率 (Seismic Image Super-Resolution)
- **Method**: GMLAN — 分组残差与多尺度大核注意力网络，包含特征提取模块（FEM）和图像重建模块（IRM）
- **Dataset**: 2000对合成地震数据（训练/验证/测试=8:1:1），F3（荷兰）、Kerry（新西兰）、Volve（挪威北海）野外数据
- **Code**: 未找到

# Research Problem / 研究问题

地震图像分辨率受采集环境、数据处理方法等多因素影响，导致同相轴模糊、噪声干扰，影响后续地质解释（断层检测、储层定位）的准确性。传统分辨率增强方法（反演、去噪、插值、反褶积等）需多步骤处理，误差累积，难以恢复细节。论文旨在设计一种端到端的深度学习方法，在保持低频信息的同时有效恢复地震图像的高频细节。

# Main Contribution / 主要贡献

1. 提出了**GMLAN（分组残差与多尺度大核注意力网络）**，融合卷积和注意力机制，实现地震图像超分辨率重建。
2. 设计了**深度特征提取（DFE）模块**，包含分组残差结构和多尺度大核注意力（MLKA）机制，有效提取多尺度特征，同时减少计算参数量。
3. 引入**残差自注意力块（RSAB）**，通过通道分组和线性变换减少自注意力计算冗余，降低计算复杂度。
4. 采用**亚像素卷积（Sub-Pixel Convolution）**进行上采样，避免传统插值方法产生的伪影和模糊。
5. 在合成数据和多个野外数据集（F3、Kerry、Volve）上验证了优越性能，PSNR和SSIM显著优于U-Net基线。

# Method Overview / 方法概述

GMLAN由两个主要模块组成：

**1. 特征提取模块（FEM）**：
- **浅层特征提取（SFE）**：3×3卷积层，提取大尺度结构特征
- **深层特征提取（DFE）**：4个GRMLKA块级联，每个块包含6层多残差组，在偶数层（第2、4、6层）后插入MLKA模块
  - **残差自注意力块（RSAB）**：将输入特征按通道分两组，分别进行线性变换和残差计算，减少计算冗余
  - **多尺度大核注意力（MLKA）**：将特征分为3组，分别用3×3、5×5、7×7卷积提取局部特征，结合空洞卷积扩大感受野，利用空间门控增强特征表示

**2. 图像重建模块（IRM）**：
- 融合浅层和深层特征，通过3×3卷积调整通道，亚像素卷积进行2倍上采样

**损失函数**：L1 Loss + MS-SSIM Loss的混合损失（α=0.6）

**关键特点**：
- 参数量仅3.38M，远低于U-Net的17.41M
- 通过分组残差和MLKA实现多尺度特征提取
- 采用连续相对位置偏置适配地震数据的结构连续性

# Dataset and Evaluation / 数据集与评估

**训练数据集**：
- 2000对合成地震数据（8:1:1划分训练/验证/测试）
- 生成方法：基于Wu et al. (2019)方法，3D反射率模型 + 褶积模型
  - 高频（35-55Hz Ricker子波）→ 高分辨率标签
  - 低频（10-25Hz Ricker子波）+ 有色噪声 + 下采样 → 低分辨率输入

**测试数据集**：
- **F3**（荷兰北海）：512道，野外数据
- **Kerry**（新西兰）：512道，野外数据
- **Volve**（挪威北海）：深部地震数据

**评估指标**：PSNR、SSIM、RMSE

**对比模型**：U-Net（相同超参数设置）

**关键结果**：
- 合成数据上：PSNR 19.42 dB vs U-Net 13.68 dB，SSIM 0.89 vs 0.68，RMSE 0.12 vs 0.25
- 参数量仅3.38M，约为U-Net（17.41M）的1/5
- 消融实验：无MLKA时PSNR降至19.20 dB，4个DFE阶段为最优配置
- 在噪声测试（SNR=1, 5, 15 dB）和深部数据上均表现良好

# Why This Paper Matters / 为什么关注这篇论文

1. **轻量级设计**（3.38M参数），非常适合RTX 4070（12GB VRAM）的硬件约束
2. 超分辨率是断层检测的重要预处理步骤，可与ResearchAI的断层检测研究形成技术栈
3. 分组残差+多尺度大核注意力的设计思路可迁移到其他地震处理任务
4. 使用合成数据训练+野外数据迁移的范式与断层检测一致，方法论可复用

# Limitations / 局限性

1. **仅与U-Net对比**，未与近年来的SOTA超分辨率方法（如SwinIR、RCAN、SRFormer等）比较
2. 低信噪比（SNR=1dB）场景下性能仍有不足，去噪效果有限
3. 野外数据上缺乏定量评估（无ground truth），仅有视觉对比
4. 训练数据仅基于单一合成方法（Wu et al. 2019），多样性有限
5. 数据不可用声明为"available from corresponding author on reasonable request"，代码未公开

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

**Reason**: 模型架构描述详细，合成数据生成方法明确（基于Wu et al. 2019），但代码未公开。参数量仅3.38M，在RTX 4070上完全可复现。F3野外数据为公开数据集。

**Notes / 备注**: 可使用Wu et al. (2019)的公开代码生成合成数据。

# My Decision / 我的决定

- [x] Read deeply / 精读
- [ ] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason / 理由**: 超轻量（3.38M参数）地震超分辨率模型，与RTX 4070硬件约束高度匹配，可作为断层检测的预处理管道组件。

# Related Knowledge / 相关知识链接

- Task: [[Seismic Super-Resolution]]
- Method: [[GMLAN]]
- Dataset: [[F3]] [[Synthetic Seismic Data]]

## Zotero

**Zotero Item Key**: J4M25UH8 (att), parent: 6JT5ZPGC