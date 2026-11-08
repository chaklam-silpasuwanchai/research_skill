---
name: plan-tickets
description: Runs the project board - tickets with a type, a 1-5 priority you rate, and a "done when", plus assist or lead mode. Use for "show the board", "what first", "rate my priorities", "let me lead", "you drive", "is this enough", or work too big to plan. Inspired by Matt Pocock's wayfinder.
---

# Plan Tickets

Plan, don't do: the board decides *what* to work on; the work happens inside tickets. Inspired by Matt Pocock's `wayfinder` (MIT license), rewritten for research. Not a waterfall: any ticket can open any time, and results can reopen an earlier decision.

## The board: `components/tickets.md`
- **Header:** **Destination** (one or two lines, named first), **Mode** (`assist` or `lead`), **Out of scope**.
- **Fog:** decisions you can sense but can't state yet.
- **Tickets** table: name · type · pri (1-5) · size (S/M/L) · status (open, doing, blocked by `<ticket>`, done, parked) · done when.
- **Done:** one-line outcome each.

**See the board beside the chat.** Offer once, when the board is first shown: "Want your board always visible next to our chat? Claude Code can build you a small add-on (a *mod*) for it. Just say: *make me a mod that shows my board from components/tickets.md in a side panel, refreshed after each turn.*" If they say yes, hand over to Claude Code's own mod-building; don't write the mod inside this skill. No mods in their tool (Codex, older Claude Code)? Open `tickets.md` in an editor beside the terminal instead. Keep the board's headings and table columns as they are, so the panel can read them.

## Six ticket types and who does the work
| Type | What it is | Skill |
|---|---|---|
| **read** | outside facts, no human needed | `find-papers` |
| **decide** | settle by conversation (human) | `grill-me`, `shape-idea` |
| **try** | a rough thing to react to: pilot, prototype, draft (human) | `run-study` |
| **make** | build or prepare: code, materials, ethics form, accounts | `write-code`, or the human |
| **write** | a paper section | `write-paper` |
| **check** | a review or submission check | `review-paper` |

Human tickets (decide, try, most make) are never answered for the researcher.

## Where tickets come from
The onboarding interview (`references/seed-board.md`), a review's Major fixes, a found paper, a pilot's surprise, fog that became clear, or the researcher. Size **L** → split it. Every ticket gets a **done-when** (1-3 observable checks, defaults in `references/done-when.md`) and a time box.

## Prioritize (1-5)
Chaky proposes a rating with a one-line reason ("4: it blocks three tickets"); the researcher accepts or changes it (tappable 1-5 options when the tool allows). **5** = do next, others wait on it · **1** = nice to have. Rate each ticket when it is created; re-rate at milestones.
**Order (fixed):** frontier tickets (open, unblocked, unclaimed) by priority ↓, then tickets unblocked ↓, then smaller size, then oldest.

## Two modes (say "let me lead" or "you drive")
- **assist:** Chaky recommends the top ticket and why, proposes ratings and done-whens, drafts, and asks only the decisions.
- **lead:** the researcher picks and rates; Chaky shows the board, answers, and suggests only when asked.

## Every session
1. **Show the board:** top 3 frontier tickets, plus anything blocked or ⚠ stale.
2. **Pick one:** assist → recommend; lead → ask.
3. **Work it** with the matching skill, one question at a time.
4. **Enough?** All done-when checks met → "This meets its done-when. Close it?" (the researcher confirms). Past its time box → split, park, or accept.
5. **Write back:** one-line outcome, close it, promote fog into tickets, rate new tickets.
6. Sync the paper and log, per `AGENTS.md`.

Chaky voice for the board: ✅ done · 🔧 frontier · ⏳ blocked · 🌫 fog.
