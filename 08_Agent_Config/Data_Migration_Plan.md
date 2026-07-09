# Data Migration Plan

## Overview

This document tracks the migration of literature data from temporary locations to the ResearchAI data layer.

---

## Current State

### Active Locations

| Path | Status | Content |
|---|---|---|
| `D:\ResearchAI_Data\Paper\MinerU_md\` | Active | MinerU Desktop output (new structure) |
| `D:\ResearchAI_Data\Paper\Origin_pdf\` | Active | Original PDF papers (new structure) |
| `C:\ResearchAI\01_Literature\` | Active | Literature management layer |

---

## Migration Plan

### Phase 1: Infrastructure (Completed)

- [x] Create `D:\ResearchAI_Data\` directory structure
- [x] Create `D:\ResearchAI_Data\Paper\Origin_pdf\`
- [x] Create `D:\ResearchAI_Data\Paper\MinerU_md\`
- [x] Create `D:\ResearchAI_Data\Datasets\`
- [x] Create `D:\ResearchAI_Data\Experiment_Results\`
- [x] Create `D:\ResearchAI_Data\Model_Checkpoints\`
- [x] Update `research_config.yaml` with new paths
- [x] Update all agent config path references

### Phase 2: Content Migration (Future)

- [ ] Move existing MinerU output to `D:\ResearchAI_Data\Paper\MinerU_md\`
- [ ] Rename UUID folders to Paper ID format
- [ ] Verify all `full.md` files are intact
- [ ] Update `02_MinerU_Output/` references

### Phase 3: Dataset Migration (Future)

- [ ] Download datasets to `D:\ResearchAI_Data\Datasets\`
- [ ] Create dataset notes in KnowledgeVault
- [ ] Update `Dataset_Template.md` entries with actual paths

---

## Current Decision

**Migration is complete for infrastructure.** The directory structure is in place and all configuration files reference the new paths.

Content migration (moving actual files) will happen when new papers are processed through the system.

---

## Tracking

| Item | Current Location | Target Location | Status |
|---|---|---|---|
| Test paper MinerU output | `D:\ResearchAI_Data\Paper\MinerU_md\` | `D:\ResearchAI_Data\Paper\MinerU_md\` | Done (already in place) |
| Test paper PDF | `D:\ResearchAI_Data\Paper\Origin_pdf\` | `D:\ResearchAI_Data\Paper\Origin_pdf\` | Done (already in place) |
| All future MinerU output | `D:\ResearchAI_Data\Paper\MinerU_md\` | `D:\ResearchAI_Data\Paper\MinerU_md\` | Ready |
