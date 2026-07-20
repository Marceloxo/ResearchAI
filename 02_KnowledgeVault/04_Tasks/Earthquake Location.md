---
task_name: "Earthquake Location"
domain: "Seismic Signal Processing"
related_methods: [GENIE, Multi-task Learning, PLAN]
input: "Multi-station phase picks or raw waveforms"
output: "Hypocenter (lon, lat, depth) and origin time"
metrics: [Location Error, Depth Error, Origin Time Error]
tags: [earthquake-location, gnn, physics-informed, multi-station, ridgecrest, japan-hinet]
created: 2026-07-19
---

# Task Definition / 任务定义

Earthquake location is the task of determining the hypocenter (epicenter coordinates + depth) and origin time of a seismic event from observed arrival times or raw waveforms at multiple stations. Traditionally performed as the third stage after phase picking and phase association, modern methods (e.g., PLAN) integrate location into a joint multi-task framework.

# Problem Formulation / 问题形式化

- **Given / 给定**: 
  - Option A (traditional): Phase picks with known station-event travel times T_k(s_i, x) for each pick k at station i, assuming a velocity model v(z)
  - Option B (end-to-end): Multi-station 3-component waveforms + station coordinates (lon, lat, elevation)
- **Goal / 目标**: Predict hypocenter (x, y, z) and origin time t_0 that best explain the observations

# Input Data / 输入数据

- **Modality / 模态**: 
  - Traditional: P/S arrival times + station coordinates + velocity model
  - End-to-end: Multi-station 3-component time series (Z, N, E) + station geographic features
- **Typical Dimensions / 典型维度**: Variable number of stations (3–1000+); 1D waveform windows (e.g., 60s × 3 channels × 100 Hz = 18,000 samples per event)
- **Characteristics / 特点**: 
  - Requires velocity model for travel-time computation
  - Station geometry critically affects location accuracy
  - Depth resolution is typically poorer than horizontal resolution

# Output / 输出

- **Type / 类型**: Hypocenter coordinates + origin time
- **Format / 格式**: {event_id, longitude, latitude, depth_km, origin_time_utc, magnitude_estimate}
- **Resolution / 分辨率要求**: Horizontal error < 1 km (dense networks); depth error < 3 km

# Evaluation Metrics / 评估指标

| Metric | Formula | Description |
|---|---|---|
| Horizontal Error | sqrt((Δlon)² + (Δlat)²) converted to km | Distance between predicted and true epicenter |
| Depth Error | \|z_pred − z_true\| | Absolute depth prediction error |
| Origin Time Error | \|t_pred − t_true\| | Absolute origin time error (seconds) |
| Location Accuracy Rate | % events with horiz. error < threshold | Fraction of events within acceptable error band |

# Common Methods / 常用方法

| Method Family | Representative Work | Key Idea | Performance |
|---|---|---|---|
| Physics-informed GNN | [[PLAN]] | Predicts station-event offset + depth via GNN; triangulation from predicted offset gives epicenter. Uses non-trainable physical roll layers for travel-time alignment | Outperforms traditional tomography on Ridgecrest and Hi-net |
| Traditional | Geiger/Linearized inversion | Iterative travel-time residual minimization with velocity model | Baseline; requires good velocity model |
| ML-based | Double-difference relocation | Differential travel-time optimization between event pairs | High relative accuracy for clustered events |

# Challenges / 挑战

- **Velocity model dependence**: Accurate location requires a good 1D or 3D velocity model; incorrect models introduce systematic bias
- **Depth ambiguity**: Depth resolution is inherently poorer than horizontal resolution, especially with shallow events and surface-only stations
- **Sparse network geometry**: Few stations or poor azimuthal coverage degrades location quality
- **Computational cost**: Traditional iterative methods scale poorly with event count; ML methods require large labeled training sets
- **Integration with picking/association**: Error cascade from upstream stages propagates to location

# Benchmark Datasets / 基准数据集

| Dataset | Size | Year | Notes |
|---|---|---|---|
| [[Northern California Seismic Network]] | ~3M events | Ongoing | High-quality catalog for validation |
| [[Japan Hi-net]] | ~100k events | 2000s | Dense network; excellent for location testing |
| Ridgecrest SCSC | ~50k events | 2019 | California; used in PLAN evaluation |

# Open Problems / 开放问题

- Joint location with uncertainty quantification (prediction intervals, not point estimates)
- Real-time location in sparse or rapidly deploying networks (e.g., aftershock sequences)
- Cross-domain transfer: methods trained on one tectonic setting to another
- Integrating waveform similarity (template matching) with ML-based location
- End-to-end differentiable location that accepts raw waveforms without explicit phase picking

# Relationship to Methods / 相关方法

This task is addressed by:

- [[PLAN]] — All-in-one multi-station GNN that jointly performs picking, association, and location
- [[Multi-task Learning]] — Training paradigm enabling joint optimization of location with other seismic tasks
