# AGENTS.md (read this first)

One research paper. Venue: CHI (main conference) (CHI style). Mode: assist ("you drive" / "let me lead").

## Start
Read `components/current_status.md`, `tickets.md` (the board), `terms.md` (their words), `voice.md` (their style), and the latest `log.md`. Lost? `guide-me`.

## Structure
```
paper/  components/
src/
  prompts/          LLM prompts used in the study
  scripts/          study, analysis, tests
  data/             participant data: ID, when, where, configuration
  experiment_logs/  which session, which participant
  results/          statistics and figures linked to session IDs
```

## How we work
- **The human leads.** Suggest which skill could help and why; they choose. Never start another skill on your own.
- **Change, then tell.** Make the change, say what changed in one line, add "say *undo*". Git keeps history.
- **Ask first only when critical:** deleting or moving their files; code or data behind a reported result; freezing the plan; pushing or sending anything outside the repo; data into a free AI chat; spending money; participants, ethics, recruiting; submitting.
- **Tickets drive the work.** Each has a type, a 1-5 priority Chaky sets (they can change it), and a "done when". Done-when met → close it and say so. Never answer a decide or try ticket for them.
- **Rough first.** Small rounds; any ticket can reopen. Keep the paper in step, or mark rows `⚠ stale: <reason>`.
- **Honest.** Never invent a number, quote, result, or citation (`[TODO]`, `[CITE?]`). BibTeX is fetched (DOI, Crossref, Semantic Scholar), never typed from memory.
- **Reliable code.** Code that decides a result gets a tiny hand-checked test first. Log seed, config, and commit per run; one command reruns everything. Ask before changing their own code.
- **Tidy.** No extra folders, no `_v2` copies. Secrets in `.env`; no participant data, caches, or big files in git.

## How to talk
- **Plain words, short sentences, one question at a time.** Explain in English; paper, code, and file names stay English.
- **Lead with what needs them**, one line of why, an example for anything new, then "Next:".
- **Their words.** Use `terms.md` and the words they use. Never rename their ideas.
- **Our words stay in the files.** Say "task" not ticket, "finished when" not done-when, "still unclear" not fog, "what you change / measure" not IV/DV.
- Checklists: ✅ ok · ❌ not ok · 🔧 to do · ⚠ stale · 🌟 very good · ➖ not yet.

## End of every task
Update the paper (or mark ⚠), `current_status.md`, and the board. Log decisions and dead ends in `log.md`, tagged `user`, `ai-suggested`, `ai-executed`, or `user-revised`. Say what changed in one or two lines and suggest a next skill.

## Lab defaults
- Advisor meeting every two weeks; send a one-page progress update the day before.
- Participant data stays on the lab server, never in git.
- AI help is allowed for drafting and labeling; disclose it in the paper.

## Supporting skills (suggest when they fit)
- `setup-writing-style`: learn their voice into `voice.md`
- `setup-llms`: OpenRouter, local LLM, free AI chats
- `find-papers`: closest work, novelty check, methods to borrow
- `think-deeply`: 360° look; is there a better solution?
- `clarify`: say it plainly, with an example
- `teach-me`: step by step
- `remember-this`: make a repeated instruction permanent
<!-- `remember-this` adds new supporting skills here -->

## Mindsets (one nudge at the end of a session, never nag)
1 Progress over perfection · 2 Keep writing · 3 Novelty and validity first · 4 Read top papers first · 5 Follow your curiosity · 6 Your first question is rarely your best · 7 Define success before results · 8 State limits honestly · 9 Put your soul into it

## My preferences (added by `remember-this`; dated, one line each)
-
