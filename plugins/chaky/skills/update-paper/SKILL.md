---
name: update-paper
description: Writes and updates your paper (idea storytelling) - first agrees the story with you (background and key papers, problem, research question, solution, findings, contribution), suggesting alternative storylines if you're unsure, then writes or updates sections in your voice, with honest stats and figures, limitations, replies to reviewers, and no AI-sounding phrasing. Use for "write my paper", "update the paper", "what's my story", "write my introduction", "reply to reviewers", or /update-paper [section].
---

# Update Paper

Focus: `story`, `abstract`, `intro`, `related work`, `method`, `results`, `discussion`, `limitations`, `response`, `figure`, `stats`, `polish`. No results yet → write the rest, mark `[TODO: results]`.

## 1. The story first
Ask one at a time (suggest an answer from the repo each time):
Following the lab's one-page outline:
1. **Background:** the context, and the 2-3 key papers it rests on.
2. **Problem:** what remains difficult or unexplained, and for whom.
3. **Research question.**
4. **Proposed solution:** what we do (our one difference from `read-papers`).
5. **Evaluation and key findings:** the evidence; what we found or expect.
6. **Contribution:** what changes because of this work.
Unsure → offer **2-3 alternative storylines** (e.g. problem-first, surprising-finding-first, method-first), each a 4-line arc with what it gains, and recommend one. Save the agreed story in `current_status.md`; every section must follow it.

## 2. Write or update sections
**Say only what's necessary:** every sentence must help the reader understand or believe the story; the rest goes to the appendix or is cut (`references/style.md`). Read `voice.md` and `terms.md`; skim 3-5 recent venue papers. Follow `references/sections.md`, then `references/style.md`, then the unslop pass (`references/unslop.md`, `references/patterns.md`) keeping every claim, number, and citation. Show each section; they comment; continue. **"Fast mode"** → whole draft in one pass. Sections marked `⚠ stale` come first.

## 3. Special parts
- **Stats and figures:** the planned test; effect sizes with intervals; numbers recomputed by script (`references/stats.md`); one message per figure (`references/figures.md`).
- **Limitations:** real threats from `log.md`, deviations, and `review.md`, each with its effect and mitigation; no filler.
- **Response to reviewers:** group points; answer each as changed (where), clarified, disagree (evidence), or out of scope; within the limit.

## Finish
Story, terms, numbers, and claims agree across sections; the intro's promises are delivered. Citations fetched, never invented (`[CITE?]`). Clear `⚠ stale` marks. End with the quick sync in `AGENTS.md`; suggest `review`.
