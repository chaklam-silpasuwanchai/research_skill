---
name: validate-idea
description: Checks whether an idea, or the paper's current status, is novel, valid, and significant enough for the venue - a real research gap, a clear contribution, testable, worth a reviewer's time - and says how to sharpen it. Use for "is this novel", "is this a good idea", "validate my idea", "is this publishable", or /validate-idea [your idea].
---

# Validate Idea

A good idea fills a **gap in the field** (not a gap in what we have read) and is publishable at the venue. Optional focus: `/validate-idea <the idea in a sentence>`. No focus → check the current idea from `ideas.md`, `experimental_design.md`, and the paper's title, abstract, and introduction.

## 1. Restate it
The idea in one sentence: what we do, for whom, and what we expect. Unclear or missing → suggest `brain-dump` and stop.

## 2. Check closest work (novelty)
Use `find-papers` for the 3-5 closest papers (verified, with links). For each: what they did, what is left open, how we differ (problem, what we change, what we measure, or method; not just "we use X").

## 3. Run the checks (✅ / ❌ / ❓ with one line each)
- **Novel:** already answered? Is "nobody did it" the only reason? Gap in the field or just unread? Can a reviewer see the contribution in one sentence?
- **Valid:** testable with what they can do in time? Clear what we change and what we measure? Obvious confounds or a trivial explanation? What result would prove it wrong?
- **Significant:** who cares, and what would they do differently? Big enough for the venue, or a workshop paper?
- **Fit:** matches the venue's taste and contribution types (`plan-method`'s contribution-types notes)?
- **Feasible:** data, participants, compute, ethics, deadline.

## 4. Sharpen
For any ❌ or ❓, offer 1-3 concrete fixes: narrow the claim ("smallest version that is still a real finding?"), reframe the gap, borrow a classic theory, or change the measure. When stuck, use 2-3 lenses from `references/idea-lenses.md`. Want a harder look → `think-deeply`. Want an outside opinion → free AI chats via `setup-llms` (verify every paper they name).

## 5. Report and save
```
Idea: <one sentence>
Novel ✅  closest: Smith 2024 tested trust, not disclosure
Valid ❓  trust scale not chosen yet
Significant ✅  sales agents are deployed now
Next: choose the trust scale (plan-method), then write the intro (write)
```
Save the checks in `ideas.md` and the closest papers in `related_work.md`; log the verdict and any change to the idea in `log.md`; add tickets for open ❌/❓ items. Say what was saved in one line.
