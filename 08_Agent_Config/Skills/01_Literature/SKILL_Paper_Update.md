# SKILL: Paper Update

## Purpose

Update existing paper records with new information.

## Input

```
Zotero Item Key
<update_type>: <details>
```

Update types:
- `code_found`: New GitHub repository URL
- `citation_update`: Updated citation count or venue info
- `dataset_update`: New dataset information
- `info_addition`: Additional relevant information

Example:
```
6VTKJ8W2
code_found: https://github.com/example/snunet-cd
```

## Permission Model

**Semi-Automatic Mode (Mode B)** — Modification preview shown before any changes.

## Workflow

### Step 1 — Locate Existing Paper

Search `02_KnowledgeVault/01_Papers/` for files matching the Zotero Item Key.

Check `MinerU_Zotero_Mapping.md` for the paper's Paper ID.

If not found: STOP — paper not in KnowledgeVault.

### Step 2 — Identify Target File(s)

Determine which files need updating:
- Literature Card (`*_card.md`)
- Paper Note (`*_note.md`)
- Survey Note (`*_survey.md`)
- Paper Logic (`*_logic.md`)

### Step 3 — Generate Modification Preview

Present to human:

```
Existing file: 02_KnowledgeVault/01_Papers/<filename>.md

Modification:
  Section: <section_name>
  Current: <current_value_or_section>
  New: <new_value_or_section>

Reason: <reason_for_update>

Waiting for confirmation.
```

### Step 4 — Execute Update (After Confirmation)

1. Read existing file
2. Apply modification to correct section
3. Preserve YAML frontmatter
4. Preserve existing content and formatting
5. Write updated file

### Step 5 — Update Cross-References

If relevant:
- Update `MinerU_Zotero_Mapping.md` if code/repository info changed
- Update `Paper_Index.md` if paper type or status changed

## Constraints

- Do NOT modify YAML frontmatter structure
- Do NOT change existing section order
- Do NOT delete existing content
- Do NOT modify files without confirmation
- Do NOT create new knowledge nodes

## Error Handling

| Condition | Action |
|---|---|
| Paper not found in KV | STOP — run Paper Intake first |
| No files match Item Key | STOP — verify key |
| Modification ambiguous | FLAG for human clarification |
