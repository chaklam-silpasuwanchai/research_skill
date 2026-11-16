---
name: think-deeply
description: For when you're not satisfied with what the AI proposed. Finds the root cause, looks from every angle, learns from other papers, and proposes the most sensible approach. Use for "think deeply", "is there a better way", "challenge this", "what is the root cause", or /think-deeply [topic].
---

# Think Deeply

Use when the researcher isn't satisfied with what was proposed. One question: **is there a better path than this?** "This" = the latest message, or what they name.

1. **Restate** the problem and the solution in one sentence each.
2. **Root cause:** why does the problem exist? Ask "why?" until you reach the cause. Does the proposal fix the **cause** or only a **symptom**? A symptom fix is never the recommendation.
3. **360° views** (a line each): reviewer · participant or data · advisor · skeptic (boring explanation, counterexample) · practitioner · ethics.
4. **First principles:** the real goal underneath; the simplest thing that meets it.
5. **Assumptions:** 2-4 the solution rests on; true here? Pick the one that matters most.
6. **Go deep** on it: ask "why?" until it is checkable, then check (repo, paper, number).
7. **Systems:** what else it touches; what happens next, and after that.
8. **Learn from other papers (always; never skip):** how do papers usually fix this root cause or handle this choice, and did it work? 3-5 papers from `related_work.md`, or a quick verified search (`update-paper` papers). No papers checked yet → do that before recommending.
9. **Propose the most sensible approach.** Compare 2-3 genuinely different paths on: the real goal · evidence (including other papers) · validity risk · time and cost · deadline and venue. Pick the overall winner, which may be a mix or the current plan.

## Answer
```
Root cause: ... (the proposal fixes it / only a symptom)
Goal underneath: ...
Worried views: reviewer (...), skeptic (...)
Weakest assumption: ... → checked: ...
How papers fix it: Lee 2023 did ... (worked) · Kim 2024 did ... (failed because ...)
Knock-on effects: ...
Paths: A (current) gains ... costs ... · B ... · C ...

✅ Recommended approach: <one sentence>
Why: <2-3 reasons>
Steps: 1 ... 2 ... 3 ...
First step now: <an action, e.g. /plan-method DV>
Would change my mind: <evidence>
Go with this, or another path?
```
End with one clear recommendation; keeping the current plan is fine. Never present a guess as a finding. If they choose a new path, end with the quick sync in `AGENTS.md`.
