# Section by section (used by `update-paper`)

**Before drafting any section,** read how 2-3 recent accepted papers at the target venue write that same section, and follow their structure. Writing rules: `writing.md`. How close papers argue in the intro, method, and discussion: `argument.md`. Citations: recent, top venues (`papers.md`).

**Where effort goes:** reviewers usually decide accept or reject from the **abstract and introduction**. Spend the most care there. The **discussion** is the other place that makes a paper strong.

**Title:** has the keywords readers search for (check titles of close recent papers); says what's new (and the method if useful); short; provokes reading without being cute; promises no more than the results show. Offer 3-5. **Re-check it after every update:** when the story, the one difference, or the findings change, suggest 2-3 better titles next to the current one, each with a reason; the researcher chooses.

**Abstract, introduction, contributions:** frame the method with `framing.md` (what it estimates and how, why the problem is hard, how each difficulty is handled, measured strengths, an explicit and searched novelty claim, and a framing that matches the method exactly).

**Abstract:** five connected parts: background, problem, methodology, key findings, contribution. Signal the gap ("However", "This paper proposes").

**Introduction:** the same five parts as the abstract, one paragraph each: **background, problem, methodology, key findings, contribution**, each backed by evidence. After reading it, a reviewer should feel **both kinds of novelty**: **idea novelty** (a new question or insight) and **technical novelty** (a method that isn't obvious or easy). One clear contribution, not a list of small ones. Don't overpromise: claim only what the results support. Include **Figure 1** (the problem, the insight, how our way changes it); offer three designs.

**Related work:** written in **subsections with clear headings**, so reviewers can find their way. **Synthesize, don't list**: for each group, say what the papers agree on and where they disagree, then how we **position** against them, what we **borrow**, and how we **differ**. Use the field summary from `references/papers.md` (consensus, disagreements, open questions). Don't teach experts.

**Methodology (and experiment):** Validate any AI-based measure MT-Bench style and report the gate, the rounds and the fresh check in the appendix. Open with a short walk-through of one interaction or trial from this study, introducing each term as it appears (`writing.md`). Learn how **this venue** writes it by reading 2-3 recent accepted papers; it usually looks the same every time, so follow that structure (CHI: design rationale, participants, apparatus, design, task and procedure, measures, analysis; ACL/NeurIPS: data, method, baselines, experimental setup). Write up the plan's decision table (`plan-method`): every decision justified, every detail reproducible, confounds and measures explained.

**Results:** **boring on purpose.** Report, don't interpret: follow best practice for the test (statistic, df, p, effect size, confidence interval, n), organized by research question or hypothesis. Tables follow `references/figures.md`: cited baselines, ours last with its variants indented, fairness stated once before the first table. No discussion here.

**Analyses:** further analyses after the main results, as close papers include them (ablation, robustness, sensitivity, subgroups, error analysis, qualitative examples; `plan-method/references/rigor.md`).

**Discussion:** perhaps **the most important part**. Students often don't know what to discuss, so cover these, one subsection or paragraph each, in this order. Each one starts from the research questions or hypotheses stated at the beginning (no clear question → suggest `/brain-dump` first).
1. **Did you find what you expected?** Go back to each question or hypothesis. Discuss **in depth** anything you did not expect: possible explanations, including alternatives.
2. **Did you achieve what you claimed?** What did you not yet achieve? What is the ultimate goal, and how far are you from it?
3. **How does it compare with related work?** Consistent, contradicting, or surprising? Name the papers.
4. **Why these design decisions** (experimental or device), and how did they affect the results?
5. **Design implications or guidelines:** if someone built an application, how would these results guide them?
6. **Significance:** in the big picture, why is this work valuable?
7. **Limitations** (below).
8. **Future work:** one or two really concrete items, no more.

**Conclusion:** **nothing new.** A short summary of the problem, what we did, what we found, and why it matters.

**Appendix (common for ACL; also supplements elsewhere):** the details needed for **reproducibility** that don't belong in the main text: prompts, hyperparameters, full tables, extra examples, annotation guidelines. Not a place for new claims.

**Limitations (own section or in the discussion):** only the **core, concrete, real** limitations that could affect the validity of **this** result: internal (confounds, order effects, leakage), construct (does the measure capture the idea), statistical (power, multiple tests), or external only when it matters for the claim. For each: the threat, how it could change the conclusion, what we did to reduce it, and why it does not matter too much. Draw them from `log.md`, plan deviations, and `review.md`.
- **Skip limitations true of almost any study** ("we tested in the US, not the UK").
- **Never a limitation that makes the work look good** ("our method is so thorough it is slow", "our sample was only experts"). This is a very common mistake.

**Response to reviewers:** `response.md`.
