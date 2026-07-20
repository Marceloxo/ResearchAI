---
task_name: "Earthquake Sequence Analysis"
domain: "Seismology / Earthquake Physics"
input: "Earthquake catalogs, waveform data, stress models"
output: "Sequence classification, causal relationships, slip models"
metrics: [Catalog completeness, Foreshock ratio, Stress drop]
tags: [earthquake-sequence, foreshock-mainshock, aseismic-slip, coulomb-stress, ridgecrest, yangbi]
created: 2026-07-19
---

# Task Definition / 任务定义

Earthquake sequence analysis is the task of characterizing the temporal, spatial, and causal relationships among earthquakes in a sequence — including foreshock-mainshock-aftershock cascades, triggered seismicity, and aseismic slip events. This task bridges machine learning detection with physical earthquake mechanics.

This task is motivated by the Zhou 2022 Yangbi earthquake sequence paper and related studies of the Ridgecrest 2019 sequence.

# Problem Formulation / 问题形式化

- **Given / 给定**: 
  - Earthquake catalog: {(x_i, y_i, z_i, t_i, M_i)} for detected events
  - Waveform data for re-detection and waveform similarity analysis
  - Optional: GPS/inSAR surface deformation measurements
- **Goal / 目标**: 
  - Classify events as mainshock, foreshock, aftershock, or swarm
  - Identify causal relationships (did event A trigger event B?)
  - Estimate coseismic and post-seismic slip distribution
  - Compute Coulomb stress changes to quantify triggering potential

# Input Data / 输入数据

- **Modality / 模态**: 
  - Relocation catalogs (hypocenters + magnitudes + timestamps)
  - Raw waveforms (for waveform clustering and template matching)
  - Surface deformation data (GPS, InSAR)
  - Tectonic/volatility model (regional stress field, fault geometry)
- **Typical Dimensions / 典型维度**: Catalogs range from hundreds to millions of events; waveform data per event: 3-component, variable length
- **Characteristics / 特点**: 
  - Gutenberg-Richter magnitude-frequency distribution
  - Omori-Utsu aftershock decay law
  - Clustering in time and space (swarms, triggered sequences)
  - Mixed seismic/aseismic deformation

# Output / 输出

- **Type / 类型**: Sequence classification, causal graph, slip inversion model
- **Format / 格式**: 
  - Event labels: {event_id, type: foreshock/mainshock/aftershock/swarm, confidence}
  - Causal graph: directed edges (triggering relationships) with stress change values
  - Slip model: 2D/3D slip distribution on fault plane
- **Resolution / 分辨率要求**: Magnitude of completeness (Mc) < 2.0 for reliable statistics

# Evaluation Metrics / 评估指标

| Metric | Formula | Description |
|---|---|---|
| Foreshock Ratio | N_fore / N_total | Fraction of mainshocks preceded by identifiable foreshocks |
| Catalog Completeness (Mc) | Magnitude at 90% frequency fit | Minimum detectable magnitude |
| Stress Change (ΔCFS) | τ + μ·b·σ_n | Coulomb failure function change; positive = promoted failure |
| Aftershock Decay Fit | n(t) = K/(t+c)^p | Omori-Utsu law fit quality; p ≈ 1.0 expected |
| Triggering Accuracy | | Fraction of correctly identified causally linked event pairs |

# Common Methods / 常用方法

| Method Family | Representative Work | Key Idea | Performance |
|---|---|---|---|
| Machine learning picker | [[PhaseNet]] | High-precision phase picks enable catalog construction | Enables detection of Mw < 1.0 events |
| ML association | [[GENIE]] | GNN-based source-arrival assignment for dense catalogs | ~4.2× more events than operational catalogs |
| All-in-one GNN | [[PLAN]] | Joint picking, association, location for rapid catalog building | Real-time capable on regional networks |
| Physical modeling | Coulomb 3.3 / stress transfer | Compute ΔCFS between events to quantify triggering | Standard in seismology; requires accurate locations |
| Waveform clustering | Template matching / STA | Group similar waveforms for consistent re-location | Detects small events missed by catalogs |

# Challenges / 挑战

- **Foreshock identification is retrospective**: True foreshocks can only be labeled after the mainshock occurs
- **Aseismic slip detection**: Requires GPS/inSAR data; not detectable from seismic catalogs alone
- **Magnitude of completeness (Mc)**: Varies spatially and temporally within a sequence; complicates statistical analysis
- **Causal inference**: Correlation ≠ causation; distinguishing triggered events from random clustering is difficult
- **Computational scaling**: Analyzing million-event catalogs (e.g., Northern California) requires efficient algorithms
- **Multi-physics coupling**: Combining seismic, aseismic, and surface deformation data in a unified model

# Benchmark Datasets / 基准数据集

| Dataset | Size | Year | Notes |
|---|---|---|---|
| [[Northern California Seismic Network]] | ~3M relocated events | Ongoing | BayAreaQuakeCAT; ML-ready catalog |
| Ridgecrest 2019 sequence | ~70k events | 2019 | M7.1 mainshock; extensive foreshock sequence |
| Yangbi 2021 (China) | ~5k events | 2021 | Zhou et al. 2022; foreshock-mainshock cascade |

# Open Problems / 开放问题

- Can ML detect foreshock patterns before the mainshock (real-time foreshock warning)?
- Joint inversion of seismic + aseismic slip from combined waveform + GPS data
- Machine learning for Coulomb stress change prediction (surrogate for physical modeling)
- Universal earthquake sequence classification across tectonic settings
- Causal graph learning from earthquake catalogs: automated discovery of triggering networks
- Integration of deep learning detection with physical earthquake mechanics models

# Relationship to Methods / 相关方法

This task draws on methods from:

- [[PLAN]] — All-in-one system for catalog construction (picking + association + location)
- [[GENIE]] — GNN-based association for dense event catalogs
- [[Multi-task Learning]] — Joint optimization of detection and classification tasks
- [[PhaseNet]] — Foundational phase picker enabling high-resolution catalogs

# Relationship to Current Research / 与当前研究的关系

Earthquake sequence analysis is a **complementary task** to seismic facies segmentation. While the primary ResearchAI focus is on 2D/3D image segmentation for subsurface interpretation, sequence analysis addresses the temporal-spatial dimension of seismic data. The Zhou 2022 Yangbi paper and Ridgecrest 2019 sequence provide concrete case studies for applying ML-based detection and association to real earthquake sequences.
