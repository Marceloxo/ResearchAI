---
title: "A deeply supervised image fusion network for change detection in high resolution bi-temporal remote sensing images"
authors: [Zhang et al.]
year: 2020
venue: "Remote Sensing"
task: [Change Detection]
method: [Deeply Supervised Image Fusion Network, DDN, Deep Supervision, Attention Fusion]
dataset: [WHU-CD, GID-CD]
code_available: Not Found Yet
importance: medium
reading_status: deep-read
tags: [change-detection, deep-supervision, image-fusion, remote-sensing, zhang]
created: 2026-07-10
---

# Basic Information

- **Title**: A deeply supervised image fusion network for change detection in high resolution bi-temporal remote sensing images
- **Authors**: Zhang et al.
- **Year**: 2020
- **Venue**: Remote Sensing
- **Task**: Change Detection in High Resolution Bi-temporal Remote Sensing Images
- **Method**: Deeply Supervised Image Fusion Network (DDN) with attention-based feature fusion
- **Dataset**: WHU-CD, GID-CD
- **Code**: Not Found Yet

# Research Problem

> Traditional change detection methods lose fine details through deep network layers. Deep features acquire large receptive fields but sacrifice spatial precision needed for accurate change boundary delineation.

# Main Contribution

> Proposes a deeply supervised network with attention-based feature fusion that integrates multi-scale features from different network depths. Deep supervision at multiple decoder levels provides auxiliary gradients for better feature learning.

# Method Overview

> Two-stream CNN encoders process bi-temporal images independently. Attention module fuses features from corresponding encoder layers. Deeply supervised decoder produces intermediate change maps at multiple scales. Multi-loss training combines primary and auxiliary supervision signals for improved boundary accuracy.

# Dataset and Evaluation

- **WHU-CD**: Aerial image change detection dataset
- **GID-CD**: Large-scale aerial image dataset
- **Metrics**: F1 Score, Precision, Recall
- **Baselines**: FC-Siam-conc, FC-Siam-diff, FCN-PP

# Why This Paper Matters

> Deep supervision is a general technique applicable to seismic image segmentation. The attention-based feature fusion approach could improve multi-resolution seismic feature integration. Auxiliary loss at multiple scales helps preserve fine boundaries — critical for fault line detection.

# Limitations

> Focused on optical remote sensing — seismic domain transfer not addressed. Deep supervision adds training complexity. No ablation study on individual supervision levels.

# Reproducibility Status

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: <!-- Not located in full text -->

## Data Status

- [x] **Public dataset available** — WHU-CD is publicly available
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

## Reproduction Feasibility

**Overall Assessment**: [x] High [ ] Medium [ ] Low

**Reason**: CNN-based architecture, standard deep supervision technique. Lightweight enough for RTX 4070.

# Zotero

**Status**: Imported
**Item Key**: UL36XRSA

# My Decision

- [x] Read deeply
- [x] Keep reference
- [ ] Ignore

**Reason**: Deep supervision technique is valuable but the paper focuses on optical RS change detection. The attention fusion concept is transferable to seismic image segmentation. Keep as reference for architecture design patterns.

# Related Knowledge

- Task: [[Seismic Image Segmentation]]
- Method: [[U-Net]], [[CNN]], [[Attention Mechanism]]
