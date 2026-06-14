# 3 Zero Movement Research — Project Navigation
> Last updated: 2026-03-28
> Status: Active

## Overview

Research project investigating the impact of the 3 Zero Movement (zero poverty, zero unemployment, zero net carbon emissions) in Bangladesh. Full paper under development following abstract publication at the 18th International Conference on Engineering & Natural Sciences (Kyrenia, TRNC, December 2025).

**Author:** Minhajul Abedin
**Department:** Applied Mathematics

---

## Folder Guide

| Folder | Contents |
|--------|----------|
| `drafts/` | Working paper outline and draft sections |
| `methods/` | Dataset descriptions, metrics definitions, model configurations |
| `literature/` | Paper summaries and reference notes |
| `experiments/` | Analysis experiments and results tracking |
| `daily-log/` | Daily research log entries (YYYY-MM-DD.md) |
| `decisions/` | Decision log — why X was chosen over Y |
| `backups/` | Preserved earlier versions for fallback |

## Key Files

- **Paper outline:** `drafts/paper-outline.md`
- **Conference article (v3):** `drafts/paper-article-v3-data-verified.md`, `drafts/paper-article-v3.tex`
- **Enriched monograph (v2):** `drafts/paper-monograph-v2-enriched.md`, `drafts/paper-monograph-v2.tex`, `drafts/paper-monograph-v2.pdf`
- **Data source map:** `data/data-source-map.md`
- **Initial proposal backup:** `backups/initial-research-proposal-backup.md`
- **Original proposal:** `../initialresearchproposal.md`
- **Published abstract:** `../publishedabstract.md`

## Reproducible Pipeline

From `research-notes/code/`:

```bash
python analysis.py          # core 3ZPI indicators → data/processed/
python fetch_secondary.py   # contextual indicators → secondary_context.csv
python generate_figures.py  # fig1–fig8 → figures/
```

Compile PDF (from `drafts/`):

```bash
pdflatex paper-monograph-v2.tex && bibtex paper-monograph-v2 && pdflatex paper-monograph-v2.tex && pdflatex paper-monograph-v2.tex
```
