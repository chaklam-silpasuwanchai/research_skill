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

## Fair analysis
- every method gets the **same data, tuning budget, compute, and care**; no tuning only our own
- the analysis plan is fixed before the main study (`git tag plan-freeze-1`); no trying tests until one is significant
- correct for multiple comparisons; report **all** conditions and measures, including the ones that didn't work
- numbers recomputed by a script from raw data

## Check
Before freezing, one line each: baselines and ablations chosen · analyses listed · confounds and controls · measures validated · fairness (same budget, plan fixed). Any gap → its root cause, then fix.
