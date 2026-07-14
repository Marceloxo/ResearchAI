# SKILL: Knowledge Node Check

## Purpose

Prevent unnecessary knowledge node creation by checking if a concept already exists.

## Input

```
<concept_name>
```

Example:
```
ChangeFormer
```

## Permission Model

**Read-only** — This skill never creates or modifies files.

## Workflow

### Step 1 — Parse Concept Name

Extract the concept name. Normalize:
- Convert to lowercase
- Remove special characters
- Handle abbreviations (e.g., "ViT" → "vision_transformer")

### Step 2 — Search Existing Nodes

Check the following directories for matching concepts:

| Directory | Check |
|---|---|
| `02_KnowledgeVault/03_Methods/` | Algorithm/method names |
| `02_KnowledgeVault/04_Tasks/` | Task definitions |
| `02_KnowledgeVault/05_Datasets/` | Dataset names |
| `02_KnowledgeVault/02_Topics/` | Topic definitions |
| `02_KnowledgeVault/07_Ideas/` | Research ideas |

Search by:
1. Exact filename match
2. Title/content keyword match
3. Common abbreviation match

### Step 3 — Evaluate Criteria

For each potential match, assess:

| Criterion | Weight | Description |
|---|---|---|
| Multiple paper usage | High | Does the concept appear in ≥2 papers? |
| Seismic AI relevance | High | Is it relevant to seismic image processing? |
| Transfer value | Medium | Can insights transfer to our research? |
| Concept maturity | Medium | Is this a stable, established concept? |

### Step 4 — Generate Recommendation

Output one of three recommendations:

#### Option A: Reuse Existing Node

```
Recommendation: Reuse Existing Node

Found: 03_Methods/Transformer.md
Match: Concept "Transformer" already exists and is referenced by 5 papers.
Action: Add wikilink [[Transformer]] instead of creating new node.
```

#### Option B: Create New Node

```
Recommendation: Create New Node

Justification:
- Appears in 2+ papers: Yes (ChangeFormer in bandara2022, fang2022)
- Seismic AI relevance: Medium (change detection patterns)
- Transfer value: High (siamese transformer architecture)
- Concept maturity: High (published in CVPR Workshops)

Suggested file: 03_Methods/ChangeFormer.md
Suggested wikilink: [[ChangeFormer]]
```

#### Option C: Wait for More Evidence

```
Recommendation: Wait for More Evidence

Reason:
- Appears in only 1 paper: Yes (only in bandara2022)
- Insufficient cross-paper validation
- Recommend processing 1-2 more papers before creating node

Action: Flag for review after next batch.
```

## Constraints

- Never automatically create nodes
- Always present recommendation for human decision
- Consider cross-directory matches (e.g., a method might be in Tasks/)
- Account for naming variations (abbreviations, synonyms)

## Error Handling

| Condition | Action |
|---|---|
| No matches found | Option B or C depending on criteria |
| Multiple matches found | Present all options to human |
| Ambiguous concept | Flag for human clarification |
