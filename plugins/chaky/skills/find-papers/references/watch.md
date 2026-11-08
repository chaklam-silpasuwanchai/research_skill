# Watch mode: scoop check


## 1. Build the search
From `terms.md`, the research questions, and the key papers in `related_work.md`: 5-8 queries using the community's terms **and** nearby synonyms. Search since the last `scoop-check` entry in `log.md` (first run: last 12 months), across top venues, arXiv, and citations of the key papers.

## 2. Filter and verify
Keep papers that match the problem, IV/DV, or method. Verify each exists (title, authors, year, venue; mark preprints). Drop the rest.

## 3. Rank by overlap (the five questions)
Same problem? Same IVs or DVs? Same method? Same data or setting? Results that support or conflict with ours? **None** (0) · **adjacent** (1-2) · **close** (3-4) · **direct** (problem, IV/DV, and method all match).

## 4. Report (Chaky voice)
Show at most the 5 most relevant, each with overlap level and one line on why. 🌟 nothing close · ⚠ close or direct overlap found. Hand each ⚠ to `find-papers`; add adjacent ones to `related_work.md` after the user agrees.

## 5. Record
Add a `scoop-check` entry to `log.md` (date, queries used, what was found). Suggest the next check in about two weeks, and always before submission.
