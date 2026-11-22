---
name: double-check
description: Checks the whole project from the ground up - code, numbers, plan, paper, citations, notes, and board - and fixes what is off, so everything agrees with the latest work. Use before sharing or submitting, after a long break or a big change, or for "double check everything", "check everything from scratch", "recheck my code", "is everything consistent", or /double-check.
---

# Double Check

Everything, from the ground up, in this order: each layer is checked against the one below it. No focus → all of it; a focus (`code`, `numbers`, `paper`) narrows it. It follows each skill's own rules rather than repeating them.

## 1. Code
- Result-deciding code has a tiny test, and the tests pass.
- What ran matches the plan: conditions, configs, models, prompts, seeds (`experimental_design.md`, `experiment_logs/`). Plan deviations are logged.
- No leakage between train and test, or between conditions (`plan-method/references/rigor.md`).
- The one command reruns everything. Rerun on a small case; a full or paid rerun is **critical: ask first**.
- A bug in code behind a result is **critical**: show the cause and the fix, then ask.

## 2. Numbers
Recompute every reported number from raw data with the script (`update-paper/references/stats.md`). A result that is not as expected → the checks in `rigor.md` (*When results are unexpected*).

## 3. Plan
The five musts and the decision table in `plan-method`; each hypothesis confirmed with the researcher.

## 4. Paper (source of truth)
Every section, table, and figure against steps 1-3. Rewrite what is off with `update-paper` rules: numbers, terms used the same everywhere, framing that matches the method, the title. Check every citation (`review/references/citations.md`). Use `⚠ stale` only for what can't be rewritten yet.

## 5. Notes and repo
Bring `components/` in line with the paper and clean up clutter (`update-repo` Update steps 1-4).

## 6. Board
A full `update-board`: every ticket, the whole log.

## Report
```
Checked: code ✅ · numbers ❌ 2 fixed · plan ✅ · paper 4 sections rewritten · citations ❌ 1 not found · notes ✅ · board ✅
Fixed: Table 2 F1 0.81 → 0.79 (script rerun) · "honest agent" used everywhere · 3 caches removed
Needs you: possible bug in scorer.py behind Table 3 (cause: ...) → fix and rerun? · [CITE?] Lee 2024 not found
Next: /review for the reviewer panel
```
Log it as `double check` in `log.md`, then run the quick sync in `AGENTS.md`.
