---
name: find-papers
description: Finds the closest work to your idea, double-checks novelty against it, and pulls out methods, measures, and analyses you can borrow - verified papers only. Also watches for new overlapping papers and handles a paper you just found. Use for "find closest work", "what has been done on X", "is anyone doing this", "what method can I copy", "I found a paper", or /find-papers [topic].
---

# Find Papers

Optional focus: `/find-papers <topic>`. Three jobs, in order of use: **closest work**, a **novelty double-check**, and **methods to borrow** (all in search mode, below). Two more modes: **watch** (`references/watch.md`: periodic scoop check, log the date), **triage** (`references/triage.md`: a new paper in hand; compare, decide, or try it on a side branch). Ask which mode if unclear. A specific paper in hand → triage. Unknown new papers → watch.

## Search mode
Builds a map of the field: what is key, what is supporting, where the gap is. Report three things:
- **Closest work:** the 3-5 papers nearest to ours, each with what it did and what it left open.
- **Novelty double-check:** for each closest paper, one line on how we differ (problem, what we change, what we measure, or method). Overlap is close or direct → say so plainly and suggest `validate-idea`.
- **Methods to borrow:** measures, scales, baselines, datasets, procedures, and analyses from those papers that fit our study, with where to find them; feed these to `plan-method`.

1. **State of the art.** Start with top venues for the area (e.g. CHI, ACL, NeurIPS, ICML); recent papers (about 3-4 years); several positioning angles.
2. **Snowball and backtrack.** For each paper note (a) what it commonly **cites** (backward) and (b) what **cites it** (forward). ACM, IEEE, Semantic Scholar, and Google Scholar show both.
3. **Go one level in.** Read their related work, repeat step 2, two to three rounds.
4. **Read the map.** Usually 1-5 key papers recur; 20+ are supporting. That tells you what Related Work should say.
5. Try close synonyms; communities name the same idea differently.
6. Stop at roughly 20-30 papers, or when searches return mostly known papers.

**Verify before adding:** the paper exists (publisher page, ACL Anthology, ACM DL, arXiv, OpenReview, DOI); title, authors, year, venue match; preprints marked as such (a venue name doesn't make a claim correct). Can't verify → don't list it; say so. **Never write BibTeX from memory:** fetch it from the DOI, Crossref, Semantic Scholar, or the publisher page. Unverifiable → visible placeholder `[CITE?]` and tell the user.

**Record** in `components/related_work.md`: group (relation to our work), citation, link/DOI, venue and year, problem/IV/DV, why it matters (inspires, extends, contrasts), verified. Mark the 1-5 key papers. Report the key papers, field structure, what's done and open, with links, in plain English.
