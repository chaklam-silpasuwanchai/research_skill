---
name: setup-writing-style
description: For when the AI doesn't write the way you write. Learns your voice from anything you wrote - one paragraph, past papers, emails, blog posts - and confirms the terms to use throughout the paper, then saves both for update-paper. Use for "this doesn't sound like me", "learn my writing style", "write like me", "here are my past papers", "here is my Google Scholar", or /setup-writing-style [link].
---

# Setup Writing Style

1. **Get samples.** Any of: a **Google Scholar profile link**, past papers, one paragraph written now, emails, blog posts, a thesis chapter (paths, links, or paste; files stay outside the repo).
   - **Scholar link:** list their papers and suggest 2-3 recent **first-author** ones (their own voice). Get the full text from open copies (arXiv, ACL Anthology, open-access pages). Scholar often blocks automated reading: then ask for the PDFs, or use Claude in Chrome if they have it.
   - Co-authored → which parts are theirs? More variety, better notes.
2. **Note their habits** in `components/voice.md` (about 20 lines), each with a short quote: sentence length, "we" and tense, signal words, hedging ("suggests" vs "shows"), how they state the gap, what to **keep**, slips to fix. Academic papers outweigh casual writing for tone; casual writing shows their natural rhythm.
3. **Confirm the terms**, one at a time. The lab terms (IV, DV, confounding variable...) come from `terms.md` and stay; then the 5-10 key words of this paper, each with one meaning and one example. "Which do you prefer: *honest agent* or *truthful agent*?" Note the field's usual word if it differs. Save in `terms.md` with "do not use" synonyms.
4. **Show** the notes, the terms, and one paragraph rewritten in their voice with their terms. Save; "tell me anything that doesn't sound like you."
5. **Refresh** when they edit drafts heavily; their edits show their style. End with the quick sync in `AGENTS.md`.
