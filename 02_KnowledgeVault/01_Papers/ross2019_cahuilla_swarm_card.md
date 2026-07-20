---
title: "3D fault architecture controls the dynamism of earthquake swarms"
authors: [Zachary E. Ross, Elizabeth S. Cochran, Daniel T. Trugman, Jonathan D. Smith]
year: 2019
venue: "Geophysics"
task: [Earthquake Swarm Analysis, Fault Architecture Imaging, Fluid-Migration Studies]
method: [Deep Learning Detection, Hypocenter Relocation, 3D Seismicity Imaging]
dataset: [Cahuilla Southern California 2016-2019 swarm]
code_available: Not Checked
importance: medium
reading_status: keep-reference
tags: [earthquake-swarm, 3d-fault-architecture, cahuilla, fluid-migration, deep-learning-detection, southern-california]
created: 2026-07-18
---

# Basic Information / 基本信息

- **Title**: 3D fault architecture controls the dynamism of earthquake swarms
- **Authors**: Zachary E. Ross, Elizabeth S. Cochran, Daniel T. Trugman, Jonathan D. Smith
- **Year**: 2019
- **Venue**: Geophysics
- **Task**: Imaging 3D fault architecture controlling earthquake swarm evolution
- **Method**: Deep learning earthquake detection + hypocenter relocation to image fault zone hosting 4-year-long swarm
- **Dataset**: Cahuilla, Southern California (2016-2019), 22,000+ events, Mw 0.7-4.4
- **Code**: Not Checked

# Research Problem / 研究问题

How does 3D fault architecture control the dynamic evolution of earthquake swarms? Why do swarms exhibit vibrant, nonstationary patterns incompatible with 2D fault models?

# Main Contribution / 主要贡献

Imaged a rich 3D fault structure controlling swarm evolution near Cahuilla. Found that fluids are naturally injected from below, diffuse through strike-parallel channels, and trigger earthquakes. A permeability barrier initially limits up-dip migration but is ultimately circumvented, enabling fundamentally different fluid migration in shallower sections.

# Method Overview / 方法概述
1. Applied deep learning earthquake detection algorithm to Cahuilla data
2. Produced catalog of 22,000+ events (Mw 0.7-4.4)
3. Relocated events to image 3D fault geometry
4. Inferred fluid migration patterns from seismicity distribution
5. Identified nonplanar right-lateral strike-slip fault surface dipping 70°-80° NE

# Dataset and Evaluation / 数据集与评估

- **Cahuilla swarm**: 4-year sequence (2016-2019)
- **Events**: 22,000+ relocated earthquakes
- **Magnitude range**: Mw 0.7 - 4.4
- **Fault geometry**: Single nonplanar surface, 70°-80° NE dip, tens of meters thick in fault-normal direction

# Why This Paper Matters / 为什么关注篇论文

Demonstrates how deep learning detection enables high-resolution 3D fault imaging. The fluid-migration framework for swarm evolution is conceptually relevant to understanding seismicity patterns in monitored regions. Applicable to understanding complex fault systems.

# Limitations / 局限性

- Deep learning detection algorithm details not fully specified
- Cahuilla-specific findings may not generalize to all swarm types
- Fluid migration inference relies on seismicity patterns alone
- No direct fluid pressure measurements

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

**Reason**: Cahuilla data should be publicly accessible. Detection algorithm details may limit reproducibility.

# My Decision / 我的决定

- [ ] Read deeply / 精读
- [x] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason**: Interesting 3D fault architecture study. Useful for understanding swarm dynamics and fluid-triggered seismicity.

# Related Knowledge / 相关知识链接

- Task: [[Earthquake Swarm Analysis]], [[Fault Architecture Imaging]]
- Method: [[Deep Learning Detection]]
- Dataset: [[Cahuilla Swarm]]
