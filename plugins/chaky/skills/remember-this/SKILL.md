---
name: remember-this
description: Makes a repeated instruction permanent, or adds a new supporting skill such as DSPy. Use for "always do X", "remember this", "from now on", "add a skill", or when you give the same correction twice.
---

# Remember This

## A. Make it permanent
Same instruction twice, or "always", "never", "from now on" → ask once: "Make *X* permanent?" Then:
- **This paper** → one dated line under *My preferences* in `AGENTS.md`.
- **All my papers** → their personal file (Claude Code: `~/.claude/CLAUDE.md`); ask before editing outside the repo.
- **Everyone using Chaky** → draft a *Skill feedback* issue (skill, what happened, expected, proposed wording) for them to post.
Never generalize from one time. If it clashes with `AGENTS.md`, say so; they decide.

## B. Add a skill
1. Ask what it does, when a paper needs it, and what docs exist. A good skill already exists → borrow ideas in your own words, credit it.
2. Write it lean (under ~300 words): a verb-noun `name`, a `description` with plain trigger phrases (no colons), then steps and what to log. Long material → `references/`.
3. One paper only → the project's `.claude/skills/`. Otherwise add a line under *Supporting skills* in `AGENTS.md`; maintainers also update the README and CHANGELOG.
4. Test on a small task; log the result.
