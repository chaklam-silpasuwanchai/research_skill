# How strong papers argue (used by `update-paper` for the intro, method, and discussion)

Layout is not enough: learn how close papers **argue**, then make ours argue as well, in our own words. Never copy their sentences.

## 1. Pick the papers
3-5 recent, closely related papers from top venues (`papers.md`), ideally accepted at the target venue. Prefer papers with a contribution type like ours.

## 2. Map each paper's argument (one line per paragraph)
- **Introduction:** what each paragraph does in order (context → problem → why it is hard → gap → our idea → findings → contributions); how they **state the gap** ("However, ...", "Yet no work has ..."); how they **make the work feel new** (idea and technical novelty); how many contributions and how each is phrased; how much they hedge.
- **Method:** the order they explain things in; how they **justify each decision** (a citation, a pilot, a reason); how they **show fairness and isolation**; how they introduce terms (a walk-through, a figure).
- **Discussion:** how they **open** (the main insight, not a summary); how they **explain** results (mechanism, alternatives); how they **compare** with past work (agree, contradict, extend); how they frame **implications** and **limitations** without weakening the contribution.
Save the maps in `components/related_work.md` under *How they argue*.

## 3. Find the common moves
In 3-5 lines per section: the moves most papers share, in order ("4 of 5 papers state the gap in paragraph 3, after naming why it is hard"). Note one or two moves that the strongest paper makes and others don't.

## 4. Compare with ours
Map our intro, method, and discussion the same way. List what is missing, in the wrong order, or weaker ("our gap comes after the method; theirs comes before"; "we never say why the problem is hard").

## 5. Update the paper
Rewrite each section to make the common moves, in the same order where it fits, in our story and our voice (`writing.md`). Keep every claim, number, and citation; the framing must still match the method (`framing.md`). Show each section with a short note: "Now follows the usual move order: hard → gap → idea (as in Lee 2025, Kim 2024)."
