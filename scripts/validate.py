#!/usr/bin/env python3
"""Validate the Chaky skill repo. Run: python scripts/validate.py  (needs: pip install pyyaml)"""
import json, re, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Install PyYAML first: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins" / "chaky" / "skills"
CORE = {"guide-me", "setup-repo", "brain-dump", "check-board", "validate-idea", "plan-method",
        "write", "review"}
OLD_NAMES = ["research-guide", "research-start", "research-ideation", "research-implementation",
             "research-storytelling", "chaky-reviewer", "pre-submission-check", "literature-snowballing",
             "elegant-writing", "paper-statistics", "find-related-work", "write-elegantly", "run-stats",
             "plan-llm-access", "ask-outside-ai", "code-reproducibly"]
OLD_BARE = ["setup", "ideate", "implement", "storytell"]
OLD_NAMES += ["start-paper", "plan-tickets", "tidy-board", "shape-idea", "run-study", "write-paper", "review-paper", "polish-prose", "analyze-results", "use-llms", "teach-chaky", "grill-me", "write-code"]
OLD_NAMES += ["ask-chaky", "map-research", "watch-scoops", "triage-paper", "unslop-prose", "pick-models", "ask-chatbots", "analyze-data", "make-figures", "check-submission"]
errors, warns = [], []
def err(m): errors.append(m)
def warn(m): warns.append(m)

names = []
for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    f = d / "SKILL.md"
    if not f.exists():
        err(f"{d.name}: SKILL.md missing"); continue
    text = f.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(f"{d.name}: no frontmatter"); continue
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        err(f"{d.name}: invalid YAML header ({str(e).splitlines()[0]})"); continue
    name, desc = fm.get("name"), fm.get("description", "")
    names.append(d.name)
    if name != d.name: err(f"{d.name}: name '{name}' != folder")
    if not re.fullmatch(r"[a-z]+(-[a-z]+){0,2}", d.name): err(f"{d.name}: name must be a lowercase verb, optionally with one or two hyphenated words (write, check-board, setup-writing-style)")
    if not desc or len(desc) > 1024: err(f"{d.name}: description missing or over 1024 chars")
    if "Use " not in desc: warn(f"{d.name}: description has no 'Use ...' trigger phrase")
    words = len(text.split())
    if words > 900: err(f"{d.name}: {words} words (limit 900)")
    elif words > 800: warn(f"{d.name}: {words} words (getting long)")
    for ref in re.findall(r"references/[\w\-]+\.md", text):
        if not (d / ref).exists(): err(f"{d.name}: mentions missing file {ref}")
    for old in OLD_NAMES:
        if f"`{old}`" in text: err(f"{d.name}: stale skill name `{old}`")
    for old in OLD_BARE:
        if f"`{old}`" in text: err(f"{d.name}: stale skill name `{old}`")

# README and AGENTS template list every skill
readme = (ROOT / "README.md").read_text()
agents = (SKILLS / "setup-repo" / "assets" / "AGENTS.template.md").read_text()
for n in names:
    if f"`{n}`" not in readme: err(f"README.md does not list `{n}`")
    if n not in CORE and f"`{n}`" not in agents: err(f"AGENTS template Supporting skills does not list `{n}`")

# versions agree
pv = json.loads((ROOT / "plugins/chaky/.claude-plugin/plugin.json").read_text())["version"]
mv = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["plugins"][0]["version"]
cl = re.search(r"^## (\d+\.\d+\.\d+)", (ROOT / "CHANGELOG.md").read_text(), re.M)
if not (pv == mv == (cl.group(1) if cl else None)):
    err(f"version mismatch: plugin {pv}, marketplace {mv}, changelog {cl.group(1) if cl else None}")

# trigger phrases point at real skills
tp = ROOT / "tests" / "trigger-phrases.md"
if tp.exists():
    for line in tp.read_text().splitlines():
        m = re.match(r"\|\s*\"[^\"]+\"\s*\|\s*`([a-z\-]+)`\s*\|", line)
        if m and m.group(1) not in names: err(f"trigger-phrases.md: unknown skill {m.group(1)}")

print(f"{len(names)} skills checked, {pv} (plugin = marketplace = changelog)" if not errors else "")
for w in warns: print("warn:", w)
for e in errors: print("ERROR:", e)
sys.exit(1 if errors else 0)
