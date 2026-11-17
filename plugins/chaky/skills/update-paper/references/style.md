# Style (used by `update-paper` on every section)

**Their voice first.** Match `components/voice.md` (sentence length, tense, signal words, hedging, what to keep) and use `terms.md` words exactly. These rules below never override their voice; they fix only what voice.md says to fix.

**Plain English, like the venue.** Write in plain English that reads like a well-written paper at the target venue.

**Terms where they're needed, never a glossary.** Never add a separate "Terms" or glossary section. Introduce each term where the reader first needs it, inside a natural sentence. The best place is usually a short **walk-through of one interaction** at the start of the method, where each term appears as part of the story with a concrete example from this study ("A customer asks whether the blender is dishwasher-safe; the agent's *answer* includes a *disclosure*, a sentence that states a limit of the product"). After that, the term means only that and is spelled the same way in the text, tables, captions, and appendix. Say everything else in everyday words: never add a new label, abbreviation, internal code, or field jargon.

**Answer the reviewer's "what?" and "why?" on the spot.** Wherever a skeptical reviewer would stop and ask "what does this mean?" or "why?", add one short example or reason right there. A definition must answer a question, not raise a new one; if it needs explaining, rewrite it more simply.

**Skeptical-reviewer pass (before showing any edit).** Write only what a skeptical reviewer needs to be convinced. Reread every sentence, table, and caption as that reviewer and cut anything that invites a question instead of answering one:
- no defensive filler ("Nothing else.", "Nothing else changes.")
- no side justifications ("as regulations require")
- no borrowed terms the reader would have to ask about ("positive control")
- no second sentence when one is enough

**One name per thing.** Each condition, variant, measure, and component has exactly one name, identical in every table, caption, figure, and section, and matching `terms.md`. No internal codes (variant letters, file names). Before showing an edit, search the whole paper for each name and fix every mismatch, and check that every term is defined before its first use and used the same way everywhere. A description uses the same words as the names it explains: if a variant is "No look-ahead", the main method's description mentions look-ahead.

**Say only what's necessary.** Writing everything is not the best way. Every extra detail is one more thing a reviewer must think about, question, or attack. Keep a sentence only if the reader needs it to understand or believe the story. Each detail must support the contribution, the method's validity, or replication; otherwise cut it, or move it to the appendix or supplement. No side results that don't serve the story, no listing everything you tried, no defending against objections nobody raised, no tutorials for experts. When in doubt, cut, then check the story still holds.

**Paragraphs:** one idea each, strong opening and ending sentence. Open with a signal ("This paper proposes...", "However, ...") that sets the tone. Make the link to the previous paragraph visible.

**Sentences and words:** strong verbs ("shows", "rules out", not "is related to"); neither too short nor too long, split when a sentence carries two ideas; words with one meaning ("good" → better on what, by how much); the same term for the same concept (`components/terms.md`); define terms and abbreviations before use; no empty sentences like "Our work is new."

**Elements of style** (after Strunk and White, *The Elements of Style*):
- **Omit needless words.** "the fact that", "it is important to note that", "in order to" → cut. A sentence has no unnecessary words, a paragraph no unnecessary sentences.
- **Active voice** by default: "We measured trust", not "Trust was measured". Use passive only when the actor doesn't matter (methods details), or when `voice.md` says so.
- **Positive form:** "rarely", not "not often"; "ignored", not "did not pay attention to". Say what is, not what isn't.
- **Definite, specific, concrete:** "accuracy rose from 71% to 84%", not "performance improved considerably".
- **Parallel form** for parallel ideas: "we measure trust, recall, and purchase intention", not "we measure trust, how well they recall, and whether they intend to buy".
- **Keep related words together:** put the subject near its verb and a modifier next to the word it modifies.
- **Emphatic words at the end** of the sentence: end on the finding, not on the citation or the hedge.
- **One tense per section:** present for what the paper shows and claims; past for what we did and found in the study.
- **Don't overstate, don't over-qualify:** one hedge per claim is enough ("suggests"), not "may possibly suggest".

**Evidence:** every sentence backed by a citation, result, or argument; no claim without it. Say which results are **surprising** and which **expected**; don't mix them. Verb strength matches evidence strength ("shows" / "suggests" / "is consistent with"). Numbers with units, sample sizes, uncertainty.

**Final pass:** cut empty words (very, quite, in order to). Read the first sentence of each paragraph in a row; they should tell the story. Captions make sense alone. Read aloud and fix what you trip on.
