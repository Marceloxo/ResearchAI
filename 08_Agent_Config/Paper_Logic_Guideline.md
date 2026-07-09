# Paper Logic Guideline — Argument Mining Standard

## Purpose

This guideline defines the **mandatory standard** for generating Paper Logic notes in the ResearchAI KnowledgeVault. It replaces the earlier simple structure-analysis approach with a rigorous **Argument Mining** framework.

## Scope

**Applies to:**
- All **Research Articles** processed through the pipeline (after Stage 1.5-3).
- Any future paper classified as `paper_type: research_article` in the Literature Card.

**Does NOT apply to:**
- Survey/Review papers → use `Survey_Template.md` instead.
- Literature Cards → these are screening notes, not deep analysis.

## Core Philosophy

A Paper Logic note is NOT a summary. It is a **structural deconstruction** of how the paper builds its argument, with explicit mapping between claims and evidence.

The goal is to enable future AI agents to:
1. Understand why the paper's design decisions were made.
2. Identify gaps that the paper did NOT address.
3. Extract transferable ideas for our own research.
4. Learn writing strategies for our own manuscripts.

## Mandatory Sections

Every Paper Logic note MUST contain all 9 sections:

### 1. Research Problem
- One-sentence problem statement.
- Why it matters (who is affected, what is at stake).

### 2. Research Gap
- Classification of existing methods.
- Specific deficiencies (at least 2-3).
- How the paper argues the gap exists.

### 3. Core Claim
- Main claim (the paper's central thesis).
- Supporting claims (usually 2-3 sub-claims).

### 4. Evidence Mapping (CRITICAL)
- Table mapping: Claim → Evidence Type → Experiment → Metric → Result → Support status.
- Support indicators: ✔ (fully supported), ✘ (not supported), ⚠️ (partially supported with caveats).
- This is the core of Argument Mining — every claim must be traced to evidence.

### 5. Method Justification
- For EACH major module/component:
  - Motivation: what problem does it solve?
  - Design Choice: why this approach?
  - Evidence: which result supports it?
  - Alternatives: what was considered and rejected?

### 6. Limitation Analysis
- Author-admitted limitations (from the paper).
- Hidden limitations (reviewer perspective — what the paper missed).
- Unanswered questions.

### 7. Transferable Research Ideas
- Directly transferable designs with target tasks.
- Inspiration for new ideas with feasibility assessment.

### 8. Writing Strategy Analysis
- Paragraph-by-paragraph breakdown of the Introduction.
- Method presentation strategy (WHY before WHAT?).
- Experiment strategy (fair baselines? comprehensive ablation?).
- Figure design lessons.
- Overall argument flow diagram.

### 9. Paper-to-Own-Research Bridge
- What we can learn.
- What we can improve.
- Specific action items (checklist format).

## Quality Checklist

Before saving a Paper Logic note, verify:

- [ ] Every claim in §3 has at least one corresponding entry in §4 Evidence Mapping.
- [ ] Evidence Mapping includes support status (✔/✘/⚠️) for each entry.
- [ ] §5 Method Justification covers ALL major modules, not just the novelty.
- [ ] §6 includes at least one hidden limitation (not just author-admitted ones).
- [ ] §7 identifies at least one directly transferable idea.
- [ ] §8 includes an argument flow diagram.
- [ ] §9 has at least 2 actionable items.

## YAML Frontmatter

```yaml
paper: \"citation_key_or_paper_id\"
venue: \"Venue Name\"
research_field: \"Field Name\"
tags: [paper-logic, argument-mining, <domain-tag>]
created: YYYY-MM-DD
```

## File Naming Convention

```
<lowercase_author><year>_<short_topic>_paper_logic.md
```

Examples:
- `chai2020_transfer_learning_phase_picking_paper_logic.md`
- `he2016_resnet_paper_logic.md`

## Relationship to Other Knowledge Nodes

A Paper Logic note links to:
- **Method** notes (§5 modules)
- **Task** notes (§1 problem domain)
- **Dataset** notes (§4 experiments)
- **Experiment** notes (§4 evidence)
- **Idea** notes (§7 transferable ideas)

These links are populated in the \"# Related Knowledge\" section at the bottom of the template.

## Historical Note

The old Paper Logic format (pre-Stage 1.5-4) contained:
- Research Question
- Paper Story
- Introduction Logic
- Method Logic
- Experiment Logic
- Writing Lessons

This format was replaced because it lacked:
- Explicit claim-evidence mapping
- Support status indicators
- Hidden limitation analysis
- Transferable idea extraction
- Actionable research bridge

Existing Paper Logic notes generated with the old format should be regenerated using this new standard when practical.

## Agent Enforcement Rule

**When an AI agent processes a Research Article:**

1. After creating the Literature Card and Paper Note, check if a Paper Logic note exists.
2. If it does NOT exist → create one using `Paper_Logic_Template.md`.
3. If it exists but was generated with the old format → flag it for regeneration (do not auto-regenerate).
4. The Paper Logic note is REQUIRED before the paper can be marked as \"fully processed.\"
