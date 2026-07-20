---
task_name: "Seismic Phase Picking"
domain: "Seismic Monitoring / Earthquake Detection"
related_methods: [GENIE, Multi-task Learning, PhaseNet, PLAN, Transfer Learning]
input: "Three-component seismograms"
output: "P-wave and S-wave arrival times"
metrics: ["Precision", "Recall", "F1 Score"]
tags: [seismic-phase-picking, task]
created: 2026-07-09
---

# Task Definition
Automatic detection of P-wave and S-wave arrival times from three-component seismogram recordings.

# Problem Formulation
- **Given**: Three-component seismic waveform data (typically 3-component, 100Hz sampled)
- **Goal**: Predict arrival times of P and S waves with sub-sample accuracy

# Input Data
- **Modality**: Three-component seismograms (horizontal X, Y + vertical Z)
- **Typical Duration**: 30 seconds (natural earthquakes) to 30 milliseconds (microseismic)
- **Sampling Rate**: 100Hz (natural) to 100kHz (microseismic) — spans 3 orders of magnitude

# Output
- **Type**: Continuous time values (arrival times)
- **Format**: P-wave pick time, S-wave pick time
- **Accuracy**: Sub-sample (millisecond) precision desired

# Evaluation Metrics
| Metric | Formula | Description |
|---|---|---|
| Precision | TP / (TP + FP) | Fraction of predicted picks that are correct |
| Recall | TP / (TP + FN) | Fraction of actual picks that were detected |
| F1 Score | 2 × P × R / (P + R) | Harmonic mean of precision and recall |

# Common Methods
| Method Family | Representative Work | Key Idea | Performance |
|---|---|---|---|
| STA/LTA | Allen (1978) | Ratio of short-term to long-term energy | Moderate |
| AR-AIC | Sleeman & van Eck (1999) | Auto-regression + Akaike criterion | Moderate |
| PhaseNet | Zhu & Beroza (2018) | CNN-based deep learning | High |
| TL-PhaseNet | Chai et al. (2020) | Transfer learning adaptation | Higher |

## Related Methods
- [[PhaseNet]] — Deep learning based seismic phase picking framework.
- [[PLAN]] — Multi-task GNN framework including phase picking, association and location.
- [[GENIE]] — Graph neural network framework related to phase association and phase processing.
- [[Multi-task Learning]] — Joint optimization strategy for seismic monitoring tasks.

# Challenges
- Scale mismatch between training and target data
- Noisy data environments
- Need for labeled training data
- Real-time processing requirements

# Benchmark Datasets
| Dataset | Size | Year | Notes |
|---|---|---|---|
| [[EGS Collab SURF]] | 69,444 waveforms | 2020 | Meter-scale hydraulic fracturing |

# Open Problems
- Can transfer learning work without ANY manual picks?
- Can a single model handle multiple scales simultaneously?
- How to quantify per-pick uncertainty?
