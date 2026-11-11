---
name: find-papers
description: Searches for papers on your topic and finds the 10-15 closest to your idea - verified papers only - so read-papers can read them closely. Also watches for new overlapping papers and handles a paper you just found. Use for "find closest work", "what has been done on X", "I found a paper", "am I scooped", or /find-papers [topic].
---

# Find Papers

Focus: a topic. A paper in hand → **triage** (`references/triage.md`). Worried about new papers → **watch** (`references/watch.md`). Otherwise **search**:

1. Recent papers (about 3-4 years) at top venues for the area; try synonyms, since fields name things differently.
2. **Snowball:** what each paper cites, and what cites it (Semantic Scholar, Google Scholar, ACM DL). Two or three rounds.
3. Stop at about 20-30 papers, or when searches return what you already have.

## Report
- **The map:** the key papers, the groups, what's done and what's open.
- **Closest 10-15:** ranked by closeness to our idea. Close or direct overlap → say so plainly.
Then suggest `/read-papers` to read the closest ones closely: what to borrow, and our one difference.

## Verify every paper
It exists (DOI, publisher, ACL Anthology, arXiv, OpenReview); title, authors, year, venue match; preprints marked. Can't verify → leave it out and say so. BibTeX is fetched, never typed from memory.

Record in `components/related_work.md`: group, citation, link, venue and year, what they change and measure, why it matters to us, verified. Mark the key papers; a close overlap becomes a ticket. End with the quick sync in `AGENTS.md`.
