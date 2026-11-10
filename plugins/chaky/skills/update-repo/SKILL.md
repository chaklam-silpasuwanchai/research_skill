---
name: update-repo
description: Sets up your paper project if it doesn't exist, or brings an existing one up to date - folders, working files, AGENTS.md, the board, and the paper itself - so everything matches your latest work. Use for "set up my paper", "update my repo", "sync everything", "is my paper up to date", "organize my project", or /update-repo chi or nlp.
---

# Update Repo

Focus: `chi`/`nlp` (new), or `paper`, `files`, `agents`. No `AGENTS.md` or `components/` → **Set up**; loose files only → **Adopt**; otherwise → **Update**.

## Set up (new project)
1. Ask one at a time: what you want to find out (one line), CHI or ACL/NeurIPS, venue and deadline, GitHub or local, explanation language, and whether I suggest each step or wait.
2. `git init`. Folders from `references/components.md`, nothing extra. Copy `assets/` templates into `components/` and fill what you know. Root: `.gitignore`, `README.md`, `AGENTS.md`, `CLAUDE.md` containing `@AGENTS.md`. Secrets in `.env`. Lab defaults from `assets/lab-defaults.md` if filled.
3. Fetch this year's official venue template into `paper/`. Install the leak guard (`assets/pre-commit.sh` → `.git/hooks/pre-commit`).
4. Commit. Seed the board (`check-board` seed list), show the top 3, mention once that Claude Code can build a mod to keep it beside the chat, show `references/mindsets.md` once, suggest `brain-dump`.

## Update (existing project)
1. **Structure:** add any missing folder, working file, or root file from the templates. Never overwrite their content.
2. **AGENTS.md:** refresh from `assets/AGENTS.template.md`, keeping their venue, mode, language, lab defaults, and *My preferences*.
3. **Working files:** read `log.md`, `review.md`, `experiment_logs/`, and `results/` since the last update; bring `current_status.md`, `experimental_design.md`, `implementation.md`, `related_work.md`, `terms.md`, and the board in line (`check-board` rules).
4. **The paper:** update every section the new facts touch: question, method, numbers, results, citations. Can't update a part yet → mark it `⚠ stale: <why>`. Never invent results (`[TODO]`).
5. **Venue:** flag a newer template or changed page limit.
6. Commit and show what changed:
```
Updated: AGENTS.md (new rules) · method section (now 3 conditions) · results table (pilot 2)
Stale: discussion (waits for main study)
Say "undo" to reverse any line.
```
Log it in `log.md`.

## Critical (ask first)
Moving or renaming their files, replacing the venue template, the first GitHub push. Never delete anything.

## Adopt
Show a mapping ("`notes.txt` → `components/ideas.md`"), ask, then move and fill the working files.
