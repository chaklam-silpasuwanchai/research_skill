# Validating AI-based measures (used by `plan-method`)

**When it applies:** the study measures with an AI tool such as a simulated user, an LLM judge, a tracker, or a checker. Check the tool before the experiment, the same way a scale gets validated before it is used.

1. **Test against labels first.** Before any tuning, write a fixed rule: what you compare, on which items, and the pass mark (e.g. ">= 90% on items all labellers agree on"). Never change labels or the pass mark after a run. A changed gate is reported as a change, with the reason.
2. **Three labellers, labels committed first.** One AI labels and commits. Two more label in fresh chats, each part in a new chat. The majority is final, and items all three agree on are "clear". Labellers see only blinded packets, never the tool's own output.
3. **Report it the MT-Bench way** (Zheng et al., NeurIPS 2023). Compare tool-vs-labeller agreement with labeller-vs-labeller agreement on the same items, as well as giving a single score.
4. **Trace every error to its cause before fixing it.** Ask whether it is a software bug (parsing, wrong input, a tag that is too loose), a measurement design problem (one big judgement where small yes/no questions would do), or a limit of the model. Fix the first two at the root, never by capping. Record the third and stop.
5. **Probe before adopting.** Test a wording change on every labelled case of every development set, for every model, and keep it only if no set gets worse. An idea that sounds better (e.g. reason-first output) is kept only if the probe shows a gain.
6. **Let code decide what code can decide.** Settle what follows from recorded facts in code. Ask the LLM only small yes/no questions, each with a word-for-word quote as evidence.
7. **Finish with a fresh held-out check.** Run new chats on profiles the fixes never saw, chosen by a fixed random seed. Commit the plan before generating anything. Scores on development sets are tuned results, not evidence. Cases you already fixed are development data (`rigor.md`).
8. **Keep every round.** Save each round's change, cause, probe, and score, including the failures. In the paper, report the rounds and the final fresh check.
