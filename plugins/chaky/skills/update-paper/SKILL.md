---
name: update-paper
description: Writes and updates your paper - first agrees the story with you (background and key papers, the key problem, the key solution, the key findings), suggesting alternative storylines if you're unsure, then writes or updates sections in your voice, with honest stats and figures, limitations, replies to reviewers, and no AI-sounding phrasing. Use for "write my paper", "update the paper", "what's my story", "write my introduction", "reply to reviewers", or /update-paper [section].
---

# Update Paper

Focus: `story`, `abstract`, `intro`, `related work`, `method`, `results`, `discussion`, `limitations`, `response`, `figure`, `stats`, `polish`. No results yet → write the rest, mark `[TODO: results]`.

## 1. The story first
Ask one at a time (suggest an answer from the repo each time):
1. **Background:** the world before us, and the 2-3 key papers it rests on.
2. **Key problem:** what's missing or broken.
3. **Key solution:** what we do (our one difference from `read-papers`).
4. **Key findings:** what we found, or expect to.
5. **So what:** who cares and what changes.
Unsure → offer **2-3 alternative storylines** (e.g. problem-first, surprising-finding-first, method-first), each a 4-line arc with what it gains, and recommend one. Save the agreed story in `current_status.md`; every section must follow it.

## 2. Write or update sections
Read `voice.md` and `terms.md`; skim 3-5 recent venue papers. Follow `references/sections.md`, then `references/style.md`, then the unslop pass (`references/unslop.md`, `references/patterns.md`) keeping every claim, number, and citation. Show each section; they comment; continue. **"Fast mode"** → whole draft in one pass. Sections marked `⚠ stale` come first.

## 3. Special parts
- **Stats and figures:** the planned test; effect sizes with intervals; numbers recomputed by script (`references/stats.md`); one message per figure (`references/figures.md`).
- **Limitations:** real threats from `log.md`, deviations, and `review.md`, each with its effect and mitigation; no filler.
- **Response to reviewers:** group points; answer each as changed (where), clarified, disagree (evidence), or out of scope; within the limit.

## Finish
Story, terms, numbers, and claims agree across sections; the intro's promises are delivered. Citations fetched, never invented (`[CITE?]`). Clear `⚠ stale` marks. End with the quick sync in `AGENTS.md`; suggest `review`.
