---
name: find-papers
description: Finds the closest work to your idea, double-checks novelty against it, and pulls out methods, measures, and analyses you can borrow - verified papers only. Also watches for new overlapping papers and handles a paper you just found. Use for "find closest work", "what has been done on X", "what method can I borrow", "I found a paper", "am I scooped", or /find-papers [topic].
---

# Find Papers

Focus: a topic. A paper in hand → **triage** (`references/triage.md`). Worried about new papers → **watch** (`references/watch.md`). Otherwise **search**:

1. Recent papers (about 3-4 years) at top venues for the area; try synonyms, since fields name things differently.
2. **Snowball:** what each paper cites, and what cites it (Semantic Scholar, Google Scholar, ACM DL). Two or three rounds.
3. Stop at about 20-30 papers, or when searches return what you already have.

## Report three things
- **Closest work:** the 3-5 nearest papers, what each did and left open.
- **Novelty check:** one line each on how we differ (problem, what we change, what we measure, method). Close or direct overlap → say so plainly; suggest `validate-idea`.
- **Methods to borrow:** scales, measures, baselines, datasets, procedures, analyses that fit our study, with where to find them (for `plan-method`).

## Verify every paper
It exists (DOI, publisher, ACL Anthology, arXiv, OpenReview); title, authors, year, venue match; preprints marked. Can't verify → leave it out and say so. BibTeX is fetched, never typed from memory.

Record in `components/related_work.md`: group, citation, link, venue and year, what they change and measure, why it matters to us, verified. Mark the key papers.
