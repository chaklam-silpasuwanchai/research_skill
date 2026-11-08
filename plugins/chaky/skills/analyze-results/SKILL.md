---
name: analyze-results
description: Statistics and figures for a paper - tests by variable type, effect sizes, planned vs exploratory analysis, honest accessible plots, and Figure 1. Use for "which test", reporting results, a chart, a plot, or a diagram.
---

# Analyze Results

Two jobs. Pick by what the researcher needs.

## A. Statistics (`references/stats.md`)
Plan before looking: write the analysis plan in `experimental_design.md` first; anything else is exploratory. Pick the test from the variable types, check assumptions, report effect sizes with intervals, correct for multiple comparisons, and recompute every reported number from raw data with a script in `src/scripts/`.

## B. Figures and plots (`references/figures.md`)
Start from the message: what should the reader conclude? One figure, one message. Offer three concepts for Figure 1. Keep plotting scripts in `src/scripts/`, follow the honesty rules (never alter data, bars start at zero, name the interval and n, show missing data), and check the venue's live figure rules.

Log figure choices and analysis deviations in `log.md`.
