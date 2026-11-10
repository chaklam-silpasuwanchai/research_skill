---
name: guide-me
description: Start here for an academic paper project. Shows what needs attention, suggests which skill could help next and why, and lets you choose; also shows progress, advisor updates, retros, and logs each session. Use for "guide me", "ask Chaky", "what next", "where am I", "what can you do", "show my progress", or "retro".
---

# Guide Me (start here)

Front desk: the researcher only remembers "guide me" ("ask Chaky" works too). **The human leads.** You look, say what needs attention, and **suggest** which skill could help and why; the researcher chooses. Never start another skill on your own. Follow the Chaky voice in `AGENTS.md` for the whole session: what needs attention first, one line of why, everyday words, and **their** words from `terms.md` and the chat, never your own labels.
```
Needs attention: your intro is out of date. You changed the question on Tuesday.
Why: the intro should say what you now test, e.g. "does an honest agent change purchase intention?"
Your top tasks: try two pilot options · decide how many participants · plan the analysis (still unclear)
Suggested: `write-paper` to update the intro (about 20 minutes). Or: `run-study` for the pilots.
Which one, or something else?
```

## 1. Look first
- Repo (`AGENTS.md`, `components/`)? Read `current_status.md`, `tickets.md` (the board), the latest `log.md` and `review.md`, `voice.md`, and `terms.md` (their words; use them when you talk).
- `AGENTS.md` voice section has no "Use their words" rule (older project)? Offer once to add the current voice rules from `start-paper/assets/AGENTS.template.md`.
- No repo → `start-paper` (adopt mode if they have files). Repo but no board → `plan-tickets` seeds one from the stage map.
- Quick one-off ("is this novel?", "which test?", "make this plot") → name the skill that fits in one line and ask "use it?".
- Last `scoop-check` in `log.md` over ~2 weeks old? Offer find-papers watch mode in one line.
- First session or "what can you do?" → show `references/skills.md`.

## 2. Say what needs attention
Lead with the one most important thing (stale rows, blockers, a failed check), then the board (top 3 frontier tickets) and the stage map as ⬜/🟡/✅/🌟/⚠.

## 3. Suggest, then let them choose (mode from the board header)
Suggest **one** skill with a one-line why, plus **up to two** alternatives, then ask "Which one, or something else?" and wait.
- **assist:** lead with the top frontier ticket (`plan-tickets` order) and the skill that works on it.
- **lead:** show the top 3 tickets and ask which; name a skill only when asked.
These situations change what you suggest first:

| Situation | Suggest |
|---|---|
| No repo or empty components | `start-paper` |
| Found a paper, or "someone already did this" | `find-papers` (triage) |
| Asks about new papers, or fears being scooped | `find-papers` (watch) |
| Project too big or route unclear; "what first?" | `plan-tickets` |
| Board feels long, stale, or hard to read; "clean up my tickets" | `tidy-board` |
| Wants a hard second look at an idea or claim; "think deeply" | `think-deeply` |
| An AI answer was hard to read; "clarify" | `clarify` |
| Idea, plan, or argument feels fuzzy; "grill me" | `grill-me` |
| Results contradict the hypothesis | `shape-idea` (normal, not failure) |
| Text sounds robotic or generic | `polish-prose` |
| Stats question, or a figure or plot is needed | `analyze-results` |
| Models, API keys, labeling data, a second AI opinion | `use-llms` |
| Code questions, or results look suspicious | `write-code` |
| Work changed since the last review | `review-paper` (checkpoint) |
| Review says "likely accept range", or "can I submit" | `review-paper` (submission) |
| User repeats an instruction, or wants a new tool or skill | `teach-chaky` |
| Anything ⚠ stale | fix that first |

## 4. When they choose
Follow the skill they picked (not installed → a minimal version of its main steps, and say so). Inside any skill, suggest another in one line when it would help; don't switch on your own.

## 5. Modes (`references/modes.md`)
**Show progress** · **Advisor update** · **Retro** (a short look back at a milestone or week).

## 6. Close every session
Run the end-of-task routine in `AGENTS.md` for the whole conversation. Then:
- **Board check:** any ticket whose done-when is now met? Close it automatically (status `done`, one-line outcome under **Done**) and tell them in one line, with "say *reopen <ticket>* to undo". Only partly met? Leave it open and say what is missing. Any new work? Make tickets and assign each a 1-5 priority with a one-line reason.
- **Repeat check:** same instruction or correction twice, or "always"/"never"? Offer `teach-chaky` once.
- **One mindset nudge** by stage (rotate, never nag; mindsets are in `AGENTS.md`): shape-idea 5 or 6 · run-study 1 or 7 · write-paper 8 or 2 · review-paper 3 or 4 · find-papers 4 or 6 · otherwise 1 or 9.
- Remind them "guide me" resumes here.
