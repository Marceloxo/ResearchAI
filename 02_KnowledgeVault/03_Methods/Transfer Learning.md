---
method_name: "Transfer Learning"
category: "Domain Adaptation Technique"
application: ["Seismic Phase Picking", "Image Segmentation", "Time Series Classification"]
related_tasks: ["Seismic Phase Picking", "Seismic Image Segmentation"]
tags: [transfer-learning, domain-adaptation, deep-learning]
created: 2026-07-09
---

# Definition
Transfer learning adapts a pre-trained model to a new domain with minimal additional training data.

# Core Idea
Instead of training a model from scratch, initialize weights from a model trained on a source domain, then fine-tune on a small target domain dataset.

# Architecture / Formulation
- **Source Model**: Pre-trained on large source dataset
- **Initialization**: Copy weights from source model
- **Fine-tuning**: Train on small target dataset with all layers updated
- **Data Efficiency**: Often requires only 0.1-1% of original training data

# Advantages
- Dramatically reduces required training data
- Faster training convergence
- Leverages knowledge from related domains
- Particularly effective when source and target domains share similar structure

# Limitations
- Requires some labeled target data for fine-tuning
- Performance depends on similarity between source and target domains
- May not work well across very different domains (e.g., images vs. seismic)

# Typical Applications
| Task | Description | Representative Work |
|---|---|---|
| Seismic Phase Picking | Adapting PhaseNet across scales | Chai et al. (2020) |
| Image Segmentation | Domain adaptation for medical imaging | Various |
| Time Series | Transfer across different sensors | Various |

# Related Papers
- [[chai2020_using_note]] 鈥?Demonstrates TL across 3 orders of magnitude in scale

# Related Methods
- [[PhaseNet]] 鈥?DNN model transferred via TL
- [[Domain Adaptation]] 鈥?Related technique
- [[Self-Supervised Learning]] 鈥?Alternative for limited-label scenarios

