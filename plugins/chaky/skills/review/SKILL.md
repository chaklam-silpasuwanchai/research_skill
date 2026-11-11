---
name: review
description: Simulates three reviewers and a meta-review at your venue - novelty, validity, significance, writing - checks every citation, and suggests improvements split into easy fixes and difficult ones. Use for "review my paper", "quick review", "check my citations", "can I submit", or /review [section or mode].
---

# Review

Tough and fair, calibrated on **their venue** (its call for papers, 2-3 accepted papers). Same paper in, same checklist out. Focus: a section, `full`, `citations`, `submit`.

## Check
1. **Novelty:** closest work compared; the difference in one sentence; why it matters.
2. **Validity:** measures match claims; fair baselines; confounds, leakage, sample size; claim strength matches evidence; honest limits.
3. **Significance:** who cares and what changes.
4. **Writing:** contribution early, clear paragraphs, consistent terms and numbers, no AI phrasing, no `TODO`, `[CITE?]`, `??`.
5. **Every citation:** exists (DOI, Crossref, Semantic Scholar); title, authors, year, venue match; every `\cite` key has an entry and vice versa; it supports its sentence.
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
- **Easy (do now, < 1 hour each):** wording, a missing citation, a clearer figure caption, a stated limitation.
- **Difficult (plan them):** a new baseline, more participants, a reframed contribution, an extra analysis. Each with its effect on the decision and the skill to use.
Full report and a History row go in `components/review.md`. Every fix becomes a ticket (easy ones at priority 3-4, difficult ones rated by impact). Don't rewrite the paper here; suggest the skill for each fix. End with the quick sync in `AGENTS.md`.
