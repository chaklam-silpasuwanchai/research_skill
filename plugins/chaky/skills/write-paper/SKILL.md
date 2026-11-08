---
name: write-paper
description: Writes or rewrites the paper in the target venue's style, title to conclusion, with consistent claims, terms, and numbers. Use to write, draft, or restructure a paper or section.
---

# Write Paper

After reading, the reader should feel **novelty, validity, significance**.
**Needs:** question, contribution, related work; results for the later sections. Missing results → draft the rest and mark `[TODO: results]`; writing early is fine.
**Calls:** `polish-prose` (always, including its unslop pass, on each section before the user checks it), `find-papers`, `analyze-results`, `grill-me`.

## Entry
Follow `AGENTS.md` (none → offer `start-paper`, adopt mode if the user has files). If a need above is missing, don't block: offer to run the earlier skill, do a quick catch-up, or continue and log an assumption. Finish with the end-of-task routine in `AGENTS.md`.

## Before writing
- Read `components/voice.md` and match the researcher's voice.
- Read 3-5 recent papers from the venue; match their conventions (openings, lengths, how results and limitations are phrased) in your own words.
- Keep claims, terms (`terms.md`), figures, methods, and numbers consistent across the whole paper.

## One sentence first
Before drafting, state the contribution in **one sentence**, and the paper's **What** (what we did), **Why** (why it matters), **So what** (what readers should take away). Confirm with the user. If you can't say it in one sentence, run `grill-me` (argument tree) or go back to `shape-idea`.

## Write in this order; after each section, the user checks before you go on
(Default, because checking each section teaches the writer. If the user says **"fast mode"**, draft the whole paper in one pass, flag open choices, and review it together afterwards.)
**Title:** has the keywords; fancy but not too fancy; provokes reading; says what's novel (and the method if useful); short. Offer 3-5.

**Abstract:** five connected parts: background, problem, methodology, findings, contribution/significance. Signal the gap ("However", "This paper proposes").

**Introduction:** the abstract expanded into five paragraphs, each backed by evidence. Include **Figure 1** (the problem, the insight, how our way changes it); propose three alternative designs for it.

**Related work:** group by how each cluster positions against ours; synthesize, don't list; say how we differ, are inspired by, or extend each. Readers should feel we read widely and know what we're doing. Don't teach experts.

**Methodology and experiment:** follow the venue. CHI: design rationale, apparatus, participants, experimental design, measures. ACL/NeurIPS: methodology = data, simulation, the technique; experiment = comparisons, baselines. Strong rationale, enough detail to replicate, ideas over implementation.

**Results:** by research question or insight; statistics as needed; follow how related work reports.

**Analysis (ACL/NeurIPS):** the planned extras (robustness, transfer, error, feature, network, input/output analysis).

**Discussion:** cover: expected vs unexpected (unexpected in depth); what you achieved vs claimed, the ultimate goal, how far away; comparison with related work; design decisions and their effect; actionable implications; significance; **limitations** (only concrete ones that threaten validity; "tested only in the US" is true of every study, skip it); **future work** (one or two concrete items).

**Conclusion:** simple, nothing new, smooth end.

## Finish
Coherence pass (terms, numbers, claims, figures; every introduction promise delivered). Update status; suggest `review-paper`.

## Loop-backs here
Claim lacks evidence → `run-study` or soften. No clear problem → `shape-idea`. Method not replicable → `run-study`. Novelty flagged → `shape-idea`.
