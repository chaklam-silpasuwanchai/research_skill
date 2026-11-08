# Models and access


## 1. Ask (one at a time)
- Do you have an **OpenRouter** or other API key? Any free credits or a budget?
- Do you have a **local** option (GPU or Apple Silicon, how much memory) for Ollama, vLLM, or LM Studio?
- Is any data **private** (it can't leave the machine)?

## 2. Write a tiered plan (in `implementation.md`, Setup needs; plain English per choice)
- **Pilot tier:** cheap, fast, or small local model; run first.
- **Main tier:** the models the paper compares.
- **Labeling tier:** free web chats through `use-llms`, or a cheap API.
- **Final-run tier:** only after pilots pass.

## 3. Set up
Keys in `.env` (git-ignored). One `call_model()` wrapper in `src/scripts/` that logs provider, exact model name and version, temperature, max tokens, seed, date, tokens used, and cost into `experiment_logs/`. Run a 3-prompt smoke test before anything big.

## 4. Control cost
Estimate before big runs: items × tokens × current price (look prices up; don't guess). Set a spending cap. Pilot on 5% or less first.

## 5. Reproducibility and privacy
Pin the exact model identifier and record the date (hosted models change and get retired). Use fixed settings where possible; save prompts in `src/prompts/` and keep raw outputs. Private data → local model only; check each provider's data policy.

## 6. No access?
Offer free tiers, a small local model, or university compute, and keep the design runnable at small scale (pilot first).

## 7. Free-tier router (optional, e.g. FreeLLMAPI)
A self-hosted proxy such as FreeLLMAPI stacks many providers' free tiers behind one OpenAI-compatible endpoint. It is handy for pilots, prompt debugging, and draft labeling. For research, add these guardrails:
- **Pin the model.** Never report results from an `auto` router setting; it can switch models between calls. Name an exact model and log the actual provider and model for every call.
- **Pilots and drafts only.** Final reported runs use stable, pinned access (your own key or a local model); free tiers change, rate-limit, and get retired.
- **Check each provider's terms.** Some free tiers are evaluation-only or non-commercial; confirm yours allows research use.
- **No private data.** Prompts go to third-party providers; keep participant and confidential data on a local model.
- **Keys in `.env`, never in git.** Read the project's current docs first: its catalog and limits change often, and it also has a paid tier. It typically needs Docker or its desktop app. Review any third-party skill or install script before running it.
