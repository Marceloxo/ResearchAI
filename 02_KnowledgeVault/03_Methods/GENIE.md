---
method_name: "GENIE"
category: "GNN-based Phase Association"
application: ["Phase Association", "Earthquake Detection", "Earthquake Location"]
related_tasks: ["Phase Association", "Earthquake Location", "Seismic Phase Picking"]
tags: [genie, graph-neural-network, phase-association, two-graph-architecture, backprojection-sampling, northern-california, synthetic-training]
created: 2026-07-19
---

# Definition / 定义

GENIE (Graph Neural Network for Earthquake Identification and Enumeration) is a GNN-based associator that simultaneously predicts source space-time localization and source-arrival association likelihoods using a two-graph architecture. It detects ~4.2x more events than USGS catalogs in Northern California while maintaining high re-detection rates (~96%) of known events.

# Core Idea / 核心思想

Seismic station networks are inherently non-Euclidean — stations have irregular geometries and variable counts over time. GNNs natively handle this structure. GENIE's key insight is to partition the association problem into two sequential functions: (1) predict where and when earthquakes occur (source prediction), then (2) assign phase picks to those sources (association). This mirrors how human analysts approach the problem and avoids the "time entanglement" problem where ML pickers produce dense arrival overlaps that break traditional associators.

# Architecture / Formulation / 架构/公式

## Forward Map Decomposition

```
f_1: (D_i, S) -> {f_2, f_3}     # Full forward map
f_2: (x, t) -> [0,1]            # Spatio-temporal source likelihood
f_3: ((x,t), tau) -> [0,1]      # Source-arrival association likelihood
```

## Backprojection Sampling (Input Encoding)

Extracts explicit input tensor from variable pick datasets:
```
h_k^0(s_i, x) = max_{tau in D_i}[exp(-(t_0 + T_k(s_i,x) - tau)^2 / (2*sigma^2))]
```

For each query time t_0 and source location x, computes max response across all picks at each station using a Gaussian kernel over travel time misfit. Creates a fixed-size tensor regardless of variable input pick counts.

## Two-Graph Architecture

**Station Graph G_s**:
- Nodes = seismic stations with positions and pick features
- Edges = K-nearest-neighbor connectivity (K=10 or K=15)
- Adjacency matrix encodes station proximity

**Spatial Source Graph G_x**:
- Nodes = spatial grid points covering the source region
- Edges = K-nearest-neighbor connectivity
- Adjacency matrix encodes spatial proximity

**Parallel Graph Convolutions**:
```
h_i^(l+1) = aggregate_{j in N(i)} [message(h_i^(l), h_j^(l), edge_ij)]
```

Shared trainable FCN weights across nodes (handles variable graph sizes). Each convolution layer expands 1-hop receptive field — 2-layer GNN sees 2-hop neighbors.

## Prediction Heads

- **Source likelihood head**: Continuous bounded prediction f_2(x,t) in [0,1]
- **Association likelihood head**: Pairwise source-arrival likelihood f_3((x,t), tau) in [0,1]
- Sequential processing: association head conditioned on source predictions

## Advantages / 优势

- **Handles variable station counts natively**: Unlike CNN/RNN which require padding or sequence ordering
- **Physical inductive bias**: Adjacency matrices encode real physical relationships (station proximity, theoretical travel times)
- **Synthetic-to-real transfer**: Trained entirely on synthetic data, tested on real seismic networks
- **Continuous outputs**: Flexible thresholding for different detection sensitivity requirements
- **RTX 4070 compatible**: GNN inference on network-sized graphs is lightweight

## Limitations / 局限性

- Published as arXiv preprint (not peer-reviewed at time of processing)
- Synthetic training may not capture all real-world complexities
- Tested only on Northern California — generalizability to other regions unverified
- Uses PhaseNet picks as input — quality depends on picker performance
- No comparison with PhaseLink (Ross & Yue, 2019) — a competing deep-learning associator
- No quantitative analysis of false positive rate — 4.2x more events could include spurious detections
- Code not publicly available — implementation must be from paper description

## Typical Applications / 典型应用

| Task | Description | Representative Work |
|---|---|---|
| Phase Association | Assign phase picks to common earthquake sources | McBrearty & Beroza (2023) |
| Earthquake Detection | Detect events missed by operational catalogs | McBrearty & Beroza (2023) |

## Related Papers / 相关论文

- [[mcbrearty2023_genie_note]] — Primary source paper

## Related Methods / 相关方法

- [[PhaseNet]] — Phase picker providing input picks to GENIE
- [[EQTransformer]] — Alternative ML picker
- [[PhaseLink]] — Competing deep-learning associator (not compared in paper)
- [[Multi-task Learning]] — Alternative paradigm for joint prediction
