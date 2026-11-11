# Chaky: your AI research partner (v0.9.0)

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
Suggested: /write intro (about 20 min). Or: /plan-method pilot
Which one, or something else?
```
- **You pick the skill.** Chaky suggests; it never jumps in on its own.
- **Small changes just happen**, with one line of what changed. Say **undo** to reverse.
- **Big things wait for your yes:** deleting files, freezing the plan, pushing, participants, money, free AI chats, submitting.
- **Everything stays in sync:** tasks, files, and paper update after every task.
- **Aim any skill:** `/write abstract`, `/plan-method IV`.

## Stuck? Find your moment
Not sure? Just say **guide me**. Or find the sentence that sounds like you:

### 🌱 Getting started
| You're thinking... | Try |
|---|---|
| "I have a topic, but I don't know where to begin." | `/update-repo chi` (or `nlp`), then `/brain-dump` |
| "It's all in my head. I can't get it onto paper." | `/brain-dump`: one question at a time, with a suggested answer each time |
| "My drafts sound like ChatGPT, not like me." | `/setup-writing-style` with a past paper, then `/write polish` |

### 📚 Ideas and papers
| You're thinking... | Try |
|---|---|
| "Is my idea even new? What if someone already did it?" | `/find-papers <topic>`, then `/read-papers <idea>` |
| "I just found a paper that looks exactly like mine. Help!" | Say **I found a paper** and paste the link. Overlap is a level, not a verdict. |
| "How do other people run this kind of study?" | `/read-papers`: what to copy from the 10-15 closest papers, and your **one** difference |

```
Borrow: within-subjects design · trust scale (Lee 2023) · n≈24
One difference: we test admitting limits, not just being accurate
Novel ✅  Valid ❓ no trust scale chosen yet
Next: /plan-method DV
```

### 🧪 Planning and running the study
| You're thinking... | Try |
|---|---|
| "What's my IV and DV? How many participants do I need?" | `/plan-method IV`, `/plan-method sample size` |
| "I need AI models, but I don't know the setup or the cost." | `/plan-method models` (OpenRouter or a local model) |
| "Labeling 2,000 examples by hand is impossible." | `/plan-method labeling` (free AI chats, humans only at the end) |
| "My results don't match my hypothesis." | `/think-deeply`, or `/read-papers` to re-check. Dead ends count as progress. |

### ✍️ Writing
| You're thinking... | Try |
|---|---|
| "I'm staring at a blank page." | `/write intro` (or `abstract`, `method`, `results`...) |
| "Which statistical test? Is this figure honest?" | `/write stats`, `/write figure` |
| "I don't know what to say in limitations." | `/write limitations`: real threats from your own notes, no filler |

### 🚀 Submitting and reviews
| You're thinking... | Try |
|---|---|
| "Is this good enough to submit?" | `/review`: three reviewers, a meta-review, and every citation checked |
| "The deadline is in 3 days." | `/review submit`: blockers first, then should-fix |
| "The reviews came back and they hurt." | Paste them, then `/write response`. One point at a time, most important first. |


### 🧭 Staying on track
| You're thinking... | Try |
|---|---|
| "I'm back after two weeks and I forgot everything." | **guide me**: where you are and what's next, in about 5 lines |
| "Too many tasks. I don't know what to do first." | `/update-board`: recap, forgotten tasks added, extras dropped, priorities set |
| "My files and paper are behind my latest results." | `/update-repo`: everything brought in line; prose that needs rewriting is marked ⚠ |
| "Advisor meeting tomorrow." | Say **progress update**: one page with what's done, results, and decisions needed |

### 💬 When the AI isn't helping
| You're thinking... | Try |
|---|---|
| "That was too technical. What does it mean for me?" | `/clarify`: the bottom line, what needs you, one example |
| "I still don't get it." | `/teach-me <topic>`: small steps with a quick check after each |
| "Please always talk simply, in my language." | `/speak-plainly Thai` (or any language), from now on |
| "I don't like what the AI proposed. Is there a better way?" | `/think-deeply`: every angle, 2-3 paths, then one clear recommendation |
| "I keep telling Chaky the same thing." | Say **always do X**. It becomes a permanent rule. |

### A typical journey
`/update-repo` → `/brain-dump` → `/find-papers` → `/read-papers` → `/plan-method` → pilot and run → `/write` → `/review` → `/write response`. You can jump around any time; **guide me** always knows where you are.

## All 14 skills
`guide-me` lost? start here · `update-repo` set up or bring up to date · `setup-writing-style` your voice · `brain-dump` get it out of your head · `update-board` your to-do list · `find-papers` search the field · `read-papers` closest 10-15, what to copy, your one difference · `plan-method` design and run the study · `write` any section, stats, figures · `review` tough panel plus citations · `think-deeply` a better path? · `clarify` say that simply · `teach-me` step by step · `speak-plainly` always simple, your language

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

`brain-dump`, `update-board`, and the retro mode are inspired by [Matt Pocock's grill-me, wayfinder, and retro](https://github.com/mattpocock/skills) (MIT). Some ideas come from [Orchestra Research's AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) (MIT), rewritten in our own words.
