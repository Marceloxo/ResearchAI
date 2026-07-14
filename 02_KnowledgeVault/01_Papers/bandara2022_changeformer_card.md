---
title: "A Transformer-Based Siamese Network for Change Detection"
authors: [Bandara and Patel]
year: 2022
venue: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops"
task: [Change Detection]
method: [ChangeFormer, Transformer-Based Siamese Network, Bi-Temporal Feature Extraction]
dataset: [LEVIR-CD, WHU-CD, NJU-RS3CD]
code_available: Not Found Yet
importance: high
reading_status: done
tags: [change-detection, transformer, siamese, bandara, changeformer]
created: 2026-07-10
---

# Basic Information

- **Title**: A Transformer-Based Siamese Network for Change Detection
- **Authors**: Umar Iqbal Bandara and Vishal M. Patel
- **Year**: 2022
- **Venue**: IEEE/CVF CVPR Workshops
- **Task**: Change Detection from Co-Registered Bi-Temporal Remote Sensing Images
- **Method**: ChangeFormer — Transformer-based Siamese Network with bi-temporal feature extraction and change modeling
- **Dataset**: LEVIR-CD, WHU-CD, NJU-RS3CD
- **Code**: Not Found Yet

# Research Problem

> Recent change detection frameworks based on fully convolutional networks (ConvNets) struggle to model long-range spatial dependencies between bi-temporal image pairs. Transformers offer superior discriminative ability but adapting them for CD requires careful architectural design.

# Main Contribution

> Proposes ChangeFormer, a transformer-based siamese network that extracts bi-temporal features using dual transformer encoders and models change through a novel change modeling block. Achieves state-of-the-art results on multiple CD benchmarks.

# Method Overview

> Dual-encoder siamese architecture with transformer blocks for bi-temporal feature extraction. Change modeling block computes cross-temporal attention between encoded features. Decoder produces pixel-level change maps. Designed to capture long-range dependencies that ConvNets miss.

# Dataset and Evaluation

- **LEVIR-CD**: Urban building change, 637 image pairs
- **WHU-CD**: Aerial image change detection
- **NJU-RS3CD**: Multi-scene remote sensing change detection
- **Metrics**: F1 Score, Precision, Recall, OA
- **Baselines**: FC-Siam-conc, FC-Siam-diff, BIT, STANet, SNUNet-CD

# Why This Paper Matters

> ChangeFormer is a foundational transformer-based CD method. The siamese transformer architecture with cross-temporal attention is directly applicable to seismic change detection scenarios (pre/post earthquake damage assessment, temporal seismic monitoring). Strong methodological contribution to the transformer-CD paradigm.

# Limitations

> Transformer-based methods are computationally intensive — may exceed RTX 4070 VRAM for large bi-temporal image pairs. Paper focuses on optical remote sensing; seismic domain transfer requires investigation.

# Reproducibility Status

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: <!-- Not located in full text -->

## Data Status

- [x] **Public dataset available** — LEVIR-CD, WHU-CD, NJU-RS3CD are all publicly available
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

## Reproduction Feasibility

**Overall Assessment**: [ ] High [x] Medium [ ] Low

**Reason**: Public datasets, clear architecture. Transformer components may require careful VRAM management on RTX 4070. Patch-based processing recommended.

# Zotero

**Status**: Imported
**Item Key**: 2XQFZKZN

# My Decision

- [x] Read deeply
- [ ] Keep reference
- [ ] Ignore

**Reason**: Foundational transformer-based change detection method. Siamese architecture with cross-temporal attention is highly relevant to seismic AI — particularly for pre/post-event analysis. Strong candidate for Level 2 deep analysis.

# Related Knowledge

- Task: [[Seismic Image Segmentation]], [[Fault Segmentation]]
- Method: [[Transformer]], [[Vision Transformer]], [[Attention Mechanism]], [[CNN]]
- Dataset: [[F3 Netherlands]], [[Marmousi]]
