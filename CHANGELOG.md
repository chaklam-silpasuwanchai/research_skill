# Changelog

**Every update bumps the version** (MINOR = a new skill or changed behavior; PATCH = wording or bug fixes; after 1.0, renaming or removing a skill is MAJOR). Change it in `plugins/chaky/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `CITATION.cff`, and the README title, and add an entry here. `scripts/validate.py` checks they match; CI fails a pull request that doesn't bump it.

**Names:** lowercase hyphenated words starting with a verb (`update-paper`, `setup-writing-style`). `guide-me` is the front door.

## 0.18.0
- **Personal preferences in their own file:** `components/preferences.md` holds the researcher's own rules ("always", "never"), read every session and followed over defaults (except safety and critical steps). `/update-repo` never touches it and moves old *My preferences* lines out of `AGENTS.md`; `speak-plainly` saves there. Skills and lab files stay free of personal preferences.
- **Lab terms "avoid":** dry run → practice run (nothing saved or sent); smoke run/test → quick test run; sanity check → quick check.

## 0.17.0
- **`plan-method` reads how others did it first:** the method sections of the 5-15 closest papers go into a table in `experimental_design.md` (design, IV and levels, DV and measure, participants or data and n, task, analysis, baseline), with the common pattern named; every planning decision then cites a paper or says why we differ.

## 0.16.0
- **Claude in Chrome:** before the AI reviewer check (and free-chat labeling), Chaky asks whether the student has the Claude in Chrome extension. If yes, it opens Claude, ChatGPT, and Gemini in their own browser, pastes the anonymized draft (or batches) after one confirmation, and collects the answers; if not, the student copies and pastes as before.

## 0.15.0
- **AI reviewer check in `review`:** many reviewers now use AI, so before sharing or submitting the student runs an anonymized draft through Claude, ChatGPT, and Gemini with one reviewer prompt (`review/references/ai-reviewers.md`). Pass = all three at accept or weak accept; points 2-3 AIs share become tickets; every paper they name is verified. Pasting an unpublished paper is a critical step (ask first, anonymize, no training on data). The old outside-review notes moved here from `plan-method`.

## 0.14.1
- **Two kinds of novelty:** the introduction should make reviewers feel both idea novelty (a new question or insight) and technical novelty (a non-obvious method); `review` checks both.

## 0.14.0
- **How to write each section** (`update-paper/references/sections.md`): reviewers mostly decide from the abstract and introduction; intro in five parts (background, problem, methodology, key findings, contribution) with one clear contribution and no overpromising; related work in subsections, synthesized (agreements, disagreements, position, borrow, differ); methodology follows the venue, every decision justified, reproducible, supports internal and construct validity; results boring, report only; analyses as close papers do; discussion the strongest part, in subsections (insights, past work, explanations, what if, limitations, future work); conclusion nothing new; appendix for reproducibility details. `review` checks the intro, results, and discussion against this.

## 0.13.0
- **Say only what's necessary:** `update-paper` keeps a sentence only if the reader needs it to understand or believe the story (the rest is cut or moved to the appendix), so reviewers have less to question; `review` flags unnecessary sentences, side results, and details.

## 0.12.0
- **`think-deeply` is now `think-deeply-and-learn-from-other-papers`**, and it does what the name says: after the 360° look, it checks how 3-5 close papers handled the same choice (from `related_work.md`, or a quick verified search) before proposing the most sensible approach. "Think deeply" still triggers it. Skill names may now be longer than three words.

## 0.11.4
- **Lean lab terms:** `lab-terms.md` is split into a short **Core** (stages, variables, words to avoid), copied into `terms.md` and read every session, and the **full list**, copied to `components/lab-terms.md` and looked up only when a term comes up. Adds zero-shot / few-shot.

## 0.11.3
- **Lab terms:** adds control condition, manipulation check, exclusion criteria, informed consent, pre-registration, order effect, novelty effect, and hallucination; "post-hoc test" now includes the multiple-comparison correction.

## 0.11.2
- **Lab terms:** adds study terms (RQ, task, procedure, questionnaire, Likert scale, think-aloud, Wizard-of-Oz, simulated users, SUS, NASA-TLX, task time, accuracy, error rate, ground truth), analysis terms (effect size, p-value, post-hoc test, confidence interval, Cohen's kappa, semi-structured interview, thematic analysis, prompt, temperature, human evaluation, error analysis, benchmark), and writing terms (contribution, research gap, design implications, limitations, future work). "Avoid" adds held-out set, novel, leverage/utilize, robust, significant.

## 0.11.1
- **Lab terms:** adds the study words the lab uses often (conditions, participants, apparatus, trials, blocks, pilot study, experiments, analyses, design rationale, study rationale, LLM judge, hypothesis, discussion), the writing verbs (propose, investigate, explore, develop, hypothesize), and words to avoid or explain (smoke run, fitting, replay).

## 0.11.0
- **Lab terms (AIT Brain Lab):** new `update-repo/assets/lab-terms.md` (IV/factor, DV/measure, confounding, control, random variables, individual differences, levels, operational measure, design terms, baseline, ablation, leakage, statistical analysis, internal/construct/external validity, contribution types, five research stages). `update-repo` copies it into each project's `terms.md`; Chaky uses these terms, glossed the first time in a session. `setup-writing-style` keeps them and confirms the paper's own terms.
- **Research stages:** idea generation, refinement, validation, testing, storytelling, shown by `guide-me` and in `current_status.md`.
- **`plan-method`:** the lab's five contribution types, named variables, individual differences as factor or random (asks), statistical analysis chosen from the design and data (no default), validity by name, optional replication of the closest paper's key result.
- **`read-papers`:** field summary (consensus, disagreements, open questions), a source trail (date, databases, terms, verified count), OpenAlex and alphaXiv added.
- **`review`:** checks the paper matches the work (numbers vs `results/`, claimed conditions vs code); validity by name.
- **`update-paper` and `brain-dump`:** the lab's one-page idea outline (Background, Problem, Research question, Proposed solution, Evaluation, Contribution).
- **README:** mindset 2 says no "autoresearch"; mindset 3 is the lab terms; credits for Kalaris Labs, Orchestra Research, Feynman, Matt Pocock, and the AIT Brain Lab guide.

## 0.10.1
- **README: "The Chaky mindset"**: everything revolves around tickets and priorities; you direct and the AI does the legwork (sloppy suggestion → `/think-deeply` or `/read-papers`).

## 0.10.0
- **README by "when you...":** one table mapping each moment (lost, confused, suspect overlap, want to write...) to the skill and what happens.
- **`find-papers` merged into `read-papers`:** search, close reading of the 10-15 closest, what to copy, the one difference, novelty and validity, plus watch and triage ("I found a paper").
- **`write` is now `update-paper`:** agrees the story first (background and key papers, key problem, key solution, key findings, so what), offers 2-3 alternative storylines if unsure, then writes or updates sections; stale sections first.
- **`review`:** improvements split into **easy** (do now) and **difficult** (plan them), all ticketed.
- **`setup-writing-style`:** learns from a paragraph, past papers, emails, or blogs, and confirms the paper's terms one at a time.
- **`update-repo`:** updates all docs and cleans up clutter (stray files, `_v2` copies, caches; moving or deleting asks first); paper prose goes to `update-paper`.
- **`plan-method`:** fair design and tools, learned from 5-15 close papers; suggests free-chat labeling whenever a study needs labels.
- **`brain-dump`:** framed as the AI getting your feedback and thinking.
- 13 skills.

## 0.9.0
- **`validate-idea` is now `read-papers`**, and it reads closely: the 10-15 closest papers (running the `find-papers` search first if needed), one table row each (question, what they change and measure, who or what data, design and analysis, finding, limitation, what we borrow, how we differ), a list of methods to borrow or copy with sources, and **the one difference** in one sentence. Then novelty, validity, significance. Principle: copy many things, differ in one.
- **New `speak-plainly`:** changes how Chaky talks for the rest of the session (plain words, their language and terms, an example, what needs them first, short) and offers to make it permanent in `AGENTS.md`. `clarify` still rewrites a single answer.
- **README by pain point:** "Stuck? Find your moment" groups what students actually think ("I'm back after two weeks and forgot everything", "the reviews came back and they hurt") with the skill to try, from getting started to reviews, plus a typical journey. Shorter overall.
- **`find-papers` focuses on searching:** the field map and a ranked list of the 10-15 closest papers, plus watch and triage; it then suggests `/read-papers`.

## 0.8.0
- **Removed `setup-llms`:** AI models now live in `plan-method` (`/plan-method models`, `/plan-method labeling`): key in `.env`, pinned models, one logged `call_model()`, local models, free-chat labeling and outside review. Its reference files moved to `plan-method/references/`.
- **Removed `remember-this`:** "always do X" is now a rule in `AGENTS.md`. Chaky asks once, then adds a dated line under *My preferences* (or the personal `CLAUDE.md` for all projects). Adding skills stays a maintainer task (`CLAUDE.md`, `MAINTAINERS.md`).
- 13 skills.

## 0.7.0
- **`think-deeply` proposes the most sensible approach.** After the 360° look, it compares 2-3 paths on the real goal, evidence, validity risk, time and cost, and deadline fit, then ends with one clear recommendation: why it's most sensible, the steps, the first step now (with the skill to use), and what evidence would change its mind.

## 0.6.0
- **Regular syncing.** The `AGENTS.md` end-of-task step is now a **quick sync** that every skill runs: close finished tickets and add new ones, fix facts in the paper (mark changed stories ⚠ stale), update status and log, commit, and report it in one line. Each relevant skill now ends with it explicitly.
- **Full updates on a rhythm:** `guide-me` suggests `/update-repo` first when there's been no full update for 7+ days, results or reviews are newer than the paper, rows are ⚠ stale, or `AGENTS.md` is older. `plan-method` suggests one after a pilot or the main study; `update-repo` logs each run as `full update`.

## 0.5.0
- **`review` simulates a panel:** after the checks, three short reviews (methods expert, domain expert, skeptic) and a meta-review with the likely decision and the 2-3 changes that would most move it. Quick mode gives one combined view.
- **`update-repo` updates facts, not prose:** numbers, counts, method details, tables, and citations; sections whose story changed are marked ⚠ stale with a suggested `/write <section>`.
- **`write` adds `/write limitations`** (real threats from the log, deviations, and reviews; no filler) **and `/write response`** (reply to reviewers: changed, clarified, disagree, out of scope, within the limit).

## 0.4.0
- **`check-board` is now `update-board`**, matching `update-repo`. Same behavior: recap, add forgotten tickets, drop or merge unneeded ones, re-prioritize, rename in plain words, close finished ones. "Check the board" still reaches it.

## 0.3.0
- **`setup-repo` is now `update-repo`.** No project yet → sets it up as before. Existing project → brings it up to date: adds missing folders and files (never overwrites), refreshes `AGENTS.md` from the template (keeping venue, mode, language, lab defaults, and preferences), aligns the working files and the board with the latest log, runs, and results, and updates the paper (method, numbers, results, citations), marking what can't be updated yet as ⚠ stale. Shows an "Updated / Stale" summary with undo. `guide-me` suggests it when files or the paper fall behind.

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
