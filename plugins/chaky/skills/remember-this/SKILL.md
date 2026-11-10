---
name: remember-this
description: Makes repeated instructions permanent preferences, or adds a supporting skill such as DSPy. Use for "always do X", "remember this", "from now on", "add a skill", or when you give the same correction twice.
---

# Remember This

## A. Learn from what the user keeps saying
**Detect:** the same instruction or correction twice, or "always", "never", "from now on".
**Ask once:** "You've told me *X* twice. Make it permanent?" Then, by their choice:
- **This paper only** → add one dated line under *My preferences* in `AGENTS.md`, tagged `user`.
- **All my papers** → add it to their personal instructions file (for Claude Code, `~/.claude/CLAUDE.md`). Ask permission before touching anything outside the repo.
- **Improve Chaky for everyone** → draft a note shaped like the repo's *Skill feedback* issue form (skill, what happened, what you expected, proposed wording) for the user to paste into a GitHub issue or send to the maintainer. Don't edit installed plugin skills; updates would overwrite them.

Rules: never generalize from one occurrence; one sentence per preference; no personal or sensitive details; if it conflicts with a working agreement in `AGENTS.md`, say so and let the user decide.

## B. Add a supporting skill (for example DSPy)
Supporting skills are tools Chaky suggests when a task matches; the researcher chooses. They never change the core flow.
1. **Ask:** what is it; when would a paper need it; which skill would suggest it (`plan-method`, `write`, ...); what source material exists (docs, the user's notes)?
2. **Adopt or write.** If a good skill already exists, borrow ideas in your own words and credit it. Don't copy large skills whole.
3. **Write it lean** (about 150 lines max): `name` (verb-noun, two words, hyphenated, like `check-board`, or a single verb like `write`), a `description` with what it does, when to use it, and plain-language trigger phrases (no colons, which break the YAML header); then when to use, steps, pitfalls, what to log (rationale, run IDs), and how it ties to `experimental_design.md` and `implementation.md`. Move long material to `references/`.
4. **Register it:** add one line under *Supporting skills* in `AGENTS.md` (name, when to use, called by). Skills read that list and suggest a matching skill.
5. **Ship it** (maintainer): add it to the README skills table and `CHANGELOG.md`, and bump the minor version in `plugin.json` and `marketplace.json`.
   **Versions:** `0.MINOR.PATCH` until the skills have been tested with real students, then `1.0.0`. Bump MINOR for a new skill or changed behavior, PATCH for wording and bug fixes. After 1.0, a rename or removal is MAJOR.
6. **Test** with a small dry-run task and log the result.

Only need it for one paper? Put it in the project's `.claude/skills/` instead of the plugin.
