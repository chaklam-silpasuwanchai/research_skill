# Review rubric (fixed; edit this file only on purpose, never mid-review)

Every test is yes/no and needs a quote or location. Question score = 1 + passes.

## A. Novelty
**N1. New vs the closest verified work**
a. At least one closest paper is named and verified in `related_work.md`.
b. The paper states in one sentence how it differs from it (quote).
c. The difference is about problem, IV, DV, or method, not just "we use X".
d. Every key paper in `related_work.md` is compared somewhere in the paper.

**N2. Why the difference matters**
a. A consequence for readers, practice, or theory is stated.
b. The motivation is not only "no one has done this".
c. It names who benefits or what decision changes.
d. That consequence is backed by a citation or result, not assertion.

**N3. What another researcher learns**
a. The contribution is stated in one sentence (what / why / so what).
b. The contribution type (empirical, design, artifact, theoretical) is stated and matches the evidence.
c. A takeaway that transfers beyond this setup is stated.
d. The listed contributions match what the results actually show.

**N4. Strongest counterexample**
a. A search for the strongest counterexample was run (record the search terms in `review.md`).
b. The closest competing paper found is named in `review.md`.
c. The paper addresses it explicitly (related work or discussion).
d. The novelty claim is worded narrowly enough to survive it.

## B. Validity
**V1. Measures what it claims**
a. Each key concept is defined.
b. Each concept has a named measure (DV or instrument).
c. The measure is justified by a citation or argument.
d. The measure was checked (pilot, manipulation check, human agreement, or an established instrument).

**V2. Fair comparison**
a. At least one baseline or comparison condition exists.
b. Baselines get the same data, information, tuning effort, and compute (stated).
c. At least one baseline is current and strong.
d. Any resource differences are reported.

**V3. Clear design**
a. Hypotheses are stated and falsifiable.
b. IVs and DVs are named per hypothesis.
c. Controls or fixed factors are listed.
d. A `plan-freeze` git tag is dated before the main results and later deviations are logged; or the paper honestly states that the plan was not frozen and labels planned vs exploratory analyses.

**V4. Alternative explanations**
a. Claim type matches evidence type (table below).
b. ML: leakage or contamination checked. CHI: sampling and assignment described.
c. At least one alternative explanation is named and addressed.
d. The universal-wording scan is clean (no claim wider than the tested conditions).

**V5. Honest reporting**
a. Uncertainty is reported (CI, error bars, seeds, n).
b. Failures, dead ends, or negative results are reported (compare `log.md`).
c. Limitations are concrete and affect validity.
d. Enough detail to reproduce (data, parameters, procedure, code or artifact plan).

**Claim type vs evidence:** causal ("causes", "leads to") needs an isolating ablation · generalization ("generalizes", "robust", "across") needs varied test conditions · improvement ("outperforms", "better") needs a fair baseline · descriptive ("accounts for", "pattern") needs representative sampling · scoping ("when", "limited to") needs declared bounds.

## C. Writing checklist (pass/fail; severity fixed)
🔴 = reject-level, 🟡 = lowers impression.

**Abstract and Introduction**
🔴 Logic is supported by evidence; each introduction paragraph rests on strong evidence
🔴 Problem is stated clearly
🔴 Motivation is not just "no one did this, so I did"

**Related Work**
🔴 No very important work missing
🔴 Gap revealed logically
🟡 Synthesizes, doesn't list (no "so what?" left)
🟡 Stays on topic
🟡 Convinces experts instead of teaching them

**Methodology**
🟡 Ideas behind the innovation, not only implementation
🔴 Enough detail to replicate
🟡 Technical novelty, challenge, or creativity
🟡 Grounded in principles; explains why it should work
🔴 Sound design: right comparisons, fair and rigorous baselines
🔴 Evaluation and metrics measure what they should
🔴 Appropriate statistical tests (present)
🟡 Good figures and data reporting

**Discussion**
🟡 Real insight, not rephrased results
🟡 Actionable implications, not common sense
🟡 No big claims unsupported by data
🔴 What the introduction promises matches what the discussion delivers

## D. Verdict (Full mode, fixed)
- **Likely accept range:** Novelty ≥ 3.5, Validity ≥ 3.5, and no ❌ on any 🔴 item.
- **Borderline, revise:** either score from 2.5 to under 3.5, or any ❌ on a 🔴 item.
- **Likely reject:** either score under 2.5.
Give the formula's result and a one-sentence reason; don't adjust it by feel.
