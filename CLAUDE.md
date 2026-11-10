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
