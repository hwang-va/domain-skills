#!/usr/bin/env bash
# Copy the domain plugin into the public skills repo. Refuses if a company or person name appears.
set -euo pipefail
SRC="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
DEST="${SKILLS_REPO:-$HOME/projects/hw-skills}/plugins/domain"
BLOCK='valitana|vantage|julian|brais|dmitry|gritsai|hwang@|\bhai\b|\bwang\b'
FILES=("$SRC/skills" "$SRC/references" "$SRC/tools/render_register.py" "$SRC/tools/profile_record.py" "$SRC/.claude-plugin/plugin.json")

if grep -rniE "$BLOCK" "${FILES[@]}"; then
  echo "publish-to-skills: blocked, names above. Nothing copied." >&2
  exit 1
fi

rm -rf "$DEST/skills" "$DEST/references" "$DEST/tools" "$DEST/docs"
mkdir -p "$DEST/.claude-plugin" "$DEST/tools"
cp -r "$SRC/skills" "$SRC/references" "$DEST/"
cp "$SRC/tools/render_register.py" "$SRC/tools/profile_record.py" "$DEST/tools/"
cp "$SRC/.claude-plugin/plugin.json" "$DEST/.claude-plugin/"
echo "publish-to-skills: copied to $DEST"
