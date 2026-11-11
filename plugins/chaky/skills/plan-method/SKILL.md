---
name: plan-method
description: Plans and runs your methodology - what you change (IV), what you measure (DV), conditions, participants or data, randomisation and counterbalancing, sample size, analysis plan, pilots, freezing the plan, and logged runs. Use for "plan my method", "what is my IV or DV", "how many participants", "plan my experiments", "run the pilot", "set up models", "help me label data", or /plan-method [part], e.g. /plan-method IV.
---

# Plan Method

Design a **fair** experiment and choose the tools, learning from 5-15 close papers. Every choice needs a reason. Focus: `IV`, `DV`, `participants`, `sample size`, `analysis`, `models`, `labeling`, `pilot`, `run` (do just that part).

## 1. Plan (plain words, an example from their study for each)
- **Learn from 5-15 close papers:** designs, measures, tools, baselines, sample sizes (`related_work.md` or `read-papers`); copy what fits, with the source. The contribution type (`references/contribution-types.md`) sets what the method must show.
- **What you change (IV):** conditions, levels, baseline.
- **What you measure (DV):** validated scales where they exist.
- **Who or what:** participants (CHI), or data and splits (NLP).
- **Tools and AI models:** apparatus, software, platforms with versions; models with pinned names, key in `.env`, one logged `call_model()` (`references/models.md`). Paid runs over the estimate: ask first.
- **Labels needed?** Free AI chats do the bulk; humans check a sample at the end (`references/labeling-review.md`).
- **Fair design:** between or within; random assignment; counterbalanced order (Latin square); blocking; baselines get the same data and tuning.
- **Sample size:** power analysis before recruiting (effect from close papers), or seeds and test size for ML.
- **Analysis:** each hypothesis → its test → what counts as success.
- **CHI ethics (critical):** approval and consent recorded before recruiting.
Write it into `experimental_design.md`, `implementation.md`, and the method section.

## 2. Pilot
2-3 people or a small sample: runs end to end? DV moves? Bugs, leaks, confusing instructions? Fix and re-pilot.

## 3. Freeze (critical: ask first)
Final hypotheses, success criteria, analysis, stopping rule → commit and `git tag plan-freeze-1`. Later changes are logged **deviations**; analyses added after seeing results are **exploratory**.

## 4. Run and reflect
One record per run in `experiment_logs/`; participant data never in git. Every ~5 runs: what worked, what surprised, why? Suggest deepen, broaden, pivot (`read-papers`), or conclude (`update-paper`); they choose. Log dead ends. End with the quick sync in `AGENTS.md`. After a pilot or the main study, suggest a full `/update-repo`.
