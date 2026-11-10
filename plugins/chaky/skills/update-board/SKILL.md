---
name: update-board
description: Recaps the project and fixes the board - adds forgotten tickets, drops, merges, or splits ones you don't need, re-prioritizes, renames in plain words, and closes finished ones. Use for "update the board", "check the board", "recap", "what did we forget", "re-prioritize", "is this task needed", "show the board", or /update-board.
---

# Update Board

The board is `components/tickets.md`: header (Destination, Mode, Out of scope), Fog, a Tickets table (Ticket · Type · Pri · Size · Status · Done when), and Done. Keep this format. New project → seed from `references/seed-board.md`; done-when defaults in `references/done-when.md`.

## 1. Recap (≤ 5 lines)
What was done since last time, where the paper is, what is blocked.

## 2. Fix every ticket
- **Missing?** Review fixes, decisions in `log.md` with no follow-up, clear fog, ⚠ stale sections, venue needs (ethics, statements, deadline).
- **Needed?** Drop, merge duplicates, park what won't fit, split size L.
- **Finished?** Done-when met → close it. Partly → say what's missing.
- **Priority:** 5 others wait on it or it has a deadline · 4 main path · 3 needed · 2 improves · 1 nice to have. Keep numbers the researcher set.
- **Name:** short plain words in their terms (`pilot-options` → `try-two-pilot-versions`); update every `blocked by`.

## 3. Apply, then show
```
Changed on your board:
+ add    say-how-we-differ (pri 4)   review found it missing
~ rename pilot-options → try-two-pilot-versions
- drop   trust-scale-v2 (merged)
✓ close  ethics-approval
Say "undo <ticket>" to reverse any line.
```
Dropped tickets go under Done as `dropped: <name> (why)`. Log it. Show the top 3 and suggest the skill for the first.
