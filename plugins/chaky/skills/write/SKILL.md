---
name: write
description: Writes the paper with you, section by section or one section you name, in your own voice and the venue's style - including honest statistics, tables, and figures, and a final pass that removes AI-sounding phrasing. Use for "write my introduction", "draft the paper", "rewrite this", "make a figure", "which test", "unslop this", or /write [section], e.g. /write abstract.
---

# Write

After reading, a reviewer should feel **novelty, validity, significance**. Optional focus: `/write abstract`, `intro`, `related work`, `method`, `results`, `discussion`, `figure`, `stats`, `polish`. With a focus, do just that part. Missing results → draft the rest and mark `[TODO: results]`; writing early is fine.

## Before writing
- Read `components/voice.md` (from `setup-writing-style`) and `terms.md`; match their voice and words.
- Read 3-5 recent papers from the venue; follow their conventions in your own words.
- State the contribution in **one sentence**, plus **What** we did, **Why** it matters, **So what**. Can't? Suggest `brain-dump` or `validate-idea` first.

## Sections
Guidance for each section, title to conclusion: `references/sections.md`. Default order: title, abstract, introduction (with Figure 1), related work, method, results, analysis (NLP), discussion, conclusion. Write a section, apply the style rules, then show it. They read it and say what to change; go on when they're happy. **"Fast mode"** → draft the whole paper in one pass and mark open choices.

## Style (every section)
`references/style.md`: one idea per paragraph, strong verbs, verb strength matches evidence ("shows" / "suggests"), every claim backed by a citation, result, or argument, same term for the same concept. Then the **unslop pass** (`references/unslop.md`, scan list `references/patterns.md`): remove generic AI phrasing; keep meaning, claims, citations, and numbers exactly.

## Results, statistics, figures
- **Statistics** (`references/stats.md`): use the planned test from `experimental_design.md`; anything else is labeled exploratory. Effect sizes with intervals, corrections, exact numbers recomputed from raw data by a script in `src/scripts/`.
- **Figures and tables** (`references/figures.md`): one message per figure; three concepts for Figure 1; honest axes, n, and intervals; plotting scripts in `src/scripts/`; the venue's figure rules.

## Citations
Never write BibTeX from memory: fetch it from the DOI, Crossref, Semantic Scholar, or the publisher page. Can't verify → visible `[CITE?]`.

## Finish
Coherence pass: terms, numbers, claims, and figures agree; every promise in the introduction is delivered. Update `current_status.md`, log choices in `log.md`, and say in one line what changed. Suggest `review` when a section or draft is done.
