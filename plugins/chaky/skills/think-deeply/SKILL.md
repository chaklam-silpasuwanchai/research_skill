---
name: think-deeply
description: Thinks about the current message, idea, plan, or claim from every angle (360 degrees) and asks whether there is a better solution - different perspectives, first principles, hidden assumptions, one key thread in depth, systems and knock-on effects. Use when an answer feels shallow or one-sided, for "think deeply", "think 360", "is there a better way", "challenge this", "are we sure", or /think-deeply [topic].
---

# Think Deeply

Use when the researcher feels the AI looked at something from only one side. One question drives it: **is there a better solution than this one?** "This" is the latest message (yours or theirs), or what they name (`/think-deeply my sample size`). Go around it fully (360°), then go **deep** where it matters most. The researcher decides.

## 1. Restate
The problem being solved and the solution on the table, in one sentence each. Unsure → ask once.

## 2. Go around it (360°): one or two lines per view
- **Reviewer at the venue:** what would make them reject it?
- **Participant or user** (or the data, for NLP): what is it like from their side? What might they do that we don't expect?
- **Advisor:** is it worth the time, and does it fit the deadline?
- **Skeptic:** what is the simplest boring explanation, or the strongest counterexample?
- **Practitioner:** would anyone outside research use this?
- **Ethics and risk:** who could be harmed, and what could leak?

## 3. First principles
What is the real goal underneath (for a paper: the claim a reviewer must believe)? Ignore "how it's usually done". What is the simplest thing that would meet that goal?

## 4. Challenge the assumptions
List the 2-4 assumptions the solution rests on: true here? How do we know? What changes if it is false? Pick the one that matters most.

## 5. Go deep on that one
Ask "why?" until you reach something checkable (a paper, a pilot, a number, the code), and check it in the repo or literature before guessing.

## 6. Systems view
What else does this touch (other tickets, design, claims, timeline, participants)? What happens next, and after that? Any loop where it feeds back on itself?

## 7. Answer
```
Goal underneath: ...
Views that worried me: reviewer (...), skeptic (...)
Weakest assumption: ... → checked: ...
Knock-on effects: ...
Better option?: keep it / switch to <alternative> because ...
Your call: <one question>
```
At most two alternatives, each with what it gains and costs. If the current solution survives, say so plainly. Never present a guess as a finding. Kind in tone, strict on substance. If they choose a new direction, log it in `log.md` and suggest the skill that fits.
