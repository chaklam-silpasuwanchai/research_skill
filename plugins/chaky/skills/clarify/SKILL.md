---
name: clarify
description: Rewrites an AI answer you found hard to follow - too technical, no example, missing context, too long - in plain words - what was done, what it means for you, what needs your attention, with an example - without changing the facts. Use for "clarify", "say that simply", "I don't understand", "too technical", "give me an example", or /clarify.
---

# Clarify

Default: your last message. Focus: a part, or pasted text.

```
In short: <what it means for you, 1-2 sentences>
What was done: <≤ 5 plain bullets; code changes as one sentence each, no diffs>
Needs you: <≤ 3 decisions or risks, or "Nothing right now">
Example: <one concrete example from their project>
Why it matters: <1 line, only if the original assumed context>
Next: <one suggested step>
```

- **Same facts, fewer words.** Add nothing, drop no warning or decision. If the original was wrong, say so.
- **Their words** (`terms.md`); jargon swapped for everyday words or explained in one line.
- End with "Want more on any part?" Still lost → suggest `teach-me`.
