# SKILL: Architecture Audit

## Purpose

Perform periodic read-only audits of the ResearchAI system integrity.

## Input

Optional:
```
<audit_scope>
```

Defaults to full audit. Scope options:
- `full` — Complete system audit
- `papers` — Paper file audit only
- `mapping` — Mapping registry audit only
- `links` — Wikilink integrity audit only

## Permission Model

**Read-Only** — This skill never modifies files. Generates audit report only.

## Workflow

### Step 1 — Define Audit Scope

Based on input scope, determine checks:

#### Full Audit Checklist

| Check | Source |
|---|---|
| Broken wikilinks | All `.md` files in KnowledgeVault |
| Naming convention compliance | `02_KnowledgeVault/01_Papers/` |
| Zotero mapping consistency | `MinerU_Zotero_Mapping.md` vs KV files |
| Duplicate papers | `01_Papers/` filename analysis |
| Template compliance | All KV paper files |
| Directory integrity | All directories |
| Architecture rule compliance | `ResearchAI_Data_Flow_Architecture.md` |

#### Focused Audit Checklist

Only the specified scope checks.

### Step 2 — Execute Checks

#### 2.1 Broken Wikilink Check

Scan all `.md` files in KnowledgeVault for `[[...]]` references.
Verify each reference resolves to an existing file.

Report:
```
Broken links found:
- 01_Papers/chai2020_using_card.md → [[NonExistent]]
```

#### 2.2 Naming Convention Check

Verify all files in `02_KnowledgeVault/01_Papers/` match:
```
{author}{year}_{keyword}_{type}.md
```

Where type is one of: `card`, `note`, `survey`, `logic`.

Report:
```
Non-compliant files:
- paper_xyz.md (missing type suffix)
```

#### 2.3 Zotero Mapping Consistency

Cross-reference:
1. `MinerU_Zotero_Mapping.md` entries vs `01_Papers/` files
2. `Paper_Index.md` entries vs `01_Papers/` files
3. Zotero Item Keys vs actual storage

Report:
```
Mapping inconsistencies:
- Key ABC12345 in mapping but no KV file
- File xyz.md in KV but not in mapping
```

#### 2.4 Duplicate Detection

Check for:
1. Same author-year-keyword in multiple files
2. Same Zotero Item Key in multiple entries
3. Identical paper titles across files

#### 2.5 Template Compliance

Sample check (not exhaustive):
1. YAML frontmatter present
2. Required sections present
3. Zotero section present (for cards)

#### 2.6 Directory Integrity

Check:
1. All directories exist per architecture
2. No stray files in wrong directories
3. Deprecated directories are empty
4. No PDFs in workspace (C: drive)

### Step 3 — Generate Audit Report

```
Architecture Audit Report

Date: <date>
Scope: <scope>

## Summary
Total checks: <N>
Passed: <P>
Warnings: <W>
Errors: <E>

## Findings

### Critical Errors
<none / list of errors>

### Warnings
<list of warnings>

### Passed Checks
<list of passed checks>

## Recommendations
1. <actionable recommendation>
2. <actionable recommendation>
```

### Step 4 — Output

Present report to human. No files modified.

## Constraints

- ALWAYS read-only (never modifies files)
- Do NOT auto-fix any issues found
- Do NOT create new files
- Report findings only
- Escalate critical issues to human

## Error Handling

| Condition | Action |
|---|---|
| Audit scope unknown | Default to full audit |
| File unreadable | Log as error, continue |
| Permission denied | Log as error, continue |
