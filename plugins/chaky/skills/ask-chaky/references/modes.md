# Chaky modes

## Show progress ("progress", "how far am I")
Score each stage-map row: ⬜ 0 · 🟡 50 · ⚠ 50 · ✅ 100 · 🌟 100. Group means: **Research** (question, related work, design, implementation, results), **Paper** (title and abstract through figures), **Quality** (reviewer check, pre-submission). Overall = 40% Research + 40% Paper + 20% Quality. Show 10-block bars:
```
Related work  ▓▓▓▓▓░░░░░ 50%
Paper         ▓▓▓░░░░░░░ 30%
Overall       ▓▓▓▓░░░░░░ 40%
```
**Journey stats** (from the repo): days since the first commit, tickets done of total, commit count, verified papers, runs logged, reviews run, dead ends logged.
**Milestones** (🏁 earned / ⬜ locked): 🥾 repo created · 📚 10 verified papers · 🧪 first pilot logged · 💀 first dead end logged (dead ends are progress) · ✍️ abstract drafted · 🎯 review ≥ 3.5 on both scores · 🚀 submission check passed.
Time = first commit to today. Chaky can't see token usage; the user can check their tool's usage command and tell Chaky the number to log. Celebrate honestly, then give one "Next:".

## Advisor update ("progress update", "meeting with my advisor")
Use the lab's meeting rhythm and format from *Lab defaults* in `AGENTS.md` if set. One plain-English page in chat (save only if asked): the question in one sentence; tickets closed since last time (from `tickets.md` and `log.md`); key results and figures; dead ends and what they taught; review score trend; decisions needing the advisor's input; next two weeks.

## Retro (milestone, end of week, or "retro")
Inspired by Matt Pocock's `retro`. Five questions, one at a time, each with Chaky's suggested answer from the log:
1. What moved the paper forward most?
2. What wasted time or surprised you?
3. Were any ticket sizes or priorities off? (change them; resize)
4. What did you have to repeat to Chaky? (offer `teach-chaky`)
5. One change for the next stretch.
Log it as a `reflection` entry in `log.md` (who: `user`). Update the board.
