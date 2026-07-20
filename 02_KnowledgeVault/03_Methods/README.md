# 03_Methods — Method and Algorithm Descriptions

## Purpose

Detailed, structured descriptions of research methods and algorithms. Each note defines a single method, its variants, its mathematical foundation, and its typical use cases.

## Contents

- Method definition notes (e.g., `Method - U-Net`, `Method - Attention Mechanism`).
- Mathematical formulations and key equations.
- Pseudocode or algorithm descriptions.
- Comparisons with related methods.
- Implementation notes and common pitfalls.
- Links to papers that introduced or significantly advanced the method.

## Relationship to Other Directories

- Referenced by paper notes in `01_Papers/`.
- Aggregated by topic notes in `02_Topics/`.
- Used by task notes in `04_Tasks/` to describe solution approaches.
- Implemented in projects under `03_Projects/` (external to vault).
- Tested in experiments tracked in `06_Experiments/`.
- Forms part of paper logic chains in `09_Paper_Logic/`.

## AI Agent Usage

1. When a paper proposes a new method, create a method note here (or update an existing one).
2. Maintain a "family tree" of method variants (e.g., U-Net → Attention U-Net → U-Net++).
3. When asked to compare methods, consult this directory and generate structured comparisons.
4. Link method notes to their implementations in `03_Projects/`.

## Knowledge Node Files

- [[Attention Mechanism]] — Attention mechanisms for seismic data
- [[CNN]] — Convolutional Neural Networks for seismic image processing
- [[GENIE]] — GNN-based phase association and earthquake detection
- [[Multi-task Learning]] — Joint optimization of multiple seismic tasks
- [[PhaseNet]] — Deep learning seismic phase picker
- [[PLAN]] — All-in-one multi-station GNN for picking, association, location
- [[ResNet]] — Residual networks for seismic classification
- [[SegFormer]] — Hierarchical Transformer encoder for segmentation
- [[Swin Transformer]] — Shifted window Transformer for seismic imagery
- [[Transfer Learning]] — Pre-trained model adaptation for seismic tasks
- [[Transformer]] — Self-attention architecture for seismic signal processing
- [[U-Net]] — Encoder-decoder segmentation for seismic fault detection
- [[U-SegFormer-Hyper]] — Lightweight U-shaped Transformer for seismic facies segmentation
- [[Vision Transformer]] — Vision Transformer for seismic image analysis
