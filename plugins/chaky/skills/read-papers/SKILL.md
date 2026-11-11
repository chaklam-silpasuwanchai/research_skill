---
name: read-papers
description: Searches the field and reads the 10-15 closest papers closely - consensus and gaps, what you can copy, your one difference, novelty and validity - plus scoop watch and a paper you found. Use for "read the closest papers", "is this novel", "has someone done this", "I found a paper", "am I scooped", or /read-papers [idea].
---

# Read Papers

**Idea validation.** Copy many things; differ in **one**. Focus: an idea or topic (none → `ideas.md`). A paper in hand or a suspicion ("someone did this") → **triage** (`references/triage.md`). Scoop check → **watch** (`references/watch.md`). Otherwise:

## 1. Search
Recent top-venue papers plus 1-2 classics; synonyms; citations both ways (Semantic Scholar, OpenAlex, Google Scholar, ACM DL, arXiv, alphaXiv). **Verify every paper** (DOI or publisher); unverifiable → left out. BibTeX fetched, never typed. Rank the closest 10-15. Keep a **source trail** at the top of `related_work.md`: date, databases, search terms, how many found and verified.

## 2. Read each closely
One row per paper in `related_work.md`:
`paper · question · what they change · what they measure · who or what data · design and analysis · finding · limitation · we borrow · we differ`

## 3. The field in three lines
**Consensus** (what most papers agree on) · **Disagreements** (where they conflict) · **Open questions** (what nobody has answered yet).

## 4. What to copy
Design, validated scales, tasks, baselines, datasets, sample sizes, analyses, framing, each with its source. Copying proven methods is a strength (feeds `plan-method`).

## 5. The one difference
One sentence: what we do that **none** of them do, and which part (question, what we change, what we measure, who, method).
None → say so; sharpen (`references/idea-lenses.md`, `think-deeply`). Several → lead with one.

## 6. Check (✅ / ❌ / ❓)
**Novel:** the difference survives all 10-15. **Valid:** borrowed methods fit; no obvious confound; we know what would prove us wrong. **Significant, fits the venue, feasible.**

## Report
```
Read: 12 closest papers (table and source trail in related_work.md)
Field: agree trust drops after errors · disagree on disclosure timing · open: admitting limits
Borrow: within-subjects design · trust scale (Lee 2023) · n≈24
One difference: we test admitting limits, not just being accurate
Novel ✅  Valid ❓ no trust scale yet  Significant ✅
Next: /plan-method DV
```
Close overlap or open ❌/❓ → tickets. End with the quick sync in `AGENTS.md`.
