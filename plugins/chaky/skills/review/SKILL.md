---
name: review
description: Simulates three reviewers and a meta-review at your venue, checks citations and that the paper matches the code, adds a Claude/ChatGPT/Gemini check, and splits fixes into easy and difficult. Use for "review my paper", "quick review", "check my citations", "can I submit", "would ChatGPT accept this", or /review [section or mode].
---

# Review

**Idea storytelling, checked.** Tough and fair, calibrated on **their venue** (call for papers, 2-3 accepted papers). Same paper in, same checklist out. Focus: a section, `full`, `citations`, `submit`.

## Check
1. **Novelty:** idea (new question) and technical (non-obvious method), vs. closest work.
2. **Validity:** internal (confounds, counterbalancing), construct (operational measures), external; fair baselines; claims match evidence.
3. **Paper matches the work:** numbers match `results/`; claimed conditions exist in the code.
4. **Significance:** who cares and what changes.
5. **Writing:** intro's five parts, one contribution, no overpromising; results report only; strong discussion; only what's necessary; no AI phrasing.
6. **Every citation:** exists (DOI, Crossref, Semantic Scholar), details match, every `\cite` has an entry, it supports its sentence.
A test passes only with a quote or location; fixed tests, fixed order; unwritten parts are ➖. Tests and scores: `references/rubric.md`. **Submit** mode: `references/submission.md`.

## Panel
Three short reviews from the tests (strengths, weaknesses, score): **methods expert**, **domain expert**, **skeptic**. Then a **meta-review**: likely decision and what would move it most.

## AI reviewer check (before sharing or submitting)
Many reviewers use AI. Ask whether they have **Claude in Chrome** (then Chaky runs the chats; otherwise they paste). Steps: `references/ai-reviewers.md`; pasting is critical. **Pass** = all three at accept or weak accept; points 2-3 AIs share become tickets.

## Checklist back
```
Novelty   3.5/5  ✅ closest work named   ❌ why it matters unclear
Validity  4.0/5  ✅ fair baselines       ❌ no leakage check
Citations        ✅ 41 ok  ❌ 2 not found
Panel            methods 3 · domain 4 · skeptic 2 → borderline
AI reviewers     Claude ✅ · ChatGPT ❌ · Gemini ✅ → not yet
Easy: fix 2 citations · add leakage check sentence
Difficult: explain why it matters → /update-paper intro
```
**Easy** (< 1 hour: wording, a citation) and **difficult** (plan them: a new baseline, a reframed contribution, each with its skill). Report and a History row go in `components/review.md`; every fix becomes a ticket. Don't rewrite the paper here. End with the quick sync in `AGENTS.md`.
