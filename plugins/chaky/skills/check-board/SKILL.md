---
name: check-board
description: Recaps the project and checks the board - which tickets we need, which we forgot, which to drop, merge, or split, re-prioritizes them, and renames them in plain words. Also auto-closes tickets whose "finished when" is met. Use for "check the board", "recap", "what did we forget", "re-prioritize", "is this task needed", "show the board", or /check-board.
---

# Check Board

The board (`components/tickets.md`) is the to-do list for the paper. This skill makes it right: a recap, then the board fixed. Optional focus: `/check-board recap`, `/check-board priorities`, `/check-board names`.

## Board format (keep it, so other tools and mods can read it)
- **Header:** **Destination** (one or two lines), **Mode**, **Out of scope**.
- **Fog:** things they sense but can't state yet.
- **Tickets** table: Ticket · Type · Pri · Size · Status · Done when. Types: read · decide · try · make · write · check. Status: open, doing, blocked by `<ticket>`, done, parked.
- **Done:** one-line outcome each.
New project → seed it from `references/seed-board.md`. Every ticket has a **done when** (1-3 observable checks; defaults in `references/done-when.md`).

## 1. Recap (5 lines max)
From `current_status.md`, the latest `log.md` and `review.md`, and the board: what was done since last time, where the paper is, what is blocked.

## 2. Check every ticket
- **Missing?** Look for work nobody ticketed: review fixes, decisions in `log.md` with no follow-up, fog that is now clear, paper sections marked ⚠ stale, venue requirements (ethics, statements, deadline).
- **Still needed?** Drop if its goal is met elsewhere or nothing depends on it; **merge** near-duplicates; **park** what won't fit before the deadline; **split** size L.
- **Finished?** All done-when checks met → close it (status done, outcome under **Done**). Partly met → keep open, note what is missing.
- **Priority** (Chaky assigns; the researcher's own numbers stay unless they agree):
  - **5:** other tickets wait on it, or it has a deadline
  - **4:** on the main path to the next milestone
  - **3:** needed, but nothing waits on it
  - **2:** makes the paper better, not required
  - **1:** nice to have
- **Name clear?** Short plain phrase in their words (`pilot-options` → `try-two-pilot-versions`). Lowercase with hyphens; update every `blocked by` that used the old name.
Order: open and unblocked by priority, then smaller size, then oldest.

## 3. Apply, then tell (one short table)
These changes are easy to undo, so make them and show what changed:
```
Changed on your board:
+ add    say-how-we-differ (pri 4)  review found it missing
~ rename pilot-options → try-two-pilot-versions
- drop   trust-scale-v2 (merged into choose-trust-scale)
✓ closed ethics-approval (approval recorded)
Say "undo <ticket>" to reverse any line.
```
Dropped tickets go under **Done** as `dropped: <name> (<why>)`, never vanish. Log the change in `log.md`. Then show the top 3 tickets and suggest the skill that fits the first one; don't start it.

## Modes
**I lead** (default): suggest the top ticket and why. **You lead** ("let me lead"): show the top 3 and wait.
