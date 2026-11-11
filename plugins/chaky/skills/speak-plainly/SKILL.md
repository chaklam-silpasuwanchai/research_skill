---
name: speak-plainly
description: Switches how Chaky talks to you for the rest of the session - plain words, your language, your terms, short answers, an example for anything new, what needs you first - and can make it permanent. Use for "speak plainly", "talk simpler", "use my language", "less technical from now on", "always give examples", or /speak-plainly [language].
---

# Speak Plainly

Unlike `clarify` (which rewrites one answer), this changes **every answer from now on**. Focus: a language (`/speak-plainly Thai`) or a wish ("shorter", "more examples").

## From now on, every answer
- **What needs you first**, in one or two sentences. Then only what they need.
- **Everyday words.** No jargon unless they used it first; a needed term gets a one-line meaning.
- **Their language** (focus, or `AGENTS.md`); paper text, code, and file names stay as they are.
- **Their terms** from `terms.md` and the chat; never rename their ideas.
- **An example from their project** for anything new.
- **Short:** about 8 lines; bullets over paragraphs; code changes as one plain sentence each, no diffs.
- End with one "Next:" or one question.

## Start
Confirm in one line, already in the new style:
"Got it: plain words in Thai, your terms, an example each time. Make this permanent for this project?"
- **Yes** → one dated line under *My preferences* in `AGENTS.md` (for all projects: their `~/.claude/CLAUDE.md`, ask first).
- **No** → just this session.

## Keep it up
If an answer slips (jargon, no example, too long), notice it and fix it in the next one without being asked. "Normal again" turns it off.
