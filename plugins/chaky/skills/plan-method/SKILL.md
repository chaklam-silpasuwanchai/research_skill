---
name: plan-method
description: Plans and runs your methodology - what you change (IV), what you measure (DV), conditions, participants or data, randomisation and counterbalancing, sample size, analysis plan, pilots, freezing the plan, and logged runs. Use for "plan my method", "what is my IV or DV", "how many participants", "plan my experiments", "run the pilot", or /plan-method [part], e.g. /plan-method IV.
---

# Plan Method

Every choice needs a reason: a past paper or a sound argument. Focus: `IV`, `DV`, `participants`, `sample size`, `analysis`, `pilot`, `run` (do just that part).

## 1. Plan (plain words, an example from their study for each)
- **Contribution type** (empirical, design, artifact, theory; `references/contribution-types.md`) decides what the method must show. Borrow methods from the closest papers (`find-papers`).
- **What you change (IV):** conditions, levels, baseline.
- **What you measure (DV):** validated scales where they exist; when measured.
- **Who or what:** participants and recruitment (CHI), or data, splits, models (NLP; `setup-llms`).
- **Design:** between or within; random assignment; counterbalance order (e.g. Latin square); block on a factor that matters.
- **Sample size:** power analysis before recruiting (effect from close papers, alpha .05, power .8), or seeds and test size for ML.
- **Analysis:** each hypothesis → its test → what counts as success.
- **CHI ethics (critical):** approval, consent, and data handling recorded before any recruiting.
Write it into `experimental_design.md`, `implementation.md`, and the method section.

## 2. Pilot
Small runs (2-3 people or a small sample): runs end to end? DV moves? Bugs, leaks, confusing instructions? Fix and re-pilot.

## 3. Freeze (critical: ask first)
Final hypotheses, success criteria, analysis, stopping rule → commit and `git tag plan-freeze-1`. Later changes are logged **deviations**; analyses added after seeing results are **exploratory**.

## 4. Run and reflect
One record per run or session in `experiment_logs/`; participant data in `src/data/`, never in git. Every ~5 runs: what worked, what surprised, why? Suggest deepen, broaden, pivot (`validate-idea`), or conclude (`write`); they choose. Log dead ends with the lesson.
