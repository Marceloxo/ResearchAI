---
method_name: "Multi-task Learning"
category: "Training Paradigm"
application: ["Phase Picking", "Phase Association", "Earthquake Location", "Seismic Monitoring"]
related_tasks: ["Seismic Phase Picking", "Phase Association", "Earthquake Location"]
tags: [multi-task-learning, joint-training, shared-representation, seismic-monitoring, plan]
created: 2026-07-19
---

# Definition / 定义

Multi-task learning (MTL) is a training paradigm where a single model is optimized to perform multiple related tasks simultaneously, sharing representations across tasks. In seismic monitoring, MTL is used to jointly optimize phase picking, phase association, and earthquake location — tasks that are inherently interdependent.

# Core Idea / 核心思想

Traditional seismic monitoring uses a sequential pipeline: pick phases → associate picks to sources → locate events. Errors at each stage propagate downstream. MTL eliminates this cascade by training a single model on all tasks at once, sharing intermediate representations. The key insight is that the tasks are not independent — phase picking accuracy affects association quality, which affects location precision, and vice versa. Joint optimization allows gradients from all tasks to improve the shared representation.

# Architecture / Formulation / 架构/公式

## General MTL Objective

```
L_total = sum_i lambda_i * L_i(task_i)
```

Where lambda_i are task-specific weighting coefficients (often set to 1 for equal contribution).

## PLAN Implementation (Si et al., 2024)

Six loss terms with equal weighting:
```
L_total = L_picking-p + L_picking-s + L_Delta_p + L_Delta_s + L_offset + L_depth
```

- Picking losses: MSE between predicted and Gaussian-target pick times
- Association losses: Absolute difference between predicted and catalog time shifts
- Location losses: MSE between predicted and catalog offset/depth

## Shared Representation Benefits

- **Feature sharing**: Waveform encoder serves all tasks simultaneously
- **Gradient regularization**: Multiple loss signals prevent overfitting to any single task
- **Implicit task coupling**: The model learns that good picks enable good associations, which enable good locations
- **Parameter efficiency**: One model replaces three separate models

## Advantages / 优势

- **Eliminates error cascade**: No sequential pipeline where errors accumulate
- **Parameter efficiency**: Single shared model vs. multiple task-specific models
- **Implicit regularization**: Multiple loss signals reduce overfitting
- **Captures task interdependence**: Model learns that picking, association, and location are coupled
- **Simplified deployment**: One model to maintain and serve

## Limitations / 局限性

- **Task balancing**: Equal weighting (lambda=1) may not be optimal; harder tasks may dominate gradients
- **Catastrophic interference**: Tasks may compete for representational capacity
- **Complexity**: Designing shared architecture that serves all tasks well is non-trivial
- **Evaluation difficulty**: Harder to isolate which task drives overall performance
- **Hyperparameter sensitivity**: Loss weighting scheme significantly impacts results

## Typical Applications / 典型应用

| Task Combination | Description | Representative Work |
|---|---|---|
| Picking + Association + Location | Full monitoring pipeline | Si et al. (2024) PLAN |
| Detection + Classification | Joint event detection and type classification | Various |
| Segmentation + Classification | Pixel-wise prediction with scene-level labels | CV literature |

## Related Papers / 相关论文

- [[si2024_plan_allinone_note]] — Primary seismic MTL application

## Related Methods / 相关方法

- [[PLAN]] — Seismic monitoring implementation of MTL
- [[Transfer Learning]] — Alternative paradigm for leveraging pre-trained representations
- [[Self-Supervised Learning]] — Related approach for limited-label scenarios
