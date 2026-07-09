# MinerU Cleaning Rules

## Purpose

Define what to keep and what to remove when converting raw MinerU `full.md` output into processed markdown for AI analysis.

---

## Keep (Retain)

### Essential Content

| Element | Reason |
|---|---|
| Title | Paper identification |
| Authors | Citation and attribution |
| Abstract | Core summary for screening |
| Keywords | Classification and search |
| Introduction | Research problem and motivation |
| Problem Definition | Formal problem statement |
| Method / Approach | Technical contribution |
| Mathematical Formulas | Core technical content |
| Tables | Results and comparisons |
| Experimental Setup | Reproducibility context |
| Results | Quantitative findings |
| Ablation Studies | Component analysis |
| Discussion | Interpretation and limitations |
| Conclusion | Main takeaways |
| References (top 10) | Key citations for knowledge linking |

### Formatting

- **Headings**: Keep all heading levels (H1-H6)
- **Section structure**: Preserve the paper's logical structure
- **Equations**: Keep LaTeX/math notation intact
- **Tables**: Preserve markdown table format

---

## Remove (Discard)

### Parsing Artifacts

| Element | Reason |
|---|---|
| Page headers | MinerU adds headers with page info |
| Page footers | Footer text, copyright notices |
| Page numbers | Not useful for AI analysis |
| Repeated text blocks | MinerU sometimes duplicates content |
| Layout JSON references | `![](uuid_hash)` — keep index, remove hash |
| Model JSON metadata | Internal MinerU files, not paper content |
| Content list files | `*_content_list.json` — parsing artifacts |
| `_model.json` | MinerU model configuration |

### Redundant Content

- Duplicate abstracts
- Repeated figure captions that appear in both text and layout files
- MinerU confidence scores or parsing metadata

---

## Image Handling

### Policy

- **Keep**: Image references in context (e.g., "Fig. 1 shows...")
- **Remove**: Large image hash references like `![](d44580195eb4cfe0e076f97c772477f90e8506d85d0ea52cec9e47881ea24b6f.jpg)`
- **Do NOT**: Copy all images into the processed markdown directory

### Rationale

Images are stored in `02_MinerU_Output/{paper}/images/`. The processed markdown should reference them by relative path, not embed them. This keeps the processed markdown lean and text-focused.

### Image Index

If the paper has important figures, add a reference table in the "Notes for AI Agent" section:

```
Important figures:
- Fig. 1: Seismic data acquisition diagram (02_MinerU_Output/{id}/images/fig1.jpg)
- Fig. 5: Method architecture (02_MinerU_Output/{id}/images/fig5.jpg)
```

---

## Encoding Fixes

### Common Issues

1. **Chinese characters garbled**: MinerU Desktop sometimes produces mojibake. Fix by:
   - Opening the raw `full.md` in UTF-8
   - Checking for replacement characters (�)
   - Re-encoding if necessary

2. **Math symbols**: Ensure LaTeX formulas are preserved as-is. Do not convert `∑` to `sum` or vice versa.

3. **Special characters**: Hyphens, dashes, quotes — normalize to standard ASCII/markdown equivalents.

---

## Processing Checklist

When cleaning a MinerU output:

- [ ] Remove page headers and footers
- [ ] Remove page numbers
- [ ] Remove layout JSON references (keep image descriptions)
- [ ] Remove model JSON and content list references
- [ ] Remove duplicate text blocks
- [ ] Fix encoding issues (Chinese characters, special symbols)
- [ ] Preserve all section headings
- [ ] Preserve all mathematical formulas
- [ ] Preserve all tables
- [ ] Preserve abstract and keywords
- [ ] Add "Notes for AI Agent" section with parsing quality assessment
- [ ] Save with Paper ID filename

---

## Quality Assessment

After cleaning, assess the result:

| Quality | Criteria |
|---|---|
| **Good** | All sections present, formulas intact, tables readable, no encoding issues |
| **Fair** | Some minor issues (missing figure, garbled equation) but core content intact |
| **Poor** | Major sections missing, severe encoding issues, unreliable for analysis |

If quality is "Poor", note it in the Literature Index and consider re-processing the PDF.
