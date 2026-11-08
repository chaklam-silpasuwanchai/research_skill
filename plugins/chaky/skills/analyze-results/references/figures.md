# Figures and plots


## 1. Start from the message
Ask: **what should the reader conclude from this figure?** One figure, one message. If you can't say it in a sentence, split or drop it. Then pick the type: comparison → bars or dots with uncertainty; trend → lines; distribution → box/violin/CDF; relationship → scatter; process or system → diagram; interface → annotated screenshot.

**Chart guide:** two groups, one measure → dots or bars with intervals · many groups → sorted dot plot · over time or steps → lines · spread → box, violin, or CDF · relationship → scatter · parts of a whole → a table is often better than a pie · process or system → diagram.

**Honesty rules (never break):**
- Never alter, hide, or invent data to improve a figure. Keep raw data and every transformation (filtering, binning, smoothing, normalization) in the script.
- Bars start at zero; points and lines may use other limits if context is shown.
- Name the interval (SD, SE, CI) and `n`; show raw points when feasible.
- Missing, zero, censored, and excluded data look different. No silent gaps.
- Avoid dual axes and 3D; label log axes; use the same scale across compared panels.
- Check the venue's figure rules from its live official guidance, not memory, and open the exported file to inspect it.

## 2. Figure 1 (the introduction)
Show the problem, the insight, and how our approach changes it. Offer **three alternative concepts** (sketch in words or a rough diagram) and let the user pick.

## 3. Data plots
- Read data from `src/results/` (NLP) or `src/data/` (CHI) and keep the plotting script in `src/scripts/`, so the figure can be regenerated; link it to run or session IDs.
- Label axes with units; show uncertainty (CI or error bars) and `n`; mark baselines clearly; sort for readability.
- One consistent color per condition across all figures; colorblind-safe palette; don't rely on color alone (use markers or line styles too).
- Fonts and sizes match the paper; legible at print size; vector output (PDF or SVG) unless it's a screenshot. Copy final files to `paper/` figures.
- Use matplotlib or seaborn unless the user prefers another tool.

## 4. Diagrams
Ask which tool the user prefers (TikZ, draw.io, Figma, PowerPoint). Keep it simple: few boxes, consistent shapes, left-to-right or top-to-bottom flow, labels in the paper's `terms.md` vocabulary.

## 5. Captions and checks
Caption states the takeaway and how to read it, and makes sense alone. Anonymize screenshots, names, paths, and logos if the venue is double-blind. Venue-required accessibility items (such as alt text) follow the venue rules. Log chosen figure concepts in `log.md`; update the "Paper: figures" row of the stage map.
