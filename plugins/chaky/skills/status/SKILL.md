---
name: status
description: A quick catch-up, especially after time away. Says what has happened since you were last here, what is happening now, what needs your attention, and which skill could help next. Reads only; changes nothing. Use for "status", "catch me up", "what's going on", "what's happening", "I've been away", "it's been a while", "remind me where we are", or /status.
---

# Status

A short catch-up the researcher can read in under a minute. **Read only:** change no file and start no skill.

```
Last here: 12 days ago (3 Nov). Since then: pilot 2 ran; results in results/pilot2.csv.
Now: idea testing. Working on: decide participant count (P1).
Needs you: ⚠ intro still uses the old question · ticket "pick baseline" waiting on your choice.
Suggested: /update-board to re-sort tasks after the break. Or: /update-paper intro
```

## 1. Read
- `current_status.md`, the board (`tickets.md`), the latest entries in `log.md`, and `git log` since the last log date.
- No project → suggest `update-repo`. Nothing else.

## 2. Say (five lines at most, plain words, their terms)
1. **Last here:** how long ago, from the latest log or commit date.
2. **Since then:** what changed (commits, new results, closed tickets). "Nothing" is fine.
3. **Now:** the stage and the top ticket in progress.
4. **Needs you:** decisions waiting on them, ⚠ stale rows, results newer than the paper, a deadline within 14 days. At most three; most urgent first. None → say so.
5. **Suggested:** one skill and why, plus at most one other. Use the table in `guide-me`.

**Long break (14+ days):** add one line, "Before you start, `/update-board` will re-sort your tasks", unless that is already the suggestion.

## 3. Wait
They choose. Want more detail → suggest `guide-me`; want the full recap → `update-board`.
