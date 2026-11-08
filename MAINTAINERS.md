# Maintainers

## Publish (once)
1. Replace `Chaklam Silpasuwanchai` and `chaklam-silpasuwanchai` in `README.md`, `WELCOME.md`, `plugins/chaky/.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json`.
2. Make the GitHub repo **public** (it is `chaklam-silpasuwanchai/research_skill`; the marketplace inside is named `ask-chaky`, so install commands use `@ask-chaky`). If you rename the repo, update `README.md`, `WELCOME.md`, `CITATION.cff`, and both JSON files.
3. On a clean machine, follow the README exactly. Fix anything that confuses you first.
4. Run one real paper through `ask-chaky` (start, idea, a pilot, a review).

## Release
- Versions: `0.MINOR.PATCH` until tested with real students, then `1.0.0`. MINOR = new skill or changed behavior. PATCH = wording or bug fixes.
- Bump in `plugin.json` and `marketplace.json`, add a `CHANGELOG.md` entry, push. Students run `/plugin marketplace update ask-chaky`.

## Add or improve skills
- Students can say "add a skill" or "always do X" to Chaky (`teach-chaky`). Choosing "improve Chaky for everyone" produces a short note for you.
- New skills: two-word verb-noun name, lean `SKILL.md`, register under *Supporting skills* in `start-paper/assets/AGENTS.template.md`, update the README table and changelog.
- Plugin skills are overwritten on update. Per-student preferences live in each project's `AGENTS.md`, not in the skills.

## Customize for your lab (once)
Edit `plugins/chaky/skills/start-paper/assets/lab-defaults.md` (preferred venues, meeting rhythm, sign-off, data and AI-use policy). `start-paper` copies it into each student's `AGENTS.md`.

## Checks
- `python scripts/validate.py` (needs `pip install pyyaml`): headers, names, README and AGENTS lists, versions, stale names. GitHub Actions runs it on every push.
- `python tests/check_project.py <project> --type chi|nlp`: checks a student project folder.
- `tests/scenarios.md`: 15 scripted dry runs to do by hand before each release. `tests/trigger-phrases.md`: which phrase should reach which skill.

## Test checklist before each release
- [ ] `scripts/validate.py` passes
- [ ] All 15 scenarios in `tests/scenarios.md` pass
- [ ] Install works on macOS and Windows
- [ ] "ask Chaky" in an empty folder creates the CHI and ACL/NeurIPS layouts correctly
- [ ] A quick `review-paper` run gives the same results twice on the same draft
- [ ] No secrets or participant data end up in git
