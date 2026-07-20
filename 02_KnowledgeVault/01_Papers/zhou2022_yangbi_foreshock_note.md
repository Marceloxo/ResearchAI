---
title: "Seismological Characterization of the 2021 Yangbi Foreshock-Mainshock Sequence, Yunnan, China: More than a Triggered Cascade"
authors: [Yijian Zhou, Chunmei Ren, Abhijit Ghosh, Haoran Meng, Lihua Fang, Han Yue, Shiyong Zhou, Youjin Su]
year: 2022
venue: "Journal of Geophysical Research: Solid Earth"
task: [Foreshock Mechanism, Coulomb Stress Modeling, Source Parameter Estimation]
methods: [Spectral Ratio Analysis, Multipoint-Source Inversion, hypoDD Relocation, Coulomb 3 Stress Modeling]
datasets: [Yangbi earthquake sequence, Yunnan regional network]
metrics: [Corner frequency, rupture area, stress drop, coseismic slip, delta-CFS]
code: "Not Found Yet"
importance: high
status: completed
paper_type: research_article
tags: [yangbi, foreshock-mechanism, coulomb-stress, spectral-ratio, multipoint-source-inversion, cascade-triggering, aseismic-slip, yunnan, china-earthquake]
created: 2026-07-19
---

# Paper Type / 論文類型

Type: research_article

# One Sentence Summary / 一句話總結

Analyzes the 2021 M6.1 Yangbi earthquake sequence using spectral ratio analysis, multipoint-source inversion, and Coulomb stress modeling to demonstrate that the foreshock-mainshock relationship involves both cascade triggering AND aseismic slip — multiple mechanisms operating simultaneously, challenging simple predictive models.

# Research Background / 研究背景

Foreshocks have long been studied as possible precursors to large earthquakes. Two end-member models dominate the field:

1. **Cascade model**: Foreshocks are independent failures of isolated asperities, triggered by stress transfer from preceding events. Unpredictable — the mainshock initiation process is identical to foreshocks.
2. **Pre-slip model**: Foreshocks are byproducts of accelerating aseismic slip during mainshock nucleation. Deterministic — nucleation size scales with final mainshock size (Ampuero & Rubin, 2008).

The implications for earthquake predictability differ fundamentally between these models, making discrimination critical. The 2021 M6.1 Yangbi earthquake in Yunnan, China, provides a rare opportunity: it has prominent foreshock activity (three M4-5 events preceding the M6.1 mainshock within 3 days), is well-recorded by a dense regional network, and is the largest event in the Chuandian block since 1996.

# Problem Definition / 問題定義

- **Input / 輸入**: High-resolution seismic catalog (7943 events, ML 1.0 completeness) from AI picker + matched filter; waveform data from Yunnan regional network
- **Output / 輸出**: (1) Fault structure determination, (2) Rupture area and source parameters for each foreshock, (3) Coulomb stress evolution modeling, (4) Triggering mechanism interpretation

# Motivation / 研究動機

1. **Discriminate foreshock models**: The cascade vs. pre-slip debate has direct implications for earthquake prediction.
2. **Rare well-recorded sequence**: Yangbi is one of the largest Chinese earthquakes with clear foreshock activity since Haicheng (1975).
3. **Inconsistent prior conclusions**: Previous studies reached different triggering interpretations — well-constrained stress modeling needed.
4. **Aseismic slip evidence**: Detecting aseismic processes in foreshock nucleation would challenge the pure cascade model.

# Main Contributions / 主要貢獻

1. **Dual-fault structure**: Identifies two intersecting fault segments (Fault_M near-vertical, Fault_F dipping NE at 60°) that hosted the foreshock-mainshock sequence.
2. **Finite rupture parameters**: Estimates rupture areas (3.25, 8.08, 13.58 km²), stress drops (~1.0, ~1.7, ~3.5 MPa), and coseismic slip (3, 7, 16 cm) for the three major foreshocks via spectral ratio analysis.
3. **Cascade + aseismic slip**: Demonstrates that Yangbi sequence involved BOTH cascade triggering (delta-CFS > 0.05 MPa after each foreshock) AND aseismic processes (localized precursor cluster, repeater sequences, logarithmic aftershock expansion).
4. **F2 re-evaluation**: Identifies the M4.9 F2 (first immediate aftershock of F1) as potentially important for triggering — previously ignored in published studies.

# Method / 方法

## Overall Framework / 整體框架

Three complementary analytical approaches applied sequentially:

1. **Spectral ratio analysis** → rupture directivity, corner frequency, source parameters
2. **Multipoint-source (MPS) moment tensor inversion** → focal mechanisms for complex overlapping events
3. **Coulomb stress modeling** (Coulomb 3) → static stress transfer between events

All approaches constrained by high-resolution relocated seismic catalog (hypoDD, ~10m lateral / ~20m vertical uncertainty).

## Key Modules / 關鍵模塊

### Module 1: Spectral Ratio Analysis

- Uses empirical Green's function (EGF) approach: aftershocks of target foreshock serve as EGFs
- 6-10 EGFs selected per foreshock (ML 2.6-4.1)
- Two-direction comparison: fault-parallel vs. fault-normal
- Rupture directivity from azimuthal corner frequency variation (Haskell, 1964)
- Rupture area from fault-normal corner frequency (minimizes directivity effect)
- Multi-taper S-wave spectrum calculation (Prieto et al., 2009)
- Multi-window strategy: three 10-s sliding windows, 1.5-s stride
- Omega-square source model fit (Boatwright, 1980) for corner frequency extraction

Source parameter equations:
```
r = 0.21 * Vs / fc     (Madariaga, 1976; Vs = 3.4 km/s)
D = M0 / (mu * pi * r^2)  (mu = 32 GPa)
Delta_sigma = (7/16) * M0 / r^3  (Eshelby, 1957)
```

### Module 2: Multipoint-Source (MPS) Moment Tensor Inversion

- Handles overlapping waveforms from immediate aftershocks
- 14 stations (30-160 km) for F1; 12 stations (40-200 km) for M
- Bandpass filter 0.01-0.5 Hz, downsample to 10 Hz
- Regional velocity model (Liu et al., 2021) for Green's functions
- Spatial grids: 10x6 (F1), 10x5 (M) over 15x6 km² rupture area
- Subevents: F1 uses 2 subevents (0-5s, 5-10s); M uses 3 subevents (0-3s, 5-8s, 8-15s)

### Module 3: Coulomb Stress Modeling

- Coulomb 3 software (Lin & Stein, 2004; Toda et al., 2005)
- Homogeneous elastic half-space assumption
- Default friction parameters: mu=0.4, nu=0.25, E=80 GPa
- Cumulative delta-CFS calculated after each foreshock
- Fault geometry from spectral ratio + MPS + aftershock distribution

### Module 4: Repeater Detection

- Identifies repeating earthquake sequences in foreshock period
- Cross-correlation between frequency bands (1-10, 1-15, 1-20 Hz)
- Evidence for preseismic slip acceleration

## Mathematical Formulation / 數學表述

Spectral ratio fitting (omega-square model):
```
U1(f)/U2(f) = (M0_1/M0_2) * sqrt[(1+(f/fc2)^4)/(1+(f/fc1)^4)]
```

Grid search minimizes summed difference between predicted and observed spectral ratio on 0.2-20 Hz band in log scale.

# Dataset / 數據集

| Dataset | Size | Modality | Description |
|---|---|---|---|
| Yangbi seismic catalog | 7,943 events (May 1-28, 2021) | Well-located earthquakes | AI picker + matched filter; ML completeness=1.0; hypoDD relocation (~10m lateral, ~20m vertical) |
| Yunnan regional network | Dense station coverage | Waveform data (3-component) | Broadband stations; sufficient for spectral ratio and MPS inversion |
| EGFs (empirical Green's functions) | 6-10 per foreshock | Aftershock waveforms | ML 2.6-4.1 for f1/f2; ML 2.9-4.1 for F1 |

# Experimental Setup / 實驗設置

**Seismic catalog**: Zhou, Ghosh, et al. (2021) — AI picker + matched filter, hypoDD relocation

**Velocity model**: Regional model from joint body/surface wave inversion (Liu et al., 2021)

**Comparison with prior studies**: 
- Disagrees with Lei et al. (2021) on F1 rupture direction (their 70-s S-wave window biased by immediate large aftershocks)
- Confirms NW-SE fault strike with spectral ratio evidence

**Validation**: Two end-member rupture models for F1 shown to produce same triggering interpretation

# Results / 實驗結果

### Foreshock Source Parameters

| Event | Rupture Area (km²) | Stress Drop (MPa) | Coseismic Slip (cm) | Rupture Direction |
|---|---|---|---|---|
| f1 (M4.3) | 3.25 | ~1.0 | ~3 | NW unilateral |
| f2 (M4.6) | 8.08 | ~1.0 | ~3 | NW unilateral |
| F1 (M5.2) | 13.58 | ~3.5 | ~16 | SE bilateral |
| F2 (M4.9) | ~11 | ~1.7 | ~7 | Bilateral |

### Coulomb Stress Evolution

- **After f1**: delta-CFS > 0.05 MPa at F1 hypocenter; cascade triggering to f2 confirmed
- **After f2**: Positive delta-CFS on both F1 and mainshock
- **After F1**: 0.02-0.05 MPa delta-CFS boundary pushed closer to mainshock hypocenter
- All values above traditional 0.01 MPa static triggering threshold

### Aseismic Evidence

1. Short-term localized cluster preceding f1 (first foreshock)
2. Three repeater sequences detected during foreshock period
3. Aftershock zones expand logarithmically with time (afterslip signature)

### Repeater Analysis

Repeating earthquakes detected pre- and post-mainshock, surrounding ruptured patches — consistent with afterslip distribution pattern.

# Ablation Study / 消融實驗

Not a machine learning paper — but the study presents methodological comparisons:

1. **Spectral ratio vs. waveform fitting**: Their spectral ratio analysis disagrees with Lei et al. (2021) waveform inversion — attributed to 70-s S-wave window contamination by immediate aftershocks
2. **Two rupture models for F1**: Both end-member models (unilateral SE vs. bilateral) produce same triggering interpretation, validating conclusion robustness
3. **MPS vs. GCMT**: MPS resolves subevent structure that GCMT averages over; different dip angles between subevents explain NDC components

# Limitation / 侷限性

### Author-Admitted Limitations

- Fault_F dip angle likely varies along strike (different focal mechanisms for F1 vs F2)
- F2 rupture area cannot be precisely determined — excluded from Coulomb stress modeling
- Some aftershock-based rupture area estimates are approximate (rectangular simplification)
- Coulomb 3 assumes homogeneous elastic half-space — real crust is heterogeneous

### Agent-Identified Limitations

- No deep learning component — not directly applicable to seismic AI segmentation research
- Relies heavily on dense regional network coverage — not generalizable to sparse networks
- Spectral ratio analysis requires careful EGF selection — subjective in some cases
- Repeater detection sensitivity depends on frequency band choice
- No dynamic rupture simulation — only static Coulomb stress changes modeled
- F2 importance acknowledged but excluded from quantitative stress modeling

# My Analysis / 我的分析

## Transferable Ideas / 可遷移思想

1. **Spectral ratio for rupture characterization**: The EGF-based spectral ratio method combined with multi-window averaging provides robust source parameter estimation — applicable to any well-recorded earthquake sequence.
2. **MPS for overlapping events**: Multipoint-source inversion handles waveform overlap from immediate aftershocks — directly useful for analyzing foreshock-mainshock sequences with closely timed events.
3. **Logarithmic aftershock expansion**: The logarithmic spatial expansion of aftershock zones as an afterslip indicator is a novel diagnostic that could be adapted for other sequences.
4. **Dual-mechanism interpretation**: The finding that cascade triggering AND aseismic slip coexist challenges binary thinking about foreshock models — similar multi-mechanism approaches may apply to other earthquake sequences.
5. **F2 re-evaluation**: The paper demonstrates that ignoring intermediate-magnitude aftershocks (like F2) can miss important triggering pathways.

## Potential Improvements / 潛在改進方向

1. **Dynamic stress transfer modeling**: Extend beyond static Coulomb stress to include dynamic triggering effects (wave-induced stress pulses).
2. **Machine learning integration**: Combine the high-resolution catalog (already AI-generated) with deep learning for real-time cascade detection.
3. **Cross-region comparison**: Apply the same methodology to other well-recorded foreshock sequences (e.g., 2019 Ridgecrest, 2009 L'Aquila).
4. **InSAR integration**: Joint inversion with InSAR coseismic slip (as done by Wang, He, et al., 2022) for more complete rupture model.
5. **Real-time Coulomb stress monitoring**: Develop ML-based approximations of Coulomb stress evolution for operational forecasting.

# Reproducibility Analysis / 復現性分析

## Official Implementation Verification / 官方實現驗證

> Distinguish "code exists" from "paper is reproducible."

**Code Status**:
- [ ] Confirmed Available
- [x] **Not Found Yet** — no code URL in paper text
- [ ] Confirmed Missing
- [ ] Not Checked

**Evidence Location**: Not found in full.md. Methods use standard tools (Coulomb 3, hypoDD) — code may be in supplementary or author repositories.

**Repository URL**: Not located in full.md. Requires checking Zhou's UC Riverside profile or supplementary materials.

**Framework**: Standard seismological tools (Coulomb 3, SAC, obspy likely)

**Checkpoint / Pre-trained Weights**: Not applicable — this is a traditional seismology paper, not ML

**Verification Method**: Text search of full.md — no code URL found

## Missing Reproduction Components / 缺失的復現組件

| Component | Available? | Source Location | Notes |
|---|---|---|---|
| Source Code | [ ] Yes [ ] No [x] Not Found Yet | Coulomb 3, hypoDD are open-source | Individual method code not in paper |
| Dataset Access | [x] Public [ ] Restricted [ ] Private | Yangbi catalog from Zhou et al. (2021); Yunnan network data | Regional network data may require application |
| Pre-trained Checkpoint | [x] N/A [ ] Yes [ ] No | Traditional seismology paper | |
| Preprocessing Scripts | [ ] Yes [ ] No [x] Not mentioned | Catalog construction described in Zhou et al. (2021) | |
| Hyperparameters | [x] Fully Listed [ ] Partially [ ] Missing | Vs=3.4 km/s, mu=32 GPa, friction=0.4, Poisson=0.25, E=80 GPa | Well-documented |
| Environment Specs | [ ] requirements.txt [ ] Docker [x] Not specified | Coulomb 3, hypoDD, standard seismology tools | |
| Random Seeds | [x] N/A [ ] Specified [ ] Not specified | | |
| Train/Val/Test Split | [x] N/A [ ] Defined [ ] Undefined | Traditional analysis, not ML | |
| Data Augmentation | [x] N/A [ ] Described [ ] Not described | Multi-window strategy for spectral ratio | |

## Reproduction Difficulty Assessment / 復現難度評估

- **Overall Difficulty**: [ ] Easy [x] Moderate [ ] Hard [ ] Impossible
- **Estimated Effort**: 2-3 weeks for a researcher familiar with seismological analysis tools
- **Hardware Requirements**: Minimal — standard laptop/workstation sufficient for Coulomb 3 and spectral analysis
- **Key Barriers**: Regional waveform data access; EGF selection methodology; repeater detection implementation
- **Workaround Options**: Use publicly available Yangbi catalog; Coulomb 3 and hypoDD are open-source

## Reproducibility vs. Code Availability

> **Important distinction**: Code existing ≠ paper is reproducible.

- **Code Exists**: [ ] Yes [x] No [ ] Not Checked
- **Paper Actually Reproducible**: [x] Yes [ ] Partially [ ] No
- **Gap Between Code Existence and Reproducibility**: The methodology is well-described and uses standard open-source tools (Coulomb 3, hypoDD). The main barrier is data access (Yunnan regional network waveforms). The paper provides all necessary parameters for reproduction.

# Related Notes / 相關筆記

- Method: [[Spectral Ratio Analysis]], [[Multipoint-Source Inversion]], [[Coulomb Stress Modeling]], [[hypoDD Relocation]]
- Task: [[Foreshock Mechanism]], [[Earthquake Sequence Analysis]]
- Dataset: [[Yangbi Earthquake Sequence]], [[Yunnan Regional Network]]
- Related: [[Zhou 2021 Yangbi Catalog]], [[Cascade Triggering]], [[Aseismic Slip]]
- Authors: [[Zhou Yijian]], [[Ghosh Abhijit]], [[Fang Lihua]]
