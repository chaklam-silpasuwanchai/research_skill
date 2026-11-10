#!/usr/bin/env python3
"""Check a student project folder created by update-repo. Usage: python tests/check_project.py <dir> --type chi|nlp"""
import re, sys
from pathlib import Path

args = sys.argv[1:]
if not args or "--type" not in args: sys.exit(__doc__)
root = Path(args[0]); kind = args[args.index("--type") + 1]
errs, warns = [], []
common = ["paper", "components", "src", "src/scripts", "src/data", "src/experiment_logs", "src/results"]
extra = {"chi": [], "nlp": ["src/prompts", "src/tests"]}[kind]
allowed_top = {"paper", "components", "src", ".git", ".gitignore", "README.md", "AGENTS.md", "CLAUDE.md"}
for d in common + extra:
    if not (root / d).is_dir(): errs.append(f"missing folder {d}")
for f in ["tickets", "terms", "experimental_design", "implementation", "ideas", "related_work", "current_status", "log", "voice"]:
    if not (root / "components" / f"{f}.md").is_file(): errs.append(f"missing components/{f}.md")
for t in root.iterdir():
    if t.name not in allowed_top and not t.name.startswith("."): warns.append(f"unexpected top-level item {t.name}")
for p in root.rglob("*"):
    if ".git" in p.parts: continue
    if re.search(r"(_v\d+|_final|_copy)\b", p.stem): warns.append(f"version-style filename {p.relative_to(root)}")
a = root / "AGENTS.md"
if not a.is_file(): errs.append("missing AGENTS.md")
else:
    t = a.read_text()
    for must in ["Working agreements", "End of every task", "Supporting skills", "nine mindsets"]:
        if must not in t: errs.append(f"AGENTS.md lacks '{must}'")
c = root / "CLAUDE.md"
if not c.is_file() or "@AGENTS.md" not in c.read_text(): errs.append("CLAUDE.md must contain @AGENTS.md")
g = root / ".gitignore"
if not g.is_file() or ".env" not in g.read_text(): errs.append(".gitignore must ignore .env")
cs = root / "components" / "current_status.md"
if cs.is_file() and cs.read_text().count("|") < 20: errs.append("current_status.md has no stage map")
print("OK" if not errs else "\n".join("ERROR: " + e for e in errs))
for w in warns: print("warn:", w)
sys.exit(1 if errs else 0)
