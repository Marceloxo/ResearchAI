# Stage 4C: Architecture Review Report (Linux Workflow)

**Date:** 2026-07-16  
**Scope:** Data flow analysis, Origin_pdf necessity, Linux MinerU architecture, migration steps  
**Status:** READ-ONLY ANALYSIS — no files modified

---

## 1. Current Data Flow: Zotero → MinerU → Agent → Obsidian

### 1.1 Physical Layout (Verified)

```
/home/lco/ResearchAI/                    ← Knowledge workspace (Obsidian vault)
├── 02_KnowledgeVault/                   ← Structured knowledge (cards, notes, methods)
├── 01_Literature/                       ← Markdown literature + bibliography.bib
├── 08_Agent_Config/Skills/              ← Agent skill definitions (runtime)
├── research_config.yaml                 ← Config (now Linux paths ✓)
└── .obsidian/                           ← Obsidian workspace (no Windows paths)

/home/lco/ResearchAI_Data/               ← External data layer
├── Zotero/
│   ├── zotero.sqlite                    ← Zotero database (4 MB)
│   ├── zotero.sqlite.bak                ← Backup
│   ├── storage/                         ← 27 items, each with a PDF (single source of truth)
│   ├── better-bibtex/                   ← Better BibTeX plugin data
│   ├── styles/                          ← 15 CSL citation styles
│   ├── translators/                     ← 756+ import translators
│   └── locate/                          ← Full-text indexing
├── Paper/
│   └── MinerU_md/                       ← 27 folders (MinerU Desktop output)
│       ├── full.md                      ← Extracted markdown
│       ├── *_content_list.json          ← Layout/content metadata
│       ├── *_model.json                 ← ML model predictions
│       ├── layout.json                  ← Block layout data
│       ├── *_origin.pdf                 ← Embedded original PDF
│       └── images/                      ← Extracted figures
├── Datasets/                            ← Empty (placeholder)
├── Experiment_Results/                  ← Empty (placeholder)
├── Model_Checkpoints/                   ← Empty (placeholder)
├── Zotero_Attachments/                  ← Empty (placeholder, deprecated)
└── locate/                              ← Top-level locate cache
```

### 1.2 Data Flow Diagram

```
┌─────────────┐     PDF ──────▶  ┌──────────────────┐
│  Zotero      │                  │  storage/{Key}/    │
│  (Desktop)   │◀─────────────────│  {paper}.pdf      │
│              │  metadata sync   └──────────────────┘
│  zotero.sqlite│
└──────┬───────┘
       │  reads PDFs from storage/
       ▼
┌──────────────────┐     full.md + JSON + images
│  MinerU Desktop   │────▶  MinerU_md/{paper_id}/
│  (Windows GUI)    │     (27 folders, ~300 MB total)
└──────────────────┘
       │
       │  reads full.md
       ▼
┌──────────────────┐     markdown cards, notes, links
│  Agent (Codex)    │────▶  02_KnowledgeVault/
│  (Linux CLI)      │     01_Literature/
└──────────────────┘
       │
       │  Obsidian vault = ResearchAI/
       ▼
┌──────────────────┐
│  Obsidian Desktop │
│  (Linux port?)    │
└──────────────────┘
```

### 1.3 Key Observations

1. **Zotero storage/ is the single source of truth** for all PDFs. 27 items, 27 PDFs confirmed.
2. **MinerU output already exists** — 27 folders in MinerU_md/, all populated with full.md and metadata.
3. **No Origin_pdf directory exists** on disk. The config references it, but the README.md in ResearchAI_Data explicitly states it is deprecated.
4. **MinerU Desktop is a Windows GUI application** — no Linux equivalent found in PATH or package managers.
5. **Zotero Desktop is a Windows/Mac/Linux app** — needs native Linux installation or Wine.
6. **Obsidian vault structure is clean** — `.obsidian/` config uses relative paths, no Windows references.

---

## 2. Is Origin_pdf Actually Required?

### Answer: NO.

Evidence from the codebase:

1. **README.md in ResearchAI_Data** explicitly states: *"The previous D:\ResearchAI_Data\Paper\Origin_pdf\ directory is deprecated. All PDFs are now managed through Zotero's storage/ directory."*
2. **No Origin_pdf directory exists** on disk under `/home/lco/ResearchAI_Data/`.
3. **All 27 PDFs** are already in `Zotero/storage/{Key}/` — each storage item contains exactly one PDF.
4. **MinerU reads from Zotero storage/**, not from Origin_pdf.
5. **bibliography.bib `file` fields** all point to `D:\ResearchAI_Data\Zotero\storage\...` — no Origin_pdf references.

### Conclusion

Origin_pdf was an intermediate concept from early migration planning. The current architecture — Zotero storage as the canonical PDF source — is correct and sufficient. **Do not create Origin_pdf.**

---

## 3. Recommended Linux MinerU Architecture

### 3.1 Problem Statement

MinerU Desktop is a Windows GUI application. There is no official Linux version. The Linux agent needs to:
- Read existing MinerU output (already done ✓)
- Process new papers added to Zotero

### 3.2 Options Ranked

| Option | Pros | Cons | Complexity |
|--------|------|------|------------|
| **A. Wine + MinerU Desktop** | Preserves exact Windows behavior, no changes needed | Requires Wine setup, occasional compatibility issues | Medium |
| **B. CLI wrapper (read-only)** | Native Linux, fast | Cannot process new papers, only reads existing output | Low |
| **C. Alternative Linux OCR** | Native, open-source | Different output format, requires skill updates | High |
| **D. Cloud/API MinerU** | Platform-independent | Network dependency, potential cost | Medium |

### 3.3 Recommended: Option A (Wine + MinerU Desktop)

**Rationale:** The existing 27 MinerU output folders were produced by MinerU Desktop. The agent skills reference `MinerU_md/{folder}/full.md` — this format must be preserved. Switching OCR engines would break all existing output and require rewriting skill files.

**Setup steps:**
1. Install Wine: `sudo apt install wine64`
2. Copy `MinerU Desktop.exe` from Windows machine or download installer
3. Configure Wine to use `/home/lco/ResearchAI_Data/Paper/MinerU_md/` as output directory
4. Configure Wine to read PDFs from `/home/lco/ResearchAI_Data/Zotero/storage/`
5. Set up a cron job or file watcher to auto-process new PDFs in Zotero storage

### 3.4 Alternative: Option B (Read-Only CLI)

If Wine is not desired, the agent can operate in read-only mode:
- All existing MinerU output is already available
- New paper processing requires manual MinerU Desktop runs on Windows (or Wine)
- Agent skills already handle `full.md` files correctly on Linux

This is the **minimum viable path** — no additional setup needed.

---

## 4. Migration Steps for Zotero, Obsidian, MinerU

### 4.1 Zotero (Linux)

**Current state:** Portable Zotero data exists at `/home/lco/ResearchAI_Data/Zotero/` with:
- `zotero.sqlite` (4 MB)
- 27 PDF items in `storage/`
- 15 CSL styles
- 756+ translators
- Better BibTeX plugin data (`better-bibtex/read-only.json`)

**Steps:**
1. Install Zotero for Linux: `sudo apt install zotero` (or Flatpak/AppImage)
2. During first-run profile creation, point to existing `zotero.sqlite`:
   - Close Zotero
   - Copy `/home/lco/ResearchAI_Data/Zotero/zotero.sqlite` to `~/.zotero/zotero.sqlite`
   - Copy `/home/lco/ResearchAI_Data/Zotero/storage/` contents to Zotero's default storage location
   - Copy `styles/` to `~/.zotero/`
3. Enable Better BibTeX plugin in Linux Zotero
4. Set Linked Attachment Base Directory to `/home/lco/ResearchAI_Data/Zotero/storage/`
5. Verify all 27 items appear correctly with attached PDFs
6. **bibliography.bib will auto-regenerate** — Better BibTeX exports paths using the current OS path separator

### 4.2 Obsidian (Linux)

**Current state:** Clean. `.obsidian/` config uses relative paths. No Windows references detected.

**Steps:**
1. Install Obsidian for Linux (AppImage or deb package)
2. Open `/home/lco/ResearchAI/` as vault
3. Verify all 108+ markdown files render correctly
4. Verify internal links resolve (they use relative paths, so they should)
5. No path migration needed — Obsidian was already Linux-compatible

### 4.3 MinerU (Linux)

**Current state:** 27 output folders already populated at `/home/lco/ResearchAI_Data/Paper/MinerU_md/`. MinerU Desktop is a Windows application.

**Steps (Option A - Wine):**
1. Install Wine: `sudo apt install wine64`
2. Copy MinerU Desktop installer from Windows machine
3. Run installer in Wine: `wine MinerU-Setup.exe`
4. Configure output directory in MinerU settings: `/home/lco/ResearchAI_Data/Paper/MinerU_md/`
5. Configure PDF source: `/home/lco/ResearchAI_Data/Zotero/storage/`
6. Test with a single paper to verify output format matches existing folders

**Steps (Option B - Read-Only):**
1. No setup required
2. Agent reads existing `full.md` files
3. New papers must be processed via Windows MinerU Desktop or Wine

---

## 5. Risks and Mitigations

| Risk | Severity | Mitigation |
|------|----------|------------|
| Wine + MinerU Desktop compatibility | Medium | Test with one paper first; keep Windows VM as fallback |
| Zotero SQLite corruption on dual-OS | High | Never run Zotero on both Windows and Linux simultaneously; backup zotero.sqlite before any changes |
| Better BibTeX path format change | Low | Auto-resolved when Zotero regenerates bibliography.bib on Linux |
| MinerU output format differences | Medium | Wine preserves exact Windows behavior; CLI alternatives produce different formats |
| File watcher reliability | Low | Cron-based polling is simpler and more reliable than inotify |

---

## 6. Summary

| Component | Current State | Action Required |
|-----------|--------------|-----------------|
| **research_config.yaml** | ✅ Linux paths | None |
| **Agent Skills** | ✅ Linux paths | None |
| **Obsidian** | ✅ Already Linux-compatible | Install Linux app only |
| **Zotero** | ✅ Data portable | Install Linux app + migrate SQLite |
| **MinerU** | ✅ Output readable | Wine setup (optional) or read-only |
| **Origin_pdf** | ❌ Not needed | Do not create |
| **bibliography.bib** | ⏳ Windows paths | Auto-fixes after Zotero Linux setup |

**Bottom line:** The most critical migration work (config files, skill paths) is complete. The remaining work is installing Linux-native applications (Zotero, Obsidian) and optionally setting up Wine for MinerU Desktop. The data layer is already correctly structured.
