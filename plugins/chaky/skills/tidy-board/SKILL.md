---
name: tidy-board
description: Cleans up the project board - re-checks every ticket's priority, asks whether each ticket is still needed (drop, merge, park, split), and renames tickets in plain, easy words. Proposes all changes first; you approve. Use for "clean up my tickets", "re-prioritize", "is this task needed?", "my board is confusing", or when the board feels long or stale.
---

# Tidy Board

The board (`components/tickets.md`) grows messy: old tickets nobody needs, duplicates, priorities that no longer fit, names only Chaky understands. Tidy it in one pass. Board format and priority rules: `plan-tickets`. **Propose first, change only what the researcher approves.**

## 1. Read
`tickets.md`, `current_status.md`, the latest `log.md` and `review.md`, and `terms.md` (their words).

## 2. Check every open ticket
- **Still needed?** Drop it if its goal is already met elsewhere, the plan changed, or nothing in the paper depends on it. **Merge** duplicates or near-duplicates. **Park** nice-to-haves that won't fit before the deadline. **Split** anything size L.
- **Priority right?** Re-apply the `plan-tickets` rules (5: others wait on it or it has a deadline · 4: main path · 3: needed · 2: improves · 1: nice to have). Keep any number the researcher set themselves unless they agree to change it.
- **Name clear?** Rename to a short plain phrase a newcomer would understand, in their words from `terms.md`: `pilot-options` → `try-two-pilot-versions`, `N1-fix` → `say-how-we-differ`. Keep names lowercase with hyphens.
- **Finished when** still observable and current? Fix if not.

## 3. Propose (one table, then wait)
```
| Now | Change | Why |
| pilot-options (pri 4) | rename → try-two-pilot-versions | clearer |
| trust-scale-v2 | merge into choose-trust-scale | same goal |
| follow-up-study (pri 2) | park | won't fit before CHI |
| sample-size 3 → 5 | priority up | recruiting waits on it |
```
Ask: "Apply all, pick some, or change any?" Apply nothing until they answer.

## 4. Apply
- Update `tickets.md`. On a rename, also update every `blocked by <old name>` on the board.
- Dropped tickets aren't deleted silently: move them under **Done** as `dropped: <name> (<why>)`; parked ones keep status `parked`.
- Log one entry in `log.md`: what was renamed, merged, dropped, or re-prioritized, tagged `user` (they approved) or `user-revised`.
- Show the top 3 tickets of the tidy board in one short block, then suggest a next skill in one line; don't start it.
