# Trigger phrases (which skill should answer)

`scripts/validate.py` checks every skill named here exists. Read this list when two skills seem to overlap.

**Disambiguation:** a *specific paper in hand* → `update-paper` (triage). *Unknown new papers or scoop fear* → `update-paper` (watch). *Related-work search* → `update-paper` (search). *Recap, missing tasks, priorities* → `update-board`. *Get what's in my head out* → `brain-dump`. *Is it novel or valid* → `update-paper`; *harder 360° look* → `think-deeply`. *Answer hard to read* → `clarify`; *still lost* → `teach-me`. *Text sounds robotic, stats, figures* → `update-paper`.

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
| "read the closest papers" | `update-paper` |
| "how do others do this kind of study?" | `update-paper` |
| "what can I copy from other papers?" | `update-paper` |
| "how are we different?" | `update-paper` |
| "is this idea novel?" | `update-paper` |
| "is this publishable at CHI?" | `update-paper` |
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
| "write my introduction" | `update-paper` |
| "draft the whole paper" | `update-paper` |
| "plan Figure 1" | `update-paper` |
| "quick review" | `review` |
| "would this pass at CHI?" | `review` |
| "check my citations" | `review` |
| "write my limitations" | `update-paper` |
| "reply to the reviewers" | `update-paper` |
| "how am I doing?" | `review` |
| "can I submit now?" | `review` |
| "camera-ready checklist" | `review` |
| "anonymize my paper" | `review` |
| "I found a new paper" | `update-paper` |
| "someone already did this" | `update-paper` |
| "any new papers on my topic?" | `update-paper` |
| "am I being scooped?" | `update-paper` |
| "find related work on X" | `update-paper` |
| "search for papers on my topic" | `update-paper` |
| "what method can I borrow?" | `update-paper` |
| "make this sound human" | `update-paper` |
| "remove AI slop" | `update-paper` |
| "polish this paragraph" | `update-paper` |
| "which statistical test?" | `update-paper` |
| "make a figure" | `update-paper` |
| "what model can I use?" | `plan-method` |
| "set up OpenRouter" | `plan-method` |
| "run a local LLM" | `plan-method` |
| "help me label data" | `plan-method` |
| "get a second opinion from Gemini" | `review` |
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
| "what is my paper's story?" | `update-paper` |
| "update the paper" | `update-paper` |
| "clean up my repo" | `update-repo` |
| "this doesn't sound like me" | `setup-writing-style` |
| "I suspect someone already did this" | `update-paper` |
| "would ChatGPT accept this paper?" | `review` |
| "check my paper with Claude, ChatGPT, and Gemini" | `review` |
