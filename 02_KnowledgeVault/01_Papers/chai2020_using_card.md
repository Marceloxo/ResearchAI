---
title: "Using a Deep Neural Network and Transfer Learning to Bridge Scales for Seismic Phase Picking"
authors: [Chai, Maceira, Santos-Villalobos, Venkatakrishnan, Schoenball, Zhu, Beroza, Thurber]
year: 2020
venue: "Geophysical Research Letters"
task: ["Seismic Phase Picking", "Microseismic Monitoring"]
methods: ["PhaseNet", "Transfer Learning", "Adam Optimizer", "Double-Difference Tomography"]
datasets: ["EGS Collab SURF"]
metrics: ["Precision", "Recall", "F1 Score"]
code: "N/A"
importance: high
status: done
paper_type: research_article
tags: [seismic-phase-picking, transfer-learning, phasenet, deep-learning, microseismic, egs, tomography]
created: 2026-07-09
---

# Basic Information
- **Title**: Using a Deep Neural Network and Transfer Learning to Bridge Scales for Seismic Phase Picking
- **Authors**: Chengping Chai, Monica Maceira, Hector J. Santos-Villalobos, Singanallur V. Venkatakrishnan, Martin Schoenball, Weiqiang Zhu, Gregory C. Beroza, Clifford Thurber
- **Year**: 2020
- **Venue**: Geophysical Research Letters
- **DOI**: 10.1029/2020GL088651
- **Task**: Seismic Phase Picking (P and S waves)
- **Method**: PhaseNet + Transfer Learning
- **Dataset**: EGS Collab SURF Experiment 1
- **Code**: Not available

# Research Problem
Can a deep learning phase picker trained on kilometer-scale natural earthquake data be adapted to meter-scale hydraulic fracturing monitoring data? What is the minimum training data needed?

# Main Contribution
Demonstrates successful transfer learning across 3 orders of magnitude in spatial/temporal scales. Only 3,500 seismograms (0.45% of original training data) needed. TL model outperforms original PhaseNet by +10% precision/recall and matches human performance at 1,900x speed.

# Method Overview
Transfer-learned PhaseNet initialized with weights from original model, retrained on 3,478 carefully selected seismograms from EGS Collab SURF data. Bandpass filter (3-20kHz) applied before network input. Adam optimizer with lr=0.01, batch=20, 100 epochs.

# Dataset and Evaluation
- **EGS Collab SURF**: 69,444 waveform segments from 1,932 triggered microseismic events
- 35 seismic sensors (24 hydrophones + 12 accelerometers)
- 100kHz sampling rate, 60m monitoring wells
- Evaluation: precision, recall, F1 score with 5-fold cross-validation

# Why This Paper Matters
Shows that pre-trained DNN models can be adapted to completely different scales with minimal retraining data. This has implications for seismic image segmentation — a model trained on natural earthquake data could potentially be adapted for seismic image tasks with minimal labeled data.

# Limitations
- Results specific to meter-scale EGS system
- Requires some manual picks (3,500) for retraining
- TL model found fewer P picks than human (though higher quality)
- Generalizability to other scales/systems untested

# My Decision
- [x] Read deeply / 精读
- [ ] Keep reference
- [ ] Ignore

**Reason**: Strong transfer learning demonstration with practical implications for seismic AI. The key insight — 0.45% of training data suffices for successful transfer — is highly relevant to seismic image segmentation where labeled data is scarce.

# Related Knowledge
- Task: [[Seismic Phase Picking]]
- Method: [[PhaseNet]], [[Transfer Learning]]
- Dataset: [[EGS Collab SURF]]
