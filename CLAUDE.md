# Working on the Chaky repo

This repo is the Chaky plugin itself (skills in `plugins/chaky/skills/`), not a student paper project.

## Every change
1. **Bump the version** in `plugins/chaky/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `CITATION.cff`, and the README title. PATCH for wording or fixes, MINOR for a new skill or changed behavior.
2. Add a `CHANGELOG.md` entry under the new version.
3. Run `python scripts/validate.py` (needs `pyyaml`); it must pass.
4. Commit, push, open a pull request, and merge it.

## Skill rules
- Keep each `SKILL.md` under 400 words; put detail in its `references/`.
- The human leads: skills suggest other skills, never start them; ask first only for critical steps.
- Plain words; the student's own terms.
- A new or renamed skill also goes in the README table, `guide-me/references/skills.md`, the `AGENTS.md` template (supporting skills), `tests/trigger-phrases.md`, and the issue form.

## One rule, one home
Each rule lives in exactly one file; everything else points to it. Add a new rule to its home and update this map; never copy it.

| Rule | Home |
|---|---|
| Principles (they lead, don't just agree, tickets, learn from papers, root cause, novelty and rigor, honest and reproducible, write so no one asks, remember, tidy) | `update-repo/assets/AGENTS.template.md` (one line each, under 600 words) |
| Finding and reading papers, recency, top venues, the one difference | `update-paper/references/papers.md` |
| Writing: plain English, coherence, consistent terms, don't invite questions, elements of style | `update-paper/references/writing.md` |
| What goes in each section | `update-paper/references/sections.md` |
| Framing and novelty claims | `update-paper/references/framing.md` |
| Tables and figures | `update-paper/references/figures.md` |
| Rigor, validity, fairness | `plan-method/references/rigor.md` |
| Citation checking | `review/references/citations.md` |
| Root cause in depth, 360° look | `think-deeply/SKILL.md` |
| Lab vocabulary | `update-repo/assets/lab-terms.md` |
| Cleanup | `update-repo/references/cleanup.md` |

Size budgets (the validator enforces them): `AGENTS.md` template under 600 words, each `SKILL.md` under 400 (500 hard), each reference under 900.
