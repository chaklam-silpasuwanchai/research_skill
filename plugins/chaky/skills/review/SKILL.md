---
name: review
description: Simulates three reviewers and a meta-review at your venue, checks citations and that the paper matches the code, and splits improvements into easy and difficult. Use for "review my paper", "quick review", "check my citations", "can I submit", or /review [section or mode].
---

# Review

**Idea storytelling, checked.** Tough and fair, calibrated on **their venue** (its call for papers, 2-3 accepted papers). Same paper in, same checklist out. Focus: a section, `full`, `citations`, `submit`.

## Check
1. **Novelty:** idea (new question) and technical (non-obvious method), vs. closest work.
2. **Validity:** internal (confounds, controls, counterbalancing), construct (operational measures), external (where it holds); fair baselines; claim strength matches evidence.
3. **Paper matches the work:** every number and table matches a script output in `results/`; every condition and method the paper claims exists in the code and logs.
4. **Significance:** who cares and what changes.
5. **Writing:** intro's five parts and one contribution, no overpromising; results report only; strong discussion; only what's necessary; no AI phrasing.
6. **Every citation:** exists (DOI, Crossref, Semantic Scholar), details match, every `\cite` has an entry and vice versa, it supports its sentence.
Tests, scores, verdict: `references/rubric.md`. **Submit** mode: `references/submission.md`.

## Panel (like a real venue)
Three short reviews grounded in the tests (strengths, weaknesses, score): **methods expert**, **domain expert**, **skeptic**. Then a **meta-review**: likely decision, where they agree and disagree, what would move it most. Quick mode: one combined view.

## Rules
A test passes only with a **quote or location**; no evidence → fail. Fixed tests, fixed order. Unwritten parts are ➖, not failures.

## Checklist back
```
Novelty   3.5/5  ✅ closest work named   ❌ why it matters unclear
Validity  4.0/5  ✅ fair baselines       ❌ no leakage check
Writing          🔧 3 placeholders
Citations        ✅ 41 ok  ❌ 2 not found  🔧 1 wrong year
Panel            methods 3 · domain 4 · skeptic 2 → borderline
Easy: fix 2 citations · add leakage check sentence
Difficult: explain why it matters (reframe intro) → /update-paper intro
```
## Improvements
- **Easy (< 1 hour each):** wording, a citation, a caption, a stated limit.
- **Difficult (plan them):** a new baseline, more participants, a reframed contribution; each with its effect and the skill to use.
Full report and a History row go in `components/review.md`. Every fix becomes a ticket. Don't rewrite the paper here; suggest the skill for each fix. End with the quick sync in `AGENTS.md`.
