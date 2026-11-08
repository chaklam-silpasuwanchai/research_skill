# Unslop: remove robotic AI phrasing


## Process
1. **Scan** against `patterns.md` (phrases, structures, rhythm). Count hits per 1,000 words (a literal count, so it is repeatable).
2. **Rewrite.** Keep meaning, claims, citations, numbers, and technical terms exactly. Replace vague with concrete: name the subject, use a strong verb, point to the evidence. Cut filler. Vary sentence length. Match `components/voice.md` and `terms.md`.
3. **Never fix slop by adding claims.** A sentence with no evidence gets `[EVIDENCE?]`, not an invented fact. Keep signal words that mark a real logical turn ("However").
4. **Add soul, honestly.** Prefer what surprised you, what you would do differently, and the specific number over the generic summary line.
5. **Show the change:** hits per 1,000 words before → after, and before/after for the 3 biggest edits. The user approves. In `review-paper` mode, report only; don't rewrite.

## Academic guardrails
- Keep hedges that match the evidence strength; cut stacked ones.
- Don't add first person, humor, or opinions the researcher's voice doesn't use.
- Don't touch quotes, equations, code, URLs, or table contents.
- If the writing is generic because the idea is vague, say so and suggest `grill-me`.
