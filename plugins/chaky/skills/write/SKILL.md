---
name: write
description: Writes the paper with you, section by section or the section you name, in your voice and the venue's style - including honest stats, figures, and a pass that removes AI-sounding phrasing. Use for "write my introduction", "draft the paper", "rewrite this", "make a figure", "which test", "unslop this", or /write [section], e.g. /write abstract.
---

# Write

A reviewer should come away feeling **novel, valid, significant**. Focus: `abstract`, `intro`, `related work`, `method`, `results`, `discussion`, `figure`, `stats`, `polish`. No results yet → write the rest and mark `[TODO: results]`.

## Before
Read `voice.md` and `terms.md`. Skim 3-5 recent papers from the venue. State the contribution in **one sentence** (what we did, why it matters, so what); can't → suggest `brain-dump`.

## Each section
Follow `references/sections.md`. Write it, apply `references/style.md`, then the unslop pass (`references/unslop.md`, `references/patterns.md`): keep every claim, number, and citation exactly. Show it; they comment; continue. **"Fast mode"** → whole draft in one pass.

## Stats and figures
- Use the planned test from `experimental_design.md`; others are labeled exploratory. Effect sizes with intervals; numbers recomputed by a script (`references/stats.md`).
- One message per figure; honest axes, n, intervals; script in `src/scripts/` (`references/figures.md`).

## Finish
Terms, numbers, and claims agree across sections; the intro's promises are delivered. Citations fetched, never invented (`[CITE?]`). Say what changed in one line; suggest `review`.
