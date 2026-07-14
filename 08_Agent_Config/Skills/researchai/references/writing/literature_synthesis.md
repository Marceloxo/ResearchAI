# SKILL: Literature Synthesis

## Purpose

Generate writing materials and literature review content from the KnowledgeVault.

## Input

```
<topic>
```

Example:
```
Transformer in Seismic AI
```

## Permission Model

**Semi-Automatic Mode (Mode B)** — Outline shown before any file creation.

## Workflow

### Step 1 — Define Scope

Parse the topic and identify:
- Related methods (Transformer, ViT, Attention Mechanism)
- Related tasks (Seismic Phase Picking, Seismic Image Segmentation)
- Related papers in KnowledgeVault

### Step 2 — Gather Sources

Read relevant files from KnowledgeVault:
1. Literature Cards — for paper summaries and classifications
2. Paper Notes — for detailed method analysis
3. Survey Notes — for taxonomy and coverage
4. Knowledge Nodes — for method/task/dataset definitions
5. Paper Logic — for argument mining and gap analysis

### Step 3 — Generate Outline

Present to human:

```
Literature Synthesis Outline:

Topic: <topic>

Structure:
1. Historical Evolution
   - Early methods (pre-2020)
   - Transition period (2020-2023)
   - Recent advances (2023+)

2. Current Methods
   - Method A: <summary>
   - Method B: <summary>
   - Method C: <summary>

3. Comparison
   - Accuracy comparison table
   - Efficiency comparison table
   - Dataset coverage

4. Research Gaps
   - Gap 1: <description>
   - Gap 2: <description>

5. Future Directions
   - Direction 1: <description>
   - Direction 2: <description>

6. References
   - <N> papers from KnowledgeVault
   - <N> external references

Source papers: <list of wikilinks>

Waiting for confirmation.
```

### Step 4 — Generate Content (After Confirmation)

Create content file in:
```
02_Writing/<topic_slug>_synthesis.md
```

Content structure:
1. **Historical Evolution**: Timeline of method development
2. **Current Methods**: Detailed analysis of each method
3. **Comparison**: Tables comparing methods on key metrics
4. **Research Gaps**: Identified gaps from paper analysis
5. **Future Directions**: Promising research avenues
6. **References**: Cited papers with wikilinks

### Step 5 — Quality Check

After generation:
1. Verify all wikilinks resolve
2. Check for fabricated information (must be from actual papers)
3. Ensure no hallucinated results or claims
4. Confirm all data sourced from KnowledgeVault

## Constraints

- Do NOT create final manuscripts automatically
- Do NOT fabricate citations or results
- Do NOT modify existing papers or notes
- Do NOT create knowledge nodes
- All claims must be traceable to existing KV files

## Error Handling

| Condition | Action |
|---|---|
| No relevant papers found | STOP — insufficient source material |
| Wikilink broken | Flag for human review |
| Insufficient detail | Recommend expanding source collection |
