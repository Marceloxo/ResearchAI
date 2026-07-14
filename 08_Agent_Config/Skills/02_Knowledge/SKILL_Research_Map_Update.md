# SKILL: Research Map Update

## Purpose

Maintain and update the Research Map navigation files in the KnowledgeVault meta directory.

## Input

```
<map_name>
<update_description>
```

Map names:
- `Research_Map` — General research progress map
- `Deep_Learning_Map` — DL method taxonomy and progress
- `Seismic_AI_Map` — Seismic AI specific maps

Example:
```
Seismic_AI_Map
Add new section: Transformer-based methods for seismic phase picking
```

## Permission Model

**Semi-Automatic Mode (Mode B)** — Preview shown before any modifications.

## Workflow

### Step 1 — Locate Target File

Map files location:
```
02_KnowledgeVault/00_Meta/<map_name>.md
```

Verify file exists. If not: STOP — map file not found.

### Step 2 — Analyze Current Structure

Read the existing map file and identify:
- Current sections and subsections
- Existing paper references (wikilinks)
- Structural patterns (headings, tables, lists)

### Step 3 — Generate Update Preview

Present to human:

```
Existing file: 02_KnowledgeVault/00_Meta/<map_name>.md

Current structure:
  ## Section A
    - [[paper_a_card]]
    - [[paper_b_card]]

  ## Section B
    - [[paper_c_card]]

Proposed update:
  ## Section A
    - [[paper_a_card]]
    - [[paper_b_card]]
    - [[paper_d_card]]  <-- NEW

  ## Section B
    - [[paper_c_card]]

Waiting for confirmation.
```

### Step 4 — Execute Update (After Confirmation)

1. Read existing file
2. Apply update to correct section
3. Preserve existing formatting and structure
4. Add new entries in appropriate location
5. Write updated file

### Step 5 — Cross-Reference Check

After update:
1. Verify all new wikilinks resolve to existing files
2. Check for broken links
3. Confirm no duplicate entries

## Constraints

- Do NOT restructure existing sections
- Do NOT change heading hierarchy
- Do NOT delete existing entries
- Do NOT modify files without confirmation
- Preserve bilingual format if present (English/Chinese)

## Error Handling

| Condition | Action |
|---|---|
| Map file not found | STOP — create placeholder or skip |
| Wikilink broken | Flag for human review |
| Update ambiguous | FLAG for human clarification |
