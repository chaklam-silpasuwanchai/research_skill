# Trigger phrases (which skill should answer)

`scripts/validate.py` checks every skill named here exists. Read this list when two skills seem to overlap.

**Disambiguation:** a *specific paper in hand* → `find-papers` (triage). *Unknown new papers or scoop fear* → `find-papers` (watch). *Related-work search* → `find-papers` (search). *Recap, missing tasks, priorities* → `update-board`. *Get what's in my head out* → `brain-dump`. *Is it novel or valid* → `validate-idea`; *harder 360° look* → `think-deeply`. *Answer hard to read* → `clarify`; *still lost* → `teach-me`. *Text sounds robotic, stats, figures* → `write`.

| Phrase | Skill |
|---|---|
| "guide me" | `guide-me` |
| "ask Chaky" | `guide-me` |
| "what should I do next?" | `guide-me` |
| "where am I?" | `guide-me` |
| "what can you do?" | `guide-me` |
| "show my progress" | `guide-me` |
| "progress update for my advisor" | `guide-me` |
| "retro" | `guide-me` |
| "set up my paper repo" | `update-repo` |
| "I want to start a new paper" | `update-repo` |
| "organize my messy project" | `update-repo` |
| "update my repo" | `update-repo` |
| "sync everything with my latest results" | `update-repo` |
| "is my paper up to date?" | `update-repo` |
| "show the board" | `update-board` |
| "what should I do first?" | `update-board` |
| "change my priorities" | `update-board` |
| "let me lead" | `update-board` |
| "you drive" | `update-board` |
| "this project is too big to plan" | `update-board` |
| "is this ticket enough?" | `update-board` |
| "validate my idea" | `validate-idea` |
| "is this idea novel?" | `validate-idea` |
| "is this publishable at CHI?" | `validate-idea` |
| "interview me" | `brain-dump` |
| "grill me" | `brain-dump` |
| "brain dump my study design" | `brain-dump` |
| "help me find a research question" | `brain-dump` |
| "stress-test my plan" | `brain-dump` |
| "plan my experiments" | `plan-method` |
| "what is my IV and DV?" | `plan-method` |
| "how many participants do I need?" | `plan-method` |
| "run a pilot" | `plan-method` |
| "freeze my plan" | `plan-method` |
| "write my introduction" | `write` |
| "draft the whole paper" | `write` |
| "plan Figure 1" | `write` |
| "quick review" | `review` |
| "would this pass at CHI?" | `review` |
| "check my citations" | `review` |
| "write my limitations" | `write` |
| "reply to the reviewers" | `write` |
| "how am I doing?" | `review` |
| "can I submit now?" | `review` |
| "camera-ready checklist" | `review` |
| "anonymize my paper" | `review` |
| "I found a new paper" | `find-papers` |
| "someone already did this" | `find-papers` |
| "any new papers on my topic?" | `find-papers` |
| "am I being scooped?" | `find-papers` |
| "find related work on X" | `find-papers` |
| "what is the closest work to my idea?" | `find-papers` |
| "what method can I borrow?" | `find-papers` |
| "make this sound human" | `write` |
| "remove AI slop" | `write` |
| "polish this paragraph" | `write` |
| "which statistical test?" | `write` |
| "make a figure" | `write` |
| "what model can I use?" | `plan-method` |
| "set up OpenRouter" | `plan-method` |
| "run a local LLM" | `plan-method` |
| "help me label data" | `plan-method` |
| "get a second opinion from Gemini" | `plan-method` |
| "clarify" | `clarify` |
| "that was too technical, say it simply" | `clarify` |
| "think deeply about this" | `think-deeply` |
| "is there a better way to do this?" | `think-deeply` |
| "think 360 about this" | `think-deeply` |
| "give me an example" | `clarify` |
| "teach me power analysis" | `teach-me` |
| "I still do not get it, walk me through it" | `teach-me` |
| "learn my writing style" | `setup-writing-style` |
| "here are my past papers" | `setup-writing-style` |
| "clean up my tickets" | `update-board` |
| "update the board" | `update-board` |
| "recap" | `update-board` |
| "did we forget any tasks?" | `update-board` |
| "is this task still needed?" | `update-board` |
