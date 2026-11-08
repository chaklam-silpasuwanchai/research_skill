# Statistics

**Plan before looking.** Write the analysis plan in `experimental_design.md` first: each hypothesis, its IVs and DVs, and the test. Anything else is **exploratory**; label it.

| Situation | Typical choice |
|---|---|
| 2 conditions, continuous DV, between | t-test; Mann-Whitney if assumptions fail |
| 2 conditions, within | paired t-test; Wilcoxon signed-rank |
| 3+ conditions | ANOVA (repeated measures if within); Kruskal-Wallis / Friedman |
| Repeated measures, many participants or items | mixed-effects model (participant, item as random effects) |
| Categorical outcome | chi-square / Fisher; logistic regression |
| Ordinal ratings (Likert) | non-parametric or ordinal regression |
| Comparing models on a test set | paired bootstrap or permutation test; several seeds with mean and spread |
| Labeler agreement | Cohen's kappa or Krippendorff's alpha |

Unsure? State the DV type, number of conditions, and paired vs not, then choose. Check assumptions (normality, equal variance, independence) and say what you did when they fail.

**Report:** effect size with a confidence interval, not only p; n, test, statistic, df, exact p; correct for multiple comparisons (Holm or Bonferroni, say which); nulls, failures, exclusions. ML: number of seeds, variance handling, same data and tuning budget for baselines. Human studies: recruitment, exclusions, whether analysis matched the plan.

**Confirmatory (planned)** results support main claims; **exploratory** ones need more skepticism and cautious wording.

**Check the numbers:** recompute every reported number from raw data in `src/results/` or `src/data/`; keep the analysis script in `src/scripts/` so it reruns.
