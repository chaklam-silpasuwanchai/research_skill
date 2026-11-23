# Rigor (used by `plan-method`, `update-paper`, `review`)

Rigor is what makes reviewers believe the result. A single comparison with a single analysis is rarely enough. Compare many things, analyze many ways, and make every comparison fair.

## Compare many things
- **Several strong baselines,** not one weak one: the common baseline in close papers, the strongest recent method, and a simple one (e.g. no intervention, random, majority class).
- **Ablations:** remove one part at a time to show which part causes the effect.
- **More than one setting:** different tasks, datasets, participant groups, models, or difficulty levels, where the claim needs it.
- **Variations of our own method:** key hyperparameters, prompts, or design choices.

## Analyze many ways
- the main planned test for each hypothesis, with effect sizes and confidence intervals
- **robustness:** does the result hold with another measure, seed, model, or subset?
- **sensitivity:** with and without outliers or exclusions; different reasonable thresholds
- **subgroup or per-condition:** where does it work, and where not?
- **error analysis:** look at failures, not only averages
- **qualitative support:** examples, quotes, or think-aloud data that explain the numbers
Label which analyses were planned and which were exploratory.

## Internal validity (did X really cause Y?)
- name every likely **confound** and how it is controlled: randomization, counterbalancing, matching, or holding it constant
- conditions differ **only** in the IV (same task, time, instructions, interface, data)
- no **leakage** between training and test, or between conditions

## Construct validity (did we measure what we claim?)
- validated scales or established metrics, used as intended
- the operational measure truly captures the concept; add a second measure of the same concept if possible
- check that the manipulation worked (participants noticed the difference)

## Fair analysis (the one home for fairness)
State it once in the paper, in a short paragraph before the first results table: same inputs, same participants or test items, same effort (tuning budget), same grading.
- every method gets the **same data, tuning budget, compute, and care**; no tuning only our own
- the analysis plan is fixed before the main study (`git tag plan-freeze-1`); no trying tests until one is significant
- correct for multiple comparisons; report **all** conditions and measures, including the ones that didn't work
- numbers recomputed by a script from raw data
- **A failed test set becomes development data.** Once you have read a check's failures and fixed them, rerunning those cases shows the fix works on them, but it is no longer fresh evidence. Before rerunning, write a new set of the same kinds with the same pass rules, commit it, then run the fix on it. *E.g. a fact checker failed 7 of 12 cases; a fresh 24-case set, written before the rerun, became the real test; the old 12 are reported as development only.*

## When results are unexpected (the one home)
A surprising result is usually a bug first. Before calling it surprising, rule out each of these, in order, and log every check in `log.md`:
1. **Code:** rerun on a tiny case where you know the answer. Check the right condition, config, model, and prompt actually ran (logs, not memory).
2. **Data:** leakage, wrong split, flipped or misaligned labels, missing or duplicated rows, exclusions applied as planned.
3. **Measure:** the measure works (manipulation check; for AI-based measures, the gate in `ai-measures.md`); reverse-coded items and scale direction are right.
4. **Analysis:** the planned test, the right grouping, numbers recomputed by a script from raw data.
5. **Chance:** other seeds, another subset, or more participants; look at the confidence interval, not just the mean.
6. **Papers:** did close papers see something similar, and how did they explain it?
Only when all six pass is the result really surprising. Then it is a finding: keep it, report it, and discuss it in depth (`update-paper/references/sections.md`). Never change the plan or drop data to make it go away. Give expected results the code and data checks too; a bug can also produce the answer you hoped for.

## Check
Before freezing, one line each: baselines and ablations chosen · analyses listed · confounds and controls · measures validated · fairness (same budget, plan fixed). Any gap → its root cause, then fix.
