# Section by section (used by `update-paper`)

**Where effort goes:** reviewers usually decide accept or reject from the **abstract and introduction**. Spend the most care there. The **discussion** is the other place that makes a paper strong.

**Title:** has the keywords; says what's new (and the method if useful); short; provokes reading without being cute. Offer 3-5.

**Abstract:** five connected parts: background, problem, methodology, key findings, contribution. Signal the gap ("However", "This paper proposes").

**Introduction:** the same five parts as the abstract, one paragraph each: **background, problem, methodology, key findings, contribution**, each backed by evidence. After reading it, a reviewer should feel **both kinds of novelty**: **idea novelty** (a new question or insight) and **technical novelty** (a method that isn't obvious or easy). One clear contribution, not a list of small ones. Don't overpromise: claim only what the results support. Include **Figure 1** (the problem, the insight, how our way changes it); offer three designs.

**Related work:** written in **subsections with clear headings**, so reviewers can find their way. **Synthesize, don't list**: for each group, say what the papers agree on and where they disagree, then how we **position** against them, what we **borrow**, and how we **differ**. Use the field summary from `references/papers.md` (consensus, disagreements, open questions). Don't teach experts.

**Methodology (and experiment):** learn how **this venue** writes it by reading 3-5 recent accepted papers; it usually looks the same every time, so follow that structure (CHI: design rationale, participants, apparatus, design, task and procedure, measures, analysis; ACL/NeurIPS: data, method, baselines, experimental setup). **Every decision is justified** (a citation or a reason). **Every detail is reproducible.** Everything supports **internal and construct validity**: say how confounds were controlled and why the measures capture the concept.

**Results:** **boring on purpose.** Report, don't interpret: follow best practice for the test (statistic, df, p, effect size, confidence interval, n), organized by research question or hypothesis. No discussion here.

**Analyses (if the venue expects them, often ACL/NeurIPS):** further analyses after the main results. Check what close papers usually include (ablation, error analysis, robustness, subgroup or per-category results, qualitative examples) and do the ones that strengthen the claim.

**Discussion:** perhaps **the most important part**, so make it strong and **in subsections**:
- the key insights, not a repeat of the results
- comparison with past work (agrees, contradicts, extends)
- possible explanations, including alternatives, for expected and unexpected results
- "what if": when would the result change, and what it means for theory and design (implications)
- limitations and future work (below)

**Conclusion:** **nothing new.** A short summary of the problem, what we did, what we found, and why it matters.

**Appendix (common for ACL; also supplements elsewhere):** the details needed for **reproducibility** that don't belong in the main text: prompts, hyperparameters, full tables, extra examples, annotation guidelines. Not a place for new claims.

**Limitations (own section or in the discussion):** 3-5 concrete threats to validity: internal (confounds, order effects, leakage), construct (does the measure capture the idea), external (who or what the result may not hold for, only if it matters for the claim), and statistical (power, multiple tests). For each: the threat, how it could change the conclusion, what we did to reduce it, and what future work would settle it. Draw them from `log.md`, plan deviations, and `review.md`. Skip true-of-every-study lines.

**Response to reviewers (rebuttal or revision letter):** open with thanks and a 2-3 line summary of the main changes. Group duplicate points; quote each concern briefly, then answer: **changed** (what and where, with page or section) / **clarified** (the misunderstanding and the new text) / **respectfully disagree** (evidence and citation) / **out of scope** (why, and where it is now acknowledged). Never promise what the paper won't contain. Keep within the venue's word limit; most important concerns first.
