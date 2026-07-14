# Encoding Audit Skill

Define a systematic encoding integrity audit for ResearchAI files.

## Workflow

### 1. Input

Optional:
- Single file path
- Directory path
- Scope (specific file types: .md, .yaml, .json)

### 2. Checks

Execute the following checks on every target file:

1. **Encoding detection** — Use chardet or equivalent to detect file encoding
2. **BOM detection** — Check for UTF-8 BOM (EF BB BF)
3. **Invalid UTF-8 detection** — Attempt UTF-8 decode, record failures
4. **Mojibake detection** — Search for known corruption patterns:
   - 閰嶇疆鍔熻兘鍩虹浜庤繃婊ゅ彂鐜扮珯鐐卞崱閫氭暟鎹搴 (GBK misinterpretation)
   - 鍩 (U+93A0)
   - 鐮 (U+9550)
   - 鏂 (U+9381)
   - 涓 (U+6D93)
   - 鍐 (U+95A7)
   - â (U+00E2, Latin-1 artifact)
   - U+FFFD replacement characters
5. **Replacement character detection** — Count U+FFFD occurrences
6. **Markdown integrity check** — Verify code blocks, frontmatter, heading levels
7. **YAML frontmatter check** — Verify frontmatter is closed and valid

### 3. Classification

Classify each file:

| Code | Category | Description |
|------|----------|-------------|
| A | Normal UTF-8 | Valid UTF-8, no corruption |
| B | UTF-8 BOM | Valid UTF-8 with BOM (acceptable) |
| C | Mojibake/Polluted | Contains encoding corruption |
| D | Unknown | Cannot determine encoding |

### 4. Output

Generate report file:

Stage_x_x_Encoding_Audit_Report.md

Report must include:

- Scan scope (directories and file types)
- Total file count
- Normal file count
- Anomalous file count
- List of corrupted files with:
  - File path
  - Detected encoding
  - Corruption type
  - Severity (High/Medium/Low)
  - Line numbers and snippets
- Root cause analysis
- Repair recommendations

### 5. Constraints

- **AUDIT MODE IS READ ONLY** — Do not modify any files during audit
- Repair requires explicit approval via a separate stage
- Do not process Zotero internal databases
- Do not process MinerU raw PDF content
- Report file must be written as UTF-8 without BOM
- After writing report, verify it passes encoding checks


---

## Output Encoding Standard

All generated audit reports must follow these encoding rules to ensure terminal-independent readability.

### File Encoding

- UTF-8 without BOM
- Explicit encoding declaration when writing files
- Never rely on Windows default encoding

### Character Policy

Avoid using characters that frequently break in Windows terminal environments:

**Do NOT use:**

- Emoji symbols:
  - ?
  - ?
  - ??
  - ??
- Decorative Unicode symbols

**Prefer ASCII-safe alternatives:**

- Use `PASS` instead of ?
- Use `FAIL` instead of ?
- Use `WARNING` instead of ??
- Use `SCAN` instead of ??

### Markdown Compatibility

Generated reports must preserve:

- YAML frontmatter
- Markdown headings
- Tables
- Code blocks
- Wikilinks
- Chinese characters

### Post-generation Validation

After writing a report file, verify:

1. UTF-8 decode succeeds without errors
2. No U+FFFD replacement characters exist
3. No known mojibake patterns (?, ?, ?, ?, ?, ?)
4. Markdown structure is readable (headings, tables, code blocks balanced)

---

## Report Template

All encoding audit reports must follow this standard header format:

```
# Encoding Audit Report

> Date: YYYY-MM-DD
> Scope: <description>
> Agent: <agent name>

## Summary

| Check | Status |
|---|---|
| UTF-8 encoding | PASS |
| BOM check | PASS |
| Mojibake detection | PASS |
| File classification | PASS |
| Structural integrity | PASS |
```

Status values must use only:

- PASS
- WARNING
- FAIL

No emoji symbols in status cells.
