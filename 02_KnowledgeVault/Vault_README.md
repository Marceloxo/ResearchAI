# ResearchAI Knowledge Vault

## Bilingual Knowledge Base Design

This vault supports Chinese-English bilingual research workflows.

### Language Conventions

| Content Type | Language | Rationale |
|---|---|---|
| Technical terms, method names, model names | English | Universal academic standard |
| Paper titles, author names, venue names | English (original) | Preserve citability |
| Core concept definitions | English + Chinese annotation | Bilingual comprehension |
| Personal notes, reflections, interpretations | Chinese (or mixed) | Natural thought language |
| Task descriptions, research questions | Chinese primary, English terms inline | Clarity for the researcher |
| File names | English with underscores | Tool compatibility and search |
| Tags | English lowercase | Obsidian tag consistency |
| YAML frontmatter keys | English | Standard format |

### When to Use English vs. Chinese

- Write in Chinese when: expressing personal understanding, brainstorming, drafting internal notes.
- Write in English when: defining formal concepts, writing content intended for future publication, maintaining compatibility with international tools.
- Mixed usage is acceptable: Chinese sentences with English technical terms embedded (e.g., "使用 U-Net 进行 seismic fault segmentation").

---

## Navigation System

### Entry Point

The vault's navigation system lives in `00_Meta/`. Start from `[[Home]]` to access all vault areas.

### Navigation Layers

| Layer | Files | Purpose |
|---|---|---|
| **Home** | `Home.md` | Main entry point; links to all major sections |
| **Research Maps** | `Research_Map.md`, `Seismic_AI_Map.md`, `Deep_Learning_Map.md` | High-level research area overviews |
| **Knowledge Indices** | `Paper_Index.md`, `Method_Map.md`, `Dataset_Map.md` | Content indices for each knowledge type |
| **Workflow Indices** | `Idea_Index.md`, `Experiment_Index.md`, `Writing_System.md` | Indices for research workflow artifacts |
| **Reference** | `Tag_System.md`, `Linking_Rules.md` | Conventions and rules for vault maintenance |

### Navigation Flow

```
Home
 ├── Research_Map ──→ Seismic_AI_Map
 │                └──→ Deep_Learning_Map
 ├── Paper_Index
 ├── Method_Map
 ├── Dataset_Map
 ├── Idea_Index
 ├── Experiment_Index
 ├── Writing_System
 ├── Tag_System
 └── Linking_Rules
```

All MOC and index files link back to `[[Home]]` for consistent navigation.

---

## Knowledge Graph Strategy

### Graph Node Types

In Obsidian's Graph View, the following node types will emerge as content is added:

| Node Type | Source Directory | Prefix | Role in Graph |
|---|---|---|---|
| **Papers** | `01_Papers/` | `Paper - ` | Source knowledge — link to methods, tasks, datasets |
| **Methods** | `03_Methods/` | `Method - ` | Core technical knowledge — linked by papers and experiments |
| **Tasks** | `04_Tasks/` | `Task - ` | Problem definitions — link methods and datasets |
| **Datasets** | `05_Datasets/` | `Dataset - ` | Data resources — linked by papers and experiments |
| **Experiments** | `06_Experiments/` | `Exp - ` | Empirical evidence — link methods, datasets, ideas |
| **Ideas** | `07_Ideas/` | `Idea - ` | Forward-looking — link to papers, methods, experiments |
| **Writing** | `08_Writing/` | `Writing - ` | Output layer — link to papers, experiments, ideas |
| **MOC/Index** | `00_Meta/` | Various | Navigation hubs — aggregate links to content nodes |

### Expected Graph Evolution

1. **Early stage** (now): MOC and index files form the skeleton. Most [[wikilinks]] are to placeholder nodes that don't exist yet.
2. **Growth stage**: As papers are added, method and task nodes are created. The graph develops clusters around research areas.
3. **Mature stage**: Dense interconnection between papers, methods, experiments, and ideas. The graph becomes a navigable research map.

### Graph Health Checks

- **Orphan nodes**: Notes with zero incoming links. Indicates knowledge that hasn't been connected.
- **Super-hub nodes**: A few nodes that link to everything. Consider splitting or using tags instead.
- **Isolated clusters**: Groups of notes disconnected from the main graph. May indicate a new research area or missing cross-links.

---

## Obsidian Link Rules

### Internal Links (Wikilinks)

Use `[[wikilink]]` syntax for all internal vault links.

```
[[Paper - Seismic Fault Segmentation with 3D CNNs]]
[[Method - U-Net]]
[[Topic - Seismic Interpretation]]
```

### Link Target Rules

- Always link to the exact note title.
- Use `[[Note Title|display text]]` for display aliases.
- Use `[[Note Title#heading]]` to link to specific sections.
- Prefer direct links over folder-path references; let Obsidian resolve by title.

### Cross-Vault Links

For content outside the vault (e.g., papers in `01_Literature/`, code in `03_Projects/`), use full paths:

```
[Paper PDF](/home/lco/ResearchAI/01_Literature\PDFs\paper.pdf)
[Project Code](/home/lco/ResearchAI/03_Projects\SeismicFaultSegmentation)
```

---

## Tag Rules

### Flat Tag Hierarchy

Use flat, semantic tags. No nested tags unless a clear hierarchy exists.

```
#seismic #fault-segmentation #cnn #unet #attention #transfer-learning
#dataset #synthetic #field-data #benchmark
#todo #in-progress #done #key-paper #to-read
#method #experiment #idea #writing #question
```

### Tag Naming Conventions

- All lowercase.
- Use hyphens for multi-word tags (`#fault-segmentation`, not `#fault_segmentation` or `#FaultSegmentation`).
- Keep tags atomic: prefer `#cnn` and `#segmentation` over `#cnn-segmentation` (combine with search).
- Reserve `#todo`, `#in-progress`, `#done` for workflow tracking.
- Reserve `#key-paper` for papers of exceptional importance.

### Tag Usage per Note

- Every note must have at least 1 topic tag.
- Paper notes should include method tags and task tags.
- Method notes should include the method family tag.
- Experiment notes should link to their parent task/method.

See `[[Tag_System]]` for the complete tag specification.

---

## File Naming Rules

### General Rules

- Use English for all file names.
- Use underscores as word separators (not spaces or hyphens).
- Keep names descriptive but concise.
- Avoid special characters (`:`, `/`, `\`, `?`, `*`, etc.).

### Category-Specific Prefixes

| Category | Prefix | Example |
|---|---|---|
| Papers | `Paper - ` | `Paper - U-Net Biomedical Image Segmentation` |
| Topics | `Topic - ` | `Topic - Seismic Fault Detection` |
| Methods | `Method - ` | `Method - Attention U-Net` |
| Tasks | `Task - ` | `Task - 3D Seismic Fault Segmentation` |
| Datasets | `Dataset - ` | `Dataset - Thebe Fault Benchmark` |
| Experiments | `Exp - ` | `Exp - UNet Baseline on Thebe` |
| Ideas | `Idea - ` | `Idea - Multi-Scale Fault Detection` |
| Writing | `Writing - ` | `Writing - Literature Review Draft` |

### MOC (Map of Content) Files

MOC files are index pages that aggregate links. Use descriptive names with underscores:

```
Research_Map.md
Seismic_AI_Map.md
Deep_Learning_Map.md
Method_Map.md
```

### Template Files

Templates live in `Templates/` and use descriptive names:

```
Literature_Card_Template.md
Paper_Template.md
Method_Template.md
```

---

## YAML Frontmatter

Every note should include YAML frontmatter for structured metadata.

### Paper Note Frontmatter

```yaml
---
title: "Paper Title"
authors: [Author 1, Author 2]
year: 2024
venue: Journal/Conference
doi: 10.xxxx/xxxxx
tags: [key-paper, seismic, fault-segmentation, cnn]
status: done
created: 2026-07-08
---
```

### General Note Frontmatter

```yaml
---
tags: [topic-tag, method-tag]
status: in-progress
created: 2026-07-08
updated: 2026-07-08
---
```

---

## Maintenance

- Review and update MOC files when adding new notes.
- Run periodic tag audits to prevent tag sprawl.
- Archive outdated notes rather than deleting them.
- Keep `00_Meta/` up to date with vault structure changes.
- See `[[Linking_Rules]]` for link maintenance guidelines.
