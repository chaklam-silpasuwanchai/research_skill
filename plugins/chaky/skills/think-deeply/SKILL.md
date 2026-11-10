---
name: think-deeply
description: Asks whether there is a better solution than the one on the table (the latest message, idea, plan, or claim) using first principles, challenged assumptions, one thread in depth, and systems thinking. Use for "think deeply", "is there a better way", "challenge this", "are we sure", or before committing to a big decision.
---

# Think Deeply

One question drives this skill: **is there a better solution than this one?** "This" is the latest message in the conversation (yours or Chaky's), or the idea, plan, claim, or code they point to. Go **deep, not broad**: follow the most important thread to the bottom rather than listing ten shallow concerns. The researcher leads; you challenge, they decide.

## Steps
1. **Restate it** in one sentence: the problem being solved, and the solution proposed. Ask if that is right when unsure.
2. **First principles.** What is the real goal underneath (for a paper: the claim a reviewer must believe)? Strip away "how it's usually done". What is the simplest thing that would meet that goal?
3. **Challenge the assumptions.** List the 2-4 assumptions the solution rests on. For each: is it true here, how do we know, and what changes if it is false? Pick the one that matters most.
4. **Go deep on that one.** Ask "why?" until you hit something you can check (a paper, a pilot, a number, the code). Look it up in the repo or the literature before guessing.
5. **Think in systems.** What else does this choice touch (other tickets, the study design, the claims, the timeline, the participants)? What happens next, and after that (second-order effects)? Where could it feed back on itself?
6. **Is there a better solution?** Give at most two alternatives that come out of steps 2-5, each with what it gains and what it costs. If the current solution survives, say so plainly; that is a good result, not a failure.

## Output (plain words, about 12 lines)
```
The goal underneath: ...
Weakest assumption: ... (why it matters)
Digging in: ... (what I checked)
Knock-on effects: ...
Better option?: keep it / consider <alternative> because ...
Your call: <one question for the researcher>
```

## Rules
- Challenge the idea, not the person; kind in tone, strict on substance.
- Never present a guess as a finding. Unverified → say so and say how to check.
- Don't change files on your own. If they choose a new direction, log it in `components/log.md` (decision, who decided) and suggest the skill that fits (`shape-idea`, `run-study`, `plan-tickets`), without starting it.
- Want questions instead of an analysis? Suggest `grill-me`.
