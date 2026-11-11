# {{PROJECT TITLE}}

Target venue: {{VENUE}} ({{CHI | ACL/NeurIPS}} style)

## What this repo is
The working repo for one research paper: notes, code, data, results, and the manuscript.

## Folders
{{paste the tree for this paper type}}

## How to work in this repo
Use Claude Code (or Codex) in this folder, on a paid plan. Not sure what to do next? Say **"guide me"** and it will read your repo and tell you. You lead; Chaky suggests. Or name a skill, with an optional focus:
- "Get my ideas out" -> `/brain-dump`
- "Read the closest papers: what to copy, how we differ" -> `/read-papers`
- "Plan the method" -> `/plan-method`
- "Write the abstract" -> `/update-paper abstract`
- "Review my paper like a tough reviewer" -> `/review`
- "Recap and fix the board" -> `/update-board`

The order is flexible. Things you can say at any time: **"I found a new paper"**, **"think deeply"**, **"clarify"**, **"teach me"**, **"undo"**, **"progress update"**, **"fast mode"** (draft the whole paper in one pass). Chaky keeps the paper and reviews up to date as you go. The AI reads `components/current_status.md` to see where you are.

## Rules
- Secrets go in `.env` (ignored by git). Never commit participant-identifying data.
- One preferred term per concept: see `components/terms.md`.
- No extra folders and no `_v2` files. Git keeps the history.
