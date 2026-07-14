---
title: "SNUNet-CD: A Densely Connected Siamese Network for Change Detection of VHR Images"
authors: [Fang et al.]
year: 2022
venue: "ISPRS Journal of Photogrammetry and Remote Sensing"
task: [Change Detection]
method: [SNUNet-CD, Siamese Network, Densely Connected, Bi-directional LSTM]
dataset: [LEVIR-CD, WHU-CD]
code_available: Not Found Yet
importance: high
reading_status: done
tags: [change-detection, snunet, siamese, vhr, remote-sensing, fang]
created: 2026-07-10
---

# Basic Information

- **Title**: SNUNet-CD: A Densely Connected Siamese Network for Change Detection of VHR Images
- **Authors**: Fang et al.
- **Year**: 2022
- **Venue**: ISPRS Journal of Photogrammetry and Remote Sensing
- **Task**: Change Detection in Very High Resolution (VHR) Remote Sensing Images
- **Method**: SNUNet-CD (Densely Connected Siamese Network with Bi-directional LSTM)
- **Dataset**: LEVIR-CD, WHU-CD
- **Code**: Not Found Yet

# Research Problem

> Change detection is sensitive to original pixel utilization. Existing methods struggle with fine-grained change boundaries in VHR imagery and lose contextual information through aggressive downsampling.

# Main Contribution

> Proposes SNUNet-CD: a densely connected siamese network that combines multi-scale feature extraction with bi-directional LSTM for modeling long-range spatial dependencies in bi-temporal image pairs.

# Method Overview

> Dual-branch siamese encoder extracts multi-scale features from bi-temporal images. Dense skip connections preserve fine-grained spatial details. Bi-directional LSTM models long-range spatial dependencies in flattened feature sequences. Decoder fuses multi-scale features with attention-weighted fusion for pixel-level change prediction.

# Dataset and Evaluation

- **LEVIR-CD**: 637 image pairs (1024x1024), urban building changes
- **WHU-CD**: Aerial image pairs with dense change annotations
- **Metrics**: F1 Score, Precision, Recall, Overall Accuracy
- **Baseline**: FC-Siam-conc, FC-Siam-diff, BIT, STANet

# Why This Paper Matters

> SNUNet-CD demonstrates that densely connected siamese architectures with LSTM-based spatial modeling achieve state-of-the-art change detection. The multi-scale feature fusion approach is directly transferable to seismic image segmentation tasks where multi-resolution feature preservation is critical.

# Limitations

> Designed for optical remote sensing — domain gap with seismic imagery not discussed. Bi-directional LSTM adds computational overhead. No discussion of RTX 4070 compatibility.

# Reproducibility Status

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: <!-- Not located in full text -->

## Data Status

- [x] **Public dataset available** — LEVIR-CD and WHU-CD are publicly available
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

## Reproduction Feasibility

**Overall Assessment**: [ ] High [x] Medium [ ] Low

**Reason**: Public datasets, clear architecture. LSTM components are lightweight. Should run on RTX 4070.

# Zotero

**Status**: Imported
**Item Key**: 6VTKJ8W2

# My Decision

- [x] Read deeply
- [ ] Keep reference
- [ ] Ignore

**Reason**: Strong methodological contribution. Densely connected siamese architecture with multi-scale fusion is highly relevant to seismic image segmentation. Worth deep analysis for architecture transfer.

# Related Knowledge

- Task: [[Seismic Image Segmentation]], [[Fault Segmentation]]
- Method: [[U-Net]], [[CNN]], [[Attention Mechanism]], [[Transformer]]
- Dataset: [[F3 Netherlands]], [[Marmousi]]
