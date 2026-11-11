# Labeling with free AI chats

**Safety first.** Never paste participant data, confidential, licensed, or unpublished sensitive material into free chats. Anonymize; check the data licence, ethics terms, and the chat's data-use setting. Unsure → don't.

## A. Label data (humans only at the very end)
1. Write the **codebook**: labels, a definition each, 2 examples and 1 edge case each, a tie-break rule, and an output format (`id,label,confidence,short_reason`).
2. Make **batches** of about 20-50 items as copy-paste text.
3. The user runs the same batches in **2-3 different AIs**, a fresh chat each, and pastes the outputs back (save under `src/data/`). **Ask first: do you have Claude in Chrome?** If yes, Chaky can open the chats in their browser, paste each batch, and collect the outputs (confirm once before pasting; stop if a site blocks it).
4. **Merge:** majority label; compute agreement (kappa or alpha, via `update-paper`); list the disagreements.
5. Fix the codebook where disagreements cluster. Log it.
6. **At the very end** (saves money and time), hire two humans to label the disagreements plus a random sample, and report human-AI agreement. The paper says honestly that labels were LLM-assisted (AI-use disclosure); LLM labels are a proxy, so claim accordingly.

Outside AI reviews of the paper: `review` (AI reviewer check).
