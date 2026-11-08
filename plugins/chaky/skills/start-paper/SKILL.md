---
name: start-paper
description: Sets up a new academic paper project (CHI-style or ACL/NeurIPS-style) - interview, agreed terms, git repo, official LaTeX template, folders, board, and your writing voice. Use to start a paper, set up a research repo, or organize a messy project.
---

# Start Paper

Sets up the repo every other skill reads. Built for Claude Code (or Codex) on a paid plan (Pro/Plus or above).
**Needs:** nothing. Existing project → adopt mode.

## 0. Mindsets
Show `references/mindsets.md` as a checklist; ask for an "ok" (or which to discuss). Record in `current_status.md`. If skipped, remind once and move on.

## 1. Interview (one question at a time, rough answers welcome)
**Needs first:** what do you want to make or find out (one line)? Who is it for, and what is the deadline? What exists already? Then **clarify the domain terms**: pick the 3-5 words your idea depends on and agree on one meaning and one example each (these go in `terms.md`). Then:
1. CHI-style or ACL/NeurIPS-style? 2. Which conference or journal? 3. GitHub or local only? 4. **Which language should Chaky explain in?** (default English; the paper, code, citations, and file names stay English unless they say otherwise) 5. **Which mode do you prefer?** `assist` (Chaky recommends the next step and proposes ratings; good for beginners) or `lead` (you steer; Chaky answers and shows the board). Default assist; switch any time. 6. **Do you have past papers of your own?** (file paths or links; they stay outside the repo, and only short style notes are saved). If none, a few of your own paragraphs will do, or skip and learn the voice from drafts later. Run `git init` either way. For GitHub use `gh` or give the one remote command; ask before the first push.

## 2. Create only these folders
Extras only if the user asks.

**ACL/NeurIPS**
```
paper/              manuscript, references, figures, official template
components/         working notes (step 3)
src/
  prompts/          prompts used
  scripts/          experiments, analysis, tests (subfolders if it grows)
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

**Lab defaults:** read `assets/lab-defaults.md`. If filled, copy it into `AGENTS.md` under *Lab defaults*, offer its preferred venues in question 2, and follow its meeting, data, and AI-use rules.

**Guard hook:** offer to install the leak guard (ask first): `cp <this skill>/assets/pre-commit.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit`. It blocks secrets, consent forms, recordings, participant data, and files over 5 MB; `git commit --no-verify` overrides it, rarely.

Root files: `.gitignore` (`assets/` common + venue extra), `README.md`, `AGENTS.md`, `CLAUDE.md` containing `@AGENTS.md`. Secrets live in `.env` (ignored). Keep protected data and large files out of git.

**Template:** search for this year's official template of the venue and download it into `paper/` from the official source. No network → tell the user which to fetch.

## 3. Component files
Copy the templates from `assets/` into `components/` (CHI or NLP variant) and fill what you already know. What each file holds: `references/components.md`. They are: `tickets`, `terms`, `experimental_design`, `implementation`, `ideas`, `related_work`, `current_status`, `voice`, `log`. `AGENTS.md` (repo root, where tools look) holds the working agreements and the voice rules; `README.md` explains the skills and that the order is flexible.

## 4. Finish
1. Learn the voice from past papers, if given.
2. Show the tree, commit (`init: repo structure for <venue>`), and set the stage map (existing work counts as 🟡/✅).
3. Seed the board with `plan-tickets` (about 7 tickets), ask the researcher to rate each 1-5, and **show it**. Then offer the board side panel once (see `plan-tickets`): a mod they ask Claude Code to build, or `components/tickets.md` open in an editor.
4. Add a first `log.md` entry (venue, paper type, mode). Point to the top ticket (usually `refine-idea`) and mention "ask Chaky".

## Adopt mode
Inventory first, show a mapping ("`notes.txt` → `ideas.md`, `exp/` → `src/scripts/`"), get approval, then move or copy and fill the components from existing material. Don't impose the structure.
