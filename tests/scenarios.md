# Scenario tests (run before each release)

Run each in a fresh folder with a clean Claude Code session. Tick every expectation. Where noted, run `python tests/check_project.py <folder> --type chi|nlp`. Student walkthroughs: `tests/student-walkthroughs.md`.

| # | Scenario | Say | Expect |
|---|---|---|---|
| 1 | Empty folder, CHI | "ask Chaky" → needs, terms, CHI, venue, local, assist | Mindsets first; one question at a time; terms agreed; folders incl. `src/prompts/`; board seeded (about 7 tickets) with priorities assigned; `check_project.py --type chi` passes; nothing pushed |
| 2 | Empty folder, ACL/NeurIPS | "ask Chaky" → NLP answers | NLP folders incl. `src/tests/`; board has `model-access`; `--type nlp` passes |
| 3 | Messy existing project | "ask Chaky" in a folder of notes and code | Adopt mode: mapping table; asks before moving; nothing deleted; board seeded from what exists |
| 4 | Resume next day | "ask Chaky" | Leads with what needs attention; why in one line; one "Next:"; ≤ ~8 lines |
| 5 | Assist mode | "you drive" | Recommends the top frontier ticket with a reason; asks only decisions |
| 6 | Lead mode | "let me lead" | Shows the top 3 and waits; suggests only when asked |
| 7 | New ticket | finish work that creates new tasks | Tickets created with done-when; each gets a 1-5 priority with a one-line reason, no question asked; "make <ticket> a 5" changes it and the change sticks |
| 8 | Ticket enough | meet a ticket's done-when | Closed automatically; one line "Closed: <ticket>. Say *reopen <ticket>* to undo."; outcome under Done; a partly met ticket stays open with what is missing; "reopen <ticket>" reopens it |
| 9 | New paper found | "I found a new paper: <link>" | Verified card; overlap level; options; a ticket created; main plan untouched until chosen |
| 10 | Try it | choose "try it" | Side branch `try/...`; success criterion and time box first; logged either way |
| 11 | Review twice | "quick review" twice on the same draft | Same tests pass/fail; History gets two rows; zero flipped tests |
| 12 | Review → tickets | full review | Major fixes become tickets with priorities assigned |
| 13 | Question changes | change the research question | Dependent rows ⚠ stale or fixed; paper sync offered; related tickets reopened or created |
| 14 | Repeated instruction | give the same instruction twice | Offers `teach-chaky` once |
| 15 | Label data | "help me label data" | Safety warning first; codebook, batches; 2-3 AIs; humans only at the end |
| 16 | Plan freeze | finish pilots, "start the main runs" | Freeze step; `git tag plan-freeze-1`; logged |
| 17 | Leak guard | stage a fake `.env` | Commit blocked (hook installed) |
| 18 | Language | choose a non-English explanation language | Explains in it; paper, code, file names stay English |
| 19 | Progress and retro | "show my progress", then "retro" | Bars from the stage map; tickets done of total; retro asks 5 questions one at a time and logs a reflection |
| 20 | Unslop | paste a generic paragraph, "unslop this" | Hits per 1,000 words before → after; no new claims; `[EVIDENCE?]` where unsupported |
| 21 | Submit tomorrow | "can I submit now?" | Submission mode: blockers first, then should-fix, then nice-to-have |
| 22 | Plain talk, their words | in a project whose `terms.md` says "honest agent", ask "ask Chaky" and "what should I measure?" | Everyday words; no ticket, done-when, fog, frontier, IV/DV, or mode names unless the student used them first; says "honest agent", never a synonym; a field term differing from theirs is mentioned once and asked about |
| 23 | Board side panel | first "show the board" | Offers once to have Claude Code build a mod showing `tickets.md` beside the chat, with the exact phrase to say; editor fallback mentioned; not offered again |
