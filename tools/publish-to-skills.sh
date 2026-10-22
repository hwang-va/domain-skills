#!/usr/bin/env bash
# Copy the domain plugin into the public skills repo. Refuses if a company name appears.
set -euo pipefail
SRC="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
DEST="${SKILLS_REPO:-$HOME/projects/hw-skills}/plugins/domain"
BLOCK='valitana|vantage|julian|brais|dmitry|gritsai|hwang@'

if grep -rniE "$BLOCK" "$SRC/skills" "$SRC/references" "$SRC/tools/render_register.py" "$SRC/tools/profile_record.py" "$SRC/docs/brief-review-level1.md" "$SRC/.claude-plugin/plugin.json"; then
  echo "publish-to-skills: blocked, company names above. Nothing copied." >&2
  exit 1
fi

rm -rf "$DEST/skills" "$DEST/references" "$DEST/tools" "$DEST/docs"
mkdir -p "$DEST/.claude-plugin" "$DEST/docs"
cp -r "$SRC/skills" "$SRC/references" "$DEST/"
mkdir -p "$DEST/tools"
cp "$SRC/tools/render_register.py" "$SRC/tools/profile_record.py" "$DEST/tools/"
cp "$SRC/docs/brief-review-level1.md" "$DEST/docs/"
cp "$SRC/.claude-plugin/plugin.json" "$DEST/.claude-plugin/"
echo "publish-to-skills: copied to $DEST"
