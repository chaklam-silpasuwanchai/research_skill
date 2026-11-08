> **This is a fictional example** showing what a project looks like a few rounds in. Papers, numbers, and names are illustrative placeholders, not real results. Do not cite anything here.

# Honest Sales Agent (EXAMPLE PROJECT)

Target venue: CHI (CHI style)

## What this repo is
The working repo for one research paper: notes, code, data, results, and the manuscript.

## Folders
```
paper/  components/
src/
  prompts/          LLM prompts used in the study
  scripts/          study, analysis, tests
  data/             participant data: ID, when, where, configuration
  experiment_logs/  which session, which participant
  results/          statistics and figures linked to session IDs
```

## How to work in this repo
Use Claude Code (or Codex) in this folder, on a paid plan. Not sure what to do next? Say **"ask Chaky"** and it will read your repo and tell you. Or say which stage you are in, for example:
- "Let's start generating ideas" -> `shape-idea`
- "Let's plan and run the study" -> `run-study`
- "Let's write the paper" -> `write-paper`
- "Review my paper like a tough reviewer" -> `review-paper`
- "Are we ready to submit?" -> `check-submission`

The order is flexible. Things you can say at any time: **"I found a new paper"**, **"I want to try X"**, **"quick review"**, **"progress update"**, **"fast mode"** (draft the whole paper in one pass), **"I'm lost"**. Chaky keeps the paper and reviews up to date as you go; the paper is never "done after". You can jump between skills, loop back, or skip ahead. The AI reads `components/current_status.md` to see where you are.

Supporting skills are called by the core skills: `find-papers`, `polish-prose`, `analyze-data`.

## Rules
- Secrets go in `.env` (ignored by git). Never commit participant-identifying data.
- One preferred term per concept: see `components/terms.md`.
- No extra folders and no `_v2` files. Git keeps the history.
