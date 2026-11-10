---
name: setup-repo
description: Sets up a paper project (CHI-style or ACL/NeurIPS-style) - git repo, folders, the official LaTeX template, the working files Chaky reads, lab defaults, a leak guard, and a first board. Also tidies an existing messy project into this layout. Use to start a paper, "set up my repo", "organize my project", or /setup-repo chi or nlp.
---

# Setup Repo

Builds the project every other skill reads. Built for Claude Code (or Codex) on a paid plan. Optional focus: `/setup-repo chi` or `/setup-repo nlp`. Existing files → **adopt mode** (bottom).

## 1. A few quick questions (one at a time; rough answers fine)
1. In one line: what do you want to make or find out? (More detail later with `brain-dump`.)
2. CHI-style or ACL/NeurIPS-style (skip if given as focus)? Which conference or journal, and the deadline?
3. GitHub or local only?
4. Which language should Chaky explain in? (default English; paper, code, citations, file names stay English)
5. Do you want Chaky to suggest each next step (**I lead**), or show your top tasks and wait (**you lead**)? Default: suggest. Switch any time ("you drive" / "let me lead").

Show the mindsets in `references/mindsets.md` once as a short checklist; record "seen" in `current_status.md`.

## 2. Folders (only these; extras only if asked)
**ACL/NeurIPS**
```
paper/              manuscript, references, figures, official template
components/         working notes (step 3)
src/
  prompts/          prompts used
  scripts/          experiments, analysis, tests
  data/             train/ and heldout/ clearly separate
  tests/            code, scoring, data-integrity checks
  experiment_logs/  one record per run: config, outputs, failures, cost
  results/          analysis and figures linked to run IDs
```
**CHI**
```
paper/  components/
src/
  scripts/          study, analysis, tests
  data/             participant data: ID, when, where, configuration
  experiment_logs/  which session, which participant
  results/          statistics and figures linked to session IDs
```
CHI gets `src/prompts/` only if the study uses AI prompts (ask once).

Root files: `.gitignore` (`assets/` common + venue extra), `README.md`, `AGENTS.md`, `CLAUDE.md` containing `@AGENTS.md`. Secrets live in `.env` (ignored). Run `git init`.
- **Lab defaults:** if `assets/lab-defaults.md` is filled, copy it into `AGENTS.md` under *Lab defaults* and follow it.
- **Template:** fetch this year's official venue template into `paper/` from the official source. No network → say which to fetch.
- **Leak guard:** install it (`cp <this skill>/assets/pre-commit.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit`) and say so; it blocks secrets, consent forms, recordings, participant data, and files over 5 MB.
- **GitHub:** create the remote only after they confirm; the first push is a critical step (ask).

## 3. Working files
Copy the templates from `assets/` into `components/` (CHI or NLP variant) and fill what you already know: `tickets`, `terms`, `experimental_design`, `implementation`, `ideas`, `related_work`, `current_status`, `voice`, `log` (what each holds: `references/components.md`). `AGENTS.md` holds the working agreements and voice rules.

## 4. Finish
1. Show the tree in a few lines, commit (`init: repo structure for <venue>`), set the stage map.
2. Seed the board from `check-board`'s seed list (about 7 tickets with priorities) and show the top 3. Mention once: Claude Code can build a small *mod* that keeps the board beside the chat ("make me a mod that shows my board from components/tickets.md in a side panel"), or open `components/tickets.md` in an editor.
3. Log the setup in `log.md`. Suggest next: `brain-dump` (tell me everything in your head), `setup-writing-style` (if they have past papers), or `setup-llms` (NLP).

## Adopt mode
Inventory the folder, move or copy files into the layout ("`notes.txt` → `components/ideas.md`, `exp/` → `src/scripts/`"), and fill the working files from what exists. **Moving or renaming their files is critical**: show the mapping and ask first. Never delete anything.
