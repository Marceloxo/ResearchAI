---
title: "FaultEdgeFormer: an edge enhanced transformer model for 3D seismic fault detection"
authors: [Xi Di, Yang Liu, Suoliang Chang, Wenbin Tian, Jiangtao Ma, Zilong Dong]
year: 2026
venue: "待确认"
task: [3D Seismic Fault Detection]
methods: [Edge-Enhanced Transformer, Trainable Sobel Convolution, Improved Swin Transformer, Parallel Multiscale Fusion]
datasets: [Synthetic 3D Seismic, F3 Netherlands, Kerry New Zealand]
metrics: [Accuracy, Precision, Recall, F1, IoU]
code: "Not Found Yet"
importance: High
status: deep_reading
paper_type: research_article
tags: [seismic-fault-detection, edge-enhancement, swin-transformer, cnn-transformer-hybrid, 3d-seismic]
created: 2026-07-20
---

# Paper Type / 论文类型

Type: research_article — 提出新方法（边缘增强Transformer架构用于3D地震断层检测）

# One Sentence Summary / 一句话总结

FaultEdgeFormer将可训练Sobel卷积（网络第一层）与改进Swin Transformer块（卷积投影+深度可分离卷积）结合，通过并行多尺度融合架构在合成和野外地震数据上实现了优于CNN和Transformer方法的断层检测性能（F1=76.57%, IoU=62.37%）。

# Research Background / 研究背景

断层检测是地震解释中的关键任务，对重建地壳变形过程、理解地质演化历史以及评估油气成藏机制和储层分布至关重要。传统方法基于地震属性（相干性、相似性、曲率等）和图像处理（蚂蚁追踪、Canny边缘检测、Sobel滤波等），但性能易受属性图质量影响。

深度学习方法，特别是CNN，在断层检测中取得了显著成功。CNN方法主要分为两类：分类方法（将断层检测视为二值分类问题，对地震块进行"断层"/"非断层"标注）和分割方法（使用全卷积网络进行逐像素分类）。U-Net及其变体通过编码器-解码器结构和跳跃连接，成为断层检测的主流架构。

然而，现有基于CNN的断层检测方法面临两个关键挑战：
1. **CNN核随机初始化问题**：卷积核从随机权重开始优化，限制了网络在早期训练阶段聚焦于断层相关特征的能力。
2. **局部感受野限制**：CNN受限于固定核大小和有限的感受野，无法学习全局上下文信息，导致长距离断层检测不连续。

近年来，Transformer（ViT、Swin Transformer）在图像处理中展现出强大的长距离依赖建模能力，但纯Transformer架构缺乏CNN的局部归纳偏置，在有限训练数据下泛化能力不足。

# Problem Definition / 问题定义

- **Input / 输入**: 三维地震数据体，尺寸为 $H \times W \times D$（训练时裁剪为 $96 \times 96 \times 96$），单通道灰度值表示地震反射振幅。
- **Output / 输出**: 与输入同尺寸的断层概率图 $H \times W \times D$，每个体素取值 $[0, 1]$，表示该位置为断层的概率（经Sigmoid激活后输出，阈值0.5二值化）。

# Motivation / 研究动机

1. **CNN的随机初始化问题**：断层本质上是地震数据中的边缘特征（振幅不连续性）。传统边缘检测算子（如Sobel）可以显式计算梯度信息，但现有CNN方法未利用这一先验知识。能否将预定义的边缘检测算子作为网络第一层，使网络在训练初期就聚焦于断层相关特征？

2. **CNN的局部感受野限制**：断层在三维空间中延伸很远（可达数公里），CNN的局部感受野导致长距离断层检测不连续。Transformer的自注意力机制可以建立长距离依赖，但缺乏CNN的局部归纳偏置，在有限训练数据下表现不佳。能否将卷积操作引入Transformer，在保持全局建模能力的同时增强局部感知能力？

3. **U-Net串行下采样的信息损失**：U-Net的编码器-解码器结构通过串行下采样逐渐减小空间分辨率，但下采样会导致断层边缘细节信息的丢失。能否采用并行多分辨率架构，在整个网络中保持高分辨率表示？

# Main Contributions / 主要贡献

1. **可训练Sobel卷积（Trainable Sobel Convolution）**：首次将3D多方向Sobel算子作为网络第一层。通过9个预定义的3×3×3方向核（3个正交梯度核 + 6个非正交梯度核）和可学习的缩放因子γ，自适应增强断层边缘特征，使网络在训练初期就聚焦于断层边缘。

2. **改进Swin Transformer块**：对标准Swin Transformer块进行两项关键改进：(a) 在W-MSA/SW-MSA中用3×3×3卷积投影替代线性投影，引入局部感知能力；(b) 在MLP的两个线性层之间插入3×3×3深度可分离卷积，增强局部特征建模。消融实验证明卷积投影贡献更大，两者结合最优。

3. **并行多尺度融合架构（Parallel Multiscale Fusion）**：与U-Net的串行下采样不同，采用五阶段四分辨率并行架构，在整个网络中保持高分辨率表示，通过交换单元实现跨分辨率信息融合，减少断层边缘信息丢失。

# Method / 方法

## Overall Framework / 整体框架

FaultEdgeFormer采用五阶段四分辨率并行架构：

- **Stage 1（输入层）**：可训练Sobel卷积（1→9通道，3×3×3核）→ 标准卷积（9→9通道）→ 3×3×3步长2卷积下采样
- **Stage 2（瓶颈层+双分辨率分流）**：瓶颈层（9→36通道）→ 分流为高分辨率流（9通道）和低分辨率流（18通道，下采样一次）
- **Stage 3（三分辨率并行）**：两个分辨率流的Transformer单元（窗口7×7×7，头数[1,2]）+ 多尺度融合 → 生成第三分辨率（36通道）
- **Stage 4（四分辨率并行）**：三个分辨率流的Transformer单元（窗口7×7×7，头数[1,2,4]）+ 多尺度融合 → 仅保留高分辨率流
- **Stage 5（输出层）**：上采样 → 1×1×1卷积 → Sigmoid输出断层概率

整体参数量仅1.34M，FLOPs 29.56G（96³输入）。

## Key Modules / 关键模块

### Module 1: 可训练Sobel卷积（Trainable Sobel Convolution）

基于3D多方向Sobel算子，包含9个预定义的3×3×3卷积核：

- **3个正交梯度核**：沿x轴（Sx）、y轴（Sy）、z轴（Sz）方向计算梯度
- **6个非正交梯度核**：在xy平面（45°和135°）、xz平面（45°和135°）、yz平面（45°和135°）方向计算梯度

每个方向核乘以可学习因子γ（初始化为1，通过反向传播优化）。Sobel卷积将9种基础核重复N次（得到9×N个核），然后与输入地震数据进行卷积，输出多通道特征图。

**关键洞察**：断层可表征为地震数据中的边缘（振幅不连续性），Sobel算子通过梯度计算显式增强边缘特征。与随机初始化的卷积核相比，预定义的Sobel核使网络在训练初期就聚焦于断层相关特征，γ因子允许网络自适应调整各方向的边缘增强强度。

### Module 2: 改进Swin Transformer块

标准Swin Transformer块包括W-MSA（窗口多头自注意力）和SW-MSA（滑动窗口多头自注意力），以及MLP模块。改进点：

**改进1 — 卷积投影（Convolutional Projection in W-MSA）**：
- 将标准线性投影（Linear Projection）替换为3×3×3卷积投影
- 输入特征x通过Conv3D(x, W_qkv)生成QKV拼接矩阵，然后沿通道维度分割为Q、K、V
- 卷积操作引入局部感知偏置，使注意力机制在计算全局关系的同时保留局部结构信息

**改进2 — 深度可分离卷积（Depthwise Convolution in MLP）**：
- 在MLP的两个线性层之间插入3×3×3深度可分离卷积
- 引入极小的计算开销，但增强了MLP的局部特征建模能力

**标准Swin Transformer块公式**（改进前）：
$$
\begin{array} { r l } & { \hat { \pmb x } ^ { l } = \mathsf { W } \mathrm { - } \mathsf { M } \mathsf { S } \mathsf { A } \left( \mathrm { L N } \left( \pmb { \mathsf { x } } ^ { l - 1 } \right) \right) + \pmb { \mathsf { x } } ^ { l - 1 } , } \\ & { \pmb { \mathsf { x } } ^ { l } = \mathsf { M } \mathrm { L P } \left( \mathrm { L N } \left( \hat { \pmb { \mathsf { x } } } ^ { l } \right) \right) + \hat { \pmb { \mathsf { x } } } ^ { l } , } \\ & { \hat { \pmb { \mathsf { x } } } ^ { l + 1 } = \mathsf { S } \mathsf { W } \mathrm { - } \mathsf { M } \mathsf { S } \mathsf { A } \left( \mathrm { L N } \left( \pmb { \mathsf { x } } ^ { l } \right) \right) + \pmb { \mathsf { x } } ^ { l } , } \\ & { \pmb { \mathsf { x } } ^ { l + 1 } = \mathsf { M } \mathrm { L P } \left( \mathrm { L N } \left( \hat { \pmb { \mathsf { x } } } ^ { l + 1 } \right) \right) + \hat { \pmb { \mathsf { x } } } ^ { l + 1 } , } \end{array}
$$

**卷积投影的QKV生成**：
$$
\mathsf { \pmb { Q } } \mathsf { \pmb { K } } \mathsf { \pmb { V } } = \mathsf { C o n v 3 D } \left( \mathsf { \pmb { x } } , \mathsf { \pmb { W } } _ { q k v } \right)
$$

**改进MLP**：
$$
\mathsf { M L P } \left( \mathbf { x } \right) = \mathsf { G E L U } \left( \mathsf { C o n v 3 D } \left( \mathsf { G E L U } \left( \mathbf { x } \mathbf { W } _ { 1 } + b _ { 1 } \right) \right) \right) \mathbf { W } _ { 2 } + b _ { 2 }
$$

### Module 3: 并行多尺度融合（Parallel Multiscale Fusion）

**与U-Net的区别**：U-Net采用串行编码器-解码器结构，通过跳跃连接融合不同分辨率的特征。但下采样导致断层边缘信息不可逆丢失。FaultEdgeFormer采用并行架构，从Stage 2开始同时维护多个分辨率流，通过交换单元（Exchange Unit）实现跨分辨率信息融合。

**交换单元**：
- 下采样：3×3×3步长2卷积
- 上采样：三线性插值（trilinear interpolation）+ 1×1×1通道对齐卷积
- 恒等映射：当输入输出分辨率相同时

**多分辨率融合公式**（以三分辨率融合为例）：
$$
\pmb { \mathsf { F } } _ { r } ^ { o } = \varepsilon _ { 1 r } ( \mathsf { T } _ { 1 } ( \pmb { \mathsf { F } } _ { 1 } ^ { i } ) ) + \varepsilon _ { 2 r } ( \mathsf { T } _ { 2 } ( \pmb { \mathsf { F } } _ { 2 } ^ { i } ) ) + \varepsilon _ { 3 r } ( \mathsf { T } _ { 3 } ( \pmb { \mathsf { F } } _ { 3 } ^ { i } ) )
$$
其中 $T_x$ 为Transformer单元，$\varepsilon_{xr}(\cdot)$ 为交换单元（根据输入/输出分辨率索引决定下采样/上采样/恒等映射）。

## Mathematical Formulation / 数学表述

**平衡交叉熵损失（BCE Loss）**：
$$
\mathsf { B C E } ( y _ { i } , \hat { y _ { i } } ) = - \frac { 1 } { N } \sum _ { i } ^ { N } \big [ \alpha y _ { i } \log ( \hat { y _ { i } } ) + ( 1 - \alpha ) ( 1 - y _ { i } ) \log ( 1 - \hat { y _ { i } } ) \big ]
$$
其中 $\alpha$ 由负样本与正样本的比例决定。

**模型复杂度对比**：FaultEdgeFormer参数量1.34M，FLOPs 29.56G（96³输入），推理时间134.26ms。

# Dataset / 数据集

| Dataset | Size | Modality | Description |
|---------|------|----------|-------------|
| 合成训练集 | 500对 128×128×128 | 合成地震数据+断层标签 | 采用Wu et al. (2019, 2020)工作流生成，Ricker子波主频30-50Hz，SNR 5-25dB，包含正断层、逆断层、平行断层、相交断层 |
| 合成验证集 | 50对 128×128×128 | 合成地震数据+断层标签 | 同上 |
| 合成测试集 | 100对 128×128×128 | 合成地震数据+断层标签 | 独立于训练/验证集 |
| F3 Netherlands | 野外子体积 | 野外地震数据 | 荷兰近海F3区块，多方向断层，Y形断层 |
| Kerry New Zealand | 野外子体积 | 野外地震数据 | 新西兰Crown Minerals提供，浅层高发育断层，相邻断层对 |

# Experimental Setup / 实验设置

**训练配置**：
- 优化器：Adam，学习率0.0001
- 训练轮数：100 epochs
- Batch size：1
- 数据增强：随机旋转、随机翻转、随机裁剪至96×96×96
- 归一化：均值-方差归一化（mean-variance normalization）
- 验证集：50对（用于监控训练过程）

**对比方法**：
- CNN方法：FaultSeg3D（Wu et al. 2019）、Fault-Net（Dou et al. 2022）
- 中间版本：FaultEdge-Net（Fault-Net + 可训练Sobel卷积）
- Transformer方法：UNETR（Hatamizadeh et al. 2022）、Swin UNETR（Hatamizadeh et al. 2021）
- 消融变体：FaultEdgeFormer-v1/v2/v3

**评估指标**：Accuracy、Precision、Recall、F1、IoU（阈值0.5二值化）

**硬件**：RTX 4070（12GB VRAM）级别

# Results / 实验结果

## 合成测试集定量结果

| Method | Accuracy (%) | Precision (%) | Recall (%) | F1 (%) | IoU (%) |
|--------|-------------|---------------|-----------|--------|---------|
| Fault-Net (baseline) | 92.73 | 47.66 | 91.98 | 62.59 | 45.85 |
| FaultEdge-Net | 95.73 | 61.79 | 95.15 | 74.69 | 60.00 |
| **FaultEdgeFormer** | **96.19** | **64.65** | **95.35** | **76.57** | **62.37** |
| FaultEdgeFormer-v1 | 95.97 | 63.26 | 95.20 | 75.79 | 61.40 |
| FaultEdgeFormer-v2 | 95.18 | 58.85 | 93.95 | 72.11 | 56.88 |
| FaultEdgeFormer-v3 | 94.26 | 54.27 | 91.45 | 67.86 | 51.85 |

**关键发现**：
- FaultEdgeFormer在所有指标上均最优，F1=76.57%显著优于Fault-Net的62.59%
- 所有模型呈现高Recall低Precision特征，说明BCE Loss倾向于过分割
- 消融变体性能排序：FaultEdgeFormer > v1 > v2 > v3，验证了卷积投影和MLP深度卷积的有效性

## 噪声鲁棒性测试

| SNR | Fault-Net (F1) | FaultEdge-Net (F1) | FaultEdgeFormer (F1) |
|-----|---------------|-------------------|---------------------|
| 20 dB | 62.15% | 74.17% | **75.90%** |
| 15 dB | 61.03% | 73.13% | **74.91%** |
| 10 dB | 57.33% | 69.86% | **72.13%** |
| 5 dB | 46.48% | 61.20% | **62.82%** |
| 0 dB | 23.92% | **39.39%** | 35.66% |

**关键发现**：FaultEdgeFormer在5-20dB SNR下均最优。但在0 dB时FaultEdge-Net反超，说明Transformer模块对训练数据分布有更强的依赖性，训练集未包含SNR<5dB的数据。

## 模型复杂度对比

| Method | Parameters (M) | FLOPs (G, 96³) | Inference Time (ms) |
|--------|---------------|----------------|-------------------|
| FaultSeg3D | — | 57.35 | 24.67 |
| Fault-Net | 0.40 | 1.48 | 12.98 |
| UNETR | 92.78 | 73.50 | 49.36 |
| Swin UNETR | 6.96 | 38.61 | 55.40 |
| **FaultEdgeFormer** | **1.34** | **29.56** | **134.26** |
| FaultEdgeFormer-v1 | 1.30 | 28.64 | 91.89 |
| FaultEdgeFormer-v2 | 0.36 | 14.91 | 125.80 |
| FaultEdgeFormer-v3 | 0.32 | 13.99 | 83.82 |

**关键发现**：FaultEdgeFormer参数量仅1.34M（轻量级），但推理时间134.26ms远高于CNN方法（Fault-Net仅12.98ms），原因是高分辨率分支重复应用Transformer。

## 损失函数对比

| Loss Function | Accuracy (%) | Precision (%) | Recall (%) | F1 (%) | IoU (%) |
|--------------|-------------|---------------|-----------|--------|---------|
| BCE | 96.19 | 64.65 | 95.35 | 76.57 | 62.37 |
| Dice | **97.53** | **79.95** | 84.09 | **81.81** | **69.65** |
| Tversky (α=0.3, β=0.7) | 97.31 | 74.65 | 90.65 | 81.73 | 69.48 |

**关键发现**：Dice Loss和Tversky Loss显著优于BCE Loss（F1提升约5%）。Dice Loss精度最高但Recall最低（过分割减少但漏检增加），Tversky Loss（加重FN惩罚）在Recall和Precision之间取得了更好的平衡。

# Ablation Study / 消融实验

## 消融实验1：Swin Transformer改进组件

论文定义了4个组件进行消融：
- **C1**：可训练Sobel卷积（所有变体均使用）
- **C2**：W-MSA中的卷积投影
- **C3**：MLP中的深度可分离卷积
- **C4**：标准Swin Transformer（无改进）

| 变体 | C1 | C2 | C3 | C4 | F1 (%) | IoU (%) |
|------|:--:|:--:|:--:|:--:|:------:|:-------:|
| FaultEdgeFormer | ✓ | ✓ | ✓ | — | **76.57** | **62.37** |
| FaultEdgeFormer-v1 | ✓ | ✓ | — | — | 75.79 | 61.40 |
| FaultEdgeFormer-v2 | ✓ | — | ✓ | — | 72.11 | 56.88 |
| FaultEdgeFormer-v3 | ✓ | — | — | ✓ | 67.86 | 51.85 |

**结论**：
- C2（卷积投影）贡献 > C3（MLP深度卷积）
- 两者结合（C2+C3）最优
- 标准Swin Transformer（v3）性能最差

## 消融实验2：Sobel核数量

| 核数量 | 核组成 | F1 (%) | IoU (%) |
|:------:|--------|:------:|:-------:|
| 1 | Sz | 75.42 | 60.91 |
| 3 | Sz + Sx + Sy | 75.63 | 61.16 |
| 5 | + Sxy45 + Sxy135 | 76.21 | 61.90 |
| 7 | + Sxz45 + Sxz135 | 76.41 | 62.14 |
| 9 | + Syz45 + Syz135 | **76.57** | **62.37** |

**结论**：
- 3个核（Sz+Sx+Sy）相比1个核（Sz）有明显提升，因为增加了检测垂直断层的能力
- 3→5→7核提升有限，表明正交走向（0°, 90°）覆盖垂直倾角可能已足够，45°和135°走向可能引入特征冗余
- 9核达到最优，因为包含了45°倾角断层的正交走向，形成更完整的特征集

## 消融实验3：训练数据量减少的稳定性

随着训练样本从500减少到50，FaultEdgeFormer和v1（含卷积投影）的性能下降最慢，而v3（标准Swin Transformer）下降最快。说明**卷积投影增强了模型在有限数据下的稳定性**。

# Limitation / 局限性

1. **仅探索了监督学习**：未涉及半监督（Dou et al. 2024）或自监督方法，而半监督/自监督已成为断层检测的前沿方向。
2. **训练数据仅为合成数据**：未包含野外数据训练，论文指出加入野外数据训练对实际应用泛化至关重要。
3. **推理速度较慢**：虽然参数量少（1.34M），但推理时间（134.26ms/96³）远高于CNN方法（Fault-Net 12.98ms），高分辨率分支重复应用Transformer是主要原因。
4. **高Recall低Precision问题**：BCE Loss倾向于过分割，虽然Dice/Tversky Loss可缓解但非论文重点。
5. **Sobel核方向覆盖有限**：仅9个方向，论文指出更复杂的Gabor滤波器可能更有效。
6. **0dB SNR性能反转**：在极端噪声水平下，FaultEdgeFormer不如FaultEdge-Net，说明Transformer对训练数据分布依赖性更强。

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

1. **传统算子+深度学习融合**：将预定义的图像处理算子（Sobel、Gabor等）作为网络初始层，为网络注入先验知识，思路简洁且可推广到其他地震任务（如盐体检测、相分类）。

2. **CNN-Transformer混合设计原则**：在Transformer中引入卷积操作的位置至关重要——在自注意力之前（卷积投影）比在前馈网络中（MLP深度卷积）更有效。这一发现可指导其他地震AI任务的混合架构设计。

3. **并行多尺度架构**：相比U-Net的串行下采样，并行架构在整个训练过程中保持高分辨率表示，减少边缘信息丢失。这一设计思路可推广到任何需要精细边界分割的任务。

4. **轻量级模型设计**：1.34M参数在RTX 4070（12GB VRAM）上完全可运行，适合硬件受限的研究环境。

## Potential Improvements / 潜在改进方向

1. **替换Sobel为Gabor滤波器**：如论文讨论中所述，3D Gabor滤波器可通过控制频率和方向生成更多尺度和方向的算子，更适合检测不同倾角的断层。这是最直接的改进方向。

2. **引入半监督/自监督训练**：论文明确指出此局限，可尝试将FaultEdgeFormer与半监督方法（如FaultSSL）结合，利用未标注的野外数据提升泛化能力。

3. **加速推理**：论文提到可在高分辨率分支减少Transformer模块或仅放在低分辨率分支。这是一种精度-速度权衡，值得探索以匹配CNN的推理速度。

4. **替换损失函数为Tversky Loss**：消融实验显示Tversky Loss（α=0.3, β=0.7）在F1上比BCE Loss提升约5%，且比Dice Loss有更好的Recall-Precision平衡。可以直接替换。

5. **在SeisMark基准上评估**：SeisMark提供了含真实纹理的基准数据，可测试FaultEdgeFormer在域偏移下的鲁棒性，与V1/V2基线对比。

# Reproducibility Analysis / 复现性分析

## Official Implementation Verification / 官方实现验证

**Code Status**:
- [ ] Confirmed Available — verified the repository exists and is accessible
- [ ] Confirmed Missing — full-text verification confirms no code is provided
- [X] **Not Found Yet** — paper mentions code but URL not located
- [ ] Not Checked — agent has not verified (requires human follow-up)

**Evidence Location**: 论文未提及代码仓库或URL。数据可用性声明："The data that support the findings of this study can be obtained from the corresponding author upon request."

**Repository URL**: 未找到

**Framework**: 未明确说明（推测为PyTorch，基于Swin Transformer的3D实现）

**Checkpoint / Pre-trained Weights**: [ ] Available [X] Not mentioned [ ] Not applicable

**Last Repository Update**: N/A

**Code Quality Indicators**: N/A

**Verification Method**: 论文全文搜索，未发现代码仓库链接

## Missing Reproduction Components / 缺失的复现组件

| Component | Available? | Source Location | Notes |
|-----------|-----------|-----------------|-------|
| Source Code | [ ] Yes [X] No [ ] Partial | 未公开 | 需自行实现 |
| Dataset Access | [ ] Public [ ] Restricted [X] Private | 需向通讯作者请求 | 合成数据生成代码未公开 |
| Pre-trained Checkpoint | [ ] Yes [X] No [ ] N/A | — | 未提供 |
| Preprocessing Scripts | [ ] Yes [X] No [ ] Not mentioned | — | 需自行实现 |
| Hyperparameters | [X] Fully Listed [ ] Partially [ ] Missing | 论文正文 | Adam, lr=0.0001, 100 epochs, batch size=1 |
| Environment Specs | [ ] requirements.txt [ ] Docker [X] Not specified | — | 未指定CUDA/Python版本 |
| Random Seeds | [ ] Specified [X] Not specified | — | 未指定随机种子 |
| Train/Val/Test Split | [X] Defined [ ] Undefined | 500/50/100 | 比例明确 |
| Data Augmentation | [X] Described [ ] Vaguely [ ] Not described | 第2.5节 | 随机旋转、翻转、裁剪至96×96×96 |

## Reproduction Difficulty Assessment / 复现难度评估

- **Overall Difficulty**: [ ] Easy [ ] Moderate [X] Hard [ ] Impossible
- **Estimated Effort**: 2-4周（有经验的深度学习研究员）
- **Hardware Requirements**: 单GPU 12GB VRAM（RTX 4070，与论文一致）
- **Key Barriers**:
  1. 合成数据生成代码未公开，需自行实现Wu et al. (2019, 2020)工作流
  2. 模型架构细节（伪代码Algorithm 1）虽详细，但3D Swin Transformer的PyTorch实现有一定复杂度
  3. 无预训练权重，需从头训练
- **Workaround Options**:
  1. 使用Wu et al.的公开数据集（若有）或自行实现数据生成
  2. 野外数据F3和Kerry可公开获取，但需自行标注
- **RTX 4070 Compatibility**: [X] Runs fine [ ] May struggle [ ] Won't fit in VRAM
  - 1.34M参数，12GB VRAM完全可运行

## Reproducibility vs. Code Availability

- **Code Exists**: [ ] Yes [X] No
- **Paper Actually Reproducible**: [ ] Yes [X] Partially [ ] No
- **Gap Between Code Existence and Reproducibility**: 即使代码公开，合成数据生成代码未公开也是主要障碍。架构描述详细（含伪代码），但3D Swin Transformer的实现细节较多，需要一定的工程能力。

# Related Notes / 相关笔记

- Method: [[Edge-Enhanced Transformer]]
- Task: [[3D Seismic Fault Detection]]
- Dataset: [[F3 Netherlands]], [[Kerry New Zealand]]
- Benchmark: [[SeisMark Benchmark]]