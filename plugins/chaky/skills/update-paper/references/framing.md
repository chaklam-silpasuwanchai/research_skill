# Framing the method (abstract, introduction, contributions)

Make the technical depth visible in plain words, and always state a clear novelty claim.

1. **What it estimates and how, in one sentence:** "X probabilistically estimates <quantity> via <model>, and chooses <decision> by <criterion>."
2. **Why the problem is hard:** name 2-4 concrete properties, each with one plain reason. Example: "checking does not teach: a check only reveals what is already understood".
3. **How the method handles each one,** in the same order: which part of the method, and how it works.
4. **One or two measured strengths,** such as speed, cost, or interpretability. Measure them first (a script and a number in `results/`); never state an unmeasured number.
5. **Claim novelty explicitly,** for the method and for any new evaluation. A plain combination of known parts is not novel, but a new combination is: one aimed at a new target, built to handle a difficulty no earlier work faced, or producing a capability no earlier system has. Credit the known parts in one sentence, then say what is new: "What is new is how we combine them: to our knowledge, X is the first <system> that <specific capability>."
6. **Search before claiming:** look for the closest recent work (top venues and recent preprints) and check that none already does it (`papers.md`). Make the "first" as specific as it needs to be to be true, and keep "to our knowledge". If a close paper exists, cite it and narrow the claim. Never make a claim the search contradicts. Log the search (terms, date, closest papers) in `related_work.md`.

**Before finishing, match the method section exactly.** Every verb in the framing must match what the method actually does. If the method scores understanding, the introduction must not say it predicts the decision. Check each sentence of the abstract, introduction, and contributions against the method section; fix the framing, not the method.
