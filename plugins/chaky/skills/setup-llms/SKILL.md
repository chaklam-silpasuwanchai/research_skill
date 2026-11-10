---
name: setup-llms
description: Sets up AI models for your study - OpenRouter or other API keys, a local LLM, and free browser AI chats for labeling data and outside reviews - with pinned models, cost checks, and data safety. Use for "set up OpenRouter", "local LLM", "which model can I use", "help me label data", "second AI opinion", or /setup-llms.
---

# Setup LLMs

Focus: `openrouter`, `local`, `labeling`, `review`. Details: `references/models.md`, `references/labeling-review.md`.

## API (OpenRouter or similar)
Key in `.env`, never in code or chat. Tiered plan in `implementation.md`: pilot (cheap), main, final (pinned). One logged `call_model()` in `src/scripts/` (model, settings, cost, run ID). Never report results from an `auto` model. **Runs over the estimate or about $20: ask first.**

## Local LLM
Ask about the computer and memory; suggest a model that fits and a runner (Ollama, LM Studio). Test one call through `call_model()`; note the exact model.

## Free AI chats
**Never paste participant, confidential, or unpublished data (critical).** Labeling: codebook, batches of 20-50, 2-3 different AIs, merge, check agreement, humans only at the end for disagreements. Outside review: prompts for novelty, validity, writing; verify every paper they name.

Test it once end to end. End with the quick sync in `AGENTS.md`.
