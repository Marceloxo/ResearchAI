# Zotero Deployment Record

## Installation Status

| Component | Status | Notes |
|---|---|---|
| Zotero | ✅ Installed | Data at `D:\ResearchAI_Data\` |
| Better BibTeX | ✅ Installed | Citation key format: `auth.lower + year + shorttitle(2)` |

## Storage Architecture (ADR-001)

### Zotero Data Directory

- **Location**: `D:\ResearchAI_Data\`
- **Contents**: `storage/` (PDFs), `zotero.sqlite` (metadata), `styles/`, `translators/`, `locate/`
- **PDFs stored in**: `D:\ResearchAI_Data\storage\`

### MinerU Reads From

- **Source**: `D:\ResearchAI_Data\storage\` (Zotero PDFs)
- **Output**: `D:\ResearchAI_Data\Paper\MinerU_md\{paper_id}\`

### No Separate Origin_pdf

Per ADR-001, there is no separate `Origin_pdf` directory. All PDFs are in Zotero's `storage/`.

## Deployment Checklist

- [x] Install Zotero
- [x] Install Better BibTeX plugin
- [x] Configure citation key format: `auth.lower + year + shorttitle(2)`
- [ ] Configure collections (Inbox, Reading, Deep Read, Reference)
- [ ] Configure tags (#to-read, #reading, #done, #key-paper, #survey, #seismic-ai, #segmentation)
- [ ] Configure BibTeX export target: `C:\ResearchAI\01_Literature\04_Literature_Index\bibliography.bib`
- [ ] Import test paper into Zotero
- [ ] Verify metadata accuracy (Codex verification)
- [ ] Verify Literature Index mapping (Codex verification)
- [ ] Verify citation integrity (Codex verification)

## Lessons Learned

<!-- Document after first test -->
