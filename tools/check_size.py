#!/usr/bin/env python3
"""
FILE:    check_size.py
MODULE:  tools
PURPOSE: Compares a built APK/AAB (arg 1) against download_mb in tools/budgets.json; fails if over.
DEPENDS: tools/budgets.json
USED BY: CI
NOTES:   Measures file size only. RAM/battery/latency are measured on devices (docs/spikes, MVP perf task M-27).
"""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
budget = json.loads((ROOT / "tools" / "budgets.json").read_text())["download_mb"]
if len(sys.argv) < 2: sys.exit("usage: check_size.py <apk-or-aab>")
mb = pathlib.Path(sys.argv[1]).stat().st_size / 1_048_576
print(f"{sys.argv[1]}: {mb:.1f} MB (budget {budget} MB)")
sys.exit(0 if mb <= budget else 1)
