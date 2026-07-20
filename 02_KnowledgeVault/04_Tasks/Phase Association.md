---
task_name: "Phase Association"
domain: "Seismic Signal Processing"
input: "Multi-station seismic waveforms with phase picks"
output: "Source-arrival associations (earthquake events)"
metrics: [F1-score, Precision, Recall]
tags: [phase-association, graph-neural-network, earthquake-detection, multi-station]
created: 2026-07-19
---

# Task Definition / 任务定义

Phase association is the task of assigning individual seismic phase picks (P-wave and S-wave arrivals) from multiple stations to their common earthquake source events. Given a set of picks from a phase picker (e.g., PhaseNet, EQTransformer), the associator determines which picks belong to the same earthquake and estimates the source location and origin time.

Phase association is the second stage in the traditional seismic monitoring pipeline:

Phase Picking → Phase Association → Earthquake Location

Modern approaches (e.g., PLAN, GENIE) eliminate this cascade by performing all three stages jointly.

# Problem Formulation / 问题形式化

- **Given / 给定**: A set of phase picks {τ_k^i} from N seismic stations, where τ is the arrival time at station i for phase k (P or S), along with station coordinates (lon, lat, elev) and per-pick confidence scores
- **Goal / 目标**: Partition picks into M source events, each defined by {(x_e, t_e, z_e)} where x_e is epicenter, t_e is origin time, z_e is depth, and assign each pick to its corresponding event

# Input Data / 输入数据

- **Modality / 模态**: 1D seismic waveforms (3-component: Z, N, E) + station metadata
- **Typical Dimensions / 典型维度**: Variable-length time series per station (e.g., 60s windows at 100Hz → 6000 samples); variable number of stations per network
- **Characteristics / 特点**: 
  - Irregular station geometry (non-Euclidean)
  - Variable station counts over time
  - Dense pick outputs from ML pickers create overlapping arrivals
  - Requires travel-time theory for source-arrival matching

# Output / 输出

- **Type / 类型**: Event catalog — list of detected earthquakes with location, origin time, and assigned phase picks
- **Format / 格式**: Structured table: {event_id, lon, lat, depth, origin_time, assigned_picks[]}
- **Resolution / 分辨率要求**: Epicentral accuracy < 1 km (regional networks); depth accuracy < 5 km

# Evaluation Metrics / 评估指标

| Metric | Formula | Description |
|---|---|---|
| F1-score | 2·(Precision·Recall)/(Precision+Recall) | Primary metric for association correctness |
| Precision | Correct associations / Total assigned | False association rate |
| Recall | Correct associations / Total ground truth | Missed event rate |
| Time window match | | Picks within Δt of true arrival accepted as correct |
| Event match rate | | Fraction of catalog events correctly reconstructed |

# Common Methods / 常用方法

| Method Family | Representative Work | Key Idea | Performance |
|---|---|---|---|
| GNN-based | [[GENIE]] | Two-graph architecture: station graph + spatial source graph; backprojection sampling for variable inputs | ~96% re-detection rate; 4.2× more events than USGS catalog |
| GNN-based (all-in-one) | [[PLAN]] | Multi-station GNN with physics-informed alignment; simultaneous picking, association, location | Outperforms PhaseNet + Aggregated-GNN on Ridgecrest and Hi-net |
| Multi-task | [[Multi-task Learning]] | Joint optimization of related seismic tasks | Reduces error propagation across pipeline stages |
| Graph-based clustering | Traditional associators | Cluster picks by travel-time consistency | Baseline performance |

# Challenges / 挑战

- **Variable station counts**: Networks change over time; methods must handle 3 to 1000+ stations natively
- **Dense pick outputs**: Modern ML pickers produce many false positives, causing "time entanglement" where arrivals overlap heavily
- **Computational scalability**: O(N²) pairwise station interactions become expensive at network scale
- **Synthetic-to-real transfer**: Training on synthetic data may not capture real-world noise and heterogeneity
- **False positive control**: Detecting more events increases spurious detections; threshold tuning is critical

# Benchmark Datasets / 基准数据集

| Dataset | Size | Year | Notes |
|---|---|---|---|
| [[Northern California Seismic Network]] | ~3M events | Ongoing | Used by GENIE; real regional network data |
| [[Japan Hi-net]] | ~100k events | 2000s | High-density network; used by PLAN |
| Ridgecrest SCSC | ~50k events | 2019 | California; used by PLAN, EQTransformer |

# Open Problems / 开放问题

- Uncertainty quantification on association decisions
- Real-time association at continental scale with streaming data
- Cross-region generalization of GNN-based associators
- Handling sparse networks (< 5 stations) where graph methods degrade
- Integration with downstream location and magnitude estimation in a single differentiable pipeline

# Relationship to Methods / 相关方法

This task is addressed by:

- [[GENIE]] — GNN-based phase association with source prediction
- [[PLAN]] — All-in-one multi-station GNN (picking + association + location)
- [[Multi-task Learning]] — Training paradigm enabling joint optimization
- [[PhaseNet]] — Phase picker whose output feeds into association
