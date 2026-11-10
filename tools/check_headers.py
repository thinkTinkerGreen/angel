#!/usr/bin/env python3
"""
FILE:    check_headers.py
MODULE:  tools
PURPOSE: Fails if any code file (.kt .kts .java .py .js .ts .sh) lacks the standard header
         (FILE/MODULE/PURPOSE) in its first 25 lines.
DEPENDS: none
USED BY: CI, angel-dev agent
NOTES:   Skips build/, .gradle/, node_modules/, .git/.
"""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
EXT = {".kt", ".kts", ".java", ".py", ".js", ".ts", ".sh"}
SKIP = {"build", ".gradle", "node_modules", ".git", ".idea"}
bad = []
for p in ROOT.rglob("*"):
    if p.suffix in EXT and p.is_file() and not (set(p.parts) & SKIP):
        head = "\n".join(p.read_text(errors="ignore").splitlines()[:25])
        if not all(k in head for k in ("FILE:", "MODULE:", "PURPOSE:")):
            bad.append(str(p.relative_to(ROOT)))
if bad:
    print("Missing header in:\n  " + "\n  ".join(bad)); sys.exit(1)
print("headers ok")
