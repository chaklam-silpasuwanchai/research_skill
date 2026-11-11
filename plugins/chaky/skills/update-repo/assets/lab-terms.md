# Lab terms (AIT Brain Lab)

The lab maintainer edits this file once. `update-repo` copies it into every project's `components/terms.md` as **Lab terms**, above the student's own terms. Every skill uses these words. The first time a term comes up in a session, give its plain meaning in a few words, e.g. "IV (independent variable, a.k.a. factor: what you change)".

## Research stages
| Stage | Main question | Skills |
|---|---|---|
| Idea generation | Where could a good idea come from? | `brain-dump` |
| Idea refinement | How do we sharpen it? | `brain-dump`, `think-deeply` |
| Idea validation | Is it new and important? | `read-papers` |
| Idea testing | How can we test it convincingly? | `plan-method` |
| Idea storytelling | How do we tell it? | `update-paper`, `review` |

## Variables
| Term | Plain meaning | Example |
|---|---|---|
| **IV** (independent variable, a.k.a. factor) | What we change on purpose. Each value is a **level**. | Agent type: honest vs. persuasive (2 levels) |
| **DV** (dependent variable, a.k.a. measure) | What we measure to see the effect. Its **operational measure** is exactly how it is measured. | Trust, measured with a 7-point validated trust scale |
| **Confounding variable** | Something that can interfere: it changes along with the IV and could explain the result instead. | The honest agent also writes shorter replies |
| **Control variable** | Something we keep the same for everyone. | Same product, same task time |
| **Random variable** | Something we let vary rather than control (not the statistics meaning). | Time of day of each session |
| **Individual differences** | How people differ (age, expertise, personality). Treat as a factor if the question is about them, otherwise as a random variable. Ask which. | Prior experience with chatbots |

## Design
| Term | Plain meaning |
|---|---|
| **Between-subjects** | Each person sees one condition. |
| **Within-subjects** | Each person sees all conditions. |
| **Mixed design** | Some factors between, some within. |
| **Counterbalancing** | Changing the order of conditions so order doesn't explain the result (e.g. Latin square). |
| **Randomization** | Assigning people or orders by chance. |
| **Baseline** | The fair comparison we must beat or match. |
| **Ablation** | Removing one part to see how much it matters. |
| **Leakage** | Test information sneaking into training or design choices. |
| **Train / validation / test** | Data to learn on / tune on / report on, kept separate. |

## Analysis and validity
| Term | Plain meaning |
|---|---|
| **Statistical analysis** | The test that answers the hypothesis (t-test, ANOVA, regression, mixed-effects models), with effect sizes, confidence intervals, and assumption checks. No default: choose from the design and the data. |
| **Internal validity** | Did the IV really cause the change in the DV? (confounds, controls, randomization, counterbalancing) |
| **Construct validity** | Did we measure the concept we claim? (operational measures, validated scales) |
| **External validity** | Where should the result hold? (participants, tasks, settings, culture) |

## Contribution types
Experimental · Design research · Artifact or system · Exploratory qualitative · Model or dataset. What each must show: `plan-method` (contribution types).
