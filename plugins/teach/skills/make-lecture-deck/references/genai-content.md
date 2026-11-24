# GenAI lecture: content decisions already made

From "Generative AI: The Big Picture" (AIT, Nov 2026). Reuse the framing; re-check every number before teaching.

## Structure
Part 1 the system (Model → Context → Agent → App → Guardrails) · Part 2 the evidence ("Does AI really deliver productivity and money?": adoption → ability → profit → successful stories → patterns) · Part 3 finding a use case → workshop (put four team tasks on a painful × repeatable 2×2).

## Framing that worked
- **Evolution**: timeline with braces for the eras: prompt → context → harness → graph engineering ("many agents working together on one goal").
- **AI is the umbrella**; each term sits inside the last.
- **Models**: two questions on a 2×2: Closed (rent it in the cloud) vs Open (download and run it yourself) × Big vs Small, labels equally big. "Thinking" is a setting called **effort** in ChatGPT and Claude.
- **Prompting**: prompt tricks matter less as models get stronger; context still matters most.
- **Context**: everything the model sees (rules, skills, documents, memory, tool results, prompt) under one brace; the prompt is one small part.
- **Context window**: name the term; 1M tokens ≈ 1,500 pages is the 2026 standard for big models; smaller open models have less (e.g. 128K–256K). In a long chat, early messages fall out and the AI "forgets"; sooner with small models. Tip: start a new chat with a summary.
- **RAG**: Retrieve, Augment, Generate, animated, showing the *augmented* prompt (question + found text). Why not paste everything: too many pages (> 1M tokens), cost, and "Lost in the Middle" (Liu et al., 2023; U-shaped accuracy).
- **Agents**: start with four kinds by autonomy (conversational, copilot, agentic with approval, agentic with *little* approval; no real product runs with zero approval). Then the anatomy: model in the middle + goal, memory, tools, skills, permissions.
- **Tools + MCP together** ("MCP plugs them in", like USB-C). **Skills alone**: a saved prompt, packaged; popular examples from skills.sh relevant to professionals (slides, market research).
- **Memory**: why it matters to executives: value compounds, hard to switch, memories go stale or conflict. Skip obvious permission tables.
- **App modes**: Chat · Work · Always on, by company (one company per row).
- **Coding**: how much code AI writes now (big-tech self-reports) with the caveat.
- **Evidence studies** each end with "So what".
- **MIT 95%**: the cause is tools that don't fit daily work and don't learn ("learning gap"); partnering beat building alone, but "build when AI is your edge"; don't skip the back office.
- **DBS**: explain how a nudge makes money, step by step, and that it lives in the normal banking app.
