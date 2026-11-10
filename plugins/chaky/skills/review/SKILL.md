---
name: review
description: Reviews your paper like a rigorous panel at your venue - three reviewers and a meta-review on novelty, validity, significance, writing - checks every citation is real and correct, and gives you a checklist of what passed, what failed, and what to fix first. Use for "review my paper", "quick review", "check my citations", "can I submit", or /review [section or mode].
---

# Review

Tough and fair, like a strong reviewer at **their venue** (calibrate on its call for papers and 2-3 accepted papers). Same paper in, same checklist out. Focus: a section, or `full`, `citations`, `submit`.

## Check
1. **Novelty:** closest work compared; the difference in one sentence; why it matters.
2. **Validity:** measures match claims; fair baselines; confounds, leakage, sample size; claim strength matches evidence; honest limits.
3. **Significance:** who cares and what changes.
4. **Writing:** contribution early, clear paragraphs, consistent terms and numbers, no AI phrasing, no `TODO`, `[CITE?]`, `??`.
5. **Every citation:** exists (DOI, Crossref, Semantic Scholar, Anthology, arXiv); title, authors, year, venue match; every `\cite` key has an entry and every entry is cited; it supports its sentence.
Tests, scores, verdict: `references/rubric.md`. **Submit** mode: `references/submission.md`.

## Panel (like a real venue)
After the checks, three short reviews (strengths, weaknesses, score each), grounded in the test results: a **methods expert**, a **domain expert**, and a **skeptic**. Then a **meta-review** (area chair): likely decision (accept, borderline, reject), where the reviewers agree and disagree, and the 2-3 changes that would most move the decision. Quick mode: one combined view.

## Rules
A test passes only with a **quote or location**; no evidence → fail. Fixed tests, fixed order. Unwritten parts are ➖, not failures.

## Checklist back
```
Novelty   3.5/5  ✅ closest work named   ❌ why it matters unclear
Validity  4.0/5  ✅ fair baselines       ❌ no leakage check
Writing          🔧 3 placeholders
Citations        ✅ 41 ok  ❌ 2 not found  🔧 1 wrong year
Panel            methods 3 · domain 4 · skeptic 2 → borderline
Fix first: why it matters (Major) → /write intro
```
Full report and a History row go in `components/review.md`. Major fixes become tickets. Don't rewrite the paper here; suggest the skill for each fix. End with the quick sync in `AGENTS.md`.
