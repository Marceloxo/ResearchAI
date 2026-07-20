---
title: "A high-resolution seismic catalog for the 2021 MS6.4/MW6.1 Yangbi earthquake sequence, Yunnan, China: Application of AI picker and matched filter"
authors: [Yijian Zhou, Abhijit Ghosh, Lihua Fang, Han Yue, Shiyong Zhou, Youjin Su]
year: 2021
venue: "Earthquake Science"
task: [Seismic Cataloging, Earthquake Detection, Phase Picking]
method: [CERP Hybrid AI Picker, Matched Filter MESS, STA/LTA + Kurtosis]
dataset: [Yangbi earthquake sequence, Yunnan, China]
code_available: Not Checked
importance: medium
reading_status: keep-reference
tags: [yangbi-earthquake, seismic-catalog, ai-picker, matched-filter, cnn-rnn, yunnan]
created: 2026-07-18
---

# Basic Information / 基本信息

- **Title**: A high-resolution seismic catalog for the 2021 MS6.4/MW6.1 Yangbi earthquake sequence, Yunnan, China: Application of AI picker and matched filter
- **Authors**: Yijian Zhou, Abhijit Ghosh, Lihua Fang, Han Yue, Shiyong Zhou, Youjin Su
- **Year**: 2021
- **Venue**: Earthquake Science
- **Task**: High-resolution seismic cataloging of Yangbi earthquake sequence
- **Method**: CERP hybrid AI picker (CNN & RNN) + matched filter MESS
- **Dataset**: Yangbi earthquake sequence, Yunnan, China (May 2021)
- **Code**: Not Checked

# Research Problem / 研究问题

How can AI-based phase picking combined with matched filtering produce a high-resolution seismic catalog that captures the complete foreshock-mainshock-aftershock evolution of the Yangbi sequence?

# Main Contribution / 主要贡献

Developed a detection strategy combining AI picker (CERP) and matched filter (MESS) that produced 9,026 detections with 7,943 well-relocated events. Catalog reveals simple fault geometry in foreshocks/mainshock but complex conjugate fault activation in post-seismic period.

# Method Overview / 方法概述

1. **CERP training**: Initial detections from STA/LTA + Kurtosis method (PAL), then CERP trained on these detections
2. **Template construction**: Built ~4,000-event template set from CERP detections
3. **Matched filtering**: MESS augments initial detections and measures differential travel times via cross-correlation
4. **Relocation**: Precise hypocenter relocation produces final catalog

# Dataset and Evaluation / 数据集与评估

- **Time range**: May 1-28, 2021
- **Final catalog**: 7,943 well-relocated events
- **Detection**: 9,026 total detections
- **Evaluation**: Power-law frequency-magnitude distribution, spatiotemporal evolution analysis

# Why This Paper Matters / 为什么关注这篇论文

Provides a practical workflow for combining AI pickers with matched filtering — directly relevant to seismic phase picking research. The CERP method is described as "light-weight" and trainable with small data volumes, which aligns with RTX 4070 constraints.

# Limitations / 局限性

- Limited to one earthquake sequence (Yangbi)
- CERP training relies on STA/LTA initial detections — quality depends on PAL performance
- No comparison with other ML pickers (PhaseNet, EQTransformer) on same data
- Template set construction details not fully specified

# Reproducibility Status / 可复现性状态

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

## Data Status / 数据可用性

- [x] **Public dataset available**
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [ ] High [x] Medium [ ] Low

**Reason**: CERP and MESS may not be publicly released. Yangbi seismic data should be accessible from Chinese seismic networks.

# My Decision / 我的决定

- [ ] Read deeply / 精读
- [x] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason**: Practical AI picker workflow demonstrated on a well-recorded sequence. Useful reference for combining ML picking with matched filtering.

# Related Knowledge / 相关知识链接

- Task: [[Seismic Phase Picking]], [[Earthquake Cataloging]]
- Method: [[CERP]], [[Matched Filter]], [[MESS]]
- Dataset: [[Yangbi Earthquake Sequence]]
