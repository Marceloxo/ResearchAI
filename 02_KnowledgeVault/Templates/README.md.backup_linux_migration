# Templates — Obsidian Note Templates

## Purpose

Obsidian-compatible templates for creating consistent, structured notes across the vault. Templates ensure that every note of a given type contains the expected sections, YAML frontmatter, and cross-linking structure.

## Template Inventory

| Template | Use Case | Target Directory | When to Use |
|---|---|---|---|
| `Literature_Card_Template.md` | Rapid paper screening (50-100 papers) | `01_Papers/` | First-pass filtering before deciding what to deep-read |
| `Paper_Template.md` | Deep paper reading and analysis | `01_Papers/` | Full analysis of a paper after Literature Card screening |
| `Method_Template.md` | Method/algorithm knowledge base | `03_Methods/` | Documenting a method: U-Net, Transformer, Attention, etc. |
| `Task_Template.md` | Research task definition | `04_Tasks/` | Defining a research problem: input, output, metrics, SOTA |
| `Dataset_Template.md` | Dataset registry | `05_Datasets/` | Documenting a dataset: format, scale, benchmarks, limitations |
| `Experiment_Template.md` | Experiment interpretation | `06_Experiments/` | Recording what was tested, why, and what was learned |
| `Idea_Template.md` | Research idea management | `07_Ideas/` | Capturing a research gap → proposed solution → experiment plan |
| `Writing_Template.md` | Manuscript planning | `08_Writing/` | Outlining a paper: story, introduction flow, experiments |
| `Paper_Logic_Template.md` | Argument Mining — paper structure reverse-engineering | `09_Paper_Logic/` | Analyzing how a research paper constructs its argument (9 sections, evidence mapping) |
| `Survey_Template.md` | Survey/review paper analysis | `01_Papers/` | Taxonomy extraction, coverage analysis, future directions |

## Recent Updates

### Stage 1.4A.1

#### Paper_Template.md
- Added `paper_type` YAML field: `research_article` | `survey` | `review` | `benchmark`
- Added "# Paper Type" section at the top — different paper types require different analysis approaches

#### Dataset_Template.md
- Added `source_type` YAML field: `mentioned_in_paper` | `personally_used` | `reproduced` | `benchmark_target`
- Added "# Relationship to Current Research" section with provenance checkboxes
- Prevents AI agents from claiming datasets are "used" when they are only "mentioned in paper"

### Stage 1.5-4

#### Paper_Logic_Template.md — Full Rewrite (Argument Mining)
- Upgraded from simple structure analysis to full Argument Mining framework
- 9 sections: Research Problem, Research Gap, Core Claim, Evidence Mapping, Method Justification, Limitation Analysis, Transferable Ideas, Writing Strategy, Paper-to-Own-Research Bridge
- Evidence Mapping table maps Claim → Evidence → Experiment → Metric → Result with support indicators (✔/✘/⚠️)
- Method Justification requires motivation, design rationale, supporting evidence, and alternatives considered for each module
- Limitation Analysis distinguishes author-admitted limitations from hidden limitations (reviewer perspective)
- Writing Strategy analyzes paragraph-by-paragraph structure, figure design lessons, and argument flow
- Paper-to-Own-Research Bridge converts analysis into actionable research items
- All Research Articles must now use this Argument Mining format

## AI Agent Template Selection Guide

When an AI agent needs to create a note, follow this decision tree:

1. **Is this about a single paper?**
   - Quick screening → `Literature_Card_Template.md`
   - Deep analysis → `Paper_Template.md`
   - Structural/argument analysis of a research article → `Paper_Logic_Template.md`
   - Survey/review paper → `Survey_Template.md`

2. **Is this about a concept/technique?**
   - Algorithm/method/architecture → `Method_Template.md`
   - Research problem definition → `Task_Template.md`

3. **Is this about data?**
   - Dataset documentation → `Dataset_Template.md`

4. **Is this about an experiment?**
   - Experiment interpretation → `Experiment_Template.md`

5. **Is this about a new idea?**
   - Research idea → `Idea_Template.md`

6. **Is this about writing a paper?**
   - Manuscript planning → `Writing_Template.md`

## Knowledge Network: How Templates Connect

```
Literature_Card ──────(promoted)────▶ Paper ─────(methods go to)────▶ Method
                    ├────(tasks go to)─────────────────▶ Task
                    ├────(datasets go to)──────────────▶ Dataset
                    └────(structure to)────────────────▶ Paper_Logic

Paper ─────(gaps found)────▶ Idea ─────(tested via)────▶ Experiment
                                Experiment ─────(reports)────▶ Writing

Task ←── Method ←── Dataset ←── Experiment
  └─────────────────────────────────────────────────────────┘
        All linked via [[wikilinks]]
```

## Usage

In Obsidian, configure this folder as the template directory (Settings → Templates → Template folder location). Then use "Insert template" when creating new notes.

## AI Agent Usage

1. Before creating any new note, read the appropriate template from this directory.
2. Populate all YAML frontmatter fields — these are the structured metadata that enable future retrieval.
3. Fill in `[[wikilinks]]` to related notes at the bottom of each template — this is what builds the knowledge network.
4. If a template doesn't fit the content, choose the closest match rather than writing freeform.
5. **Always check `source_type`** in dataset notes — never assume a dataset is "used" just because it has a note.
6. **Always check `paper_type`** in paper notes — survey papers require different analysis than research articles.
7. **All Research Articles must generate an Argument Mining Paper Logic** using the upgraded `Paper_Logic_Template.md` (Stage 1.5-4).
