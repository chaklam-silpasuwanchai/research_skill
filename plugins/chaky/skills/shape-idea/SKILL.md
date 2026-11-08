---
name: shape-idea
description: Turns a rough interest into a narrow, novel, publishable research question and drafts the title, abstract, introduction, and related work. Use to find or sharpen a research idea, define hypotheses, or check novelty.
---

# Shape Idea

A good idea is a real **research gap in the field**, not the researcher's knowledge gap, and it must be publishable at the venue.
**Needs:** repo from `start-paper` and a known venue. A rough interest is enough to begin.
**Calls:** `find-papers`, `grill-me`, `polish-prose`, `analyze-results` (for Figure 1). Fallbacks below.

## Entry
Follow `AGENTS.md` (none → offer `start-paper`, adopt mode if the user has files). If a need above is missing, don't block: offer to run the earlier skill, do a quick catch-up, or continue and log an assumption. Finish with the end-of-task routine in `AGENTS.md`.

## 1. Announce
"We're in the **idea generation** phase. Everything we discuss becomes a first draft of the paper, starting with the abstract and introduction. Rough is fine." Update `terms.md`, `ideas.md`, `related_work.md`, `experimental_design.md` as you talk.

## 2. Draw out the idea (one question at a time; rough answers welcome)
1. What domain or thing interests you? (e.g. *I want to create an honest sales agent*)
2. What are you curious about? Ask 2-3 questions (e.g. *what counts as honest? what benchmarks exist? does AI lie?*)
3. What are your rough hypotheses? (e.g. *agents that admit uncertainty are trusted more*)
4. Any related paper you love or that feels very close? (Fine if none.)

## 3. Map the landscape
Use `find-papers`. Fallback: find 5-10 recent (3-4 years) papers from top venues, from different positioning angles, trying nearby terms and following citations both ways. Give the user links, then explain for the closest ones: problem, IV, DV, what's done, what can be extended, what's unanswered, how the question could be tightened. Only verified papers go in `related_work.md`.

## 4. Sharpen together
Offer several alternatives; sometimes propose, sometimes ask the user to revise. The thinking is theirs. Core tools: **first principles**, **challenge assumptions**, **systems thinking**, **second-order thinking**, **borrow a classic theory**, and **narrow, don't widen** ("smallest version that is still a real finding?"). When the idea feels fuzzy, run `grill-me` (idea tree). When stuck or starting cold, use 2-3 lenses from `references/idea-lenses.md` (problem-first vs solution-first, abstraction ladder, what changed, resolve a tension, and more). Log chosen and rejected options in `log.md`.

Gap test: Already answered? Is "nobody did it" the only reason? Gap in the field, or just unread? Can a reviewer see the contribution in one sentence?

## 5. Loop question <-> papers
Alternate refining and checking, reaching about **20-30 papers**: enough to see the landscape and what's open, not a flood. Go deeper, not broader. Update components as the question moves.

## 6. Draft the paper
In `paper/`: title, abstract, introduction, related work (rough but coherent; `polish-prose`, or: one idea per paragraph, signal the gap with "However", back every claim). Ask the user to read and comment; revise until they're happy.

## 7. Outside novelty check
Use `use-llms` (novelty prompt, ideation stage): the user pastes the draft into free Gemini, Claude, or ChatGPT chats and brings back their reviews. Fallback: ask another AI to check novelty against named closest papers and list concrete changes. Verify every paper it names, then ask **one question at a time**: what do you think, what can be revised?

## 8. Close the round
Update all components and the draft (title, abstract, introduction, related work). Log decisions, rejected ideas, and dead ends in `log.md`. Ask for anything missing. Say it's ready for `run-study` and that coming back is fine.

## Loop-backs here
Pilot contradicts the hypothesis or idea already done → steps 4-5. Reviewer flags novelty → steps 4-5. Vague question while writing → steps 2-4.
