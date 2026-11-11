# Chaky: your AI research partner (v0.14.0)

Chaky helps you go from a rough idea to a submitted paper (CHI, ACL, NeurIPS style). **You lead. Chaky suggests, keeps you organized, and does the busy work.**

You only need to remember one phrase: **"guide me"**.

## The Chaky mindset
1. **Everything revolves around tickets and priorities.** Your board (`components/tickets.md`) is the clear path: every task is a ticket with a 1-5 priority and a "finished when". Lost? Look at the top ticket, or say **guide me**.
2. **You direct; the AI does the legwork.** Chaky isn't meant to do everything for you; that rarely works well. So no "autoresearch" here: Chaky never runs experiments or writes the paper in a loop on its own. It gives you better ways to tell the AI what to do. Suggestion feels sloppy? Try `/think-deeply-and-learn-from-other-papers` or `/read-papers`. Answer too technical? `/clarify`. Writing doesn't sound like you? `/setup-writing-style`.
3. **One set of lab terms.** Everyone uses the same words, from the AIT Brain Lab: **IV** (independent variable, a.k.a. factor: what you change), **DV** (dependent variable, a.k.a. measure: what you measure), **confounding variables** (what could interfere), **control variables** (what we keep the same), **random variables** (what we let vary), **individual differences** (how people differ), and **statistical analysis** (t-test, ANOVA, regression...). Research moves through five stages: idea generation, refinement, validation, testing, storytelling. Full list: [`lab-terms.md`](plugins/chaky/skills/update-repo/assets/lab-terms.md). Every project gets the core in `terms.md` and the full list in `components/lab-terms.md`.

## Set up (once, about 15 minutes)
You need: a paid Claude plan (Pro or higher), Git (`git --version` to check), and an empty folder for your paper.

**1. Install Claude Code.** Mac, Linux, or WSL:
```
curl -fsSL https://claude.ai/install.sh | bash
```
Windows (PowerShell):
```
irm https://claude.ai/install.ps1 | iex
```
Open a **new** terminal; check with `claude --version`. New to terminals? [Guide](https://code.claude.com/docs/en/terminal-guide), or use the Claude desktop app.

**2. Add Chaky.** Type `claude`, log in, then type:
```
/plugin marketplace add chaklam-silpasuwanchai/research_skill
/plugin install chaky@ask-chaky
```
Restart Claude.

**3. Start.**
```
mkdir my-paper
cd my-paper
claude
```
Say **guide me**. Rough answers are fine. **Coming back?** `cd my-paper`, `claude`, **guide me**. Chaky remembers where you are.

## How Chaky works with you
```
Needs attention: your intro is out of date (you changed the question Tuesday).
Suggested: /update-paper intro (about 20 min). Or: /plan-method pilot
Which one, or something else?
```
- **You pick the skill.** Chaky suggests; it never jumps in on its own.
- **Small changes just happen**, with one line of what changed. Say **undo** to reverse.
- **Big things wait for your yes:** deleting files, freezing the plan, pushing, participants, money, free AI chats, submitting.
- **Everything stays in sync:** tasks, files, and paper update after every task.
- **Aim any skill:** `/update-paper abstract`, `/plan-method IV`.

## Which skill when?
Not sure? Just say **guide me**.

| When you... | Use | What happens |
|---|---|---|
| are lost | `/guide-me` | Where you are, what needs you, and which skill helps now |
| want to know what your tasks are | `/update-board` | A recap, then your to-do list: missing tasks added, extras dropped, priorities set |
| are confused by what the AI said | `/clarify` | The bottom line, what needs you, and one example from your project |
| don't know enough to follow what the AI said | `/teach-me <topic>` | Small steps, a quick check after each, then you do it for real |
| think the AI isn't thinking in enough ways | `/think-deeply-and-learn-from-other-papers` | Every angle, 2-3 different paths, then one clear recommendation |
| want the AI to get your feedback | `/brain-dump` | It asks you one question at a time and saves your answers |
| suspect something (has someone done this? is it new?) | `/read-papers <idea>` | Reads the 10-15 closest papers: what to copy, your one difference, novel and valid? |
| plan to try something | `/plan-method` | A fair experiment and the right tools, learned from 5-15 close papers; then pilot and run |
| want to write | `/update-paper` | First your story (background and key papers, problem, solution, findings), with alternative storylines if you're unsure; then the sections |
| want reviewers' opinions | `/review` | Three reviewers and a meta-review, every citation checked, improvements split into easy and difficult |
| feel the AI doesn't write like you | `/setup-writing-style` | Learns from a paragraph, past papers, emails, or blogs, and confirms the terms you'll use |
| want your repo tidy and up to date | `/update-repo` | Updates all the docs and cleans up clutter (asks before moving or deleting) |
| want the AI to always talk simply, in your language | `/speak-plainly Thai` | Every answer from then on: what needs you first, plain words, your terms, examples |

```
Read: 12 closest papers
Borrow: within-subjects design · trust scale (Lee 2023) · n≈24
One difference: we test admitting limits, not just being accurate
Novel ✅  Valid ❓ no trust scale yet
Next: /plan-method DV
```

**A typical journey:** `/update-repo` → `/brain-dump` → `/read-papers` → `/plan-method` → pilot and run → `/update-paper` → `/review` → `/update-paper response`. Jump around any time.

More: [cheat sheet](docs/cheatsheet.md) · [how it works](docs/how-it-works.md) · [example project](examples/honest-sales-agent).

## Good habits
- Small rounds: rough first, polish later.
- API keys go in `.env`; never paste participant data into free AI chats.
- CHI: ethics approval before recruiting.
- New task? Type `/clear`, then **guide me**. Chaky's files remember everything.

## Something wrong?
| Problem | Try this |
|---|---|
| `claude: command not found` | Open a new terminal; run `claude doctor` |
| "guide me" does nothing | Restart Claude; type `/` and look for the skills |
| Chaky forgot what we did | Say **guide me**; it re-reads your project files |
| Hit a usage limit | Wait for the reset; work in smaller rounds |

**Update Chaky:** `/plugin marketplace update ask-chaky`, then `/plugin update chaky@ask-chaky`, then restart.
**No plugin support?** Copy the folders in `plugins/chaky/skills/` into `~/.claude/skills/` and restart. Codex works the same way with its own skills folder.
**Your paper as a PDF:** upload `paper/` to [Overleaf](https://www.overleaf.com).

## More
Changes: `CHANGELOG.md` · Labs and maintainers: `MAINTAINERS.md` · Problems or ideas: open an issue · License: MIT · Cite: `CITATION.cff`.

## Credits
Chaky stands on good ideas from others, rewritten in our own words:
- [Kalaris Labs' research agent skills](https://github.com/KalarisLabs/research-agent-skills) and [Orchestra Research's AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs): broad research skill collections. They are large; Chaky keeps a small set that students can remember.
- [Feynman](https://github.com/companion-inc/feynman): consensus, disagreements, and open questions in literature reviews; a source trail; checking a paper against its code; replicating before building.
- [Matt Pocock's skills](https://github.com/mattpocock/skills) (MIT): grill-me, wayfinder, and retro inspired `brain-dump`, `update-board`, and the retro mode.
- The [AIT Brain Lab research guide](https://ait-brainlab.github.io/researchguide/): the five research stages, lab terms, contribution types, and the one-page idea outline.
