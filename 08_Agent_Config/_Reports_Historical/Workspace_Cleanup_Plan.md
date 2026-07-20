# Workspace Cleanup Plan

> This document identifies obsolete directories and proposes migration/cleanup actions.
> **Nothing is deleted without human approval.** This is a plan only.

---

## Identified Obsolete Directories

### 1. C:\ResearchAI\01_Literature\PDFs\

**Status:** Empty placeholder directory.

**Why obsolete:**
- PDFs are managed by Zotero (ADR-001: Zotero-centered PDF architecture).
- No PDFs have ever been stored here.
- The directory exists from Stage 0 initialization but was never used.

**Proposed action:** Leave in place as a placeholder. No migration needed.

---

### 2. C:\ResearchAI\01_Literature\01_PDFs\

**Status:** Empty placeholder directory.

**Why obsolete:**
- Same as above. Duplicate of `PDFs/` with a different naming convention.
- PDFs are managed by Zotero. MinerU output goes to `D:\ResearchAI_Data\Paper\MinerU_md\`.

**Proposed action:** Leave in place. No migration needed.

---

### 3. C:\ResearchAI\01_Literature\02_MinerU_Output\

**Status:** Empty placeholder directory.

**Why obsolete:**
- MinerU output is stored on D: drive at `D:\ResearchAI_Data\Paper\MinerU_md\`.
- This directory was created during Stage 0 but MinerU output was always directed to D:.
- The directory map in AGENT_BOOTSTRAP.md references it, but actual MinerU output lives on D:.

**Migration impact:**
- AGENT_BOOTSTRAP.md directory map would need updating if this directory is removed.
- Currently, no references point to this directory — it's a dead leaf.

**Proposed action:** Leave in place. Mark as "unused" in documentation.

---

### 4. D:\ResearchAI_Data\Zotero_Attachments\

**Status:** Empty directory (placeholder for linked attachment base directory).

**Why it exists:**
- Was configured as Zotero's Linked Attachment Base Directory.
- No attachments have been moved here.
- Zotero's own `storage/` directory holds all PDFs.

**Proposed action:** Leave in place. It serves as a reserved path for future use.

---

## Summary

| Directory | Status | Action Needed | Impact of Removal |
|---|---|---|---|
| `01_Literature/PDFs/` | Empty placeholder | None | None |
| `01_Literature/01_PDFs/` | Empty placeholder | None | None |
| `01_Literature/02_MinerU_Output/` | Empty placeholder | None | None |
| `D:\ResearchAI_Data\Zotero_Attachments/` | Empty placeholder | None | None |

**Total impact of removing all above:** Zero files lost. Zero data affected. Only directory structure reduced by 4 empty directories.

**Recommendation:** Leave all four directories in place. They serve as placeholders and take negligible disk space. Removing them provides no benefit and adds maintenance overhead.

---

## Directories That Need Attention (Non-Obsolete)

These directories are NOT obsolete but could benefit from cleanup:

### D:\ResearchAI_Data\Paper\MinerU_md\ — 5 papers processed, 2 in vault

| Paper | MinerU Output | In KnowledgeVault? |
|---|---|---|
| chai2020.pdf | ✅ Processed | ✅ Yes (card + note + logic) |
| Literature-review-on-deep-learning...pdf | ✅ Processed | ✅ Yes (card + note) |
| liu2020.pdf | ✅ Processed | ❌ No |
| park2020.pdf | ✅ Processed | ❌ No |
| tsr-2021001.1.pdf | ✅ Processed | ❌ No |
| zhu2018.pdf (PhaseNet original) | ✅ Processed | ❌ No |

**Action:** These 4 unprocessed MinerU outputs are candidates for future stress test papers (Stage 1.5-6B).

---

## Decision

**No immediate cleanup action required.** The obsolete directories are empty placeholders that consume negligible space. The real opportunity is in processing the 4 unprocessed MinerU outputs on D:, not in deleting empty directories.
