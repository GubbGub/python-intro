#!/usr/bin/env bash
# Rebuild lessons.js from the lesson READMEs, then commit and push.
# Usage: ./publish.sh "what changed"
set -e
cd "$(dirname "$0")"
python build.py
git add -A
git commit -m "${1:-Update course}"
git push
