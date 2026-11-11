---
name: read-papers
description: Finds and reads the papers closest to your idea - searches the field, reads the 10-15 closest closely, shows what you can copy and the one thing that makes you different, checks novelty and validity, watches for new papers, and handles a paper you found or suspect overlaps. Use for "read the closest papers", "is this novel", "has someone done this", "I found a paper", "am I scooped", or /read-papers [idea].
---

# Read Papers

Copy many things; differ in **one**. Focus: an idea or topic (none → `ideas.md`). A paper in hand or a suspicion ("someone did this") → **triage** (`references/triage.md`). Scoop check → **watch** (`references/watch.md`). Otherwise:

## 1. Search
Recent top-venue papers plus 1-2 classics; synonyms; snowball citations both ways (Semantic Scholar, Google Scholar, ACM DL). **Verify every paper** (DOI, publisher, Anthology, arXiv); unverifiable → left out. BibTeX fetched, never typed. Rank the closest 10-15.

## 2. Read each closely
One row per paper in `related_work.md`:
`paper · question · what they change · what they measure · who or what data · design and analysis · finding · limitation · we borrow · we differ`

## 3. What to copy
Patterns across papers: design, validated scales, tasks, baselines, datasets, sample sizes, analyses, framing, each with its source. Copying proven methods is a strength (feeds `plan-method`).

## 4. The one difference
One sentence: what we do that **none** of them do, and which part (question, what we change, what we measure, who, method).
None → say so; sharpen with `references/idea-lenses.md` or `think-deeply`. Several → lead with one.

## 5. Check (✅ / ❌ / ❓)
**Novel:** the difference survives all 10-15. **Valid:** borrowed methods fit; no obvious confound; we know what would prove us wrong. **Significant, fits the venue, feasible.**

## Report
```
Read: 12 closest papers (table in related_work.md)
Borrow: within-subjects design · trust scale (Lee 2023) · n≈24
One difference: we test admitting limits, not just being accurate
Novel ✅  Valid ❓ no trust scale yet  Significant ✅
Next: /plan-method DV
```
Close overlap or open ❌/❓ → tickets. End with the quick sync in `AGENTS.md`.
