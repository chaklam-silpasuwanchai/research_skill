# Triage mode: a new paper in hand

Mid-project discoveries are normal and valuable. Handle them without derailing the main plan.

## 1. Intake
Fetch and **verify** the paper (it exists; title, authors, year, venue; preprint or peer-reviewed). Ask one question: **why did it catch your eye?** (worried it overlaps / a method or measure to borrow / a new idea / a baseline to add / just interesting).

## 2. Paper card (plain English, at most 10 lines)
Problem · IVs · DVs · method · key result · limitations · data or code available? · venue and year.

## 3. Compare with our project (checklist)
- Same problem?
- Same IVs or DVs?
- Same method?
- Same data or setting?
- Do its results support or conflict with our hypotheses?

Overlap level: **none** (0 yes) · **adjacent** (1-2) · **close** (3-4) · **direct** (all 5 on problem, IV/DV, and method).

## 4. Decide (the researcher chooses; recommend one)
| Option | When | Actions |
|---|---|---|
| **Cite** | none or adjacent | Add to `related_work.md` under its group; plan where the paper mentions it |
| **Borrow** | useful method, measure, baseline, theory | Add to `experimental_design.md` or `implementation.md` with rationale; consider a pilot |
| **Differentiate** | close | State what we do that they don't; run `shape-idea` to sharpen the contribution |
| **Pivot or reframe** | direct | Log pivot options; run `shape-idea`; don't hide the overlap |
| **Park** | interesting, not now | Add to `ideas.md` |
| **Ignore** | irrelevant | Log why in one line |

## 5. If the user wants to **try it**
1. Create a side branch: `git switch -c try/<short-name>`. The main plan stays untouched.
2. Before running: write the question, the **success criterion**, and a time box (e.g. one afternoon, N runs).
3. Run a tiny pilot with `run-study` rules (log runs).
4. Reflect: **merge** into the plan (update design and paper), **park**, or **drop**. A dropped try is a logged dead end with the lesson.

## 6. Sync
Update `related_work.md`, `ideas.md` or the design as chosen. Update the paper's related work and novelty claims (mark ⚠ stale if not done now). Log the decision with who made it. Offer a quick `review-paper` checkpoint if novelty was touched.

## Checklist summary to the user
Use ✅ ok · ❌ not ok · 🔧 to do · ⚠ stale · 🌟 very good. Example: "✅ verified · ⚠ overlap is close (3 of 5) · 🔧 write how we differ · Next: pick Differentiate or Borrow."
