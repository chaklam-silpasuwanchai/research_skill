---
name: read-papers
description: Reads the 10-15 closest papers closely - how they did it, what you can copy, and the one thing that makes you different - then checks novelty and validity. Use for "read the closest papers", "is this novel", "what can I copy", "how are we different", or /read-papers [idea].
---

# Read Papers

Copy many things; differ in **one** clear thing. Borrowing proven methods makes the study valid; the one difference makes it novel. Focus: the idea or topic; none → the current idea in `ideas.md`.

## 1. The idea in one sentence
Too vague → suggest `brain-dump` first.

## 2. Get the 10-15 closest papers
From `related_work.md`; fewer than 10 → `find-papers` search first. Verified only; recent top-venue papers plus 1-2 classics.

## 3. Read each one (abstract, method, results, limitations)
One row per paper in `related_work.md`:
`paper · question · what they change · what they measure · who or what data · design and analysis · key finding · their limitation · we borrow · we differ`

## 4. What we can borrow or copy
Patterns across the papers: design, validated scales, tasks, baselines, datasets, sample sizes, analyses, framing. Each with its source ("trust scale from Lee 2023"). Copying proven methods is a strength.

## 5. The one difference
Say it in one sentence: what we do that **none** of the 10-15 do, and which part it is (the question, what we change, what we measure, who, or the method). Then check it:
- **None** → say so; sharpen with `references/idea-lenses.md` or `think-deeply`.
- **Several** → lead with one; the rest support it.
- A gap in the field, not just in our reading? Would a reviewer care?

## 6. Novelty and validity (✅ / ❌ / ❓, a line each)
- **Novel:** the one difference survives all 10-15 papers.
- **Valid:** borrowed methods fit our question; no obvious confound; we know what would prove us wrong.
- **Significant, fits the venue, feasible** (data, people, time, ethics).

## Report
```
Read: 12 closest papers (table in related_work.md)
Borrow: within-subjects design (most papers) · trust scale (Lee 2023) · n≈24
One difference: we test admitting limits, not just being accurate
Novel ✅  Valid ❓ no trust scale chosen yet  Significant ✅
Next: /plan-method DV
```
The borrow list goes to `experimental_design.md`; open ❌/❓ become tickets. End with the quick sync in `AGENTS.md`.
