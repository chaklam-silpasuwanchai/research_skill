---
name: clarify
description: Rewrites an AI answer you found hard to follow - too technical, no examples, missing context, or too long - in plain words - what was done, what it means for you, what needs your attention, with a concrete example - without adding or dropping facts. Use for "clarify", "say that simply", "I don't understand", "too technical", "give me an example", "what does this mean for me", or /clarify.
---

# Clarify

The last answer was too technical, had no example, assumed context the researcher doesn't have, or was too long. Make it readable in under a minute. Works with or without a paper project. Optional focus: `/clarify <the part, or pasted text>`; default is your last message.

## Write it in this shape
1. **In short:** what it means for you, in one or two sentences. Bottom line first.
2. **What was done:** at most five plain bullets. Code changes become one sentence each ("the test set no longer leaks into training"), never diffs, file lists, or code.
3. **Needs your attention:** decisions, blockers, risks; at most three, one line each. Nothing → "Nothing needs you right now."
4. **Example:** one concrete example from their own project for the hardest idea ("Like this: if participant 7 sees the honest agent first, ...").
5. **Context you may be missing:** one or two lines on why it matters or how it connects (only if the original assumed it).
6. **Next:** one step, as a suggestion.

## Rules
- **Same facts, fewer words.** Don't add claims, numbers, or advice the original lacked; don't drop a warning or a decision. If the original was wrong or unclear, say so.
- **Their words.** Use `terms.md` and the words they use in chat. Swap jargon for everyday words; if a technical word must stay, explain it in one line.
- Short sentences. Tables only to compare options. Their explanation language from `AGENTS.md`; file names and code identifiers as they are.
- End with "Want more on any part?" Still lost after that → suggest `teach-me`.
