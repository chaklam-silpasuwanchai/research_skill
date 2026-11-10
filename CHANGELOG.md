# Changelog

**Every update bumps the version** (MINOR = a new skill or changed behavior; PATCH = wording or bug fixes; after 1.0, renaming or removing a skill is MAJOR). Change it in `plugins/chaky/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `CITATION.cff`, and the README title, and add an entry here. `scripts/validate.py` checks they match; CI fails a pull request that doesn't bump it.

**Names:** a lowercase verb, optionally with one or two hyphenated words (`write`, `check-board`, `setup-writing-style`). `guide-me` is the front door.

## 0.2.0

**Idea:** the human leads. Chaky suggests which skill could help; the researcher chooses. Inside a task, Chaky makes the change and says so ("say *undo*"); it asks first only for critical steps (deleting or moving files, changing code or data behind a reported result, freezing the plan, pushing, free-chat data, spending money, participants and ethics, submitting).

**15 skills.** Every skill takes an optional focus (`/write abstract`, `/plan-method IV`, `/validate-idea <idea>`).
- **Front door:** `guide-me` (renamed from `ask-chaky`; "ask Chaky" still works): what needs attention, suggests a skill, progress, advisor update, retro, session log.
- **Setup:** `setup-repo` (folders, git, template, working files, lab defaults, leak guard, first board, adopt mode), `setup-writing-style` (voice from past papers), `setup-llms` (OpenRouter, local LLM, free AI chats for labeling and outside review).
- **Research:** `brain-dump` (interview one question at a time, any phase), `check-board` (recap, missing or unneeded tickets, priorities Chaky assigns, plain names, auto-close), `validate-idea` (novel, valid, significant, fit, feasible), `find-papers` (closest work, novelty double-check, methods to borrow; watch; triage), `plan-method` (IV, DV, design, randomisation and counterbalancing, sample size, analysis plan, pilots, plan freeze, runs, reflection).
- **Writing:** `write` (section by section in your voice; statistics, figures, unslop), `review` (rigorous venue reviewer: novelty, validity, significance, writing, every citation checked; checklist back; quick, full, citations, submission).
- **Any time:** `think-deeply` (360° views, first principles, assumptions, depth, systems: is there a better solution?), `clarify` (plain words, an example, what needs you), `teach-me` (step by step when `clarify` isn't enough), `remember-this` (make a repeated instruction permanent; add a skill).
- **Merged or removed** since 0.1.0: `start-paper` → `setup-repo` + `setup-writing-style` + `brain-dump`; `grill-me` → `brain-dump`; `plan-tickets` and `tidy-board` → `check-board`; `shape-idea` → `validate-idea`; `run-study` → `plan-method`; `write-paper`, `polish-prose`, `analyze-results` → `write`; `review-paper` → `review`; `use-llms` → `setup-llms`; `teach-chaky` → `remember-this`; `write-code` → rules in `AGENTS.md` (test result-deciding code, reproducible runs, ask before changing the researcher's code).

**Behavior**
- **Voice:** everyday words and the researcher's own terms (`terms.md` and the chat); internal words (ticket, done-when, fog, IV/DV, modes) stay in the files. `guide-me` offers to update older projects' `AGENTS.md`.
- **Board:** Chaky assigns every ticket's 1-5 priority with a one-line reason (the researcher can change any); tickets whose done-when is fully met close automatically with "say *reopen*"; human tickets close only once the researcher's own decision or result is recorded. Offers once to have Claude Code build a mod showing `tickets.md` beside the chat.

**Lean:** every SKILL.md is under 400 words (validator limit 500; detail lives in `references/`), and the `AGENTS.md` template is about half its earlier size. The README teaches skills by situation.

**Repo:** plugin manifests, CI validation (`scripts/validate.py`), scenario tests, trigger phrases, student walkthroughs (`tests/`), a filled-in example project, docs, issue forms, MIT license, `CITATION.cff`. Student safety: lab defaults file, pre-commit leak guard, explanation-language setting, CHI ethics tracker.

## 0.1.0 (first upload)
- **Front door:** `ask-chaky` (what needs attention, next step, progress, advisor update, retro, session log).
- **Board:** `plan-tickets` (tickets with type, 1-5 priority, done-when; assist or lead mode; fog and frontier; seeded at onboarding).
- **Core:** `start-paper`, `shape-idea`, `run-study` (pilots, plan freeze, reflection), `write-paper`, `review-paper` (deterministic checklist; checkpoint, full, or submission mode).
- **Supporting:** `grill-me`, `find-papers` (search, watch, triage), `polish-prose` (with unslop), `analyze-results` (statistics and figures), `write-code` (tested, mutation testing), `use-llms` (model access, free-chat labeling, outside review).
- **Meta:** `teach-chaky` (learn repeated preferences, add supporting skills).
- **Repo:** CI validation (`scripts/validate.py`), scenario tests, trigger phrases, student walkthroughs (`tests/`), a filled-in example project, docs, issue forms, MIT license, `CITATION.cff`.
- **Student safety and fit:** lab defaults file, optional pre-commit leak guard, explanation-language setting, CHI ethics tracker.
- 14 skills: merged from an earlier 20 to keep the suite lean.
