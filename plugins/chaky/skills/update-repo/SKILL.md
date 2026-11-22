---
name: update-repo
description: Sets up your paper project, or brings the paper (the source of truth) and the internal notes for the AI in line with your latest work and cleans up clutter. Use for "set up my paper", "update my repo", "clean up my repo", "remove clutter", or /update-repo chi or nlp.
---

# Update Repo

Focus: `chi`/`nlp` (new), or `docs`, `agents`, `cleanup`. No `AGENTS.md` or `components/` → **Set up**; loose files only → **Adopt**; otherwise → **Update**.

## Set up (new project)
1. Ask one at a time: the question (one line), CHI or ACL/NeurIPS, venue and deadline, GitHub or local, explanation language, suggest-or-wait.
2. `git init`. Folders from `references/components.md`, nothing extra. Copy `assets/` templates into `components/`. Root: `.gitignore`, `README.md`, `AGENTS.md`, `CLAUDE.md` containing `@AGENTS.md`. Secrets in `.env`. Lab defaults (`assets/lab-defaults.md`) into `AGENTS.md`; lab terms: Core of `assets/lab-terms.md` into `terms.md`, full file to `components/`.
3. Fetch this year's official venue template into `paper/`. Install the leak guard (`assets/pre-commit.sh` → `.git/hooks/pre-commit`).
4. Commit. Seed the board (`update-board` seed list), show the top 3, mention once that a Claude Code mod can keep it beside the chat, show `references/mindsets.md`, suggest `brain-dump`.

## Update (existing project)
**Always the whole repo,** not just what changed since the last update: every folder, working file, log, result, and paper section.
1. **Structure:** add any missing folder, working file, or root file from the templates. Never overwrite their content.
2. **AGENTS.md and lab terms:** refresh `AGENTS.md` (keep venue, mode, language, lab defaults) and both lab-terms copies. **Never touch `preferences.md`**; move any old *My preferences* lines from `AGENTS.md` into it.
3. **Working files:** read all of `log.md`, `review.md`, `experiment_logs/`, and `results/`; bring `current_status.md`, `experimental_design.md`, `implementation.md`, `related_work.md`, `terms.md`, and the board in line (`update-board` rules).
4. **Cleanup** (`references/cleanup.md`): **safe junk** (caches, LaTeX build files, `.DS_Store`, empty folders) → clean it and tell; **their work** (stray files, `_v2`/`final` copies, unused or big files) → suggest and ask first; tidy duplicate rows in the working files.
5. **Paper (source of truth):** rewrite every section behind the new work (`update-paper` rules, their voice). `⚠ stale: <why>` only what can't be rewritten yet.
6. **Venue:** flag a newer template.
7. Commit and show what changed:
```
Updated: AGENTS.md · current_status · related_work · board
Cleaned: 14 LaTeX build files · 3 caches · 2 empty folders
Asks: method_v2.tex → keep the newest?
Paper: rewrote method, results · ⚠ discussion waits on pilot 2
Say "undo" to reverse any line.
```
Log it as `full update`.

## Critical (ask first)
Moving, renaming, or deleting their files; replacing the venue template; the first GitHub push.

## Adopt
Show a mapping, ask, then move.
