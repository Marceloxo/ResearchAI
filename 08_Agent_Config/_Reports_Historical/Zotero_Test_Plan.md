# Zotero Integration Test Plan

## Purpose

Define a single-paper test to validate Zotero -> ResearchAI integration before scaling to the full pipeline.

## Test Paper

Use one paper already in the system for testing.

**Recommended**: `2023_Monteiro_DeepLearningSeismicSegmentation` (the survey paper already processed)

**Alternative**: Any single paper with known metadata.

---

## Test Workflow

```
1. Import paper to Zotero
2. Verify metadata accuracy
3. Configure Better BibTeX (citation key format: authorYEARkeyword)
4. Export BibTeX to ResearchAI
5. Verify Literature Index mapping
6. Run MinerU processing
7. Generate Processed Markdown
8. Create Literature Card
9. Verify all cross-references
```

---

## Step-by-Step Test

### Step 1: Import to Zotero

- [ ] Import PDF to Zotero (drag & drop or File -> Add)
- [ ] Verify Zotero auto-detected metadata (title, authors, year, journal)
- [ ] Verify DOI field is populated
- [ ] Assign to `ResearchAI/Inbox` collection
- [ ] Assign tags: `#to-read`, `#seismic-ai`, `#survey`

### Step 2: Verify Metadata

- [ ] Zotero title matches paper title exactly
- [ ] Zotero authors list is complete and accurate
- [ ] Zotero year matches publication year
- [ ] Zotero DOI resolves correctly
- [ ] Zotero journal/conference name is correct

### Step 3: Configure Better BibTeX

- [ ] Better BibTeX plugin is installed and enabled
- [ ] Citation key format is set to: `authorYEARkeyword` (e.g., `monteiro2023deeplearning`)
- [ ] Auto-export is enabled
- [ ] Export target is: `C:\ResearchAI\01_Literature\04_Literature_Index\bibliography.bib`
- [ ] Zotero item key is noted (6-char code)

### Step 4: Export and Verify BibTeX

- [ ] Trigger BibTeX export (Zotero -> Tools -> Better BibTeX -> Export Bibliography)
- [ ] Verify `bibliography.bib` exists in `01_Literature/04_Literature_Index/`
- [ ] Verify BibTeX entry contains correct title, authors, year, DOI
- [ ] Verify citation key format is `authorYEARkeyword` (NOT Paper ID format)

### Step 5: Verify Literature Index Mapping

- [ ] Add row to `Literature_Index.md` with:
  - `paper_id`: `2023_Monteiro_DeepLearningSeismicSegmentation`
  - `zotero_key`: (from Zotero)
  - `citation_key`: (from BibTeX, e.g., `monteiro2023deeplearning`)
  - `doi`: (from Zotero)
- [ ] Verify bidirectional lookup works:
  - Literature Index -> Zotero item key OK
  - Zotero citation key -> BibTeX entry OK

### Step 6: MinerU Processing

- [ ] Run MinerU Desktop on the test PDF
- [ ] Verify output folder in `02_MinerU_Output/`
- [ ] Rename UUID folder to Paper ID

### Step 7: Processed Markdown

- [ ] Apply cleaning rules from `MinerU_Cleaning_Rules.md`
- [ ] Generate processed markdown using `Processed_Markdown_Template.md`
- [ ] Save to `03_Processed_Markdown/` with Paper ID filename
- [ ] Quality assessment: Good / Fair / Poor

### Step 8: Literature Card

- [ ] Create Literature Card using `Literature_Card_Template.md`
- [ ] Include `zotero_key` and `citation_key` in card metadata
- [ ] Decision: Deep Read / Keep Reference / Ignore

### Step 9: Cross-Reference Verification

- [ ] Literature Card links to Zotero via `zotero_key`
- [ ] Literature Card links to BibTeX via `citation_key`
- [ ] Paper Note (if deep read) links to Zotero via `zotero_key`
- [ ] No duplicate metadata between Zotero and ResearchAI
- [ ] Citation in any manuscript would pull from Zotero, not be fabricated

---

## Success Criteria

All of the following must pass:

| Criterion | Pass Condition |
|---|---|
| Metadata match | Zotero title, authors, year match ResearchAI fields |
| Citation key format | `authorYEARkeyword` (e.g., `monteiro2023deeplearning`), NOT Paper ID format |
| DOI match | Zotero DOI matches ResearchAI DOI field |
| No manual duplication | Metadata entered once, shared via Zotero |
| Bidirectional lookup | Literature Index <-> Zotero item key works both ways |
| Citation integrity | Manuscript citations can be traced to Zotero entry |

## Failure Scenarios

If any criterion fails:

1. **Metadata mismatch**: Re-import paper to Zotero, verify auto-detection.
2. **Citation key wrong format**: Adjust Better BibTeX to `authorYEARkeyword`.
3. **DOI missing**: Manually add DOI to Zotero, re-export.
4. **Lookup broken**: Check Literature Index for correct `zotero_key` value.

---

## Post-Test Actions

After successful test:

1. Document lessons learned in this file.
2. Update `Zotero_Integration_Design.md` if any changes are needed.
3. Proceed to full pipeline processing of 3-5 papers.
4. Archive this test plan or mark as completed.

## Post-Test Actions (if failed)

After failed test:

1. Document what failed and why.
2. Fix the issue (Zotero config, BBT settings, etc.).
3. Retry the test.
4. Do NOT proceed to full pipeline until test passes.
