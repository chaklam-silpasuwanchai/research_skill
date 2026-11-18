# Writing (used by `update-paper` on every edit; the one home for writing rules)

**Their voice first.** Match `components/voice.md` and use `terms.md` words exactly. These rules fix only what `voice.md` doesn't already decide.

## 1. Plain English, like the venue
Write in plain English that reads like a well-written paper at the target venue. Say everything in everyday words; never add a new label, abbreviation, internal code, or field jargon.

## 2. Coherence
One story from title to conclusion (the agreed story in `current_status.md`). Each paragraph has one idea, opens with a signal ("However, ..."), and links visibly to the one before. Read the first sentences in a row: they should tell the story. Story, terms, numbers, and claims agree across every section; the introduction's promises are all delivered.

## 3. Consistent terms
- **No glossary section.** Introduce each term where the reader first needs it, inside a natural sentence; ideally in a short **walk-through of one interaction** at the start of the method, with a concrete example ("A customer asks whether the blender is dishwasher-safe; the agent's *answer* includes a *disclosure*, a sentence that states a limit of the product").
- **One name per thing:** each condition, variant, measure, and component has one name, identical in every table, caption, figure, section, and appendix, matching `terms.md`. No internal codes. Descriptions use the same words as the names they explain (a variant "No look-ahead" → the main method's description mentions look-ahead).

## 4. Don't invite questions
Write only what a skeptical reviewer needs to be convinced.
- Wherever they would ask "what does this mean?" or "why?", add one short example or reason right there. A definition answers a question; if it needs explaining, rewrite it more simply.
- Cut anything that raises a question instead: defensive filler ("Nothing else changes."), side justifications ("as regulations require"), borrowed terms ("positive control"), a second sentence when one is enough.
- **Say only what's necessary.** Keep a detail only if it supports the contribution, validity, or replication; otherwise cut it or move it to the appendix. No side results, no list of everything tried, no defending against objections nobody raised, no tutorials for experts.

## 5. Elements of style (after Strunk and White)
Omit needless words ("the fact that", "in order to", "very"). Active voice by default ("We measured trust"). Positive form ("rarely", not "not often"). Definite and concrete ("accuracy rose from 71% to 84%"). Parallel form for parallel ideas. Subject near its verb. End the sentence on the finding. Present tense for what the paper shows, past for what the study did. One hedge per claim. Strong verbs ("shows", "rules out", not "is related to"), matched to the evidence ("shows" / "suggests" / "is consistent with").

## 6. Evidence
Every claim backed by a citation, result, or argument. Say which results are surprising and which expected. Numbers with units, n, and uncertainty.

## Before showing any edit
1. Reread every sentence, table, and caption as a skeptical reviewer (section 4).
2. Search the whole paper for each name: defined before first use, spelled the same everywhere (section 3).
3. Check coherence with the rest of the paper (section 2).
4. Run the unslop pass (`unslop.md`, `patterns.md`), keeping every claim, number, and citation.
