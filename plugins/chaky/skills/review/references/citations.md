# Citation check (used by `review`; every entry, every time)

A wrong or invented reference can sink a paper. Check **every** entry in the `.bib` and **every** `\cite`, not a sample. Never mark an entry ✅ without a source link you actually opened.

## For each entry
1. **Find it** at a real source: DOI (doi.org), Crossref, Semantic Scholar, OpenAlex, DBLP, ACL Anthology, ACM DL, IEEE Xplore, arXiv, OpenReview, or the publisher. Not found anywhere → ❌ `not found` (likely invented); mark the cite `[CITE?]`.
2. **Match every detail** against that source: exact title, all authors in order, year, venue, volume and pages, DOI. Any mismatch → 🔧 with the correct value.
3. **Right version:** a preprint that has since been published → cite the published version. Mark preprints as preprints.
4. **Retracted or corrected?** Check the publisher page or Crossref; retracted → ❌.
5. **Supports its sentence:** open the paper (abstract, the relevant section) and check the sentence that cites it says what the paper actually shows. Not supported or overstated → ❌ with a short quote from the paper.
6. **Recent:** per `update-paper/references/papers.md` (recent, or a classic).
7. **BibTeX fetched,** never typed from memory: re-fetch from the DOI or the source if fields look hand-made.

## Across the paper
- every `\cite` key has a `.bib` entry, and every entry is cited
- no duplicates (same paper under two keys)
- consistent format (venue names, capitalization protected with `{}`)
- self-citations neutral if the venue is double-blind

## Report (one row per entry, saved in `components/review.md`)
```
key        status  evidence                            fix
lee2023    ✅      doi.org/10.1145/...                 -
kim2024    🔧      dblp: year is 2023, not 2024        change year
smith2022  ❌      not found in Crossref, S2, DBLP     remove or replace; [CITE?]
park2021   ❌      paper shows X, sentence claims Y    reword the sentence or cite another paper
Total: 41 ✅ · 2 🔧 · 2 ❌
```
Every ❌ and 🔧 becomes a ticket. Can't reach a source (network) → say which entries are unchecked; never guess.
