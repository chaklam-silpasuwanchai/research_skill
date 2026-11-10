# Chaky: your AI research partner (v0.1.0)

Chaky guides you from a rough idea to a submitted paper (CHI, ACL, NeurIPS style). It sets up your project, helps you find a real research gap, plans your study, writes with you, reviews like a tough reviewer, and checks everything before you submit. **You stay in charge. Chaky keeps you organized.**

You only ever need one phrase: **"guide me"** ("ask Chaky" works too). You lead; Chaky suggests.

## Before you start (5 checks)
- [ ] A paid Claude plan (Pro or higher)
- [ ] A computer with macOS, Windows 10+, or Linux
- [ ] Git installed. Check with `git --version`. Mac offers to install it; Windows: https://git-scm.com/downloads/win
- [ ] An empty folder for your paper
- [ ] About 15 minutes

## Step 1. Install Claude Code (once)
**Mac, Linux, or WSL** (Terminal):
```
curl -fsSL https://claude.ai/install.sh | bash
```
**Windows** (PowerShell):
```
irm https://claude.ai/install.ps1 | iex
```
Open a **new** terminal window and check it worked:
```
claude --version
```
New to the terminal? Read the [terminal guide](https://code.claude.com/docs/en/terminal-guide). Prefer no terminal? The Claude desktop app includes Claude Code ([details](https://code.claude.com/docs/en/overview)).

## Step 2. Add Chaky (once)
Type `claude` and press Enter. Log in the first time. Then type these two lines inside Claude:
```
/plugin marketplace add chaklam-silpasuwanchai/research_skill
/plugin install chaky@ask-chaky
```
Quit Claude and start it again with `claude`.

**Lazy way:** paste this into Claude instead:
> Read https://raw.githubusercontent.com/chaklam-silpasuwanchai/research_skill/main/WELCOME.md and follow it.

## Step 3. Start your paper
In your Terminal or PowerShell:
```
mkdir my-paper
cd my-paper
claude
```
Then say:
> **guide me**

Chaky asks a few short questions (paper style, venue, GitHub or local, your past papers), then sets up your project folder. Answer roughly; you can fix things later.

## Every time you come back
Open the terminal, `cd my-paper`, run `claude`, and say **"guide me"**. Chaky reads your project, tells you where you are, and suggests what could come next; you choose.

## Things you can say
*guide me* · *what can you do?* · *show my progress* · *I found a new paper* · *I want to try X* · *quick review* · *help me label data* · *any new papers on my topic?* · *help me code this reliably* · *show the board* · *let me lead* · *you drive* · *retro* · *grill me* · *think deeply* · *clarify* · *clean up my tickets* · *unslop this* · *progress update* (for your advisor) · *fast mode* · *always do X* · *I'm lost*

## What Chaky helps with
Say **"guide me"** and Chaky suggests a skill; you pick. You can also name one yourself. (Full list with example phrases: [`guide-me/references/skills.md`](plugins/chaky/skills/guide-me/references/skills.md).)
| Skill | In plain English |
|---|---|
| `guide-me` | Start here: what needs attention, which skill could help next (you choose), progress, advisor update, retro |
| `start-paper` | Interviews you, sets up your project, learns your voice, makes your board |
| `plan-tickets` | Your board: tickets, 1-5 priorities, "done when", assist or lead mode |
| `shape-idea` | Finds and sharpens a publishable idea |
| `tidy-board` | Cleans up the board: re-checks priorities, drops or merges tasks, renames them in plain words |
| `grill-me` | Asks one question at a time to stress-test an idea, plan, or argument |
| `run-study` | Plans and runs your study; freezes the plan; reflects |
| `write-paper` | Writes the paper with you |
| `review-paper` | Tough reviewer (quick or full) and the submission check |
| `find-papers` | Finds papers, watches for overlaps, handles a new paper you found |
| `polish-prose` | Clear writing in your voice; removes robotic AI phrasing |
| `analyze-results` | Statistics and honest figures |
| `write-code` | Tested, reproducible research code |
| `use-llms` | Which models to use; free-chat labeling and outside reviews |
| `think-deeply` | Is there a better solution? Challenges the latest idea with first principles, assumptions, depth, systems thinking |
| `clarify` | Rewrites a hard-to-read AI answer in plain words: what it means, what needs your attention |
| `teach-chaky` | Makes repeated instructions permanent; adds skills |

**How you work:** Chaky keeps a **board** (`components/tickets.md`) of tickets, each with a 1-5 priority (Chaky sets it; you can change it) and a "done when". You always choose what happens next. Say **"let me lead"** to see your top tasks and pick, or **"you drive"** to have Chaky suggest one each time. Not a waterfall: new ideas, papers, and review fixes become tickets any time.

## New to Chaky? See an example
Look at [`examples/honest-sales-agent`](examples/honest-sales-agent) to see a project a few rounds in, and print the [cheat sheet](docs/cheatsheet.md). [How it works](docs/how-it-works.md) shows how the skills connect.

## Good habits
- Work in small rounds. Rough first, polish later.
- Keep secrets (API keys) in `.env`, never in git. Chaky sets this up and offers a guard that blocks secrets, consent forms, recordings, and participant data from being committed.
- Prefer another language? Tell Chaky which one to explain in; your paper stays English.
- Record ethics approval before recruiting participants (CHI-style projects).
- Never paste participant data or confidential material into free web chats.
- Before you stop, let Chaky finish: it logs what you decided and updates your paper.

## Writing in LaTeX
Your paper lives in the `paper/` folder (official template). To make a PDF, upload the folder to [Overleaf](https://www.overleaf.com), or install a LaTeX distribution on your computer.

## Something wrong?
| Problem | Try this |
|---|---|
| `claude: command not found` | Close and reopen the terminal. Run `claude doctor` |
| `/plugin` isn't recognized | Update Claude Code and restart it |
| "guide me" does nothing | Restart Claude. Type `/chaky` and see if skills appear. Otherwise use the fallback below |
| `git` not found | Install Git (see the checklist above) |
| Chaky forgot what we did | Say "guide me"; it re-reads `components/current_status.md` |
| Hit a usage limit | Wait for the reset. Long sessions use more, so start with small pilots |

**Fallback (no plugin):** download this repo, then copy every folder inside `plugins/chaky/skills/` into `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`), and restart Claude.

**Update Chaky:** `/plugin marketplace update ask-chaky`, then restart.

Using Codex instead? Same idea; check the Codex docs for its plugin commands, or use the fallback folder copy.

## More
Version history: `CHANGELOG.md`. Labs and maintainers: `MAINTAINERS.md`. Found a problem or have an idea? Open an issue (the forms guide you). License: MIT. To cite Chaky, see `CITATION.cff`.

`grill-me`, `plan-tickets`, and the retro mode are inspired by [Matt Pocock's grill-me, wayfinder, and retro](https://github.com/mattpocock/skills) (MIT). Some ideas were inspired by [Orchestra Research's AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) (MIT license) and rewritten in our own words.
