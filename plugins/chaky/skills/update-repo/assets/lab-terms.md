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

## Study words we use often
| Term | Plain meaning |
|---|---|
| **Conditions** | The versions of the study people experience (one per IV level, or combination of levels). |
| **Participants** | The people who take part. |
| **Apparatus** | The equipment and software used to run the study. |
| **Trials** | Single attempts at the task. |
| **Blocks** | Groups of trials run together, often one condition per block. |
| **Pilot study** | A small trial run to check the study works before the main one. |
| **Experiments** | The main studies that test the hypotheses. |
| **Analyses** | The statistical or qualitative work on the results. |
| **Design rationale** | Why the system or interface is designed the way it is. |
| **Study rationale** | Why the study is designed the way it is (conditions, measures, task). |
| **LLM judge** | An LLM that scores or labels outputs; check it against humans on a sample. |
| **Hypothesis (H1, H2...)** | A testable prediction, written before seeing results. |
| **Discussion** | The section that explains what the results mean, their limits, and implications. |

## More study terms
| Term | Plain meaning |
|---|---|
| **Research question (RQ1, RQ2...)** | The specific question the study answers. |
| **Task** | What participants (or the model) are asked to do. |
| **Procedure** | The steps of a session, in order. |
| **Questionnaire** | A set of written questions participants answer. |
| **Likert scale** | A rating scale, e.g. 1 (strongly disagree) to 7 (strongly agree). |
| **Think-aloud** | Participants say their thoughts while doing the task. |
| **Wizard-of-Oz** | A person secretly plays the system's role to test an idea before it is built. |
| **Simulated users / personas** | AI-generated or described users that stand in for real ones. |
| **Usability (SUS)** | How easy a system is to use, measured with the System Usability Scale. |
| **Workload (NASA-TLX)** | How demanding a task feels, measured with the NASA Task Load Index. |
| **Task time, accuracy, error rate** | How long, how correct, and how often wrong. |
| **Ground truth / gold labels** | The correct answers we compare against. |
| **Control condition** | The "no change" or standard version we compare against. |
| **Manipulation check** | A quick check that the conditions really felt different to participants. |
| **Exclusion criteria** | Rules, set before the study, for which data we drop (e.g. failed attention checks). |
| **Informed consent** | Participants agree, knowing what the study involves. |
| **Pre-registration** | Writing down hypotheses and analysis publicly before collecting data. |
| **Order effect** | Results change because of the order of conditions, not the conditions; counterbalancing fixes it. |
| **Novelty effect** | People like something just because it's new. |

## More analysis terms
| Term | Plain meaning |
|---|---|
| **Effect size** | How big the difference is, not just whether it exists (e.g. Cohen's d). |
| **p-value / significance** | How surprising the result would be if there were no real effect. Say "significant" only after a statistical test. |
| **Post-hoc test** | Follow-up comparisons after a main test (which conditions differ), with a correction for running many comparisons (e.g. Holm, Tukey). |
| **Confidence interval** | The range the true value likely falls in. |
| **Inter-rater agreement (Cohen's kappa)** | How much two labelers (people or LLM judges) agree. |
| **Semi-structured interview** | An interview with planned questions plus follow-ups. |
| **Thematic analysis** | Finding patterns in qualitative data: **codes** (labels on quotes) grouped into **themes**. |
| **Prompt, temperature** | The instruction given to an LLM; how random its output is. |
| **Hallucination** | An LLM stating things that aren't true. |
| **Human evaluation** | People judging outputs, often to check an LLM judge or a metric. |
| **Error analysis** | Looking at where and why the system fails. |
| **Benchmark** | A standard dataset and task used to compare systems. |

## Writing terms
**contribution** (what the paper adds) · **research gap** (an open question in the field, not just in our reading) · **design implications** (what designers should do, given the results) · **limitations** · **future work**.

## Writing verbs we use
**propose** (a new method or design) · **investigate** (test a question) · **explore** (open-ended, exploratory work) · **develop** (build a system or tool) · **hypothesize** (state a prediction).

## Avoid, or explain in plain words
| Don't say | Say instead |
|---|---|
| smoke run | quick test run (or pilot, if it's with people) |
| fitting | training the model, or estimating the statistical model |
| replay | re-running a saved session or log |
| held-out set | test set |
| novel | say what is new, specifically |
| leverage, utilize | use |
| robust | only if robustness was tested; say against what |
| significant | only after a statistical test; otherwise "large" or "clear" |

## Analysis and validity
| Term | Plain meaning |
|---|---|
| **Statistical analysis** | The test that answers the hypothesis (t-test, ANOVA, regression, mixed-effects models), with effect sizes, confidence intervals, and assumption checks. No default: choose from the design and the data. |
| **Internal validity** | Did the IV really cause the change in the DV? (confounds, controls, randomization, counterbalancing) |
| **Construct validity** | Did we measure the concept we claim? (operational measures, validated scales) |
| **External validity** | Where should the result hold? (participants, tasks, settings, culture) |

## Contribution types
Experimental · Design research · Artifact or system · Exploratory qualitative · Model or dataset. What each must show: `plan-method` (contribution types).
