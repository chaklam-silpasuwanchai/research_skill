---
name: plan-method
description: Plans and runs a study that is novel, valid, justified, and reproducible, learning from how 5-15 close papers did it. Use for "plan my method", "what is my IV or DV", "how many participants", "help me label data", or /plan-method [part].
---

# Plan Method

**Idea testing**, in lab terms. Focus: `IV`, `DV`, `design`, `sample size`, `analysis`, `models`, `labeling`, `pilot`, `run`.

## 1. Read how others did it
Read the **method sections** of the 5-15 closest papers (`related_work.md`; too few → `update-paper`). One row each in `experimental_design.md`:
`paper · design · IV and levels · DV and measure · participants or data, n · task · analysis · baseline`
Name the common pattern.

## 2. Plan
- **Contribution type** (`references/contribution-types.md`) sets what to specify and show.
- **IV** and levels; **DV** and operational measure (validated scales where they exist).
- **Confounding, control, random variables:** name each. **Individual differences:** factor or random? Ask.
- **Design:** between, within, or mixed; randomization; counterbalancing; several strong baselines and ablations.
- **Sample size:** power analysis, or seeds and test size for ML. **Analysis:** ask about design and data first; no default.
- **Tools, AI models, labeling:** `references/models.md`, `references/labeling-review.md`; paid runs over the estimate: ask first.
- **CHI ethics (critical):** approval and consent before recruiting.
Every major decision goes in a **decision table** in `experimental_design.md`: `decision · choice · why · source (paper or reason)`.

## 3. The five musts (check before the pilot and before freezing)
- **Novelty:** the method tests our one difference (idea and technical novelty hold).
- **Validity and rigor:** internal (no confounds), construct (measures fit), external; many comparisons and analyses, all fair (`references/rigor.md`).
- **Papers and justification:** each choice matches common practice or says why not; every decision-table row has a why and a source.
- **Reproducible:** another lab could rerun it (versions, seeds, configs, prompts, materials, procedure, one command).
Any ❌ → fix its root cause first.

## 4. Replicate, then pilot
Optional: reproduce the closest paper's key result as the baseline. Pilot with 2-3 people or a small sample: does it run, does the DV move? Something off → find the cause.

## 5. Freeze (critical: ask first)
Five musts ✅; hypotheses, analysis, stopping rule → commit, `git tag plan-freeze-1`. Later changes are logged deviations.

## 6. Run and reflect
One record per run in `experiment_logs/`; participant data never in git. Every ~5 runs reflect; suggest deepen, pivot, or conclude (`update-paper`). Quick sync (`AGENTS.md`).
