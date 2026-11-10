# Submission and camera-ready check

Catch avoidable problems that cause desk rejection or embarrass after acceptance. Mostly mechanical; quality judgement belongs to `review`.
**Needs:** paper draft in `paper/`, venue in `AGENTS.md`. A recent review helps; if none, recommend one first.

## 1. Get the current rules
Rules change yearly; don't use memory. Search the venue's **current-year call for papers and author guidelines** and extract: length limits (and what counts), template version, anonymity, required sections/statements/checklists, AI-use disclosure, supplement and artifact policy, dual-submission rules, deadlines (abstract and paper may differ). Save links in `components/submission_checklist.md`. Unfound rule → say so and ask.

## 2. Run the checklist (✅ / ❌ / ➖ with location)
**Format:** this year's official template, unmodified; compiles cleanly, fonts embedded; within length; metadata matches the submission form.
**Anonymity (if double-blind):** no names, affiliations, acknowledgements (also in PDF metadata); neutral self-citations; no identifying links (anonymous artifact links); no identifying names or paths in figures and logs.
**Content:** no generic AI-sounding phrasing left (`write` count); no `TODO`, `[CITE?]`, `??`, `XXX`; every reference exists, is verified, and its BibTeX was fetched, not typed from memory; terms match `terms.md`; numbers match across abstract, results, discussion; every figure and table referenced, legible, self-captioned, with venue-required accessibility items; limitations concrete; claims match evidence.
**Required statements:** every venue-required section, statement, or checklist (limitations, ethics, reproducibility, etc.; confirm against current rules); human-subjects ethics approval/exemption, consent, data handling; LLM/AI-use disclosure per policy (draft it from the `who` tags in `components/log.md`: what the AI suggested vs executed vs the user decided); accurate data and code availability.
**Artifacts and repo:** shared code and data cleaned, documented, runnable, licensed; no secrets, keys, or identifying/protected data in the repo or git history; logs and results support every number; plan-freeze deviations from `log.md` are disclosed in the paper; analysis scripts rerun.
**Process:** `review` run on this draft with open 🔴 items resolved or consciously accepted; co-authors approved; advisor sign-off if the Lab defaults require it; track and subject area chosen; deadlines in the user's time zone with a buffer.

## 3. Report
Plain English: **blockers**, **should-fix**, **nice-to-have**. Offer to fix what you can (placeholders, template, anonymity leaks, references). Ask: "Which blocker first?" Update the stage map.

## Camera-ready
Re-read the reviews, confirm every promised change, switch to the de-anonymized camera-ready template, add authors, acknowledgements, funding, final artifact links, and rerun the checklist with camera-ready rules.

## Where problems go
Missing evidence or non-reproducible result → `plan-method`. Text or consistency → `write`. Novelty or validity doubts → `review`, then that skill.
