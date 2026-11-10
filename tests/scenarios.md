# Scenario tests (run before each release)

Run each in a fresh folder with a clean Claude Code session. Tick every expectation. Where noted, run `python tests/check_project.py <folder> --type chi|nlp`. Student walkthroughs: `tests/student-walkthroughs.md`.

| # | Scenario | Say | Expect |
|---|---|---|---|
| 1 | Empty folder, CHI | "guide me" → suggests `update-repo`; pick it; answer CHI, venue, local | A few setup questions one at a time; mindsets shown once; folders incl. `src/prompts/` if AI prompts; board seeded (about 7 tickets) with priorities; suggests `brain-dump` next; `check_project.py --type chi` passes; nothing pushed |
| 2 | Empty folder, ACL/NeurIPS | "guide me" → NLP answers | NLP folders incl. `src/tests/`; board has `model-access`; `--type nlp` passes |
| 3 | Messy existing project | "guide me" in a folder of notes and code | Adopt mode: mapping table; asks before moving; nothing deleted; board seeded from what exists |
| 4 | Resume next day | "guide me" | Leads with what needs attention; why in one line; one "Next:"; ≤ ~8 lines |
| 5 | You drive | "you drive" | Suggests the top ticket and the skill for it, with a reason; waits for the pick |
| 6 | Lead mode | "let me lead" | Shows the top 3 and waits; suggests only when asked |
| 7 | New ticket | finish work that creates new tasks | Tickets created with done-when; each gets a 1-5 priority with a one-line reason, no question asked; "make <ticket> a 5" changes it and the change sticks |
| 8 | Ticket enough | meet a ticket's done-when | Closed automatically; one line "Closed: <ticket>. Say *reopen <ticket>* to undo."; outcome under Done; a partly met ticket stays open with what is missing; "reopen <ticket>" reopens it |
| 9 | New paper found | "I found a new paper: <link>" | Verified card; overlap level; options; a ticket created; main plan untouched until chosen |
| 10 | Try it | choose "try it" | Side branch `try/...`; success criterion and time box first; logged either way |
| 11 | Review twice | "quick review" twice on the same draft | Same tests pass/fail; History gets two rows; zero flipped tests |
| 12 | Review → tickets | full review | Major fixes become tickets with priorities assigned |
| 13 | Question changes | change the research question | Dependent rows ⚠ stale or fixed; paper sync offered; related tickets reopened or created |
| 14 | Repeated instruction | give the same instruction twice | Offers `remember-this` once |
| 15 | Label data | "help me label data" | Safety warning first; codebook, batches; 2-3 AIs; humans only at the end |
| 16 | Plan freeze | finish pilots, "start the main runs" | Freeze step; `git tag plan-freeze-1`; logged |
| 17 | Leak guard | stage a fake `.env` | Commit blocked (hook installed) |
| 18 | Language | choose a non-English explanation language | Explains in it; paper, code, file names stay English |
| 19 | Progress and retro | "show my progress", then "retro" | Bars from the stage map; tickets done of total; retro asks 5 questions one at a time and logs a reflection |
| 20 | Unslop | paste a generic paragraph, "unslop this" | Hits per 1,000 words before → after; no new claims; `[EVIDENCE?]` where unsupported |
| 21 | Submit tomorrow | "can I submit now?" | Submission mode: blockers first, then should-fix, then nice-to-have |
| 22 | Plain talk, their words | in a project whose `terms.md` says "honest agent", ask "guide me" and "what should I measure?" | Everyday words; no ticket, done-when, fog, frontier, IV/DV, or mode names unless the student used them first; says "honest agent", never a synonym; a field term differing from theirs is mentioned once and asked about |
| 23 | Board side panel | first "show the board" | Offers once to have Claude Code build a mod showing `tickets.md` beside the chat, with the exact phrase to say; editor fallback mentioned; not offered again |
| 24 | Human leads | "guide me" in a project with open tickets | Suggests one skill with why plus up to two alternatives; asks "Which one?"; starts nothing until the student picks |
| 25 | Clarify | after a long technical answer, "clarify" | Bottom line first; what needs attention (≤ 3); ≤ 5 plain bullets; no diffs or code; no new facts; their terms |
| 26 | Think deeply | propose a plan, then "think 360" | Restates goal; reviewer, participant, advisor, skeptic, practitioner, ethics views; weakest assumption dug into and checked; knock-on effects; 2-3 genuinely different paths with gains and costs; recommends one; one question; changes no files |
| 27 | Check board | a board with a duplicate, a stale ticket, a cryptic name, and a review fix with no ticket | Recap ≤ 5 lines; adds the missing ticket; merges, drops or parks, renames, re-prioritizes; applies the changes and shows a "Changed on your board" table with "undo"; `blocked by` names updated; dropped tickets under Done; logged |
| 28 | Brain dump, any phase | mid-study, "/brain-dump my analysis" | One question at a time with a suggested answer; "So far" every ~4 questions; stops at one sentence or "enough"; saves to components and says what was saved |
| 29 | Validate idea with focus | "/validate-idea LLM sales agents that admit limits" | Restates it; 3-5 closest verified papers; novel, valid, significant, fit, feasible as ✅/❌/❓; fixes for each ❌/❓; saved to `ideas.md`; tickets for open items |
| 30 | Plan one part | "/plan-method IV" | Plans only the IV: conditions, levels, baseline, why; explained with an example from their study; writes it to `experimental_design.md` |
| 31 | Write one section | "/write abstract" | Writes only the abstract in their voice (`voice.md`), five parts, unslop pass; shows it and waits for comments |
| 32 | Citation check | "/review citations" on a `.bib` with one fake and one wrong-year entry | Every entry checked against DOI, Crossref, or Semantic Scholar; the fake is ❌ not found, the year is 🔧; uncited and missing keys listed; checklist returned |
| 33 | Teach me | "/teach-me power analysis" | Asks what they know; 3-7 steps with their own study as the example; a check after each step, re-explains if wrong; ends with doing it on their project; offers a cheat note |
| 34 | Change, then tell | ask `write` to tighten a paragraph | Makes the change, says what changed in one line with "undo"; no permission question |
| 35 | Critical step asks | ask to delete an old folder, or to start the main runs | Asks first (delete or move files; freeze the plan) and does nothing until confirmed |
| 36 | Writing style | "learn my writing style" with two past papers | Papers stay outside the repo; about 25 lines in `voice.md` with examples from their text; one sample paragraph in their voice; saved and said so |
| 37 | Local LLM | "/setup-llms local" | Asks about the computer and memory; suggests a model size and runner; tests one call through `call_model()`; logs the exact model |
| 38 | Update an existing project | a project with an old `AGENTS.md`, two new pilot runs, and a method section that says 2 conditions (now 3) | Doesn't re-run setup; adds missing files without overwriting; refreshes `AGENTS.md` keeping venue, mode, lab defaults, and preferences; updates working files and board; method and results updated, unfinished parts marked ⚠ stale; no invented numbers; shows an "Updated / Stale" summary with undo; logged |
