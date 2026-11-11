---
name: update-repo
description: Sets up your paper project if it doesn't exist, or updates all the docs in an existing one (working files, AGENTS.md, README, the board) to match your latest work, and cleans up clutter. Use for "set up my paper", "update my repo", "sync everything", "clean up my repo", "organize my project", or /update-repo chi or nlp.
---

# Update Repo

Focus: `chi`/`nlp` (new), or `docs`, `agents`, `cleanup`. No `AGENTS.md` or `components/` → **Set up**; loose files only → **Adopt**; otherwise → **Update**.

## Set up (new project)
1. Ask one at a time: what you want to find out (one line), CHI or ACL/NeurIPS, venue and deadline, GitHub or local, explanation language, and whether I suggest each step or wait.
2. `git init`. Folders from `references/components.md`, nothing extra. Copy `assets/` templates into `components/` and fill what you know. Root: `.gitignore`, `README.md`, `AGENTS.md`, `CLAUDE.md` containing `@AGENTS.md`. Secrets in `.env`. Lab defaults from `assets/lab-defaults.md` if filled.
3. Fetch this year's official venue template into `paper/`. Install the leak guard (`assets/pre-commit.sh` → `.git/hooks/pre-commit`).
4. Commit. Seed the board (`update-board` seed list), show the top 3, mention once that a Claude Code mod can keep it beside the chat, show `references/mindsets.md`, suggest `brain-dump`.

## Update (existing project)
1. **Structure:** add any missing folder, working file, or root file from the templates. Never overwrite their content.
2. **AGENTS.md:** refresh from `assets/AGENTS.template.md`, keeping their venue, mode, language, lab defaults, and *My preferences*.
3. **Working files:** read `log.md`, `review.md`, `experiment_logs/`, and `results/` since the last update; bring `current_status.md`, `experimental_design.md`, `implementation.md`, `related_work.md`, `terms.md`, and the board in line (`update-board` rules).
4. **Cleanup:** stray files in the root, `_v2` or `final_final` copies, empty folders, caches, big files that belong outside git. List them with a suggested home or removal; moving or deleting is critical (ask first).
5. **Paper:** mark sections behind the new work `⚠ stale: <why>` and suggest `/update-paper <section>`.
6. **Venue:** flag a newer template or page limit.
7. Commit and show what changed:
```
Updated: AGENTS.md · current_status · related_work · board
Cleaned: 3 stray notebooks → src/scripts/ (you approved)
Stale: method, results → /update-paper method
Say "undo" to reverse any line.
```
Log it as `full update`.

## Critical (ask first)
Moving, renaming, or deleting their files; replacing the venue template; the first GitHub push.

## Adopt
Show a mapping ("`notes.txt` → `components/ideas.md`"), ask, then move and fill the working files.
