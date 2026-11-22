# Changelog

**Every update bumps the version** (MINOR = a new skill or changed behavior; PATCH = wording or bug fixes; after 1.0, renaming or removing a skill is MAJOR). Change it in `plugins/chaky/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `CITATION.cff`, and the README title, and add an entry here. `scripts/validate.py` checks they match; CI fails a pull request that doesn't bump it.

**Names:** lowercase hyphenated words starting with a verb (`update-paper`, `setup-writing-style`). `guide-me` is the front door.

## 0.43.0
- **`update-repo` covers the whole repo too:** every folder, working file, log, result, and paper section, not just what changed since the last update.

## 0.42.0
- **Do everything, not just what changed recently.** With no focus, `review` checks the whole paper (every section, table, figure, citation, and appendix against the code and results), `update-paper` goes through the whole paper (papers, story, title, every section, table, and figure; `⚠ stale` first), and `update-board` reads the whole project (every ticket, all of `log.md` and `review.md`, every working file, the whole paper). A focus still narrows it.

## 0.41.1
Fixes from a full double-check:
- `status` said "change no file", but the `AGENTS.md` template said to run the quick sync at the end of every skill. The quick sync now runs only after skills that changed something.
- Confirming their hypothesis is now in the critical list in the `AGENTS.md` template (`plan-method` already marked it critical).
- `review` gives the full path to `update-paper/references/sections.md`, and its validity check now asks whether a surprising result passed the checks in `rigor.md`.
- Tests: walkthrough 8 (back after two weeks) now uses `status`; new scenarios 72-74 cover the catch-up, confirming the hypothesis, and an unexpected result.

## 0.41.0
- **Confirm their hypothesis** (`plan-method`, critical): state each hypothesis back in the researcher's words and get a yes before designing around it.
- **When results are unexpected** (`plan-method/references/rigor.md`): before calling a result surprising, rule out code, data, measure, analysis, and chance, and check what close papers saw; log every check. Only then is it a finding to keep and discuss in depth. Expected results get the code and data checks too. `plan-method` step 6 and the discussion guide point to it.

## 0.40.0
- **No word limits.** The validator no longer checks the length of skills, references, or the `AGENTS.md` template. Skills stay lean by trimming only when the meaning stays (`CLAUDE.md`).
- Reviewed every skill:
  - `plan-method` now asks for the research questions and hypotheses, each with the result that would challenge it, and defines success before any data. Before, the freeze needed hypotheses but the plan never asked for them.
  - `think-deeply`: the assumption check and "go deep" are merged into one step (same meaning, one step fewer), and a line repeating the description is removed.
  - `guide-me` suggests `status` for a catch-up after a break.
  - The other skills were already right-sized and are unchanged.

## 0.39.0
- **New skill `status`:** a read-only catch-up, especially after time away. Five lines at most: when you were last here, what changed since, what is happening now, what needs your attention (at most three), and one suggested skill. After 14+ days away it also suggests `/update-board`. Added to the README, `guide-me`'s skill list, the `AGENTS.md` supporting skills, trigger phrases, and the issue form.

## 0.38.0
- **Validating AI-based measures** (`plan-method/references/ai-measures.md`): when a study measures with an AI tool (simulated user, LLM judge, tracker, checker), validate it first: a fixed gate against committed labels; three blinded labellers; MT-Bench-style agreement reporting (Zheng et al., NeurIPS 2023); every error traced to a software bug, a measurement design problem, or a model limit; probes before adopting a change; code decides what code can; a fresh held-out check with a fixed seed; every round kept and reported.
- `think-deeply` step 2: classify a problem in a measuring tool (software bug, design of the measure, or model limit).
- `update-paper` method guidance: report the gate, the rounds, and the fresh check in the appendix.

## 0.37.0
- **What to discuss:** the discussion guide (`update-paper/references/sections.md`) lists eight points, one subsection or paragraph each, all anchored to the research questions: what you expected and the unexpected (in depth) · what you achieved and how far from the ultimate goal · comparison with related work · why the design decisions and their effect · design implications · significance · limitations · one or two concrete future work items. Limitations: only core, concrete, real ones that could affect validity, each with why it does not matter too much; never ones true of any study, and never ones that make the work look good.

## 0.36.0
- **Learn how close papers argue** (`update-paper/references/argument.md`, `/update-paper argue`): for the intro, method, and discussion, map the argument of 3-5 recent close top-venue papers one line per paragraph (how they state the gap, show novelty, justify decisions, show fairness, explain results, frame limitations), find the common moves, compare ours, and rewrite our sections to make those moves in our own words and voice. Maps saved under *How they argue* in `related_work.md`; never copies their sentences.

## 0.35.0
- **One rule, one home.** Every rule now lives in exactly one file; other files point to it. The rule map is in the repo's `CLAUDE.md`.
- **`AGENTS.md` template: 906 → under 600 words**, as ten one-line principles: they lead · **don't just agree** (new: say so once with evidence, then they decide) · tickets and priorities · learn from papers at any stage · root cause, not patches · strong novelty, validity, rigor · honest and reproducible · write so no one has to ask · remember what they repeat · rough first, tidy always.
- **`writing.md` replaces `style.md`:** one home for plain English, coherence (new section), consistent terms, don't invite questions, elements of style, and the checks before any edit is shown.
- Duplicates removed from `update-paper`, `sections.md`, `figures.md`, `review`, `think-deeply`, and `citations.md`: recency and venues live only in `papers.md`, fairness only in `rigor.md`, writing rules only in `writing.md`.
- Validator: enforces the size budgets (AGENTS template under 600 words, references under 900) and resolves cross-skill reference paths.

## 0.34.0
- **Framing the method** (`update-paper/references/framing.md`) for the abstract, introduction, and contributions: one sentence on what it estimates and how; 2-4 concrete difficulties, each with a plain reason; which part of the method handles each, in the same order; one or two measured strengths (never unmeasured); an explicit novelty claim for the method and any new evaluation (credit the known parts, then "to our knowledge, X is the first <system> that <capability>"), made only after a search of recent top-venue work and preprints, narrowed if a close paper exists. Before finishing, the framing must match the method section exactly. `review` checks the claim and the match.

## 0.33.0
- **Plain English like the venue:** before drafting any section, `update-paper` reads how 2-3 recent accepted papers at the target venue write that section and follows their structure.
- **Terms where they're needed, never a glossary:** no separate "Terms" section; each term is introduced in a natural sentence where first needed, ideally in a short walk-through of one interaction at the start of the method, with a concrete example; then used and spelled the same everywhere; no new labels, abbreviations, codes, or jargon.
- **Answer "what?" and "why?" on the spot:** one short example or reason wherever a skeptical reviewer would stop; a definition must answer a question, not raise one.
- Before an edit is shown: every term defined before first use and used the same way everywhere. `review` checks it.

## 0.32.0
- **Skeptical-reviewer pass before any edit is shown:** write only what a skeptical reviewer needs; cut anything that invites a question (defensive filler, side justifications, borrowed terms, a second sentence when one is enough).
- **One name per thing:** each condition, variant, measure, and component has one name, identical in every table, caption, figure, and section and matching `terms.md`; no internal codes; the whole paper is searched for mismatches before an edit is shown; descriptions use the same words as the names they explain.
- **Results tables:** baselines cited as (Author et al., VENUE YEAR) from verified top venues in the last five years; our method last, uncited, with its variants indented under it in the same order in every table; no "compared with" or "what changes" columns; each description names the one component it adds; fairness stated once in a short paragraph (same inputs, same participants or items, same effort, same grading).
- `review` checks both rules.

## 0.31.3
- **Results tables:** baselines from top-tier venues in the last 5 years, each with citation and venue; our method last, labeled "Ours", no citation; the caption shows the comparison is fair by saying how each condition was treated the same ("For each condition, we use the same X and Y; only Z differs").

## 0.31.2
- **Venues in table labels and top venues first:** baseline rows read "Honest agent (Xxx et al., ACL 2025)" (preprints as "arXiv 2025"); paper searches and baseline choices prefer top venues (NLP and ML: ACL, EMNLP, NAACL, TACL, NeurIPS, ICLR, ICML; HCI: CHI, UIST, CSCW, TOCHI), now the lab's default preferred venues in `lab-defaults.md`.

## 0.31.1
- **Cited baselines in results tables:** every baseline or borrowed method row names its source, e.g. "Honest agent (Xxx et al., 2025)"; borrowed datasets, metrics, and scales are cited in the header or caption; our method is marked "Ours".

## 0.31.0
- **Rigor above all:** a new `AGENTS.md` rule and `plan-method/references/rigor.md`: compare many things (several strong baselines, ablations, settings, variations), analyze many ways (planned tests with effect sizes, robustness, sensitivity, subgroups, error analysis, qualitative support), protect internal validity (every confound named and controlled, conditions differ only in the IV, no leakage) and construct validity (validated measures, a second measure, manipulation check), and keep the analysis fair (same data, tuning, and compute for every method; plan fixed first; corrections; report everything). Part of `plan-method`'s five musts; `update-paper` analyses point to it.

## 0.30.0
- **Rigorous citation check in `review`** (`review/references/citations.md`): every `.bib` entry and every `\cite`, not a sample. Each entry is found at a real source (DOI, Crossref, Semantic Scholar, OpenAlex, DBLP, Anthology, arXiv...), every detail matched, the published version used, retractions checked, the cited sentence checked against the paper itself, recency checked, BibTeX re-fetched if hand-made; plus missing or unused keys and duplicates. One row per entry with an evidence link; never ✅ without one; unreachable sources are reported as unchecked. Every ❌ and 🔧 becomes a ticket.

## 0.29.1
- **Recent citations everywhere:** the "mostly ≤ 5 years, at most 6-7" rule now covers every section (intro, method, discussion), not only related work, and defines a **classic** (foundational theory, the scale or instrument used, the original method or dataset, a field landmark), paired with recent work that uses it.

## 0.29.0
- **`plan-method` five musts:** before the pilot and before freezing, the plan must pass novelty (tests the one difference), validity (internal, construct, external), papers consulted, justified (every major decision in a decision table with why and source), and reproducible (versions, seeds, configs, prompts, materials, procedure, one command). Any ❌ → fix the root cause first; freezing needs all ✅.

## 0.28.0
- **Title check in `update-paper`:** after every update it checks whether the title still fits the story and the one difference; if a better one exists, it suggests 2-3 with reasons next to the current one, and the researcher chooses. Title guidance adds keywords from close papers and no overpromising.

## 0.27.0
- **`update-repo` cleans for real** (`references/cleanup.md`): safe junk (caches, LaTeX build files, `.DS_Store`, empty folders) is removed and `.gitignore` updated without asking; the student's work (stray files, `_v2`/`final` copies, unused or big files) gets a suggested action and waits for a yes; secrets or participant data in git → stop and ask; duplicate rows and old Done tickets in the working files are tidied.

## 0.26.0
- **Check how papers do it, at any stage:** a new `AGENTS.md` rule for every skill. Before deciding how to do anything (design, measure, analysis, figure, section structure, fix), look at how recent close papers did it (`related_work.md`, else a quick verified search), follow common practice unless there's a reason to differ, and name the paper. Never invent a "standard way".

## 0.25.2
- **Recent related work:** paper search and related work use mostly the last 5 years, at most 6-7, so the work doesn't look dated; older papers only for 1-2 classics (a theory, a scale, the original method). `review` flags older citations.

## 0.25.1
- **`think-deeply` always consults papers:** step 8 is marked never-skip; it asks how papers usually fix this root cause, and no recommendation is made until papers are checked. The answer line is now `How papers fix it:`.

## 0.25.0
- **`think-deeply` finds the root cause first:** step 2 asks "why?" until the cause of the problem, and checks whether the proposal fixes the cause or only a symptom; a symptom fix is never the recommendation. The answer starts with `Root cause:`.

## 0.24.0
- **Root cause, not patches:** a new `AGENTS.md` rule for every skill. When something fails, ask "why?" until the cause, fix that, say it in one line, and log it; never patch the symptom (rewording an overclaim, tuning until numbers look good, hiding failed runs, defensive sentences). `review` fixes target the root cause; `plan-method` finds the cause before changing a pilot.

## 0.23.0
- **Elements of style:** `update-paper`'s style guide adds the core rules of Strunk and White's *The Elements of Style*, in our own words with research examples: omit needless words, active voice, positive form, definite and concrete language, parallel form, related words together, emphatic words at the end, one tense per section, no over-qualifying. The researcher's voice still comes first. `review` checks them; README credits the book.

## 0.22.1
- **`update-paper` reads `voice.md` first:** a clear first step before writing any section (with `terms.md`); an empty or template `voice.md` → suggests `/setup-writing-style`. The style guide now puts the researcher's voice above its own rules.

## 0.22.0
- **Marketplace renamed `ask-chaky` → `research_skill`**, matching the GitHub repo. Install with `/plugin install chaky@research_skill`. Older installs: uninstall `chaky@ask-chaky`, remove the `ask-chaky` marketplace, and install again (README).
- **README rewritten** by the maintainer (personal overview, mindset, cheat-sheet table, mods, credits); grammar fixes only. The older update and migration notes are no longer in the README.
- **Removed `docs/`** (cheat sheet, how-it-works): no longer linked; the README table is the cheat sheet.

## 0.21.1
- **Removed the example project** (`examples/honest-sales-agent`) and its README link.

## 0.21.0
- **Every skill ends with a light `update-board`:** the quick sync closes finished tickets, adds new ones, re-checks priorities with the `update-board` rules, and shows the top 3 tasks plus the next skill. It is part of every skill, not a separate skill start; the full `/update-board` (recap, drop or merge, plain names) is suggested weekly or when the board is messy, and by `guide-me` after 7+ days.

## 0.20.0
- **`setup-writing-style` takes a Google Scholar link:** lists your papers, suggests 2-3 recent first-author ones, and reads open copies (arXiv, ACL Anthology, open access); if Scholar blocks it, asks for PDFs or uses Claude in Chrome.

## 0.19.0
- **`read-papers` merged into `update-paper`:** step 1 of `update-paper` finds and reads the 10-15 closest papers when there are fewer than 10 verified ones, on `/update-paper papers`, or on "is this novel?" (search, read, field in three lines, what to copy, the one difference, novelty and validity: `references/papers.md`; triage and watch moved too). The related work section uses the same field summary.
- **`think-deeply-and-learn-from-other-papers` is `think-deeply` again**; it still learns from other papers.
- **Removed `speak-plainly`:** plain talk is already the default (`AGENTS.md`); "always talk simpler, in Thai" goes into `preferences.md`.
- 11 skills.

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
