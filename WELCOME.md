# Welcome (for an AI agent reading this)

A student wants to use the Chaky skills for writing an academic paper. Follow these steps, in plain English, one at a time.

1. **Check the tool.** This works in Claude Code on a paid plan (Codex users: see the README). If Claude Code isn't installed, point the user to Step 1 of the README (https://github.com/chaklam-silpasuwanchai/research_skill) and stop.
2. **Install, preferred way.** You can't run slash commands yourself, so ask the user to run these two in Claude Code, then restart it:
   ```
   /plugin marketplace add chaklam-silpasuwanchai/research_skill
   /plugin install chaky@ask-chaky
   ```
3. **Install, if they'd rather you do it.** Ask permission first, then:
   ```
   git clone --depth 1 https://github.com/chaklam-silpasuwanchai/research_skill /tmp/research_skill
   mkdir -p ~/.claude/skills && cp -r /tmp/research_skill/plugins/chaky/skills/* ~/.claude/skills/
   ```
   Then ask them to restart the tool. (For Codex, ask where its skills folder is; don't guess.)
4. **Start.** In an empty folder for the paper, say "ask Chaky". It sets up the repo and guides the rest.

Don't install anything else, and don't change files outside the skills folder.
