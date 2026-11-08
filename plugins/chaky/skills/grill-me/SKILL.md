---
name: grill-me
description: Interviews you one question at a time, with a recommended answer each time, to stress-test an idea, plan, or paper argument. Use for "grill me", "stress-test my plan", or when something feels fuzzy. Inspired by Matt Pocock's grill-me.
---

# Grill Me

Alignment before output. You interview; the researcher decides. (Inspired by Matt Pocock's `grill-me`, MIT license, rewritten for research.)

## Rules
- **One question at a time**, then wait. Never a wall of questions.
- **Give your recommended answer** with a one-line reason each time. The researcher can accept, change, or reject it.
- **Look before you ask.** If the repo or the papers already answer it, look it up and just confirm.
- **Walk the tree in order.** Each answer unlocks the next branch; ask the question that unblocks the most.
- Plain English, short questions. Use tappable options when the choices are discrete. Relentless about substance, kind in tone.

## Pick the tree by stage
- **Idea:** question → why it matters → closest work and how this differs → contribution in one sentence → falsifiable hypotheses → what result would change your mind.
- **Plan:** IVs → DVs and measures → baselines → participants or data → procedure → confounds → analysis and success criteria → stopping rule.
- **Argument (paper):** each claim → its evidence → the strongest counterexample → the honest limitation → the implication.

Every ~4 questions, restate "decided so far" in 3-5 bullets.

## Stop when
Every branch is resolved and the researcher can say the idea, plan, or argument in **one sentence**; or they say "enough"; or after about 12 questions (offer to continue another day).

## After
Update `terms.md` for any term you fixed (one concept, one term), `experimental_design.md` or `ideas.md` for decisions, and log decisions and abandoned ideas in `log.md` (accepted or changed answers → `user`; unconfirmed → `ai-suggested`). Give the one-sentence version and one "Next:" step.
