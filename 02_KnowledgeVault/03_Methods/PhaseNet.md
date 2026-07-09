---
method_name: "PhaseNet"
category: "CNN-based Phase Picker"
application: ["Seismic Phase Picking", "Microseismic Monitoring"]
related_tasks: ["Seismic Phase Picking", "Event Detection"]
tags: [phasenet, cnn, phase-picking, deep-learning]
created: 2026-07-09
---

# Definition
PhaseNet is a deep neural network for automatic seismic phase picking (P and S waves) trained on natural earthquake data.

# Core Idea
Uses a CNN architecture to predict arrival times of seismic phases from three-component seismograms. Trained on 0.7M seismograms from northern California natural earthquakes.

# Architecture / Formulation
- **Input**: 3-component seismograms (30s long, 100Hz sampled)
- **Architecture**: CNN with multiple convolutional layers
- **Output**: P-wave and S-wave arrival time probability distributions
- **Training**: Supervised learning with manual picks as ground truth

# Advantages
- High accuracy on natural earthquake data
- Fast inference (suitable for real-time monitoring)
- Handles noisy data reasonably well
- Pre-trained models available for transfer learning

# Limitations
- Performance degrades when applied to data significantly different from training domain
- Requires manual picks for retraining in new domains
- Trained on km-scale data 鈥?may not generalize to m-scale without adaptation

# Typical Applications
| Task | Description | Representative Work |
|---|---|---|
| Seismic Phase Picking | P and S wave arrival time detection | Zhu & Beroza (2018) |
| Microseismic Monitoring | Hydraulic fracturing event detection | Chai et al. (2020) |
| Earthquake Detection | Natural earthquake phase picking | Multiple follow-up studies |

# Related Papers
- [[chai2020_using_note]] 鈥?Transfer learning application of PhaseNet

# Related Methods
- [[AR Picker]] 鈥?Traditional automatic picker (ObsPy implementation)
- [[STA/LTA]] 鈥?Short-term average/long-term ratio picker
- [[Transfer Learning]] 鈥?General framework used to adapt PhaseNet

