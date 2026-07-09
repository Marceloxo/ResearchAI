---
tags: [meta, linking-rules]
created: 2026-07-08
---

# Linking Rules / 链接规则

This document defines how notes connect to form a navigable knowledge graph. Good links are intentional — they capture meaningful relationships, not just co-occurrence.

---

## The Knowledge Pipeline / 知识管道

Notes flow through a directional pipeline. Links should reflect this direction:

```
Paper
  ↓
Task (what problem does this paper solve?)
  ↓
Method (how does it solve it?)
  ↓
Dataset (what data is used?)
  ↓
Experiment (how was it tested?)
  ↓
Idea (what gaps remain? what can we try?)
  ↓
Writing (how do we communicate findings?)
```

---

## Link Types / 链接类型

### 1. Hierarchical Links / 层级链接

From specific to general, or general to specific.

```
[[CNN]] → [[Deep Learning]]
[[Fault Segmentation]] → [[Seismic AI]]
[[U-Net]] → [[CNN]]
```

### 2. Associative Links / 关联链接

Between related concepts at the same level.

```
[[U-Net]] ↔ [[Attention U-Net]]
[[Fault Segmentation]] ↔ [[Seismic Denoising]]
```

### 3. Dependency Links / 依赖链接

When one note's content depends on understanding another.

```
[[Paper - U-Net]] → [[Method - U-Net]]
[[Experiment - UNet Baseline]] → [[Method - U-Net]]
[[Experiment - UNet Baseline]] → [[Dataset - DeepFault]]
```

### 4. Derivation Links / 派生链接

When one note was inspired by or derived from another.

```
[[Idea - Multi-Scale Fault Detection]] → [[Paper - U-Net]]
[[Idea - Multi-Scale Fault Detection]] → [[Exp - UNet Baseline]]
```

---

## Link Direction Conventions / 链接方向约定

| From | To | Relationship |
|---|---|---|
| Paper | Task | Paper addresses a task |
| Paper | Method | Paper uses/proposes a method |
| Paper | Dataset | Paper uses a dataset |
| Task | Method | Task is solved by method |
| Task | Dataset | Task has benchmark datasets |
| Method | Method | Method is a variant/improvement of |
| Experiment | Method | Experiment tests a method |
| Experiment | Dataset | Experiment uses a dataset |
| Experiment | Task | Experiment evaluates on a task |
| Idea | Paper | Idea was inspired by paper |
| Idea | Method | Idea involves a method |
| Idea | Experiment | Idea was tested by experiment |
| Writing | Paper | Writing cites a paper |
| Writing | Experiment | Writing reports experiment results |

---

## What NOT to Link / 不应链接的内容

Do not create links that are:

- **Obvious**: Don't link `[[CNN]]` from every paper that mentions CNN. Only link when the relationship is substantive.
- **Vague**: Don't link `[[Deep Learning]]` from every note. That's what tags are for.
- **Redundant**: If Note A links to Note B, and Note B links to Note C, don't force A → C unless it's a direct relationship.

---

## Link Maintenance / 链接维护

1. When creating a new note, always add the appropriate links from the table above.
2. When a note's content changes, review whether its links are still accurate.
3. Use Obsidian's Graph View periodically to spot orphan notes (no incoming links) and isolated clusters.
4. MOC pages in `00_Meta/` should be updated when new notes are added to their category.

---

## Graph View Strategy / 图谱视图策略

In Obsidian's Graph View, the expected structure over time:

- **Hub nodes** (large, many connections): MOC files, major methods (U-Net, Transformer), key tasks.
- **Cluster nodes** (medium, within-domain connections): Papers in the same subfield, experiments on the same task.
- **Leaf nodes** (small, few connections): Individual ideas, writing plans, paper logic analyses.

A healthy graph has:
- No orphan nodes (zero connections).
- Few "super-hub" nodes that connect to everything indiscriminately.
- Distinct clusters for different research areas that are connected through cross-cutting method nodes.

---

## Navigation / 导航

- Back to [[Home]]
- See also: [[Tag_System]]
- See also: [[Vault_README]]
