# Component files (copy from `assets/`, CHI or NLP variant)
| File | Holds |
|---|---|
| `tickets.md` | The board: destination, mode, fog, tickets with type, 1-5 priority, size, status, done-when. Seeded by `update-board` and rated with the researcher. |
| `terms.md` | One preferred term per concept, in the researcher's own words (they choose when the field's word differs). No synonyms. Chaky uses these in chat as well as in the paper and code. |
| `experimental_design.md` | 3-5 RQs, hypotheses, IVs (baselines), DVs, apparatus. NLP adds extra analyses (error, feature importance, robustness, transfer, feature, what-if). CHI adds participants, task and procedure, design rationale. |
| `implementation.md` | What to build or prepare and status (planned/implemented/tested/dropped), linked to `src/`. CHI: sampling, apparatus, IV, DV instruments. |
| `ideas.md` | Uncommitted ideas for novelty, experiments, analysis. |
| `related_work.md` | Table of **verified** citations grouped by relation to our work. |
| `current_status.md` | Plain-English done / in progress / blocked / next, plus the stage map. |
| `voice.md` | The researcher's writing style (sentence rhythm, voice and tense, favorite signal words, paragraph and hedging habits, recurring English slips they want fixed, keep / change). Learned by reading their past papers; write about 25 lines, never copy passages. |
| `preferences.md` | The researcher's own rules ("always", "never"), one dated line each. Read every session; never overwritten by updates. |
| `log.md` | Append-only story of the project: decisions, dead ends (what, why it failed, lesson), pivots, reflections, each tagged by who (`user` / `ai-suggested` / `ai-executed` / `user-revised`). |

`AGENTS.md` (repo root, where tools look) is the AI entry point and holds the working agreements; `README.md` explains the skill set and says order is flexible.


## Folder trees (create only these)
**ACL/NeurIPS**
```
paper/              manuscript, references, figures, official template
components/         working notes
src/
  prompts/          prompts used
  scripts/          experiments, analysis, tests
  data/             train/ and heldout/ clearly separate
  tests/            code, scoring, data-integrity checks
  experiment_logs/  one record per run: config, outputs, failures, cost
  results/          analysis and figures linked to run IDs
```
**CHI** (add `src/prompts/` only if the study uses AI prompts)
```
paper/  components/
src/
  scripts/          study, analysis, tests
  data/             participant data: ID, when, where, configuration
  experiment_logs/  which session, which participant
  results/          statistics and figures linked to session IDs
```
