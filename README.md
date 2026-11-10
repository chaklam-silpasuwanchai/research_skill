# Chaky: your AI research partner (v0.2.0)

Chaky helps you go from a rough idea to a submitted paper (CHI, ACL, NeurIPS style). **You lead. Chaky suggests, keeps you organized, and does the busy work.**

You only need to remember one phrase: **"guide me"**.

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
Open a **new** terminal and check: `claude --version`. New to the terminal? See the [terminal guide](https://code.claude.com/docs/en/terminal-guide), or use the Claude desktop app.

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
Say **guide me**. Chaky asks a few short questions and sets up your project. Rough answers are fine.

**Coming back later?** `cd my-paper`, run `claude`, say **guide me**. Chaky remembers where you are.

## How Chaky talks to you
Short, plain, and it always ends with a choice for you:
```
Needs attention: your intro is out of date (you changed the question Tuesday).
Top tasks: try two pilot versions · decide participant count · plan the analysis
Suggested: /write intro (about 20 min). Or: /plan-method pilot
Which one, or something else?
```
- **You pick the skill.** Chaky never jumps into one on its own.
- **Small changes just happen.** Chaky makes the change, tells you in one line, and you can say **undo**.
- **Big things wait for your yes:** deleting or moving files, freezing your study plan, pushing to GitHub, anything with participants or ethics, spending money, pasting data into free AI chats, submitting.
- **You can aim any skill:** add a focus after the name, like `/write abstract` or `/plan-method IV`.

## Which skill when? (by situation)

**"I'm starting a new paper."**
→ `/setup-repo chi` (or `nlp`). Folders, git, the venue's LaTeX template, and a to-do board.
→ Then `/brain-dump`. Chaky asks one question at a time and writes down your idea.
→ Have past papers? `/setup-writing-style` so drafts sound like you.

**"I have an idea, but is it any good?"**
→ `/validate-idea agents that admit what they don't know`
```
Novel ✅  closest: Smith 2024 tested trust, not admitting limits
Valid ❓  you haven't picked a trust scale yet
Next: /plan-method DV
```

**"What has been done already? Am I scooped?"**
→ `/find-papers honest sales agents`. You get the closest papers, how you differ, and methods you can borrow. Found a paper yourself? Say **I found a paper** and paste the link.

**"How do I design my study?"**
→ `/plan-method`. It covers what you change (IV), what you measure (DV), who takes part, how many, the order of conditions, and the analysis. Do one part at a time with `/plan-method IV` or `/plan-method sample size`. Then pilot, freeze the plan, and run.

**"I need to use AI models in my study."**
→ `/setup-llms openrouter`, `/setup-llms local`, or `/setup-llms labeling` (free AI chats to label data).

**"Time to write."**
→ `/write abstract`, `/write intro`, `/write results`, and so on. It writes in your voice, adds honest stats and figures, and removes AI-sounding phrases. Want the whole draft at once? Say **fast mode**.

**"Is my paper ready?"**
→ `/review`. Chaky reviews like a tough reviewer at your venue and checks every citation.
```
Novelty   3.5/5  ✅ closest work named   ❌ why it matters unclear
Citations        ✅ 41 ok  ❌ 2 not found  🔧 1 wrong year
Fix first: why it matters → /write intro
```
Before the deadline: `/review submit`.

**"I've lost track of what to do."**
→ `/check-board`. A short recap, then your to-do list fixed up: forgotten tasks added, unneeded ones dropped, priorities set, names made plain.

**"I'm not happy with what the AI proposed."**
→ `/think-deeply`. Chaky looks from every side (reviewer, participant, advisor, skeptic), explores 2-3 different paths, and tells you which looks best.

**"The AI is too technical. I need context or an example."**
→ `/clarify`. You get the bottom line, what needs you, and one example from your project.
→ Still lost? `/teach-me power analysis`. One small step at a time, with a quick check after each.

**"I keep telling Chaky the same thing."**
→ Say **always do X**. `remember-this` makes it a permanent rule.

## All skills: use it when...
| Skill | Use it when... | Try |
|---|---|---|
| `guide-me` | you feel lost and want to know which skill is useful right now | "guide me" |
| `setup-repo` | you are at the very beginning, or your project folder is a mess | /setup-repo chi |
| `setup-writing-style` | you want drafts to sound like you, not like an AI | "learn my writing style" |
| `setup-llms` | your study needs AI models: OpenRouter, a local model, or free AI chats for labeling | /setup-llms local |
| `brain-dump` | the idea is in your head but not on paper yet, at any stage | /brain-dump |
| `check-board` | you've lost track of tasks, or the to-do list feels wrong or messy | /check-board |
| `validate-idea` | you have an idea (or a draft) and want to know if it's novel, valid, and worth a paper | /validate-idea <idea> |
| `find-papers` | you need the closest work, want to double-check novelty, or want a method to borrow | /find-papers <topic> |
| `plan-method` | you need to decide what to change and measure, who takes part, how many, and how to run it | /plan-method IV |
| `write` | you need a section written or rewritten, a stats test, a figure, or less AI-sounding text | /write abstract |
| `review` | you want a tough reviewer's opinion and every citation checked before you share or submit | /review |
| `think-deeply` | you're not satisfied with what the AI proposed and want it to explore different possible paths | /think-deeply |
| `clarify` | the AI spoke too technically, or you want more context or an example | /clarify |
| `teach-me` | clarify wasn't enough and you want to be walked through it step by step | /teach-me <topic> |
| `remember-this` | you keep telling Chaky the same thing and want it to stick | "always do X" |

Printable list: [cheat sheet](docs/cheatsheet.md). How the skills connect: [how it works](docs/how-it-works.md). A project a few weeks in: [`examples/honest-sales-agent`](examples/honest-sales-agent).

## Good habits
- Small rounds. Rough first, polish later.
- Keep API keys in `.env`. Chaky sets up a guard that stops secrets and participant data from being committed.
- Never paste participant data into free AI chats.
- CHI studies: record ethics approval before recruiting.
- Prefer another language? Tell Chaky. Your paper stays in English.
- Starting a new task? Type `/clear`, then **guide me**. Chaky's files remember everything.

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

`brain-dump`, `check-board`, and the retro mode are inspired by [Matt Pocock's grill-me, wayfinder, and retro](https://github.com/mattpocock/skills) (MIT). Some ideas come from [Orchestra Research's AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) (MIT), rewritten in our own words.
