# Changelog

**Versions:** `0.MINOR.PATCH` until the skills have been tested with real students, then `1.0.0`. MINOR = a new skill or changed behavior; PATCH = wording or bug fixes; after 1.0, renaming or removing a skill or changing the repo structure is MAJOR. Bump the version in `plugins/chaky/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, and add an entry here.

**Names:** every skill is a two-word, hyphenated verb-noun (`make-figures`), or a single verb (`clarify`). `guide-me` is the front door.

## 0.1.0 (first release, not yet published)
Bump to 0.2.0 only after students have installed 0.1.0.
- **Front door:** `guide-me` (renamed from `ask-chaky`; "ask Chaky" still works). Humans lead: it suggests a skill for the next step and the researcher chooses; no skill starts on its own. Also progress, advisor update, retro, session log.
- **Board:** `plan-tickets` (tickets with type, 1-5 priority, done-when; assist or lead mode; fog and frontier; seeded at onboarding).
- **Core:** `start-paper`, `shape-idea`, `run-study` (pilots, plan freeze, reflection), `write-paper`, `review-paper` (deterministic checklist; checkpoint, full, or submission mode).
- **Supporting:** `grill-me`, `find-papers` (search, watch, triage), `polish-prose` (with unslop), `analyze-results` (statistics and figures), `write-code` (tested, mutation testing), `use-llms` (model access, free-chat labeling, outside review).
- **Meta:** `teach-chaky` (learn repeated preferences, add supporting skills).
- **Repo:** CI validation (`scripts/validate.py`), scenario tests, trigger phrases, student walkthroughs (`tests/`), a filled-in example project, docs, issue forms, MIT license, `CITATION.cff`.
- **Student safety and fit:** lab defaults file, optional pre-commit leak guard, explanation-language setting, CHI ethics tracker.
- 17 skills (14 merged from an earlier 20, plus `clarify`, `think-deeply`, `tidy-board`).
- **Voice:** Chaky talks in everyday words and uses the researcher's own terms (`terms.md` and the chat) in conversation, not just in the paper. Internal words (ticket, done-when, fog, IV/DV, modes) stay in the files. `guide-me` offers to update the voice rules in older projects.
- **New skills:** `clarify` (rewrite a hard-to-read AI answer in plain words), `think-deeply` (is there a better solution? first principles, assumptions, depth, systems thinking), `tidy-board` (re-prioritize, drop or merge, rename tickets; propose first).
- **Auto-priority:** Chaky assigns every ticket's 1-5 priority itself (fixed rules, one-line reason) in both modes; the researcher changes any number whenever they like.
- **Auto-close:** a ticket whose done-when is fully met is closed automatically with a one-line note and an easy "reopen <ticket>"; human tickets close only once the researcher's own decision or result is recorded.
- **Board side panel:** `plan-tickets` and `start-paper` offer once to have Claude Code build a mod that shows `tickets.md` beside the chat (editor side panel as the fallback).
