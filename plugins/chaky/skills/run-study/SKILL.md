---
name: run-study
description: Plans and runs the study or system for an academic paper - contribution type, methodology, pilots, a frozen plan, logged runs, reflection. Use to plan experiments or user studies, build a prototype, run pilots, or collect data.
---

# Run Study

Every decision needs a rationale: past-paper evidence or a sound argument.
**Needs:** RQs, hypotheses, IVs, DVs in `experimental_design.md`. If missing, offer the catch-up from `shape-idea` first.
**Calls:** `find-papers`, `analyze-results`, `polish-prose`, `use-llms`, `write-code`, `grill-me`, and any other supporting skill listed in `AGENTS.md` that matches the task (for example a DSPy skill).

## Entry
Follow `AGENTS.md` (none → offer `start-paper`, adopt mode if the user has files). If a need above is missing, don't block: offer to run the earlier skill, do a quick catch-up, or continue and log an assumption. Finish with the end-of-task routine in `AGENTS.md`.

## 1. Contribution type
Name it (empirical, design, artifact, or theoretical) in `experimental_design.md` and `current_status.md`; it decides what the implementation must show. See `references/contribution-types.md`.

## 2. Learn how others do it
Read the **methods** of the closest papers. Note their tools, frameworks, theories, approaches, analyses, and why. Borrow what fits, with rationale.

## 3. Plan
Write the plan in `implementation.md` and the matching method/experiment sections of the paper.
- **CHI:** **ethics first**: record approval or exemption, consent, and data handling in `implementation.md` before any recruiting (Chaky never advises skipping it). Then participants (who, how many, recruited how), apparatus or prototype, IVs, DVs and instruments, task and procedure, analysis methods.
- **ACL/NeurIPS:** steps, scripts, tests, prompts, models, datasets and splits (train/heldout separate), setup (e.g. OpenRouter; keys in `.env`; how Claude Code or Codex runs it all). `src/tests/` checks code, scoring, and data integrity, including train/heldout leakage.
- **Models and keys (NLP):** use `use-llms` to check what the user actually has (OpenRouter or other API key, local LLM) and plan pilot vs main vs final models.
- **Labeling:** human labeling isn't needed now. Use `use-llms` (free chats in batches, 2-3 AIs, merge, check agreement); only at the very end hire two humans for disagreements and a sample.

Run `grill-me` (plan tree) before freezing. Ask: "Is the plan ok? Does the method text match?" Encourage small steps, not perfection.

## 4. Pilot first
"Now we implement. Do **pilot studies**: small steps, adjust as we learn, go big only when quite sure; the goal is the data to write the paper." Pilots check: runs end to end? does the DV move? leaks, bugs, confusing instructions?

## 5. Freeze the plan
Before the main runs (after pilots), write the final hypotheses, success criteria, analysis plan, and stopping rule into `experimental_design.md`. Commit and tag: `git tag plan-freeze-1`. Log it. Afterward, any change to the plan is a logged **deviation** (what changed, why, who decided); analyses changed after seeing results are labeled **exploratory** in the paper. Pilot-informed changes made before the tag are normal.

## 6. Run, pause, report
Follow the plan step by step. After each step, **pause**, explain in plain English, ask if they want to change the plan, and update the repo.
- **NLP:** one record per run in `experiment_logs/` (config, outputs, failures, cost, run ID); `results/` links to run IDs; keep every result.
- **CHI:** ask the user to upload spreadsheets and participant data to `src/data/` (ID, when, where, configuration); log sessions in `experiment_logs/`; keep identifiable data out of git.

## 7. Reflect (every ~5 runs, at each milestone, or when stuck or surprised)
1. Cluster the results: what worked, what didn't, what surprised you?
2. Ask **why**: what mechanism explains the pattern? If surprised, check related work before guessing.
3. Recommend a direction and let the user decide: **deepen** (a supported result raises follow-ups), **broaden** (solid results, adjacent questions untested), **pivot** (a core assumption failed, or something more interesting appeared), or **conclude** (a claim is strongly supported, you can explain why, obvious alternatives are addressed, and the abstract could be written from the log; then move to `write-paper`).
4. Log it in `log.md` (reflection, direction chosen, who decided). Log dead ends with hypothesis, why it failed, and the lesson.

## Loop-backs here
No effect or trivial explanation → `shape-idea` or step 3. Someone already ran this → `shape-idea`. Reviewer finds confound, unfair baseline, or leakage → step 3. Method text reveals a missing detail → step 3.
