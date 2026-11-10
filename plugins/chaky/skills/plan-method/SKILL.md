---
name: plan-method
description: Plans and runs the methodology - what you change (IV), what you measure (DV), conditions, participants or data, randomisation and counterbalancing, sample size, baselines, analysis plan, pilots, freezing the plan, logged runs, and reflection. Use for "plan my method", "what is my IV or DV", "how many participants", "plan my experiments", "run the pilot", or /plan-method [part], e.g. /plan-method IV.
---

# Plan Method

Every decision needs a reason: evidence from past papers or a sound argument. Optional focus: `/plan-method IV`, `DV`, `participants`, `sample size`, `analysis`, `pilot`, `run`. With a focus, do just that part.

## 1. Know the shape
Read `experimental_design.md` and `implementation.md`. Name the **contribution type** (empirical, design, artifact, theoretical; `references/contribution-types.md`): it decides what the method must show. Read the **methods** of the 3-5 closest papers (`find-papers`) and borrow what fits, with a reason.

## 2. Plan the parts (explain each in plain words, with an example from their study)
- **What you change (IV):** conditions and levels; why these; the baseline or control.
- **What you measure (DV):** measures and instruments (validated scales where they exist), when measured.
- **Who or what:** CHI: participants, recruitment, inclusion; ACL/NeurIPS: datasets, splits (train and heldout separate), models (`setup-llms`).
- **Design:** between or within; **randomisation** of assignment; **counterbalancing** of order (e.g. Latin square for several conditions); **blocking** if a factor like expertise matters.
- **Sample size:** a power analysis before recruiting (expected effect from close papers, alpha, power 0.8; G*Power or `pwr`), or seeds and test-set size for ML.
- **Analysis plan:** each hypothesis → its test (statistics notes in `write`), corrections, what counts as success.
- **CHI ethics (critical):** approval or exemption, consent, and data handling recorded in `implementation.md` **before any recruiting**. Never advise skipping it.
Write the plan into `experimental_design.md`, `implementation.md`, and the method section of the paper (rough is fine).

## 3. Pilot first
Small runs (2-3 people, or a small sample): does it run end to end? Does the DV move? Leaks, bugs, confusing instructions? Fix and re-pilot. Code that decides a result gets a tiny test first (`AGENTS.md`).

## 4. Freeze the plan (critical: ask first)
Before the main runs, write final hypotheses, success criteria, analysis plan, and stopping rule into `experimental_design.md`, commit, and tag `git tag plan-freeze-1`. Afterward, a plan change is a logged **deviation** (what, why, who); analyses changed after seeing results are labeled **exploratory**.

## 5. Run and log
- **NLP:** one record per run in `experiment_logs/` (config, outputs, failures, cost, run ID); `results/` links to run IDs.
- **CHI:** participant data goes to `src/data/` (ID, when, where, configuration), never into git if identifiable; sessions logged in `experiment_logs/`.
After each step, say in a line what happened and what's next.

## 6. Reflect (every ~5 runs, or when surprised)
What worked, what didn't, what surprised you, and **why** (check related work before guessing). Suggest a direction and let them choose: **deepen**, **broaden**, **pivot** (`validate-idea`), or **conclude** (then `write`). Log the reflection and dead ends (what, why it failed, lesson) in `log.md`.
