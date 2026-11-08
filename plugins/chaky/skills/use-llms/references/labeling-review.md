# Labeling and outside review with free chats

**Safety first.** Never paste participant data, confidential, licensed, or unpublished sensitive material into free chats. Anonymize; check the data licence, ethics terms, and the chat's data-use setting. Unsure → don't.

## A. Label data (humans only at the very end)
1. Write the **codebook**: labels, a definition each, 2 examples and 1 edge case each, a tie-break rule, and an output format (`id,label,confidence,short_reason`).
2. Make **batches** of about 20-50 items as copy-paste text.
3. The user runs the same batches in **2-3 different AIs**, a fresh chat each, and pastes the outputs back (save under `src/data/`).
4. **Merge:** majority label; compute agreement (kappa or alpha, via `analyze-results`); list the disagreements.
5. Fix the codebook where disagreements cluster. Log it.
6. **At the very end** (saves money and time), hire two humans to label the disagreements plus a random sample, and report human-AI agreement. The paper says honestly that labels were LLM-assisted (AI-use disclosure); LLM labels are a proxy, so claim accordingly.

## B. Outside review (any stage)
Tell the other AI the stage ("ideation", "draft", "near-final") and venue. Ask it to name specific papers, quote the sentences it criticizes, and write its review as a Markdown file. Offer three prompts (or combine):
- **Novelty:** "Check novelty against the closest work you know, naming papers. Could this be published at [venue] if the idea holds? List concrete changes."
- **Validity:** "List threats to validity: confounds, leakage, unfair baselines, wrong measures, over-claiming. For each, quote the sentence and say what evidence would fix it."
- **Writing:** "Check the logic, whether each introduction paragraph is supported by evidence, whether related work synthesizes or lists, and whether the discussion offers insight. Quote the weak sentences."

When the review comes back (paste, or `components/external_review.md`, overwritten each time): verify every paper it names; mark each point agree / disagree / unsure with a reason; fold the agreed points into the fixes. Outside reviews **don't change** the `review-paper` scores. Where AIs disagree, use the majority plus the user's judgement. Log decisions with who decided.
