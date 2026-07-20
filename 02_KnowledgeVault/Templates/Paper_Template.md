---
title: "{{title}}"
authors: [{{authors}}]
year: {{year}}
venue: "{{venue}}"
task: [{{task}}]
methods: [{{methods}}]
datasets: [{{datasets}}]
metrics: [{{metrics}}]
code: "{{code}}"
importance: {{importance}}
status: {{status}}
paper_type: research_article  # research_article | survey | review | benchmark
tags: []
created: {{date}}
---

# Paper Type / 论文类型

<!-- 明确论文类型，不同类型采用不同分析方式：
- research_article: 提出新方法/新模型 → 重点分析方法、实验、结果
- survey/review: 综述现有工作 → 重点分析taxonomy、coverage、gaps
- benchmark: 提供基准测试 → 重点分析任务定义、评估指标、基线方法 -->

Type: {{paper_type}}

# One Sentence Summary / 一句话总结

<!-- 用一句话概括这篇论文做了什么、怎么做的、效果如何？ -->

# Research Background / 研究背景

<!-- 论文解决什么问题？为什么这个问题重要？ -->

# Problem Definition / 问题定义

- **Input / 输入**:
- **Output / 输出**:

# Motivation / 研究动机

<!-- 已有方法的不足是什么？论文针对什么痛点？ -->

# Main Contributions / 主要贡献

1. 
2. 
3. 

# Method / 方法

## Overall Framework / 整体框架

<!-- 系统整体架构描述 -->

## Key Modules / 关键模块

### Module 1: {{module_name}}

<!-- 描述 -->

### Module 2: {{module_name}}

<!-- 描述 -->

## Mathematical Formulation / 数学表述

<!-- 核心公式及解释 -->

$$

$$

# Dataset / 数据集

| Dataset | Size | Modality | Description |
|---|---|---|---|
| | | | |

# Experimental Setup / 实验设置

<!-- 训练配置、超参数、对比方法等 -->

# Results / 实验结果

<!-- 关键结果表格/图表分析 -->

# Ablation Study / 消融实验

<!-- 各模块的有效性验证 -->

# Limitation / 局限性 <!-- 论文自己承认的局限 + 你看到的局限 -->

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

<!-- 哪些思路可以用到自己的研究？ -->

## Potential Improvements / 潜在改进方向

<!-- 如果你来做，会怎么改进？ -->


# Reproducibility Analysis / 复现性分析

## Official Implementation Verification / 官方实现验证

> 区分「代码存在」与「论文可复现」。代码存在不等于可复现。

**Code Status**:
- [ ] **Confirmed Available** — verified the repository exists and is accessible
- [ ] **Confirmed Missing** — full-text verification confirms no code is provided
- [ ] **Not Found Yet** — paper mentions code but URL not located
- [ ] **Not Checked** — agent has not verified (requires human follow-up)

**Evidence Location**: <!-- where in the paper was code availability mentioned? -->

**Repository URL**: <!-- link — verify it is reachable -->

**Framework**: <!-- PyTorch / TensorFlow / etc. -->

**Checkpoint / Pre-trained Weights**: [ ] Available [ ] Not mentioned [ ] Not applicable

**Last Repository Update**: <!-- commit date or "unknown" -->

**Code Quality Indicators**: <!-- stars, forks, issues responsiveness, documentation quality -->

**Verification Method**: <!-- how was this confirmed? e.g. "URL reachable", "repo cloned", "paper text only" -->

## Missing Reproduction Components / 缺失的复现组件

> 即使代码公开，也可能缺少某些关键组件导致无法复现。逐项评估。

| Component | Available? | Source Location | Notes |
|---|---|---|---|
| Source Code | [ ] Yes [ ] No [ ] Partial | <!-- repo/file path --> | |
| Dataset Access | [ ] Public [ ] Restricted [ ] Private | <!-- URL or access method --> | |
| Pre-trained Checkpoint | [ ] Yes [ ] No [ ] N/A | <!-- URL if available --> | |
| Preprocessing Scripts | [ ] Yes [ ] No [ ] Not mentioned | <!-- repo/file path --> | |
| Hyperparameters | [ ] Fully Listed [ ] Partially [ ] Missing | <!-- which params are missing? --> | |
| Environment Specs | [ ] requirements.txt [ ] Docker [ ] Not specified | <!-- CUDA/Python versions --> | |
| Random Seeds | [ ] Specified [ ] Not specified | | |
| Train/Val/Test Split | [ ] Defined [ ] Undefined | <!-- split ratio if known --> | |
| Data Augmentation | [ ] Described [ ] Vaguely [ ] Not described | | |

## Reproduction Difficulty Assessment / 复现难度评估

- **Overall Difficulty**: [ ] Easy [ ] Moderate [ ] Hard [ ] Impossible
- **Estimated Effort**: <!-- hours/days needed for a skilled researcher -->
- **Hardware Requirements**: <!-- GPU VRAM, RAM, storage needed -->
- **Key Barriers**: <!-- what makes this hard to reproduce? -->
- **Workaround Options**: <!-- how to work around missing details? -->
- **RTX 4070 Compatibility**: [ ] Runs fine [ ] May struggle [ ] Won't fit in VRAM

## Reproducibility vs. Code Availability

> **Important distinction**: Code existing $\neq$ paper is reproducible.

- **Code Exists**: [ ] Yes [ ] No
- **Paper Actually Reproducible**: [ ] Yes [ ] Partially [ ] No
- **Gap Between Code Existence and Reproducibility**: <!-- explain if code exists but paper is not reproducible -->
# Related Notes / 相关笔记

- Method: [[{{methods}}]]
- Task: [[{{task}}]]
- Dataset: [[{{datasets}}]]




