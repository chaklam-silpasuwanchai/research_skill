# Cleanup (used by `update-repo`)

Keep the project lean so the student (and Chaky) can find things. Two kinds of clutter:

## 1. Safe junk: just clean it, then tell
Rebuildable or system files. Delete them, make sure `.gitignore` covers them, and untrack any that were committed (`git rm --cached`).
- caches: `__pycache__/`, `*.pyc`, `.ipynb_checkpoints/`, `.cache/`
- LaTeX build files: `*.aux`, `*.log`, `*.out`, `*.toc`, `*.synctex.gz`, `*.fls`, `*.fdb_latexmk`, `*.blg`, `*.bbl` (keep the `.bib`)
- OS and editor files: `.DS_Store`, `Thumbs.db`, `~$*` temp files
- empty folders not in the standard layout

## 2. Their work: suggest, then ask (critical)
List each with a suggested action; move or delete only after a yes. Never touch `components/`, `paper/*.tex`, `.bib`, `src/data/`, or `preferences.md` without asking.
- **Stray files in the root** → their home (`notes.txt` → `components/ideas.md`, `test.py` → `src/scripts/`).
- **Version copies** (`_v2`, `final`, `final_final`, `copy`, `old`, dated duplicates): keep the newest; git keeps history.
- **Unused files:** scripts, notebooks, or figures nothing refers to (not in the paper, `results/`, or the logs).
- **Big files in git** (over ~5 MB, models, datasets): move out of git, add to `.gitignore`, note where they live in `implementation.md`.
- **Secrets or participant data in git:** stop and ask; removing them from history needs care.

## 3. Working files
Just tidy (easy to undo): merge duplicate rows in `related_work.md` and `ideas.md`; move old **Done** tickets (over ~30) into one summary line per month; remove empty template rows.

## Report
```
Cleaned: 14 LaTeX build files · 3 __pycache__ · 2 empty folders (.gitignore updated)
Asks: notes.txt → components/ideas.md? · method_v2.tex and method_final.tex → keep the newest? · model.pt (420 MB) out of git?
```
