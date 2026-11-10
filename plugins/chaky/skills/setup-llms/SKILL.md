---
name: setup-llms
description: Sets up the AI models a study or workflow needs - OpenRouter or other API keys, a local LLM, and free browser AI chats for labeling and outside reviews - with a tiered plan, pinned models, cost checks, and data-safety rules. Use for "set up OpenRouter", "local LLM", "which model can I use", "help me label data", "get a second AI opinion", or /setup-llms local.
---

# Setup LLMs

Optional focus: `/setup-llms openrouter`, `/setup-llms local`, `/setup-llms labeling`, `/setup-llms review`.

## A. API access (OpenRouter or another provider)
Details: `references/models.md`. Ask one at a time: do you have an API key or free credits? Any private or participant data involved?
- Put the key in `.env` (never in code or chat); check `.gitignore` covers it.
- Write a **tiered plan** in `implementation.md`: pilot (cheap or free), main, labeling, final (stable, pinned).
- One logged `call_model()` wrapper in `src/scripts/`: exact model name, provider, parameters, cost, run ID.
- Estimate cost before big runs. **A run over the estimate or over about $20 is critical: ask first.**
- Free routers: never report results from an `auto` model; pin exact names.

## B. Local LLM
Ask: which computer, how much memory (RAM or GPU)? Suggest a model size that fits, and a runner (for example Ollama or LM Studio). Test one call through the same `call_model()` wrapper, and note the exact model file and settings in `implementation.md`.

## C. Free browser AI chats (labeling and outside review)
Details: `references/labeling-review.md`.
- **Safety first (critical):** never paste participant, confidential, licensed, or unpublished sensitive data into free chats. Anonymize; check the data licence, ethics terms, and the chat's data-use setting. Unsure → don't.
- **Labeling:** codebook, batches of 20-50, 2-3 different AIs in fresh chats, merge by majority, check agreement (kappa or alpha, see `write`'s statistics notes), humans only at the very end for disagreements plus a sample.
- **Outside review:** prompts for novelty, validity, and writing; verify every paper they name; their points inform fixes but never change `review` scores.

## Finish
Test that it works end to end (one call, one label batch, or one review prompt). Log the setup, who decided, and the models chosen in `log.md`.
