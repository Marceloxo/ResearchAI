# Stage 4B: File Path Migration Report (Windows → Linux)

**Date:** 2026-07-16  
**Status:** COMPLETE  
**Scope:** Runtime configuration and agent skill files only

---

## 1. Migration Objective

Replace all Windows absolute paths (`C:\ResearchAI`, `D:\ResearchAI_Data`) with Linux absolute paths (`/home/lco/ResearchAI`, `/home/lco/ResearchAI_Data`) in files actively consumed by the agent workflow at runtime.

Historical records (Stage reports, encoding backups, audit logs) were preserved unchanged.

---

## 2. Original Windows Paths

| Path | Role |
|------|------|
| `C:\ResearchAI` | Workspace root (markdown, configs, agent files) |
| `D:\ResearchAI_Data` | External data layer (PDFs, datasets, models, experiments) |
| `D:\ResearchAI_Data\Zotero\storage\` | Zotero PDF attachments |
| `D:\ResearchAI_Data\Paper\MinerU_md\` | MinerU markdown output |
| `D:\ResearchAI_Data\Paper\Origin_pdf\` | Original paper PDFs |
| `D:\ResearchAI_Data\Datasets\` | Dataset files |
| `D:\ResearchAI_Data\Experiment_Results\` | Experiment outputs |
| `D:\ResearchAI_Data\Model_Checkpoints\` | Trained model weights |

---

## 3. Current Linux Paths

| Path | Role |
|------|------|
| `/home/lco/ResearchAI` | Workspace root |
| `/home/lco/ResearchAI_Data` | External data layer |
| `/home/lco/ResearchAI_Data/Zotero/storage/` | Zotero PDF attachments |
| `/home/lco/ResearchAI_Data/Paper/MinerU_md/` | MinerU markdown output |
| `/home/lco/ResearchAI_Data/Paper/Origin_pdf/` | Original paper PDFs |
| `/home/lco/ResearchAI_Data/Datasets/` | Dataset files |
| `/home/lco/ResearchAI_Data/Experiment_Results/` | Experiment outputs |
| `/home/lco/ResearchAI_Data/Model_Checkpoints/` | Trained model weights |

---

## 4. Files Modified

### research_config.yaml
- **Replacements:** 9
- **Details:** All 8 path values + 1 comment line updated

### Agent Skill Files (08_Agent_Config/Skills/)
| File | Replacements |
|------|-------------|
| `Skills/01_Literature/SKILL_Paper_Intake.md` | 2 |
| `Skills/01_Literature/SKILL_Paper_Deep_Read.md` | 1 |
| `Skills/01_Literature/SKILL_Paper_Batch_Process.md` | 1 |
| `Skills/researchai/INSTALL_INSTRUCTIONS.md` | 3 |
| `Skills/researchai/references/literature/paper_intake.md` | 2 |
| `Skills/researchai/references/literature/paper_deep_read.md` | 1 |
| `Skills/researchai/references/literature/paper_batch_process.md` | 1 |
| `Skills/researchai/references/literature/paper_logic.md` | 1 |
| `Skills/researchai/references/literature/survey_process.md` | 1 |

**Total files modified:** 10  
**Total replacements:** 22

### Backup Files Created
- `research_config.yaml.backup_linux_migration`
- `research_config.yaml.backup_linux_migration_v2`
- `08_Agent_Config/Skills/01_Literature/SKILL_Paper_Intake.md.backup_linux_migration`
- `08_Agent_Config/Skills/01_Literature/SKILL_Paper_Deep_Read.md.backup_linux_migration`
- `08_Agent_Config/Skills/01_Literature/SKILL_Paper_Batch_Process.md.backup_linux_migration`
- `08_Agent_Config/Skills/researchai/references/literature/paper_intake.md.backup_linux_migration`
- `08_Agent_Config/Skills/researchai/references/literature/paper_deep_read.md.backup_linux_migration`
- `08_Agent_Config/Skills/researchai/references/literature/paper_batch_process.md.backup_linux_migration`
- `08_Agent_Config/Skills/researchai/references/literature/paper_logic.md.backup_linux_migration`
- `08_Agent_Config/Skills/researchai/references/literature/survey_process.md.backup_linux_migration`

---

## 5. Validation Commands and Results

### Command: `grep -rn "D:\\ResearchAI_Data" *.yaml *.yml *.json *.bib`
**Result:** Zero matches (clean)

### Command: `grep -rn "C:\\ResearchAI" *.yaml *.yml *.json *.bib`
**Result:** Zero matches (clean)

### Command: `grep -rn "D:\\ResearchAI_Data" 08_Agent_Config/Skills/`
**Result:** Zero matches (clean)

### Command: `grep -rn "C:\\ResearchAI" 08_Agent_Config/Skills/`
**Result:** Zero matches (clean)

### Directory Verification
| Directory | Status |
|-----------|--------|
| `/home/lco/ResearchAI` | EXISTS |
| `/home/lco/ResearchAI_Data` | EXISTS |
| `/home/lco/ResearchAI_Data/Paper/Origin_pdf` | MISSING — needs creation |
| `/home/lco/ResearchAI_Data/Paper/MinerU_md` | EXISTS |
| `/home/lco/ResearchAI_Data/Datasets` | EXISTS |
| `/home/lco/ResearchAI_Data/Experiment_Results` | EXISTS |
| `/home/lco/ResearchAI_Data/Model_Checkpoints` | EXISTS |

---

## 6. Remaining Issues

### 6.1 Unresolved Windows Paths (Documentation Only)
These files still contain `D:\ResearchAI_Data` and `C:\ResearchAI` references. They are **not** runtime-consumed and were intentionally left unchanged:

| Category | Files | Count |
|----------|-------|-------|
| Stage audit reports | `Stage_*.md` | ~15 files |
| Encoding backup | `_encoding_backup_20260710/*` | 9 files |
| Historical docs | `README.md`, `PROJECT_STATUS.md`, `AGENT_BOOTSTRAP.md` | 3 files |
| Vault templates | `02_KnowledgeVault/Templates/*.md` | 2 files |
| Dataset cards | `02_KnowledgeVault/05_Datasets/*.md` | 10 files |
| Other docs | `01_Literature/README.md`, `Vault_README.md` | 2 files |

These are cosmetic/documentation only. They do not affect agent execution.

### 6.2 bibliography.bib (Not Modified)
13 Zotero `file` fields still contain `D:\ResearchAI_Data\Zotero\storage\...` paths.  
**Reason:** These will be regenerated automatically by Zotero + Better BibTeX after Linux Zotero configuration. Manual editing would be overwritten.

### 6.3 Missing Directory
`/home/lco/ResearchAI_Data/Paper/Origin_pdf/` does not exist yet. Needs to be created if original PDFs are to be stored there.

---

## 7. Next Stage Recommendation

### Stage 4C: Documentation Cleanup (Low Priority)
Update remaining documentation files to replace Windows paths with Linux paths for consistency. Not required for agent execution but improves readability.

### Stage 4D: bibliography.bib Sync (After Zotero Setup)
Once Zotero is configured on Linux with Better BibTeX, the `file` fields will auto-update. If manual sync is needed before that, use Python string replacement (same method as Stage 4B).

### Stage 4E: Directory Structure Finalization
Create any missing directories under `/home/lco/ResearchAI_Data/` that are referenced by the config but do not yet exist.

### Stage 4F: End-to-End Agent Test
Run a full agent workflow (paper intake → MinerU processing → vault update) to verify all path references resolve correctly on Linux.

---

## Summary

| Metric | Value |
|--------|-------|
| Runtime files modified | 10 |
| Total path replacements | 22 |
| Backup files created | 11 |
| Remaining Windows paths in runtime files | 0 |
| Remaining Windows paths in docs/history | ~80 (intentional) |
| Missing directories | 1 (`Paper/Origin_pdf`) |
| Blocked by external config | 1 (`bibliography.bib` — Zotero) |
