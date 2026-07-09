# Paper Type: Research Article
# Title: Using a Deep Neural Network and Transfer Learning to Bridge Scales for Seismic Phase Picking
# Authors: Chai et al. (2020)
# Venue: Geophysical Research Letters
# Type: research_article

# One Sentence Summary
A transfer-learned PhaseNet model, retrained with only 3,500 seismograms (0.45% of original training data), achieves human-level seismic phase picking accuracy on meter-scale EGS Collab data while running 1,900x faster than human analysts.

# Research Background
Seismic monitoring is critical for oil/gas, mining, CCS, and geothermal industries. Accurate earthquake locations depend on precise seismic phase picking, which is labor-intensive and time-consuming. Traditional auto-pickers (STA/LTA, AR-AIC) require intensive human refinement and don't benefit from previous picks. Deep learning-based pickers (PhaseNet, etc.) show remarkable accuracy for natural earthquake data but whether they work for industrial/small-scale monitoring is unclear.

# Problem Definition
- **Input**: Three-component seismograms (P and S waves)
- **Output**: P-wave and S-wave arrival time picks

# Motivation
PhaseNet was trained on kilometer-scale natural earthquake data (0.7M seismograms, 100Hz sampling, km-scale source-sensor distance). The EGS Collab data is meter-scale (100kHz sampling, m-scale distance) — three orders of magnitude difference. Can a model trained on one scale work on another? If not, how much retraining data is needed?

# Main Contributions
1. Demonstrated successful transfer learning of PhaseNet across three orders of magnitude in spatial and temporal scales
2. Designed TL-aided double-difference tomography (TADT) workflow combining deep learning with seismic imaging
3. Showed TL model outperforms original PhaseNet (+10% precision/recall) and matches human performance
4. Reduced human picking effort from days to ~3,500 manually picked seismograms for retraining

# Method
## Overall Framework
TL-aided double-difference tomography (TADT) workflow:
1. Pre-trained PhaseNet → transfer learning → TL model
2. Apply TL model to all triggered seismograms → P/S wave picks
3. Use tomoDD for double-difference tomography → updated seismic catalog + 3D velocity model

## Key Modules
### Module 1: Transfer Learning
- Initialize weights with PhaseNet model
- Exclude 9% incorrect picks (343 waveforms)
- 3,478 seismograms → 0.45% of original training data
- Random split: 2,443 train / 345 validation / 690 test
- Adam optimizer, lr=0.01, batch=20, 100 epochs
- Bandpass filter 3-20kHz applied before feeding to network

### Module 2: Double-Difference Tomography
- tomoDD package (Zhang & Thurber, 2003, 2006)
- 1,743 events relocated in 77×83×40m volume
- 1m node spacing, interpolated to 0.1m
- L-curve analysis: smoothing=10, damping=200
- 8 iterations to convergence

# Dataset
| Dataset | Size | Modality | Description |
|---|---|---|---|
| EGS Collab SURF | 69,444 waveforms | 3-component seismograms | Meter-scale hydraulic fracturing data, 100kHz sampling |

# Experimental Setup
- **Baseline**: AR picker (ObsPy), original PhaseNet, human analysts (3 analysts)
- **TL Model**: PhaseNet retrained with 3,478 waveforms
- **Metrics**: Precision, Recall, F1 score (with 5-fold cross-validation for uncertainty)
- **Hardware**: 32 Intel Xeon cores for training; 6 Intel i9 cores for inference

# Results
| Method | P Precision | S Precision | P Recall | S Recall |
|---|---|---|---|---|---|
| AR Picker | Low | Low | Low | Low |
| Original PhaseNet | Good | Good | Good | Good |
| TL Model | +10% vs PhaseNet | +10% vs PhaseNet | +10% vs PhaseNet | +10% vs PhaseNet |
| Human Expert | Baseline | Baseline | Baseline | Baseline |

Key findings:
- TL model found 32% fewer P picks but 48% more S picks than human
- TL model speed: 1,900x faster than human (excl. training)
- S-wave constrained volume: +133% with TL picks vs manual
- P-wave constrained volume: -8% with TL picks vs manual
- Average location uncertainty: 0.2m

# Ablation Study
- Bandpass filtering improves performance over raw data
- 5-fold cross-validation confirms statistical significance
- F1 scores improve as more training data included
- Weight comparison between PhaseNet and TL model shows small but meaningful changes

# Limitation
- TL model more prone to error on very complex signals
- Fewer P-wave picks than human (though higher quality)
- Results specific to meter-scale EGS Collab system — generalizability untested
- Transfer learning requires some manual picks (3,500) for retraining

# My Analysis
## Transferable Ideas
- **Transfer learning across scales**: If PhaseNet can bridge 3 orders of magnitude, similar approaches may work for seismic image segmentation
- **Minimal retraining data**: 0.45% of original training data sufficed — suggests pre-trained models can be adapted with very little labeled data
- **Bandpass filtering before DNN**: Simple preprocessing that improves DNN performance
- **Human-in-the-loop**: Analyst only needs to pick 3,500 waveforms, then DNN does the rest

## Potential Improvements
- **Domain adaptation**: Could we transfer without ANY manual picks? Self-supervised pre-training on target domain?
- **Multi-scale training**: Train on multiple scales simultaneously instead of transfer learning
- **Uncertainty estimation**: Per-pick uncertainty quantification
- **Real-time deployment**: 1,900x speedup enables real-time monitoring
- **Application to segmentation**: TL approach could transfer to seismic image segmentation tasks

# Related Notes
- Method: [[PhaseNet]], [[Transfer Learning]], [[CNN]]
- Task: [[Seismic Phase Picking]]
- Dataset: [[EGS Collab SURF]]
