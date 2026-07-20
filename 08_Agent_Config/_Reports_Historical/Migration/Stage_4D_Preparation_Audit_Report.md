# Stage 4D Preparation: Read-Only Audit Report

**Date:** 2026-07-16  
**Status:** READ-ONLY — no files modified  
**Purpose:** Verify migration readiness before Stage 4D (application installation + Zotero migration)

---

## 1. ResearchAI Structure Verification

| Item | Status | Details |
|------|--------|---------|
| Top-level directories | ✅ OK | 8 numbered folders + .agents, .codex, .git, .obsidian |
| Markdown files | ✅ OK | 216 .md files across workspace |
| Git repository | ✅ OK | Branch: master, working tree tracked |
| research_config.yaml | ✅ OK | Linux paths confirmed |
| Backup files | ✅ OK | 2 backup versions present |

---

## 2. Zotero Migration Readiness

### 2.1 Database

| File | Status | Size |
|------|--------|------|
| `zotero.sqlite` | ✅ EXISTS | 4,038,656 bytes (~3.8 MB) |
| `zotero.sqlite.bak` | ✅ EXISTS | 2,060,288 bytes (~2.0 MB) |

**Assessment:** Database and backup are present. The .bak is older (Jul 9) vs main sqlite (Jul 10). Consider taking a fresh backup before Linux Zotero installation.

### 2.2 Storage

| Item | Status | Details |
|------|--------|---------|
| `storage/` directory | ✅ EXISTS | 27 items |
| Items with PDFs | ✅ ALL 27 | Every storage item has a PDF |
| Total PDF count | ✅ 27 | Matches MinerU output count |

**Assessment:** All 27 papers have PDFs attached. Perfect 1:1 correspondence with MinerU output folders.

### 2.3 Better BibTeX

| Item | Status | Details |
|------|--------|---------|
| `better-bibtex/read-only.json` | ✅ EXISTS | 2 chars (`[]`) |

**Assessment:** Better BibTeX was installed on Windows. The read-only.json is empty, suggesting minimal or no read-only citation keys were configured. On Linux, Better BibTeX will need to be re-enabled in the new Zotero installation.

### 2.4 Styles and Translators

| Item | Status | Count |
|------|--------|-------|
| `styles/` | ✅ EXISTS | 15 CSL files |
| `translators/` | ✅ EXISTS | 756 translator files |

**Assessment:** Complete Zotero portable installation. All standard components present.

---

## 3. Obsidian Vault Readiness

| Item | Status | Details |
|------|--------|---------|
| `.obsidian/app.json` | ✅ EXISTS | Empty config `{}` |
| `.obsidian/workspace.json` | ✅ EXISTS | 473 KB, relative paths only |
| `.obsidian/plugins.json` | ❌ MISSING | No plugins.json found |
| `.obsidian/plugins/` | ⚠️ EXISTS | Contains `plugins.tar` and extracted plugin dir |
| Windows paths in config | ✅ NONE | No C:\ or D:\ references |

**Assessment:** Vault structure is clean and Linux-compatible. The missing plugins.json is unusual — Obsidian typically creates it on first launch. The `plugins.tar` suggests a backup of installed plugins. Obsidian for Linux will recreate plugins.json automatically.

---

## 4. Runtime-Critical Windows Path Check

### Files Audited

| File | Windows Paths | Status |
|------|--------------|--------|
| `research_config.yaml` | 0 | ✅ Clean |
| `Skills/01_Literature/SKILL_Paper_Intake.md` | 0 | ✅ Clean |
| `Skills/01_Literature/SKILL_Paper_Deep_Read.md` | 0 | ✅ Clean |
| `Skills/01_Literature/SKILL_Paper_Batch_Process.md` | 0 | ✅ Clean |
| `references/literature/paper_intake.md` | 0 | ✅ Clean |
| `references/literature/paper_deep_read.md` | 0 | ✅ Clean |
| `references/literature/paper_batch_process.md` | 0 | ✅ Clean |
| `references/literature/paper_logic.md` | 0 | ✅ Clean |
| `references/literature/survey_process.md` | 0 | ✅ Clean |

**Result:** Zero Windows paths in any runtime-critical file. Stage 4B migration is verified complete.

---

## 5. MinerU Output Completeness

| Metric | Value |
|--------|-------|
| Total folders | 27 |
| Folders with full.md | 27/27 (100%) |
| Total output size | 388.2 MB |

**Assessment:** All 27 papers have complete MinerU output. Every folder contains full.md plus supporting JSON and image data.

---

## 6. bibliography.bib Status

| Metric | Value |
|--------|-------|
| Total entries | ~27 |
| `D:\ResearchAI_Data` references | 27 |
| `C:\ResearchAI` references | 0 |
| Linux path references | 0 |

**Assessment:** All 27 entries have Windows Zotero storage paths. These will be auto-regenerated when Better BibTeX exports on Linux Zotero. No manual intervention needed.

---

## 7. Pre-Migration Checklist

### Items Ready for Stage 4D

- [x] All runtime config files use Linux paths
- [x] Zotero database + storage intact (27 PDFs)
- [x] Better BibTeX data present (read-only.json)
- [x] Styles and translators exported (15 CSL, 756 translators)
- [x] MinerU output complete (27/27 folders)
- [x] Obsidian vault clean (no Windows paths)
- [x] Backup files created for all modified files

### Items to Address in Stage 4D

1. **Fresh Zotero backup** — Take a new copy of zotero.sqlite before Linux installation
2. **Install Linux Zotero** — `apt install zotero` or AppImage
3. **Migrate database** — Copy zotero.sqlite to `~/.zotero/`
4. **Copy storage** — Link or copy Zotero storage to Linux Zotero profile
5. **Enable Better BibTeX** — Reinstall plugin, configure read-only keys
6. **Configure Linked Attachment Base** — Point to `/home/lco/ResearchAI_Data/Zotero/storage/`
7. **Verify bibliography.bib** — Confirm Better BibTeX exports correct paths
8. **Install Obsidian for Linux** — AppImage or deb package
9. **Verify vault renders correctly** — Check all links and internal references

### Items Out of Scope for Stage 4D

- Documentation cleanup (Stage 4E) — cosmetic only
- MinerU Linux setup (Stage 4F) — optional, Wine-based
- Bibliography.bib manual fix — auto-regenerated by Better BibTeX

---

## 8. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Zotero SQLite corruption during migration | Low | Critical | Fresh backup before any operation |
| Better BibTeX plugin incompatibility with Linux | Low | Medium | Plugin is cross-platform; unlikely issue |
| Obsidian vault link breakage | Very Low | Low | All links are relative; vault is clean |
| MinerU output unreadable on Linux | None | Low | Output is plain markdown + JSON |
| Double Zotero session (Windows + Linux) | N/A | Critical | Document rule: never run on both OS simultaneously |

---

## 9. Conclusion

**Migration readiness: GREEN**

All Stage 4B path replacements are verified correct. The Zotero portable data is complete and ready for Linux migration. The Obsidian vault has no platform-specific dependencies. MinerU output is fully intact. No runtime files contain Windows paths.

Stage 4D can proceed with confidence.
