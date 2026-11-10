---
name: review
description: Reviews the paper like a rigorous reviewer at your venue - novelty, validity, significance, and writing - checks every citation is real and correct, and gives you a checklist of what passed, what failed, and what to fix first. Quick, full, or submission mode. Use for "review my paper", "quick review", "check my citations", "can I submit", or /review [section or mode].
---

# Review

Tough, fair, constructive, like a strong reviewer at **their venue** (read its call for papers and 2-3 recent accepted papers to calibrate). Reviews are frequent and cheap, not a final exam. Same paper in, same checklist out. Optional focus: a section (`/review intro`), or a mode (`/review full`, `/review citations`, `/review submit`).

## Modes
- **Quick** (default): only the tests whose inputs exist; short checklist, next 3 fixes, what changed since last time.
- **Full:** all tests, whole paper, the strongest counterexample search, and a verdict.
- **Citations:** the citation check below, alone.
- **Submission:** `references/submission.md`: current venue rules, template, anonymity, required statements, placeholders, artifacts, deadlines; also camera-ready.

## What gets checked
1. **Novelty:** closest work named and compared; the difference stated in one sentence; why it matters.
2. **Validity:** what is measured matches what is claimed; fair baselines; confounds, leakage, sample size and seeds; claim strength matches evidence (causal, generalization, improvement); limits stated honestly.
3. **Significance:** who cares and what changes for them.
4. **Writing:** clear contribution early, one idea per paragraph, consistent terms (`terms.md`) and numbers, figures that stand alone, no AI-sounding phrasing, no `TODO`, `[CITE?]`, `??`, `XXX`.
5. **Citations (every entry in the `.bib`):** the paper exists (DOI resolves, or ACL Anthology, ACM DL, arXiv, OpenReview); title, authors, year, and venue match Crossref or Semantic Scholar; preprints marked as such; every `\cite` key exists and every entry is cited; each citation supports the sentence it is attached to. Can't verify → `[CITE?]` and list it.
Full test list, scoring, and verdict formula: `references/rubric.md`.

## Rules that keep it fair and repeatable
- **Binary tests.** A test passes only with a **quote or location**. No evidence → fail ("not found"). Never pass on effort or tone.
- **Fixed tests, fixed order.** Don't add, drop, or reword tests during a review. Unsure → fail, and say what evidence would flip it.
- **Scores are arithmetic** (rubric). Unwritten parts are ➖ not yet applicable, not failures.

## Give back a checklist (20-second read, then details)
```
Novelty   3.5/5  ✅ closest work named   ❌ why it matters unclear
Validity  4.0/5  ✅ fair baselines       ❌ no leakage check
Writing          🔧 3 placeholders left
Citations        ✅ 41 verified   ❌ 2 not found   🔧 1 wrong year
Since last time: +4 passed, 1 newly failed
Fix first: "why it matters" (Major) → write intro
```
Legend: ✅ passed · ❌ failed · 🔧 to fix · ➖ not yet applicable · 🌟 section mean ≥ 4.5.
Save the full report in `components/review.md`: what the paper claims, strengths (quoted), every test with location, fixes by severity (**Major** or **Suggestion**, each naming the skill that helps), what would flip each fail, and a History row (date, mode, scores, fails).

## After
Every **Major** fix becomes a ticket on the board with a priority. Don't rewrite the paper during a review; suggest `write`, `plan-method`, `validate-idea`, or `find-papers` for each fix. Optional second opinion: free AI chats via `setup-llms`; their points inform fixes but never change the scores.
