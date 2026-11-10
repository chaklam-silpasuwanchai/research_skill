---
name: setup-repo
description: Sets up a paper project (CHI-style or ACL/NeurIPS-style) - git, folders, the official LaTeX template, the working files Chaky reads, a leak guard, and a first board. Also organizes an existing messy project. Use for "set up my paper", "organize my project", or /setup-repo chi or nlp.
---

# Setup Repo

Optional focus: `chi` or `nlp`. Existing files → **adopt mode** (bottom).

## 1. Ask (one at a time)
1. In one line, what do you want to find out? (Details later with `brain-dump`.)
2. CHI or ACL/NeurIPS style? Which venue and deadline?
3. GitHub or local only?
4. Which language should I explain in? (Paper, code, file names stay English.)
5. Should I suggest each next step, or show your top tasks and wait?

## 2. Build
- `git init`. Folders from `references/components.md` (CHI or NLP tree), nothing extra.
- Copy `assets/` templates into `components/`; fill what you know. Root: `.gitignore` (common + venue extra), `README.md`, `AGENTS.md`, `CLAUDE.md` containing `@AGENTS.md`. Secrets in `.env`.
- Lab defaults filled in `assets/lab-defaults.md` → copy into `AGENTS.md`.
- Fetch this year's official venue template into `paper/`.
- Install the leak guard (`assets/pre-commit.sh` → `.git/hooks/pre-commit`); it blocks secrets, consent forms, recordings, participant data, files over 5 MB.
- GitHub remote and first push: **ask first**.

## 3. Finish
Commit (`init: repo for <venue>`). Seed the board from the `check-board` seed list with priorities; show the top 3. Mention once that Claude Code can build a mod that keeps the board beside the chat ("make me a mod that shows my board from components/tickets.md in a side panel"). Show `references/mindsets.md` once. Log it. Suggest `brain-dump` next.

## Adopt mode
Show a mapping ("`notes.txt` → `components/ideas.md`"). Moving files is critical: **ask first**. Never delete anything.
