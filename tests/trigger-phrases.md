# Trigger phrases (which skill should answer)

`scripts/validate.py` checks every skill named here exists. Read this list when two skills seem to overlap.

**Disambiguation:** a *specific paper in hand* → `find-papers` (triage). *Unknown new papers or scoop fear* → `find-papers` (watch). *Related-work search* → `find-papers` (search). *Whole project too big or priorities unclear* → `plan-tickets`. *One idea, plan, or argument feels fuzzy* → `grill-me`. *Text sounds robotic* → `polish-prose` (unslop). *Stats or figures* → `analyze-results`.

| Phrase | Skill |
|---|---|
| "ask Chaky" | `ask-chaky` |
| "what should I do next?" | `ask-chaky` |
| "where am I?" | `ask-chaky` |
| "what can you do?" | `ask-chaky` |
| "show my progress" | `ask-chaky` |
| "progress update for my advisor" | `ask-chaky` |
| "retro" | `ask-chaky` |
| "set up my paper repo" | `start-paper` |
| "I want to start a new paper" | `start-paper` |
| "organize my messy project" | `start-paper` |
| "show the board" | `plan-tickets` |
| "what should I do first?" | `plan-tickets` |
| "rate my priorities" | `plan-tickets` |
| "let me lead" | `plan-tickets` |
| "you drive" | `plan-tickets` |
| "this project is too big to plan" | `plan-tickets` |
| "is this ticket enough?" | `plan-tickets` |
| "help me find a research question" | `shape-idea` |
| "is this idea novel?" | `shape-idea` |
| "sharpen my hypotheses" | `shape-idea` |
| "grill me" | `grill-me` |
| "stress-test my plan" | `grill-me` |
| "plan my experiments" | `run-study` |
| "run a pilot" | `run-study` |
| "freeze my plan" | `run-study` |
| "write my introduction" | `write-paper` |
| "draft the whole paper" | `write-paper` |
| "plan Figure 1" | `analyze-results` |
| "quick review" | `review-paper` |
| "would this pass at CHI?" | `review-paper` |
| "how am I doing?" | `review-paper` |
| "can I submit now?" | `review-paper` |
| "camera-ready checklist" | `review-paper` |
| "anonymize my paper" | `review-paper` |
| "I found a new paper" | `find-papers` |
| "someone already did this" | `find-papers` |
| "any new papers on my topic?" | `find-papers` |
| "am I being scooped?" | `find-papers` |
| "find related work on X" | `find-papers` |
| "make this sound human" | `polish-prose` |
| "remove AI slop" | `polish-prose` |
| "polish this paragraph" | `polish-prose` |
| "which statistical test?" | `analyze-results` |
| "make a figure" | `analyze-results` |
| "what model can I use?" | `use-llms` |
| "help me label data" | `use-llms` |
| "get a second opinion from Gemini" | `use-llms` |
| "help me code this reliably" | `write-code` |
| "my results look suspicious" | `write-code` |
| "always do X" | `teach-chaky` |
| "add a skill for DSPy" | `teach-chaky` |
