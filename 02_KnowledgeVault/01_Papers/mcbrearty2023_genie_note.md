---
title: "Earthquake Phase Association with Graph Neural Networks"
authors: [I.W. McBrearty, G.C. Beroza]
year: 2023
venue: "arXiv preprint"
task: [Phase Association, Earthquake Detection, Catalog Building]
methods: [GENIE GNN, Two-Graph Architecture, Synthetic Training, Backprojection Sampling]
datasets: [Northern California seismic network, PhaseNet picks]
metrics: [Re-detection rate, Event count multiplier, Magnitude distribution]
code: "Not Found Yet"
importance: high
status: completed
paper_type: research_article
tags: [phase-association, genie, graph-neural-network, northern-california, phasenet, synthetic-training, two-graph-architecture, earthquake-catalog]
created: 2026-07-19
---

# Paper Type / 論文類型

Type: research_article

# One Sentence Summary / 一句話總結

Develops GENIE, a Graph Neural Network that simultaneously predicts source space-time localization and source-arrival association likelihoods using a two-graph architecture (station graph + source region graph), detecting 4.2x more events than USGS in Northern California while re-detecting 96% of known M>1 events.

# Research Background / 研究背景

Improved earthquake catalogs are essential for understanding active fault structures, foreshock/aftershock behaviors, and subsurface tomography. Traditional cataloging involves: (1) picking arrivals on individual stations, (2) associating arrivals to common sources, (3) characterizing events (location, origin time, magnitude).

Machine learning pickers (PhaseNet, EQTransformer, etc.) produce dramatically higher pick rates, including many arrivals from closely overlapping small events. This creates a "time entanglement" problem where traditional associators fail — they cannot distinguish arrivals from multiple nearby sources occurring simultaneously.

Existing associators include back-projection, RNN-based likelihood prediction, probabilistic models, random sample consensus clustering, and Bayesian mixture models. None directly combine the structural inductive bias of graphs with the representational power of deep learning for the full association problem.

# Problem Definition / 問題定義

- **Input / 輸入**: Variable-set of seismic stations S with positions, variable pick sets D_i per station (each containing arrival times tau_1, tau_2, ..., tau_M_i without phase type labels)
- **Output / 輸出**: (1) Continuous spatio-temporal source likelihood f_2(x,t) over spatial grid X x [0,W] where W=10s; (2) Discrete source-arrival association likelihoods f_3((x,t), tau); (3) Implicit source enumeration (number and location of earthquakes)

# Motivation / 研究動機

1. **Time entanglement**: ML pickers produce P and S picks in roughly equal numbers, creating dense arrival time overlaps that break traditional associators.
2. **Non-Euclidean data**: Seismic station networks are irregular manifures — no canonical grid ordering. GNNs are designed for this data structure.
3. **Variable network geometry**: Available stations change over time (maintenance, deployments). Method must handle time-varying station sets.
4. **High event rates**: Tectonically active regions produce thousands of detectable arrivals per day; associator must scale to hundreds of stations and dense seismicity.

# Main Contributions / 主要貢獻

1. **GENIE GNN architecture**: First GNN-based associator that jointly predicts continuous source likelihoods AND discrete source-arrival associations using two separate graphs (station graph + spatial source graph).
2. **Physically-inspired graph construction**: Adjacency matrices encode real physical relationships — station proximity, theoretical travel times, K-nearest-neighbor topology — injecting domain knowledge as inductive bias.
3. **Synthetic training with real testing**: Method trained entirely on synthetic data (simulated arrivals on theoretical moveout curves), tested on real Northern California seismic network data from 2000-2022.
4. **Operational demonstration**: Over 100-day continuous processing in 2017-2018, detected ~4.2x more events than USGS catalog, with new events concentrated near active faults and quarries.

# Method / 方法

## Overall Framework / 整體框架

GENIE operates in a sequential two-stage process:

1. **Stage 1 — Source Prediction**: GNN processes station graph + spatial graph + pick data to produce continuous spatio-temporal source likelihood f_2(x,t) over a 4D grid (3D space + 10s time window).
2. **Stage 2 — Association**: Given source locations from Stage 1, GNN produces source-arrival association likelihoods f_3((x,t), tau) to assign picks to sources.

The key insight: partitioning the forward map into sequential functions allows the network to first decide which sources are active, THEN assign picks to those sources — mirroring how human analysts approach the problem.

## Key Modules / 關鍵模塊

### Module 1: Backprojection Sampling

- Extracts explicit input tensor from variable pick dataset D
- Uses physically inspired heuristic: for query time t_0 and source location x, compute max response across all picks at each station using Gaussian kernel over travel time misfit
- h_k^0(s_i, x) = max_{tau_i in D_i}[exp(-(t_0 + T_k(s_i,x) - tau_i)^2 / (2*sigma^2))]
- Creates a fixed-size tensor regardless of variable input pick counts

### Module 2: Station Graph G_s

- Nodes = seismic stations with positions and pick features
- Edges = K-nearest-neighbor connectivity (K=10 or K=15 in experiments)
- Adjacency matrix encodes station proximity — nearby stations share information
- Captures pairwise station relationships for a fixed source

### Module 3: Spatial Source Graph G_x

- Nodes = spatial grid points covering the source region
- Edges = K-nearest-neighbor connectivity
- Adjacency matrix encodes spatial proximity — nearby grid points share information
- Captures pairwise source relationships for a fixed station
- Enables detection of multiple overlapping events at nearby locations

### Module 4: Two-Graph GNN

- Parallel graph convolutions on G_s and G_x
- Shared trainable FCN weights across nodes (handles variable graph sizes)
- Each convolution layer expands 1-hop receptive field — 2-layer GNN sees 2-hop neighbors
- Heterogeneous graph sizes handled naturally (unlike CNN/RNN which require padding/sequence truncation)

### Module 5: Prediction Heads

- Source likelihood head: produces continuous bounded prediction f_2(x,t) in [0,1]
- Association likelihood head: produces pairwise source-arrival likelihood f_3((x,t), tau) in [0,1]
- Sequential processing: association head conditioned on source predictions

## Mathematical Formulation / 數學表述

Forward map decomposition:
```
f_1: (D_i, S) -> {f_2, f_3}
f_2: (x, t) -> [0,1]    (spatio-temporal source likelihood)
f_3: ((x,t), tau) -> [0,1]  (source-arrival association likelihood)
```

Backprojection sampling:
```
h_k^0(s_i, x) = max_{tau_i in D_i}[exp(-(t_0 + T_k(s_i,x) - tau_i)^2 / (2*sigma^2))]
```

Graph convolution (message passing):
```
h_i^{(l+1)} = aggregate_{j in N(i)} [message(h_i^{(l)}, h_j^{(l)}, edge_ij)]
```

## Key Design Choices

- **K-nearest-neighbor edges**: Rather than distance-threshold, K-NN ensures each station/source has comparable number of neighbors regardless of local density
- **Parallel graph processing**: Station and source graphs processed in parallel, then combined
- **Continuous output**: Unlike discrete classifiers, continuous likelihood allows flexible thresholding for different detection sensitivity requirements

# Dataset / 數據集

| Dataset | Size | Modality | Description |
|---|---|---|---|
| Northern California seismic network | ~500 random days (2000-2022), 100-day continuous (2017-2018) | Seismic waveforms | Dense network with hundreds of stations; used for real-data testing |
| PhaseNet picks | Variable per day | P and S arrival times | Input picks generated by PhaseNet deep learning picker |
| USGS catalog (Northern California) | Reference ground truth | Event locations, magnitudes, origin times | Used for validation and comparison |
| Synthetic training data | Unlimited (simulated) | Simulated arrivals on theoretical moveout curves | Generated from simulated sources on theoretical travel times; enables arbitrary complexity and noise levels |

# Experimental Setup / 實驗設置

**Input**: Unlabeled arrival times from PhaseNet (no phase type labels, no amplitude/azimuth info)

**Network**: Northern California (NC) seismic network with variable station geometry

**Training**: Synthetic data only — simulated sources with theoretical P/S travel times, added noise and false picks

**Testing**:
1. **500 random days** (2000-2022): Re-detection rate of USGS M>1 events
2. **100-day continuous** (Oct 2017 - Jan 2018): Full processing test, event count comparison with USGS

**Baselines**: USGS catalog (operational reference), traditional associators (back-projection, PhaseLink)

**Evaluation**:
- Re-detection rate (fraction of USGS events recovered)
- Spatial/temporal residuals between GENIE and USGS locations
- Event count multiplier vs USGS
- Magnitude distribution (Gutenberg-Richter plots)
- New event localization relative to known faults/quarries

# Results / 實驗結果

### 500-Random-Day Test (USGS Re-detection)

- **Re-detection rate**: ~96% of all USGS M>1 events successfully re-detected
- Spatial and temporal residuals show close agreement with USGS locations
- Most mismatches attributed to genuine USGS misses or location differences

### 100-Day Continuous Test

- **Event count**: ~4.2x more events detected than USGS catalog
- **Magnitude**: New events concentrated below USGS magnitude of completeness
- **Spatial distribution**: New events cluster near active faults and quarries (geologically plausible)
- **Magnitude-frequency**: Gutenberg-Richter relationship maintained for new detections

### Network Robustness

- Handles hundreds of stations simultaneously
- Robust to variable station coverage and quality
- Effective even with high false-pick rates

# Ablation Study / 消融實驗

The paper does not present a formal ablation study. However, the architectural design choices are justified by comparison to prior work:

1. **GNN vs. CNN/RNN**: GNNs handle variable station counts natively; CNNs require padding, RNNs require sequence ordering
2. **Two-graph vs. single-graph**: Separate station and source graphs enable capturing both station-pairwise and source-pairwise interactions
3. **K-NN vs. distance threshold**: K-NN provides more uniform neighbor counts across varying station densities

# Limitation / 侷限性

### Author-Admitted Limitations

- Published as arXiv preprint — not yet peer-reviewed
- Synthetic training may not capture all real-world complexities
- Tested only on Northern California network — generalizability to other regions unverified
- Uses PhaseNet picks as input — quality depends on picker performance
- Initial application uses unlabeled arrival times only (no phase type, amplitude, or azimuth features)

### Agent-Identified Limitations

- No comparison with PhaseLink (Ross & Yue, 2019) — a competing deep-learning associator
- No quantitative analysis of false positive rate — 4.2x more events could include many spurious detections
- No ablation on K-NN parameter (K=10 vs K=15) — choice appears heuristic
- No analysis of computational latency — real-time applicability not demonstrated
- Magnitude estimation methodology not detailed in full.md — how are magnitudes assigned to new detections?
- No uncertainty quantification on association likelihoods — hard binary assignments without confidence
- Double-difference relocation used in post-processing (Fig. 10) but not integrated into GNN training

# My Analysis / 我的分析

## Transferable Ideas / 可遷移思想

1. **Two-graph architecture for paired entities**: The station graph + source graph paradigm generalizes to any problem with two interacting entity types (e.g., sensor-target, agent-resource). Could adapt for seismic source localization in other regions.
2. **Synthetic-to-real transfer**: Training entirely on synthetic data with theoretical moveout curves, then deploying on real data, is a powerful paradigm for domains with well-understood physics but limited labeled real data.
3. **Physical inductive bias in graphs**: Encoding domain knowledge (travel times, station proximity) directly into adjacency matrices rather than learning topology from data — this is a general principle for GNN applications in geophysics.
4. **Sequential prediction decomposition**: Splitting a complex prediction problem into sequential simpler functions (f_1 -> f_2 -> f_3) mirrors good engineering practice and could be applied to other multi-stage ML pipelines.
5. **Continuous likelihood over discrete classification**: Producing continuous bounded outputs [0,1] rather than hard classifications enables flexible thresholding — useful when operating conditions vary (e.g., high-seismicity vs. quiescent periods).

## Potential Improvements / 潛在改進方向

1. **End-to-end with phase type labels**: Extend to accept P/S phase type, amplitude, and azimuth features alongside arrival times.
2. **Cross-region validation**: Test on Southern California, Japan, or Italy networks to establish generalization.
3. **False positive analysis**: Quantify what fraction of "new" detections are genuine vs. artifacts.
4. **Integration with detection**: Combine GENIE with PhaseNet/EQTransformer in a single end-to-end model.
5. **Real-time capability**: Measure inference latency to assess operational deployment feasibility.
6. **Uncertainty estimates**: Add Bayesian uncertainty or ensemble-based confidence to association predictions.
7. **Comparison with PhaseLink**: Direct benchmark against Ross & Yue (2019) under identical conditions.

# Reproducibility Analysis / 復現性分析

## Official Implementation Verification / 官方實現驗證

> Distinguish "code exists" from "paper is reproducible."

**Code Status**:
- [ ] Confirmed Available
- [x] **Not Found Yet** — paper is arXiv preprint, no code mention in abstract or text
- [ ] Confirmed Missing
- [ ] Not Checked

**Evidence Location**: Not found in full.md text. Authors are from Stanford Geophysics (Beroza group) — code may be in their lab repo.

**Repository URL**: Not located in full.md. Requires human follow-up to check Beroza group GitHub or contact authors.

**Framework**: Likely PyTorch (Stanford geophysics group standard)

**Checkpoint / Pre-trained Weights**: Not mentioned in full.md

**Last Repository Update**: N/A — repository not located

**Code Quality Indicators**: N/A

**Verification Method**: Text search of full.md — no code URL found

## Missing Reproduction Components / 缺失的復現組件

| Component | Available? | Source Location | Notes |
|---|---|---|---|
| Source Code | [ ] Yes [ ] No [x] Not Found Yet | Not in paper text | Check Beroza group GitHub |
| Dataset Access | [x] Public [ ] Restricted [ ] Private | NC seismic data from Northern California Seismic Network (NCEDC) | Free registration |
| Pre-trained Checkpoint | [ ] Yes [ ] No [x] Not mentioned | | |
| Preprocessing Scripts | [ ] Yes [ ] No [x] Not mentioned | Synthetic data generation methodology described | |
| Hyperparameters | [ ] Fully Listed [x] Partially [ ] Missing | K-NN values (10, 15), time window W=10s, sigma for Gaussian kernel | |
| Environment Specs | [ ] requirements.txt [ ] Docker [x] Not specified | | |
| Random Seeds | [x] Specified [ ] Not specified | Not found in text | |
| Train/Val/Test Split | [x] Defined [ ] Undefined | Synthetic train / NC real-data test | |
| Data Augmentation | [ ] Described [x] Vaguely [ ] Not described | Noise added to synthetic picks | |

## Reproduction Difficulty Assessment / 復現難度評估

- **Overall Difficulty**: [ ] Easy [x] Moderate [ ] Hard [ ] Impossible
- **Estimated Effort**: 2-4 weeks for a researcher familiar with PyTorch and GNNs (PyG/DGL)
- **Hardware Requirements**: RTX 4070 sufficient — GNN inference on NC-sized networks is lightweight
- **Key Barriers**: Code not publicly available; synthetic data generation details partially described; phase type handling not implemented in current version
- **Workaround Options**: Implement from architectural description; synthetic data generation is well-described; contact authors for code

## Reproducibility vs. Code Availability

> **Important distinction**: Code existing != paper is reproducible.

- **Code Exists**: [ ] Yes [x] No [ ] Not Checked
- **Paper Actually Reproducible**: [x] Yes [ ] Partially [ ] No
- **Gap Between Code Existence and Reproducibility**: The methodology is sufficiently described (graph construction, backprojection sampling, GNN architecture, synthetic data generation) that implementation from paper text is feasible. The main missing piece is code — but the paper provides enough detail for a competent researcher to reconstruct the method.

# Related Notes / 相關筆記

- Method: [[GENIE]], [[Graph Neural Network]], [[Two-Graph Architecture]], [[Backprojection Sampling]]
- Task: [[Phase Association]], [[Earthquake Detection]], [[Catalog Building]]
- Dataset: [[Northern California Seismic Network]]
- Related: [[PhaseNet]], [[EQTransformer]], [[PhaseLink]]
- Authors: [[Beroza Group]]
