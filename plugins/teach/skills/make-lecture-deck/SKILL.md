---
name: make-lecture-deck
description: Builds and revises lecture or workshop slide decks the way Dr. Chaklam wants them - plain English, low cognitive load, a map per part, big visuals, a source on every claim, interesting real cases, and a hands-on workshop at the end - and works through his slide comments one by one. Use for "make a lecture", "redesign my slides", "build a deck for professionals", "handle my comments on the deck", or /make-lecture-deck.
---

# Make a Lecture Deck

Chaklam's lectures are for busy professionals and executives. The deck has to teach in plain words, make the point at a glance, and leave people with something they can use on Monday. Everything below comes from many rounds of his feedback: follow it from the first draft, so he doesn't have to comment on it again.

## 1. Settle the shape first
- **Audience and time.** Default: professionals; 2 hours = about 1 hour lecture + 1 hour activity. Ask only if the request doesn't say.
- **Parts with maps.** Split the lecture into 2–4 parts. Each part opens with a map slide (numbered stages), and every slide in that part shows tabs (crumbs) for where we are. Then zoom into each concept, one slide each.
- **Order teaches.** Introduce the big idea before its parts (e.g. "kinds of AI by autonomy" before "inside an agent"). Group related ideas together (MCP goes with tools; skills stand alone).
- **The workshop is the end.** One task done deeply, not the whole method. Timed steps on the left, a blank canvas (e.g. an empty 2×2) on the right. No hand-in forms, no extra "finished example" slide unless asked; put an example in the notes.
- **No filler slides:** no agenda recap, no takeaways list, no book list (weave a book into the slide whose point it supports), no "questions?" slide.

## 2. Write every slide by the rules
Read `references/rules.md` before writing and again before publishing. The short version:
- Plain English, complete sentences, low reading load. **Delete anything obvious.**
- Every term, acronym, company and number is explained where it appears (what S$370M *means*, what "DBS" is, 48% vs 44% = "about 9% more money back").
- Every piece of evidence ends with **So what** for an executive.
- Pictures, charts, big numbers and tables over paragraphs. No square boxes. Big fonts.
- Every claim has a linked source at the bottom of the slide; facts that change (models, prices, dates, context windows) are searched today, never from memory.

## 3. Pick cases people will remember
Read `references/cases.md`. Prefer AI agents that *act* (collect debts, settle claims, negotiate, book trips, check diagnoses) over chatbots that answer. One slide per case: problem → what they did → what changed or the honest limit → 2–3 big numbers.

## 4. Check before showing
- Preview every changed slide: nothing overflows, sources sit at the bottom, fonts are readable from the back of a room.
- Re-read titles: one line, says the point.
- Double-check every date, price and name against its source (e.g. a launch's *first* release, not its 1.0).

## 5. Work through his comments
He reviews by leaving comments on slides, often many in a row. Follow `references/comments.md`: re-read the live slide, make the change, reply in that thread with the new wording, one short line in chat. A question ("what is X?", "is this because of Y?") usually means the slide is unclear: answer it **and** fix the slide. When a comment teaches a new general preference, offer to add it to `references/rules.md`.

## Domain notes
For a GenAI lecture, `references/genai-content.md` holds the content decisions already made (how to explain context, RAG, agents, memory, skills, the 95% study, and so on). Reuse them; re-check every number.
