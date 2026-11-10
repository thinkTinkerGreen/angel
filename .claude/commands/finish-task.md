---
description: Close out the current task - update memory files and status
---
Run `python tools/check_headers.py` and `python tools/gen_context_map.py`. Update the module's MODULE.md if its API changed, add one line to docs/CHANGELOG.md, set the task status with `python tools/backlog.py set <ID> <status>`, fill the card's Hand-off notes, and print a short hand-off note (what changed, what's next, open issues).
