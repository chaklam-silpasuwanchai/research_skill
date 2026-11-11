---
name: plan-method
description: Plans and runs your study by first reading how 5-15 close papers did it - IV, DV, confounding, control, and random variables, design, sample size, analysis, tools, AI models, labeling, pilots, and runs, in the lab's terms. Use for "plan my method", "what is my IV or DV", "how many participants", "run the pilot", "help me label data", or /plan-method [part].
---

# Plan Method

**Idea testing.** Lab terms (`terms.md`, `lab-terms.md`), glossed the first time. Focus: `IV`, `DV`, `variables`, `design`, `sample size`, `analysis`, `models`, `labeling`, `pilot`, `run`, `replicate`.

## 1. Read how others did it
Read the **method sections** of the 5-15 closest papers (`related_work.md`; too few → `read-papers`; verified only). One row each in `experimental_design.md`:
`paper · design · IV and levels · DV and measure · participants or data, n · task · analysis · baseline`
Name the common pattern ("most use within-subjects, n≈24, a validated trust scale").

## 2. Plan
Each decision cites a paper ("as Lee 2023") or says why we differ, with an example from their study.
- **Contribution type** (`references/contribution-types.md`) sets what to specify and show.
- **IV** and levels; **DV** and operational measure (validated scales where they exist).
- **Confounding, control, random variables:** name each. **Individual differences:** ask, factor or random?
- **Design:** between, within, or mixed; randomization; counterbalancing; fair baselines; internal, construct, external validity.
- **Sample size:** power analysis, or seeds and test size for ML.
- **Statistical analysis:** ask about design and data first; no default.
- **Tools and AI models:** versions; pinned models, key in `.env`, one logged `call_model()` (`references/models.md`); paid runs over the estimate: ask first. **Labels?** Free AI chats, humans check a sample at the end (`references/labeling-review.md`).
- **CHI ethics (critical):** approval and consent before recruiting.
Write it into `experimental_design.md` and `implementation.md`.

## 3. Replicate, then pilot
Optional (mostly model work): reproduce one key result of the closest paper as the baseline. Pilot with 2-3 people or a small sample: does it run, does the DV move, any confounds?

## 4. Freeze (critical: ask first)
Hypotheses, success criteria, analysis, stopping rule → commit, `git tag plan-freeze-1`. Later changes are logged deviations; post-hoc analyses are exploratory.

## 5. Run and reflect
One record per run in `experiment_logs/`; participant data never in git. Every ~5 runs: what worked, what surprised? Suggest deepen, broaden, pivot (`read-papers`), or conclude (`update-paper`). End with the quick sync in `AGENTS.md`.
