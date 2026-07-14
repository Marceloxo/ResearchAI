---
title: "Hybrid lightweight transformer for efficient landslide change detection in remote sensing imagery"
authors: [Yadav et al.]
year: 2025
venue: "Journal"
task: [Landslide Change Detection]
method: [CDCTNet, Hybrid Transformer, Convolutional Encoder, Vision Transformer, Local Grouped Self-Attention, Attention Gate, Gated Convolutional Decoder]
dataset: ["Remote sensing imagery", "UAV dataset"]
code_available: Not Found Yet
importance: medium
reading_status: done
tags: [landslide, change-detection, transformer, lightweight, yadav]
created: 2026-07-10
---

# Basic Information

- **Title**: Hybrid lightweight transformer for efficient landslide change detection in remote sensing imagery
- **Authors**: Yadav et al.
- **Year**: 2025
- **Venue**: Journal
- **Task**: Landslide Change Detection in Remote Sensing Imagery
- **Method**: CDCTNet — Convolution-Transformer Change Detection Network combining convolutional encoder blocks with vision transformer and locally grouped self-attention
- **Dataset**: Remote sensing imagery, UAV dataset
- **Code**: Not Found Yet

# Research Problem

> Change detection for landslide monitoring requires efficient models that can process high-resolution remote sensing imagery while maintaining computational feasibility. Pure transformers are too heavy; pure CNNs lack global context modeling.

# Main Contribution

> Proposes CDCTNet, a hybrid lightweight transformer that combines convolutional encoder blocks with vision transformer layers and locally grouped self-attention for efficient landslide change detection. Includes ablation studies, explainability analysis, and UAV dataset evaluation.

# Method Overview

> CDCTNet architecture: Convolutional encoder block for local feature extraction → Vision transformer with locally grouped self-attention for global context → Attention gates for feature refinement → Gated convolutional decoder for pixel-level change prediction. Designed for computational efficiency with lightweight transformer components.

# Dataset and Evaluation

- **Remote sensing imagery**: Multi-temporal satellite/aerial data
- **UAV dataset**: Drone-based change detection evaluation
- **Metrics**: F1 Score, Precision, Recall, IoU
- **Experiments**: SOTA comparison, ablation study, hyperparameter sensitivity, computational efficiency analysis

# Why This Paper Matters

> Lightweight transformer design is directly relevant to RTX 4070 constraints. The hybrid CNN-Transformer approach balances local feature extraction with global context — a pattern useful for seismic image segmentation where both fine detail and large-scale geological context matter.

# Limitations

> Focused on landslide change detection — seismic domain transfer not discussed. UAV dataset evaluation may not generalize to satellite-scale seismic data.

# Reproducibility Status

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: <!-- Not located in full text -->

## Data Status

- [x] **Public dataset available** — Remote sensing and UAV datasets likely public
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

## Reproduction Feasibility

**Overall Assessment**: [x] High [ ] Medium [ ] Low

**Reason**: Lightweight transformer design explicitly targets efficiency. CNN backbone is standard. Should run on RTX 4070.

# Zotero

**Status**: Imported
**Item Key**: 3ZLDQRA3

# My Decision

- [x] Read deeply
- [ ] Keep reference
- [ ] Ignore

**Reason**: Lightweight transformer architecture is highly relevant to RTX 4070 constraints. Hybrid CNN-Transformer design pattern directly transferable to seismic image segmentation. Strong candidate for deep analysis.

# Related Knowledge

- Task: [[Seismic Image Segmentation]], [[Fault Segmentation]]
- Method: [[Transformer]], [[Vision Transformer]], [[CNN]], [[Attention Mechanism]]
