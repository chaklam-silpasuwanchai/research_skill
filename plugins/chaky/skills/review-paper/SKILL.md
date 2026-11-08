---
name: review-paper
description: Chaky as a tough, repeatable reviewer - yes/no checklist for novelty, validity, and writing, as a quick checkpoint or full review, plus the submission and camera-ready check. Use for "quick review", "how am I doing", "would this pass at CHI", "can I submit now", or anonymizing.
---

# Review Paper (Chaky as Reviewer)

Tough, fair, constructive. Reviews are **frequent and cheap**, not a final exam. Same paper in, same checklist out.
**Needs:** something to review (a section, a draft, or at least the question and abstract). Unwritten parts are ➖ not yet applicable, not failures.

## Entry
Follow `AGENTS.md` and read the previous `components/review.md`. No repo → offer `start-paper`. Finish with the end-of-task routine in `AGENTS.md`; the summary is the checklist below.

## Three modes
- **Checkpoint** (default, any time; after each stage, milestone, or section). Run only the tests whose inputs exist. Output: short checklist, next 3 fixes, what changed since last time.
- **Full** (on request, or before submitting). All tests, whole paper, plus the counterexample search and the verdict.
- **Submission** (when Full says "likely accept range", or on "can I submit now"). Follow `references/submission.md`: current venue rules, template, anonymity, required statements, references, placeholders, artifacts, deadlines. Also handles camera-ready.

## What makes it deterministic
1. **Binary tests only** (`references/rubric.md`). A test passes only with a **quote or location** from the paper or repo. No evidence found → fail ("not found"). Never pass on effort or tone.
2. **Fixed tests and order.** Run them in rubric order. Don't add, drop, reword, or reweigh tests, severities, or thresholds during a review. Unsure → fail and say what evidence would flip it.
3. **Scores are arithmetic.** Question score = 1 + tests passed (of 4), so 1-5. Section score = mean of assessable questions (1 decimal). Coverage = assessable questions / total.
4. **Scans are literal.** Placeholders (`TODO`, `[CITE?]`, `??`, `XXX`); universal words ("all", "any", "always", "never", "state of the art", "across", "generaliz*", "robust") each compared with the conditions tested; baseline count; sample or seed count; a promises-vs-delivery table (each introduction promise → where it is delivered).
5. **Record, then compare.** Write `components/review.md`; append a History row (date, mode, scope, Novelty, Validity, fails by severity); list the tests that flipped since the last row.

## Report (plain English first)
Start with a checklist the user can read in 20 seconds, with this legend: ✅ passed · ❌ failed · 🔧 fix to do · ➖ not yet applicable · 🌟 section mean ≥ 4.5.

```
Novelty 3.5/5  ✅ closest work named  ❌ why it matters is unclear
Validity 4.0/5 ✅ fair baselines      ❌ no leakage check
Writing        🔧 3 placeholders left
Since last time: +4 passed, 1 newly failed
Next: fix "why it matters" (Major)
```
Then `review.md` holds: 1) what the paper claims (shows whether it was understood); 2) strengths (passed tests, quoted); 3) all tests with ✅/❌/➖ and locations; 4) writing checklist; 5) fixes, ordered by severity, then lowest section score, then rubric order, each labeled **Major** (a 🔴 fail, or a failed test in a question scoring ≤3) or **Suggestion**, each naming the skill that helps; 6) what evidence would flip the failed tests; 7) History table.

## Outside reviews (optional, Full mode)
Offer `use-llms` so free Gemini, Claude, or ChatGPT chats review novelty, validity, and writing. Their points inform the fixes; they never change the scores.

## Verdict (Full mode only; fixed formula in the rubric)
Checkpoint mode reports trend, not a verdict.

## Fixes become tickets
Every **Major** fix becomes a ticket on the board (`plan-tickets`), rated 1-5 with the researcher. Suggestions stay in `review.md`.

## Where weak areas go
Novelty → `shape-idea`. Validity and methodology → `run-study`. Writing → `write-paper`. Figures → `analyze-results`.
