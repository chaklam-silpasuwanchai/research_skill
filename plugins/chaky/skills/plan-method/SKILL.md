---
name: plan-method
description: Plans and runs your study in the lab's terms - IV, DV, confounding, control, and random variables, design, sample size, analysis, tools, AI models, labeling, pilots, and runs - learning from 5-15 close papers. Use for "plan my method", "what is my IV or DV", "how many participants", "run the pilot", "help me label data", or /plan-method [part].
---

# Plan Method

**Idea testing:** design a fair study and choose the tools, learning from 5-15 close papers. Lab terms (`terms.md`), glossed the first time; every choice needs a reason. Focus: `IV`, `DV`, `variables`, `design`, `sample size`, `analysis`, `models`, `labeling`, `pilot`, `run`, `replicate`.

## 1. Plan (an example from their study for each)
- **Contribution type** (experimental, design research, artifact or system, exploratory qualitative, model or dataset; `references/contribution-types.md`) sets what to specify and show.
- **Learn from close papers** (`related_work.md` or `read-papers`): copy designs, measures, tools, baselines, with the source.
- **IV** and its levels; **DV** and its operational measure (validated scales where they exist).
- **Confounding, control, random variables:** name each. **Individual differences:** ask whether they're a factor or a random variable here.
- **Design:** between, within, or mixed; randomization; counterbalancing; fair baselines. Check internal, construct, external validity.
- **Sample size:** power analysis, or seeds and test size for ML.
- **Statistical analysis:** ask about the design and data first, then choose the test for each hypothesis; no default.
- **Tools and AI models:** versions; pinned model names, key in `.env`, one logged `call_model()` (`references/models.md`). Paid runs over the estimate: ask first. **Labels needed?** Free AI chats do the bulk; humans check a sample at the end (`references/labeling-review.md`).
- **CHI ethics (critical):** approval and consent before recruiting.
Write it into `experimental_design.md` and `implementation.md`.

## 2. Replicate, then pilot
Optional (mostly model or dataset work): first reproduce one key result of the closest paper as your baseline. Pilot with 2-3 people or a small sample: does it run, does the DV move, any confounds? Fix and re-pilot.

## 3. Freeze (critical: ask first)
Hypotheses, success criteria, analysis, stopping rule → commit, `git tag plan-freeze-1`. Later changes are logged deviations; analyses added after results are exploratory.

## 4. Run and reflect
One record per run in `experiment_logs/`; participant data never in git. Every ~5 runs: what worked, what surprised? Suggest deepen, broaden, pivot (`read-papers`), or conclude (`update-paper`). End with the quick sync in `AGENTS.md`.
