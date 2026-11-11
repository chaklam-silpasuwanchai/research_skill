---
name: think-deeply
description: For when you're not satisfied with what the AI proposed. Looks at it from every angle, learns how other papers handled the same choice, explores different paths, and proposes the most sensible approach with first steps. Use for "think deeply", "think 360", "is there a better way", "other options", "challenge this", "how do other papers do this", or /think-deeply [topic].
---

# Think Deeply

Use when the researcher isn't satisfied with what was proposed. One question: **is there a better path than this?** "This" = the latest message, or what they name.

1. **Restate** the problem and the solution in one sentence each.
2. **360° views** (a line each): reviewer · participant or data · advisor · skeptic (boring explanation, counterexample) · practitioner · ethics.
3. **First principles:** the real goal underneath; the simplest thing that meets it.
4. **Assumptions:** 2-4 the solution rests on; true here? Pick the one that matters most.
5. **Go deep** on it: ask "why?" until it is checkable, then check (repo, paper, number).
6. **Systems:** what else it touches; what happens next, and after that.
7. **Learn from other papers:** how did 3-5 close papers handle this same choice, and what happened? Use `related_work.md`; missing → a quick verified search (`update-paper` papers). Never cite a paper you haven't checked.
8. **Propose the most sensible approach.** Compare 2-3 genuinely different paths on: the real goal · evidence (including other papers) · validity risk · time and cost · deadline and venue. Pick the overall winner, which may be a mix or the current plan.

## Answer
```
Goal underneath: ...
Worried views: reviewer (...), skeptic (...)
Weakest assumption: ... → checked: ...
Other papers: Lee 2023 did ... (worked) · Kim 2024 did ... (failed because ...)
Knock-on effects: ...
Paths: A (current) gains ... costs ... · B ... · C ...

✅ Recommended approach: <one sentence>
Why: <2-3 reasons>
Steps: 1 ... 2 ... 3 ...
First step now: <an action, e.g. /plan-method DV>
Would change my mind: <evidence>
Go with this, or another path?
```
End with one clear recommendation, not a menu; keeping the current plan is fine. Never present a guess as a finding. If they choose a new path, end with the quick sync in `AGENTS.md`.
