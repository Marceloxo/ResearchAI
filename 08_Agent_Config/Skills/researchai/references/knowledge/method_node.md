# SKILL: Method Node

## Purpose

Create Method knowledge nodes extracted from Paper Notes in the KnowledgeVault. Searches existing paper analyses to identify method concepts, extracts definitions and formulations, and creates structured method documentation.

## Input

```
<concept_name>
```

Example:
```
Attention Mechanism
```

## Output

Creates a Method node file in:
```
02_KnowledgeVault/03_Methods/<method_name>.md
```

Uses `Method_Template.md` as the output format.

## Preconditions

1. At least one Paper Note exists that discusses the method concept
2. Knowledge Node Check has been run and recommends "Create" for this concept, OR user explicitly requests method creation
3. Method name is unambiguous (not confused with similar concepts)
4. No existing Method node with the same name in `02_KnowledgeVault/03_Methods/`

If any precondition is not met: STOP and report the specific issue.

## Source Files

- `02_KnowledgeVault/01_Papers/*_note.md` — All paper notes (search for method mentions)
- `02_KnowledgeVault/00_Meta/Method_Map.md` — Existing method map (for cross-reference)
- `02_KnowledgeVault/03_Methods/` — Existing method nodes (for deduplication)
- `02_KnowledgeVault/Templates/Method_Template.md` — Output format reference

## Workflow

### Step 1 — Locate Sources

1. Search all paper notes for mentions of the method concept
2. Check Method_Map.md for existing entries
3. Check `02_KnowledgeVault/03_Methods/` for existing nodes
4. Identify all papers that discuss this method

If no source notes found: STOP — "No evidence found in existing paper notes."

### Step 2 — Deduplication Check

1. Check if a Method node with this name already exists
2. If exists: STOP — "Method node already exists. Offer to update instead."
3. Check for similar/overlapping method names (e.g., "Transformer" vs "Vision Transformer")
4. If ambiguous: FLAG for human review

### Step 3 — Extract Method Definition

From all source paper notes:
1. Identify the core definition of the method
2. Extract the key insight or innovation
3. Determine the method category (e.g., "Attention-Based Architecture", "Convolutional Network")
4. Synthesize a single-sentence definition

### Step 4 — Extract Architecture/Formulation

1. Identify the network structure or algorithmic formulation
2. Extract key mathematical equations
3. Note any architectural diagrams described in the notes
4. Document the input/output specification

### Step 5 — Extract Advantages

1. List claimed advantages from paper notes
2. Include comparative results (vs. other methods)
3. Note efficiency metrics (parameter count, speed, accuracy)
4. Identify domains where this method excels

### Step 6 — Extract Limitations

1. Identify author-admitted limitations
2. Note practical constraints (computational, data requirements)
3. Identify scenarios where the method underperforms

### Step 7 — Extract Related Papers

1. Collect all [[wikilinks]] to related papers from source notes
2. Identify papers that introduced the method
3. Identify papers that improved or extended the method
4. Identify papers that applied the method to new domains

### Step 8 — Extract Related Methods

1. Collect all [[wikilinks]] to related methods from source notes
2. Identify predecessor methods
3. Identify variants and extensions
4. Identify alternative methods solving similar problems

### Step 9 — Generate Execution Plan

Present plan to human:

```
Execution Plan:

Input:
  Method concept: <concept_name>
  Source notes: <list of paper notes>

Will create:
  02_KnowledgeVault/03_Methods/<method_name>.md

Will extract:
  - Method definition and category
  - Architecture/formulation details
  - Advantages and comparative results
  - Limitations and constraints
  - Related papers and methods (wikilinks)

Waiting for confirmation.
```

### Step 10 — Execute (After Confirmation)

1. Create Method node file using `Method_Template.md`
2. Fill all sections with extracted analysis
3. Update `Method_Map.md` with new entry
4. Update relevant paper notes with back-links to the method node
5. Update `Paper_Index.md` if needed

## Validation Rules

After creating the Method node, verify:

1. Definition is a single clear sentence
2. At least 1 advantage listed
3. At least 1 limitation identified
4. Related papers list has at least 1 entry
5. Related methods list has at least 1 entry (if available)
6. File is valid UTF-8 without BOM
7. No U+FFFD replacement characters
8. Wikilinks follow [[WikiLink]] format

## Failure Handling

| Condition | Action |
|---|---|
| Method name ambiguous | FLAG for human review |
| No source notes found | STOP — no evidence to extract from |
| Method already exists | STOP — offer update instead |
| Knowledge Node Check not run | FLAG — recommend running check first |

## Human Confirmation Points

1. After Step 9 (before Step 10): Present execution plan and wait for approval
2. If method name is ambiguous: Require human clarification before proceeding

## Constraints

- **Must use Knowledge Node Check**: Run Knowledge Node Check before creating a method node. If it recommends "Reuse" or "Wait", do not create.
- **Existing node triggers update suggestion**: If a method node already exists, offer to update rather than create duplicate.
- **Mode B (Semi-Automatic)**: No modifications before human confirmation.
- **Do NOT fabricate**: All content must be extracted from existing paper notes. If information is not found, mark as "Not Found Yet".
- **Do NOT modify templates**: Use Method_Template.md as-is.
- **All claims must be traceable** to existing KV files (paper notes).
