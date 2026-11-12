# My personal research skill (v0.22.1)

I have recently tried out Claude Code for my research, and developed several key skills after many months of trial and error.   Hopefully this skill can help you as well in your research journey.   For your information, I have published in top venues like CHI and ACL, so you can trust me a little bit :P

## The skill mindset
1. **Everything revolves around tickets and priorities.** I found it extremely difficult to keep track of all the things I need to do, especially when AI keeps throwing information at you.   So the first idea revolves around tickets and priorities which can be found in `components/tickets.md`.  It is inspired by agile practices.   You can use `/update-board` to ask AI to check all tasks, reprioritize stuff, so you don't get lost.
2. **You are the main researcher, not AI.** I found AI loves to confuse me when doing research, so I built my skill around the idea that I am the one who drives. For those who know,  there is a very popular skill out there named `autoresearch` which does not suit me very much.   My favorite skill, for example, is `/think-deeply`, which I use when I think AI is not thinking multi-dimensionally or has not read enough papers.   Another favorite skill is a simple `/clarify` which asks AI to speak in plain English, provide enough context, and always give at least one example.   Another one is `/brain-dump` which allows me to tell AI what I am thinking via interviewing.
3. **Define terms early.** It can get very confusing after a few days of talking to AI;  one thing I found extremely useful is agreeing with AI on a set of terms that we work with.  This results in better collaboration with AI,  better writing, and just overall better research.  You can take a look at the initial terms I define for myself:  [`lab-terms.md`](plugins/chaky/skills/update-repo/assets/lab-terms.md). Every project gets the core in `terms.md` and the full list in `components/lab-terms.md`.

## How to set up
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

**2. Install the skill.** Type `claude`, log in, then type:
```
/plugin marketplace add chaklam-silpasuwanchai/research_skill
/plugin install chaky@research_skill
```
Restart Claude.

**3. Inside your terminal, go to your folder and call Claude.**
```
mkdir my-paper
cd my-paper
claude
```
## Which skill when?

This is a cheat sheet.

| When you... | Use | What happens |
|---|---|---|
| are lost | `/guide-me` | Where you are, what needs you, and which skill helps now |
| want to know what your tasks are | `/update-board` | Updates your to-do list |
| are confused by what the AI said | `/clarify` | Explain plainly, with enough context and examples |
| don't know enough to follow what the AI said | `/teach-me <topic>` | Teaches you when `/clarify` does not work, likely due to a knowledge gap |
| think the AI isn't thinking in enough ways | `/think-deeply` | Tries to think differently, and also consults papers |
| want the AI to get your feedback | `/brain-dump` | Asks you one question at a time and saves your answers |
| want to organize your idea (has someone done this? is it new?) | `/update-paper` | Updates your paper, and also consults the 10-15 closest papers: what to copy, your one difference, novel and valid? |
| want to experiment with something | `/plan-method` | Lets AI help plan a fair experiment and the right tools, learned from 5-15 close papers; then pilot and run |
| want reviewers' opinions | `/review` | Three reviewers and a meta-review, every citation checked, a Claude/ChatGPT/Gemini check, improvements split into easy and difficult |
| feel the AI doesn't write like you | `/setup-writing-style` | Learns from your Google Scholar link, past papers, a paragraph, emails, or blogs, and confirms the terms you'll use |
| want your repo tidy and up to date | `/update-repo` | Updates all the docs and cleans up clutter (asks before moving or deleting) |

## Claude mod

I highly recommend installing Claude mods in your terminal or desktop app:

**Simple ticket boards:** Ask your Claude to set up a ticket board in the right pane.
**Cheatsheet skill:** Ask your Claude to list all the available skills you can use, to remind you of the tools you have.

## Credits
This skill stands on good ideas from others:
- [Kalaris Labs' research agent skills](https://github.com/KalarisLabs/research-agent-skills) and [Orchestra Research's AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs): broad research skill collections. They are large; Chaky keeps a small set that students can remember.
- [Feynman](https://github.com/companion-inc/feynman): consensus, disagreements, and open questions in literature reviews; a source trail; checking a paper against its code; replicating before building.
- [Matt Pocock's skills](https://github.com/mattpocock/skills) (MIT): grill-me, wayfinder, and retro inspired `brain-dump`, `update-board`, and the retro mode.
- The [AIT Brain Lab research guide](https://ait-brainlab.github.io/researchguide/): the five research stages, lab terms, contribution types, and the one-page idea outline.
