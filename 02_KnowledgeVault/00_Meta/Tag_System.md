---
tags: [meta, tag-system]
created: 2026-07-08
---

# Tag System / 标签系统

ResearchAI uses a flat, semantic tag system for filtering and retrieval. Tags are for **classification**; [[wikilinks]] are for **relationships**.

---

## Design Principles / 设计原则

1. **Flat over nested**: Use flat tags (`#fault-segmentation`) rather than nested (`#seismic/fault/segmentation`). Flat tags are easier to search, combine, and maintain.
2. **Atomic over compound**: Prefer `#cnn` and `#segmentation` over `#cnn-segmentation`. You can combine tags in search.
3. **Stable over evolving**: Once a tag is established, don't rename it without updating all tagged notes.
4. **Fewer is better**: Start with minimal tags. Add new ones only when a clear category emerges.

---

## Tag Categories / 标签分类

### Domain / 领域

| Tag | Meaning |
|---|---|
| `#seismic-ai` | Seismic data processing with AI |
| `#computer-vision` | General computer vision |
| `#deep-learning` | Deep learning methods and theory |
| `#geoscience` | Geoscience applications |

### Task / 任务类型

| Tag | Meaning |
|---|---|
| `#segmentation` | Semantic/instance segmentation |
| `#denoising` | Noise removal |
| `#reconstruction` | Data reconstruction |
| `#classification` | Classification tasks |
| `#detection` | Object detection |
| `#inversion` | Geophysical inversion |

### Method / 方法

| Tag | Meaning |
|---|---|
| `#cnn` | Convolutional neural networks |
| `#transformer` | Transformer architectures |
| `#attention` | Attention mechanisms |
| `#frequency-domain` | Frequency domain methods |
| `#gan` | Generative adversarial networks |
| `#diffusion` | Diffusion models |

### Status / 状态

| Tag | Meaning |
|---|---|
| `#to-read` | Paper not yet read |
| `#reading` | Currently reading |
| `#done` | Completed reading/analysis |
| `#key-paper` | Exceptionally important paper |
| `#implemented` | Method has been implemented |
| `#published` | Work has been published |

### Meta / 元信息

| Tag | Meaning |
|---|---|
| `#meta` | Navigation and system files |
| `#navigation` | MOC and index pages |
| `#template` | Template files |

---

## Tag Usage Rules / 标签使用规则

1. Every note must have at least **one domain tag** and **one status tag**.
2. Paper notes should include relevant **task tags** and **method tags**.
3. Method notes should include the **method family tag** (e.g., `#cnn`, `#transformer`).
4. Experiment notes should include **task**, **method**, and **dataset** tags.
5. Idea notes should include the **domain** and **task** tags.

---

## Tag vs. Wikilink / 标签 vs. 链接

| Purpose | Tool | Example |
|---|---|---|
| "What category is this?" | Tag | `#seismic-ai` |
| "What is this related to?" | Wikilink | `[[U-Net]]` |
| "Show me all fault segmentation papers" | Tag search | Search `#fault-segmentation` |
| "Show me everything about U-Net" | Backlinks | Check `[[U-Net]]` backlinks |

Tags are for **filtering**. Wikilinks are for **knowledge graph navigation**.

---

## Adding New Tags / 添加新标签

Before creating a new tag, ask:

1. Does an existing tag already cover this?
2. Will this tag apply to at least 5 notes?
3. Is this tag clearly distinct from existing tags?

If yes, add it to the appropriate section above and document it here.

---

## Navigation / 导航

- Back to [[Home]]
- See also: [[Linking_Rules]]
