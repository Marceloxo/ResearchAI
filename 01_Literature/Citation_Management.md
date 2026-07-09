# Citation Management

## Purpose

Define how citations are managed in ResearchAI writing workflows.

---

## Citation Source of Truth

### Rule: All citations must come from Zotero

When writing in `06_Writing/`, all paper citations must reference entries in the Zotero database.

**Never** generate citations from memory or guess bibliographic details.

### Why

- AI agents (including Codex) can hallucinate citations
- Fake citations destroy research credibility
- Zotero provides verified, authoritative metadata
- BibTeX ensures consistent formatting

---

## Citation Workflow

### For Human Researchers

1. Write manuscript in `06_Writing/`
2. Look up citation in Zotero
3. Insert citation from Zotero (via Zotero plugin or manual BibTeX copy)
4. Verify all citations exist in Zotero before submission

### For AI Agents

When an AI agent is asked to write or edit a manuscript:

1. **Check KnowledgeVault first** — if a paper was already analyzed, its note contains the verified citation info.
2. **Check Zotero** — if the paper is in the Zotero database, use the BibTeX entry.
3. **If neither exists** — do NOT fabricate a citation. Instead:
   - Note `[citation needed: <paper title>]` as a placeholder
   - Flag it for the human researcher to verify and add to Zotero

---

## Prohibited Actions

### Never Fabricate

The following are strictly prohibited:

- Inventing author names
- Guessing publication years
- Creating fake DOIs
- Making up journal/conference names
- Fabricating page numbers or volume/issue info

### When in Doubt

If a citation detail is uncertain:

1. Mark it as `[uncertain: <detail>]` in the manuscript
2. Add a TODO note in the writing plan
3. Do not proceed with the citation until verified

---

## Citation Verification Checklist

Before submitting any manuscript:

- [ ] Every citation has a matching entry in Zotero
- [ ] All author names match Zotero exactly
- [ ] All years match Zotero exactly
- [ ] All DOIs are verified (clickable and resolving)
- [ ] No citations are missing from the bibliography
- [ ] No bibliography entries are missing from citations

---

## Future: Automated Citation Insertion

When Zotero + Better BibTeX is configured:

1. AI agent reads `bibliography.bib` from `01_Literature/04_Literature_Index/`
2. Agent searches BibTeX for matching paper by title/authors
3. Agent inserts the verified BibTeX key into the manuscript
4. Manuscript is compiled with proper citation formatting

This automation is planned for a future stage.
