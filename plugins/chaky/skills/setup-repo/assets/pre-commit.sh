#!/bin/sh
# Chaky pre-commit guard: blocks secrets, participant data, and very large files.
# Override only when you are sure: git commit --no-verify
bad=0
files=$(git diff --cached --name-only --diff-filter=ACM)
for f in $files; do
  case "$f" in
    .env|.env.*|*.pem|*.key|*consent*|*.mp4|*.wav|*.mov|src/data/raw/*|src/data/identifiable/*)
      echo "BLOCKED: $f looks like a secret, consent form, recording, or participant data"; bad=1;;
  esac
  if [ -f "$f" ]; then
    size=$(wc -c < "$f")
    if [ "$size" -gt 5000000 ]; then echo "BLOCKED: $f is larger than 5 MB"; bad=1; fi
  fi
done
if git diff --cached -U0 | grep -E '^\+' | grep -E -q 'sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----|[Aa][Pp][Ii][_-]?[Kk][Ee][Yy][[:space:]]*[:=][[:space:]]*[A-Za-z0-9_-]{16,}'; then
  echo "BLOCKED: staged changes look like they contain an API key or private key"; bad=1
fi
if [ "$bad" -eq 1 ]; then echo "Commit stopped. Remove the item, add it to .gitignore, or say "guide me"."; exit 1; fi
exit 0
