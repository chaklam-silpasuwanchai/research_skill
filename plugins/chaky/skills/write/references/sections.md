# Section by section (used by `write`)

**Title:** has the keywords; fancy but not too fancy; provokes reading; says what's novel (and the method if useful); short. Offer 3-5.

**Abstract:** five connected parts: background, problem, methodology, findings, contribution/significance. Signal the gap ("However", "This paper proposes").

**Introduction:** the abstract expanded into five paragraphs, each backed by evidence. Include **Figure 1** (the problem, the insight, how our way changes it); propose three alternative designs for it.

**Related work:** group by how each cluster positions against ours; synthesize, don't list; say how we differ, are inspired by, or extend each. Readers should feel we read widely and know what we're doing. Don't teach experts.

**Methodology and experiment:** follow the venue. CHI: design rationale, apparatus, participants, experimental design, measures. ACL/NeurIPS: methodology = data, simulation, the technique; experiment = comparisons, baselines. Strong rationale, enough detail to replicate, ideas over implementation.

**Results:** by research question or insight; statistics as needed; follow how related work reports.

**Analysis (ACL/NeurIPS):** the planned extras (robustness, transfer, error, feature, network, input/output analysis).

**Discussion:** cover: expected vs unexpected (unexpected in depth); what you achieved vs claimed, the ultimate goal, how far away; comparison with related work; design decisions and their effect; actionable implications; significance; **limitations** (only concrete ones that threaten validity; "tested only in the US" is true of every study, skip it); **future work** (one or two concrete items).

**Conclusion:** simple, nothing new, smooth end.

**Limitations (own section or in the discussion):** 3-5 concrete threats to validity: internal (confounds, order effects, leakage), construct (does the measure capture the idea), external (who or what the result may not hold for, only if it matters for the claim), and statistical (power, multiple tests). For each: the threat, how it could change the conclusion, what we did to reduce it, and what future work would settle it. Draw them from `log.md`, plan deviations, and `review.md`. Skip true-of-every-study lines.

**Response to reviewers (rebuttal or revision letter):** open with thanks and a 2-3 line summary of the main changes. Group duplicate points; quote each concern briefly, then answer: **changed** (what and where, with page or section) / **clarified** (the misunderstanding and the new text) / **respectfully disagree** (evidence and citation) / **out of scope** (why, and where it is now acknowledged). Never promise what the paper won't contain. Keep within the venue's word limit; most important concerns first.
