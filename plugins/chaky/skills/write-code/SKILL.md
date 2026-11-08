---
name: write-code
description: Writes research code that is tested and reproducible - test-first metrics and splits, mutation testing, pinned environments, configs, seeds, one-command reruns. Use when writing or fixing code in src, when results look suspicious, or when a run cannot be reproduced.
---

# Write Code

Called by `run-study`. Also works alone. Code that decides a result must be trusted before the result is.

## 1. Test first where it matters
For metrics, scoring, data loading, splits, and leakage checks: write a test with a tiny hand-computed answer **first**, watch it fail, then implement. Put tests in `src/tests/` (CHI analysis scripts: a small fixture with a known summary). Run all tests before any real run.

### Test the tests (light mutation testing)
For the few functions that decide results (metrics, scoring, splits, label mapping), check the tests would catch a bug. A mutation tool (Python: `mutmut` or `cosmic-ray`) makes small changes (flip a comparison, off-by-one, swap labels) and reruns the tests. A **surviving** mutant means the tests are too weak: add a test that kills it, or note it as equivalent (no behavior change). No tool? Make 5 mutants by hand (flip an operator, shift an index, swap two labels, drop a filter, change a threshold); each must make a test fail. Scope: result-deciding code only (it is slow on whole projects). Log the outcome in `log.md`. CHI: apply to the analysis script on a fixture; skip UI prototypes.

## 2. Diagnose before patching
Reproduce → shrink to the smallest failing case → state a hypothesis → test it → fix the **cause** → add a regression test. A bug that touched results gets a `log.md` entry (what, effect, lesson).

## 3. Reproducibility checklist
- Pinned environment (lockfile or versioned requirements)
- One config file per run: hyperparameters, paths, seeds
- Seeds set and logged; data version or hash recorded; git commit hash logged with each run
- Raw outputs kept; no hard-coded absolute paths; secrets only in `.env`
- **One command** reruns raw data → results → figures

## 4. Track runs simply
One record per run in `src/experiment_logs/`: run ID, commit, config, metrics, cost, notes. Add W&B or MLflow only if the user wants it.

## 5. Small steps
Run on a tiny sample first (pilot), commit often with clear messages. Treat AI-written code as untrusted until you've read it, run the tests, and checked for silent failures (swallowed errors, wrong split, wrong label order); tag it `ai-executed` in the log.
