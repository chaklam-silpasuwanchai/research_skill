# AI reviewer check (Claude, ChatGPT, Gemini)

Many reviewers now paste papers into an AI before writing their review. If Claude, ChatGPT, and Gemini don't think the paper is acceptable, human reviewers likely won't either. Run this before sharing or submitting.

## Safety first (critical: ask first)
An unpublished paper is confidential. Use an **anonymized** draft, turn off "use my data for training" (or use a paid or institutional account with that guarantee), and follow the lab's AI-use policy. Unsure → don't paste.

## Run it
The student pastes the same anonymized PDF or text into **three fresh chats** (Claude, ChatGPT, Gemini) with this prompt, then pastes each answer back (or saves to `components/ai_reviews.md`, overwritten each time):

> You are a rigorous reviewer for [venue]. Review this paper as you would for the real conference. Give: a summary; strengths; weaknesses (quote the sentences you criticize); idea novelty and technical novelty against the closest work you know (name papers); validity (confounds, unfair baselines, wrong measures, over-claiming); clarity; a score on the venue's scale; accept or reject, with the 3 changes that would most change your decision.

## Read the results
```
AI reviewers   Claude 4/5 accept · ChatGPT 3/5 borderline · Gemini 2/5 reject
Shared weak points: novelty vs. Lee 2023 unclear (all 3) · small sample (2 of 3)
Pass: ❌ (needs all three at accept or weak accept)
```
- **Pass** = all three at accept or weak accept on the venue's scale.
- Points raised by **2-3 AIs** are the priority: they are what human reviewers will probably raise too. Make them tickets.
- **Verify every paper they name** before acting on it; AIs invent or misremember papers.
- Mark each point agree / disagree / unsure with a reason; disagree only with evidence.
- These reviews don't change Chaky's own test scores; they are a second gate. Log decisions and who made them.
