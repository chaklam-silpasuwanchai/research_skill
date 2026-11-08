---
name: use-llms
description: Plans which LLM access to use (API keys, free routers, local models) and prepares free-chat packages (Gemini, Claude, ChatGPT) for batch labeling and outside reviews. Use for "what model can I use", API keys, cost, "help me label data", or a second AI opinion.
---

# Use LLMs

Two jobs. Pick by what the researcher needs.

## A. Models and access (ACL/NeurIPS-style, or any LLM in a study)
Read `references/models.md`. Ask one at a time: API key or free credits? A local option and its memory? Any private data? Then write a tiered plan (pilot, main, labeling, final) in `implementation.md`, set up one logged `call_model()` wrapper, estimate cost before big runs, pin exact model names, and apply the free-router guardrails.

## B. Free chats: labeling and outside review
Read `references/labeling-review.md`. Safety first: never paste participant, confidential, licensed, or unpublished sensitive material into free chats. Labeling: codebook, batches of 20-50, 2-3 different AIs, merge, check agreement, **humans only at the very end** (disagreements plus a sample). Outside review: prompts for novelty, validity, and writing; verify every paper they name; their points inform fixes but never change `review-paper` scores.

Log decisions and who made them.
