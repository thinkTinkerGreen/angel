#!/usr/bin/env python3
"""
FILE:    backlog.py
MODULE:  tools
PURPOSE: CLI over docs/backlog.json (source of truth). Commands: next, show <ID>,
         set <ID> <status>, render (rebuilds docs/BACKLOG.md and missing task cards).
DEPENDS: docs/backlog.json
USED BY: angel-dev agent, humans
NOTES:   Never overwrites an existing task card (keeps hand-off notes).
"""
import json, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB = ROOT / "docs" / "backlog.json"
STATUSES = ["todo", "in-progress", "review", "done", "blocked", "human", "planned"]
READY_DEPS = {"done", "review"}

def load(): return json.loads(DB.read_text())
def save(d): DB.write_text(json.dumps(d, indent=1) + "\n")
def find(d, i):
    for it in d["items"]:
        if it["id"] == i: return it
    sys.exit(f"unknown id {i}")

def cmd_next(d):
    st = {it["id"]: it["status"] for it in d["items"]}
    for it in d["items"]:
        if it["status"] in ("in-progress",):
            print(f'{it["id"]}  {it["title"]}  [in-progress - resume]'); return
    for it in d["items"]:
        if it["status"] == "todo" and all(st.get(x) in READY_DEPS for x in it["deps"]):
            print(f'{it["id"]}  {it["title"]}  (card: docs/tasks/{it["id"]}.md)'); return
    print("No ready task. Check items with status 'human' or 'blocked' in docs/BACKLOG.md.")

def card(it):
    acc = "\n".join(f"- {a}" for a in it["acceptance"]) or "- (define when phase starts)"
    files = "\n".join(f"- `{f}`" for f in it["files"]) or "- (none yet; see docs/CONTEXT_MAP.md)"
    return f"""# {it['id']}: {it['title']}

**Phase:** {it['phase']} | **Priority:** {it['pri']} | **Size:** {it['size']} | **Module:** {it['module']} | **PRD:** {it['prd']}
**Depends on:** {', '.join(it['deps']) or 'none'}

## Open these files only
{files}
(+ `AGENTS.md`, `docs/PROJECT_SUMMARY.md`, `docs/CONTEXT_MAP.md`)

## Goal
{it['goal']}

## Acceptance criteria
{acc}

## Out of scope
Anything not listed above; other modules; later phases.

## Done checklist
Headers - tests - budgets - no idle background work - consent+audit if remote capability - MODULE.md/CONTEXT_MAP/CHANGELOG/backlog updated.

## Hand-off notes
(agent fills in: what changed, what is next, open issues, UNVERIFIED items)
"""

def cmd_render(d):
    rows = ["# Backlog (generated from docs/backlog.json - do not edit by hand)",
            "", "Status: todo, in-progress, review, done, blocked, human (needs device/human), planned", ""]
    phase = None
    for it in d["items"]:
        if it["phase"] != phase:
            phase = it["phase"]
            rows += ["", f"## {phase}", "", "| ID | Item | Pri | Size | Module | Status | Deps |", "|---|---|---|---|---|---|---|"]
        rows.append(f'| {it["id"]} | {it["title"]} | {it["pri"]} | {it["size"]} | {it["module"]} | {it["status"]} | {", ".join(it["deps"])} |')
    (ROOT / "docs" / "BACKLOG.md").write_text("\n".join(rows) + "\n")
    n = 0
    for it in d["items"]:
        if it.get("card"):
            p = ROOT / "docs" / "tasks" / f'{it["id"]}.md'
            if not p.exists(): p.write_text(card(it)); n += 1
    print(f"BACKLOG.md rebuilt; {n} new task cards")

def main():
    a = sys.argv[1:]
    d = load()
    if not a or a[0] == "next": cmd_next(d)
    elif a[0] == "show": print(json.dumps(find(d, a[1]), indent=1))
    elif a[0] == "set":
        if a[2] not in STATUSES: sys.exit(f"status must be one of {STATUSES}")
        find(d, a[1])["status"] = a[2]; save(d); cmd_render(d)
    elif a[0] == "render": cmd_render(d)
    else: sys.exit(__doc__)

if __name__ == "__main__": main()
