# How Chaky works

**You lead; Chaky suggests.** Say "guide me" (`guide-me`) and Chaky reads your project and **board**, tells you what needs attention, and **suggests** which skill could help. You choose. Inside a task, Chaky just makes the change and tells you in one line ("say *undo* to reverse it"); it asks first only for critical steps (deleting or moving files, freezing the plan, pushing, participants and ethics, spending money, pasting data into free AI chats, submitting).

Work happens in **tickets**; each has a 1-5 priority Chaky sets (you can change it) and a "done when". The paper is a living draft: `update-paper` keeps it in step, and `review` checks it often.

```mermaid
flowchart TD
  G([guide-me]) -->|suggests, you choose| B[update-board: recap, tasks, priorities]
  S[update-repo · setup-writing-style] --> B
  B --> D[brain-dump: get it out of your head]
  B --> V[read-papers: search, 10-15 closest, what to copy, one difference]
  B --> M[plan-method: IV, DV, sample size, models, pilots, runs]
  B --> W[update-paper: story first, then sections]
  B --> R[review: 3 reviewers, easy and difficult fixes]
  D --> B
  V --> B
  M --> B
  W --> B
  R -->|Major fixes become tickets| B
  M -. results contradict .-> V
  subgraph anytime[Any time]
    T[think-deeply-and-learn-from-other-papers: 360°, better solution?]
    C[clarify: say it plainly]
    E[teach-me: step by step]
    P[speak-plainly: plain from now on]
  end
```

**Two ways to lead:** "you drive" (Chaky suggests the top task each time) or "let me lead" (Chaky shows your top tasks and waits). Either way you pick.

**Every skill takes an optional focus:** `/update-paper abstract`, `/plan-method IV`, `/read-papers <idea>`, `/review citations`, `/teach-me <topic>`.

**Where things live in your project**
- `components/tickets.md`: the board (destination, fog, tickets)
- `components/current_status.md`: the stage map and plain-English status
- `components/log.md`: decisions, dead ends, pivots (who decided each)
- `components/review.md`: the latest review and its history
- `components/voice.md` and `terms.md`: your writing style and your words
- `AGENTS.md`: the rules every skill follows (and your lab's defaults)
