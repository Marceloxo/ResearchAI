---
experiment_id: "exp_chai2020_phase_picking"
project: "EGS Collab SURF"
task: "Seismic Phase Picking"
dataset: "EGS Collab SURF"
method: "PhaseNet (TL)"
date: 2020
status: completed
tags: [seismic-phase-picking, transfer-learning, experiment]
created: 2026-07-09
---

# Experiment Objective
Validate that a PhaseNet model trained on km-scale natural earthquake data can be adapted to m-scale hydraulic fracturing data via transfer learning, and compare performance against traditional pickers and human analysts.

# Hypothesis
A transfer-learned PhaseNet model, retrained with a small subset of target-domain data, will achieve human-level picking accuracy while running orders of magnitude faster.

# Configuration
- **Model**: [[PhaseNet]] initialized with original weights
- **Dataset**: [[EGS Collab SURF]] 鈥?69,444 waveforms from 1,932 events
- **Task**: [[Seismic Phase Picking]] 鈥?P and S wave arrival times
- **Hyperparameters**:
  - Learning rate: 0.01
  - Batch size: 20
  - Epochs: 100
  - Optimizer: Adam
  - Loss: Gaussian distribution (std=0.1ms) around manual picks
- **Preprocessing**: Bandpass filter 3-20kHz
- **Hardware**: 32 Intel Xeon cores (training), 6 Intel i9 cores (inference)
- **Code Location**: Not available

# Results

## Quantitative Results
| Metric | AR Picker | Original PhaseNet | TL Model | Human Expert |
|---|---|---|---|---|
| P Precision | Low | Good | +10% vs PhaseNet | Baseline |
| S Precision | Low | Good | +10% vs PhaseNet | Baseline |
| P Recall | Low | Good | +10% vs PhaseNet | Baseline |
| S Recall | Low | Good | +10% vs PhaseNet | Baseline |
| Speed | Slow | 1,900x human | 1,900x human | Baseline |

Key numbers:
- TL model: 12,050 P picks, 13,297 S picks
- Human: 18,543 P picks, 8,935 S picks
- TL found 32% fewer P picks but 48% more S picks
- Average location uncertainty: 0.2m

## Qualitative Results
- TL model corrects some human errors
- TL model skips difficult-to-pick signals (more for P than S)
- TL-derived picks lead to tighter fracture clustering
- S-wave constrained volume: +133% with TL vs manual

# Comparison
| Method | P Precision | S Precision | Notes |
|---|---|---|---|
| TL Model (Ours) | High | High | +10% over original PhaseNet |
| Original PhaseNet | Good | Good | Baseline DNN |
| AR Picker | Low | Low | Traditional |
| Human Expert | Baseline | Baseline | 3 analysts averaged |

# Ablation
| Variant | Result | Conclusion |
|---|---|---|
| Full TL model | Best performance | Complete fine-tuning works |
| Filtered data | Better than raw | Preprocessing matters |
| 5-fold CV | Significant improvement | Results statistically robust |
| More training data | F1 improves monotonically | Data quantity helps |

# Analysis
The TL model's superior S-wave picking (+48% more picks than human) likely reflects the model's ability to detect subtle signals that humans miss. The fewer P picks (鈭?2%) but higher quality suggests the model is more conservative and selective, removing low-quality picks. This trade-off is beneficial because double-difference tomography with TL picks shows better fracture geometry.

The key insight: **0.45% of original training data (3,500 waveforms) was sufficient for successful transfer across 3 orders of magnitude in scale**. This suggests pre-trained models are highly adaptable with minimal retraining.

# Conclusion
Transfer learning successfully bridged the scale gap between natural earthquake data and hydraulic fracturing data. The TL model outperforms both traditional pickers and the original PhaseNet, matches human performance, and runs 1,900x faster. The TADT workflow (TL + double-difference tomography) produces better seismic catalogs and velocity models than manual workflows.

# Related
- Method: [[PhaseNet]], [[Transfer Learning]]
- Dataset: [[EGS Collab SURF]]
- Task: [[Seismic Phase Picking]]
- Paper: [[chai2020_using_note]]

