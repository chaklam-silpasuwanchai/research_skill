---
name: validate-idea
description: Checks whether an idea, or the paper so far, is novel, valid, and significant enough for your venue, and how to sharpen it. Use for "is this novel", "is this a good idea", "is this publishable", "validate my idea", or /validate-idea [your idea].
---

# Validate Idea

A good idea fills a gap **in the field**, not in what we've read. Focus: the idea in a sentence; none → the current idea from `ideas.md` and the paper.

1. **Restate** it in one sentence. Too vague → suggest `brain-dump`.
2. **Closest work:** 3-5 verified papers via `find-papers`; how we differ from each (problem, what we change, what we measure, or method).
3. **Check** (✅ / ❌ / ❓, one line each):
   - **Novel:** already done? Is "nobody did it" the only reason? Contribution clear in one sentence?
   - **Valid:** testable in time? Confounds, or a boring explanation? What result would prove it wrong?
   - **Significant:** who cares, and what would they do differently?
   - **Fits the venue**, and **feasible** (data, people, compute, ethics, deadline)?
4. **Sharpen** each ❌/❓ with 1-3 fixes: narrow the claim, reframe the gap, borrow a theory, change the measure. Stuck → `references/idea-lenses.md`.
5. **Report and save:**
```
Idea: ...
Novel ✅ closest: Smith 2024 tested trust, not disclosure
Valid ❓ trust scale not chosen
Next: choose the scale (/plan-method DV)
```
Save to `ideas.md` and `related_work.md`; open ❌/❓ become tickets; log the verdict.
