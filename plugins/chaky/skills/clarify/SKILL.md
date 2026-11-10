---
name: clarify
description: Rewrites a hard-to-read AI answer (the last message, or text you paste) in plain words - what it means for you, what needs your attention, what to do next - without adding or dropping facts. Use for "clarify", "say that simply", "I don't understand", "too technical", or "what does this mean for me".
---

# Clarify

The researcher got an answer that is too long, too technical, or full of code talk. Turn it into something they can read in under a minute. Works with or without a paper project.

## What to clarify
- Default: **your last message** in this conversation.
- Text they paste or name ("clarify the review", "clarify that error") → that.
- Unsure which → ask once.

## How to write it
1. **What it means for you** (one or two sentences). The bottom line first.
2. **Needs your attention** (only if something does): decisions, blockers, risks. At most three, each one line. Nothing needed → say "Nothing needs you right now."
3. **What happened, in short**: at most five bullets in everyday words. Code changes become one plain sentence each ("the test set no longer leaks into training"), never diffs, file lists, or code.
4. **Next:** one step, as a suggestion they can take or ignore.

## Rules
- **Same facts, fewer words.** Don't add claims, numbers, or advice the original didn't have; don't drop a warning or a decision. If the original was wrong or unclear, say so instead of smoothing it over.
- **Their words.** Use the terms in `components/terms.md` (if it exists) and the words they use in chat. Swap jargon for everyday words; if a technical word must stay, explain it in one line with an example.
- **Short sentences**, no headings longer than the content, no tables unless comparing options.
- Explain in the language they chose (`AGENTS.md`); keep file names and code identifiers as they are.
- End with "Want more detail on any part?" Only expand the part they ask about.
