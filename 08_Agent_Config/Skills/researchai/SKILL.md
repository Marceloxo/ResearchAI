---
name: researchai
description: >
  Execute standardized ResearchAI paper processing workflows through the frozen Zotero→MinerU→KnowledgeVault pipeline.
  Use when the user wants to process a new paper, perform deep reading, batch process papers, update existing papers,
  check knowledge nodes, maintain research maps, generate literature synthesis, run argument mining, process survey papers, create method knowledge nodes, or run architecture audits.
  Triggers: paper intake, deep read, batch process, paper update, knowledge node check, research map update,
  literature synthesis, architecture audit, /SKILL commands, "process paper", "deep read paper", "batch process papers".
---

# ResearchAI Skill System

Execute standardized workflows for the ResearchAI scientific research workspace.
Architecture is frozen: Zotero (source) → MinerU (processing) → KnowledgeVault (knowledge).

## Permission Model

**All skills: Semi-Automatic Mode (Mode B).**
1. Analyze request → 2. Generate execution plan → 3. Show plan for confirmation → 4. Execute after approval.
No skill silently modifies KnowledgeVault. Exception: Architecture Audit is read-only.

## Quick Reference

| Command | Input | Purpose |
|---|---|---|
| `/SKILL Paper Intake` | Zotero Item Key | New paper → Literature Card |
| `/SKILL Deep Read` | Zotero Item Key | Existing paper → Paper Note (Level 2) |
| `/SKILL Batch Process` | Multiple Item Keys | Bulk Literature Card creation |
| `/SKILL Paper Update` | Key + update type | Update existing paper info |
| `/SKILL Knowledge Node Check` | Concept name | Check if new node needed |
| `/SKILL Research Map Update` | Map name + desc | Update navigation files |
| `/SKILL Literature Synthesis` | Topic | Generate writing materials |
| `/SKILL Architecture Audit` | Scope (optional) | Read-only system audit |
| `/SKILL Encoding Audit` | File/directory | Check UTF-8 integrity and detect encoding corruption |
| `/SKILL Paper Logic` | Zotero Item Key | Level 3 argument mining and evidence mapping |
| `/SKILL Survey Process` | Zotero Item Key | Survey/review paper taxonomy and gap analysis |
| `/SKILL Method Node` | Concept name | Create Method knowledge nodes from paper notes |
| `/SKILL Paper Logic` | Zotero Item Key | Level 3 argument mining and evidence mapping |
| `/SKILL Survey Process` | Zotero Item Key | Survey/review paper taxonomy and gap analysis |
| `/SKILL Method Node` | Concept name | Create Method knowledge nodes from paper notes |

## Workflows

Load detailed workflow from references/ when executing a skill.

### 1. Paper Intake
Reference: [paper_intake.md](references/literature/paper_intake.md)
- Verify Zotero storage → Locate PDF → Verify MinerU output → Check duplicates → Determine level → Generate plan → Create Literature Card

### 2. Deep Read
Reference: [paper_deep_read.md](references/literature/paper_deep_read.md)
- Read full.md + existing card → Extract analysis sections → Generate note using Paper_Template.md → Post-processing updates

### 3. Batch Process
Reference: [paper_batch_process.md](references/literature/paper_batch_process.md)
- Parse keys → Pre-processing verification → Classification → Execute Level 1 for each paper → Summary

### 4. Paper Update
Reference: [paper_update.md](references/literature/paper_update.md)
- Locate existing paper → Identify target file(s) → Show modification preview → Execute update

### 5. Knowledge Node Check
Reference: [node_check.md](references/knowledge/node_check.md)
- Search all KV directories → Evaluate reuse criteria → Recommend: Reuse / Create / Wait

### 6. Research Map Update
Reference: [research_map_update.md](references/knowledge/research_map_update.md)
- Locate map file → Analyze structure → Show update preview → Execute update

### 7. Literature Synthesis
Reference: [literature_synthesis.md](references/writing/literature_synthesis.md)
- Define scope → Gather sources → Generate outline → Create synthesis document

### 8. Architecture Audit
Reference: [architecture_audit.md](references/system/architecture_audit.md)
- Define scope → Execute checks (wikilinks, naming, mapping, duplicates, templates, directories) → Generate report


### 9. Encoding Audit
Reference: [encoding_audit.md](references/system/encoding_audit.md)
- Define scope (file or directory) ? Execute encoding checks ? Generate audit report ? Recommend repair

### 10. Paper Logic
Reference: [paper_logic.md](references/literature/paper_logic.md)
- Locate sources (card + note + full.md) -> Extract argument structure -> Build evidence mapping -> Justify modules -> Generate plan -> Create Paper Logic file

### 11. Survey Process
Reference: [survey_process.md](references/literature/survey_process.md)
- Locate sources (card + full.md) -> Extract taxonomy -> Coverage analysis -> Key findings -> Future directions -> Generate plan -> Create Survey file

### 12. Method Node
Reference: [method_node.md](references/knowledge/method_node.md)
- Locate sources (paper notes) -> Deduplication check -> Extract definition/architecture/advantages/limitations -> Related papers/methods -> Generate plan -> Create Method node
## Constraints

- Do NOT modify templates, directory structure, or processing framework
- Do NOT process papers without Zotero verification
- Do NOT auto-create knowledge nodes
- Do NOT fabricate reproducibility information
- All claims must be traceable to existing KV files
## Encoding Policy

All ResearchAI generated or modified files must follow these encoding rules:

1. Markdown, YAML, and JSON files must be UTF-8 without BOM.
2. File writing operations must explicitly specify UTF-8 encoding.
3. Never rely on Windows system default encoding.
4. Never use PowerShell default output redirection for writing ResearchAI files.
5. Preserve:
   - Chinese characters
   - Unicode symbols
   - Markdown syntax
   - YAML frontmatter
   - Wikilinks
6. After writing files, verify:
   - UTF-8 decoding succeeds
   - No U+FFFD characters exist
   - No mojibake patterns exist


