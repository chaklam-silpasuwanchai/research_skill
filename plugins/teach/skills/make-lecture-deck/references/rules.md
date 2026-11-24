# Slide rules (from Chaklam's feedback)

Each rule has the comment that taught it, so the reason is clear.

## Words
- **Plain English, complete sentences.** No telegraph style, no consultant shorthand. *"use simple english here....."*
- **Low cognitive load.** One idea per slide; cut text until the point survives. *"too many things to read"*, *"too much to read....can this be stats or graph or diagrams..."*
- **Delete the obvious.** If the audience already knows it, it costs attention. *"it's soooo obvious, why write??? please remember this"*; deleted "higher stakes, lower level", "No confidential data in public chatbots", "Everyone can buy the same model…" (*"delete...useless"*).
- **No unexplained words.** Define or replace: "vendor" → "the AI company (ChatGPT, Claude, Gemini)"; "client" → "customer"; "set workflow" → "many agents working together on one goal"; "GenAI pilot"; "find a cause in data" → "solve a business puzzle" + what the task was. *"i am confused what is vendor and client...."*
- **Explain every number.** What it measures, against what, and whether it is a percentage point or a relative change. *"only 4% gained?"* → "48% vs 44%: about 9% more money back". Say savings the strong way: *"but 2/3 cost reduce!"* → "−67% cost", not "⅓ of the cost". Spell out comparisons: "64% reached a deal: 3× the 20% target".
- **Name things the way people know them.** Use the product's real name and capitalization (Dots, not dots); the term users see in the app ("effort" for thinking level, in **bold**); his own words for titles ("Successful stories").
- **Say the implication.** After any study or chart, one green **So what:** line an executive can act on. *"what is the implication here..."*
- **Insight over description.** Tell executives what they must know (memory compounds value and creates lock-in; tools are where the integration cost sits), not how the feature works. *"write more insightful, something that executives must know"*
- **Don't contradict the audience's sense.** If a finding sounds absurd ("never build in-house"), state it as the source actually does and give the nuance. *"so you don't recommend in-house...it does not make sense"*
- **No hedging labels on the slide** ("Illustrative numbers") — put caveats in the speaker notes.

## Visuals
- **Pictures, charts, big numbers, tables** before text. Replace a text table with a big stat plus a small chart when you can.
- **No square boxes.** Use rounded bands, open layouts, dots on a line, braces.
- **Big fonts.** Body ≥ 28px; tables 30–36px; part-map labels ~42px; when two label sets sit on the same chart (Big/Small, Open/Closed), make them the same size. *"bigger font", "bigger, cannot see", "bigger circle"*
- **Number sequences 1, 2, 3…** whenever there is an order. *"need to say 1, 2, 3, 4, 5"*
- **Braces to show grouping** (e.g. everything in the context window, with the prompt as one part of it). Give braces and diagrams fixed pixel heights so they render the same in every viewer.
- **Animate processes** (fragments, a fly-in for the step that matters), e.g. RAG: retrieve → augment → generate.
- **Prompts in italic.** Key terms in bold.
- **Sources always at the bottom**, just above the footer, on every slide (pin with `margin-top:auto` if nothing else pushes them down). *"reference should always be bottom"*
- Logo and footer on every slide.

## Evidence
- **Every claim gets a source link** on the slide. Books are woven into the slide they support.
- **Search, don't remember**, for anything that changes: model names and versions, context windows, prices (give the *lowest* price to get it), launch dates, adoption numbers. *"i think grok bot is around Sep ?? double check all timeline again"*
- **Double-check timelines and names**; separate companies get separate rows (Meta ≠ xAI).
- **Suspicious numbers get explained or dropped.** Company estimates are labeled as such.
- **Honest caveats** go in one short clause on the slide (e.g. "patient-reported outcomes did not change measurably") and in full in the notes.
- Compute derived numbers yourself and say so in the notes (e.g. "a third as often" → ~22%).
