---
name: update-paper
description: Reads the 10-15 closest papers (what to copy, your one difference), agrees the story with you, then writes or updates the paper in plain English like your venue. Use for "is this novel", "I found a paper", "write my paper", "reply to reviewers", or /update-paper [part].
---

# Update Paper

Focus: `papers`, `story`, `abstract`, `intro`, `related work`, `method`, `results`, `discussion`, `limitations`, `response`, `figure`, `stats`, `polish`. No results yet → write the rest, mark `[TODO: results]`.

## 1. Papers first
Fewer than 10 verified papers in `related_work.md`, focus `papers`, or "is this novel?" → follow `references/papers.md`: search, read the 10-15 closest, the field in three lines (consensus, disagreements, open questions), what to copy, **the one difference**, novelty and validity. A paper in hand → `references/triage.md`; scoop check → `references/watch.md`.

## 2. The story
Ask one at a time, suggesting an answer each time (the lab's one-page outline): **background** and 2-3 key papers · **problem** · **research question** · **proposed solution** (our one difference) · **evaluation and key findings** · **contribution**. Unsure → **2-3 alternative storylines**, each a 4-line arc; recommend one. Save it in `current_status.md`.

## 3. Write or update sections
**First read `voice.md` (their style) and `terms.md` (their words)**; every sentence follows them. Empty `voice.md` → suggest `/setup-writing-style`.
Reviewers mostly decide from the **abstract and introduction**: most care there, then the **discussion**. **Say only what's necessary**; the rest goes to the appendix or is cut. Before each section, read how 2-3 recent accepted venue papers write it and follow their structure; plain English, terms introduced where first needed, never a glossary. Follow `references/sections.md`, `references/style.md`, then the unslop pass (`references/unslop.md`, `references/patterns.md`), keeping every claim, number, and citation. Show each section; they comment. **"Fast mode"** → whole draft at once. `⚠ stale` sections first. **Before showing any edit:** the skeptical-reviewer pass, and every term defined before first use and named the same everywhere (`references/style.md`).
- **Framing** (abstract, intro, contributions): `references/framing.md`; novelty searched first, framing matches the method.
- **Stats, figures, limitations, reviewer replies:** `references/stats.md`, `figures.md`, `sections.md`.

## Finish
**Title check:** does the title still fit the story and the one difference? If a better one exists, suggest 2-3 with a reason each next to the current one; they choose (keeping it is fine). Story, terms, numbers, and claims agree; the intro's promises are delivered; citations fetched, never invented (`[CITE?]`). End with the quick sync in `AGENTS.md`; suggest `review`.
