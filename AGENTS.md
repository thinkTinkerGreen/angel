# AGENTS.md - rules for ANY LLM working on Angel

Read this file first, every session. Then `docs/PROJECT_SUMMARY.md`. Then ONE task card.

## What Angel is
Android app. A trusted remote helper (an **Angel**, human or AI) sees, guides and (later) operates a **User's** phone, only with the User's explicit, revocable, session-based consent. Full PRD: `docs/prd/`.

## Session protocol (always)
1. Read `AGENTS.md` -> `docs/PROJECT_SUMMARY.md` -> `python tools/backlog.py next` (or the card the human named).
2. Open ONLY the files the task card lists, plus `docs/CONTEXT_MAP.md` to find module APIs. Never paste or read the whole repo.
3. Implement the card. Smallest diff that meets the acceptance criteria. Touch ONE module per task; if you need two, stop and split the task.
4. Run: `python tools/check_headers.py && python tools/gen_context_map.py` (and Gradle tests for the module if network/SDK exist).
5. Update: the module's `MODULE.md` (if API changed), `docs/CHANGELOG.md` (one line), `python tools/backlog.py set <ID> <status>`, and the card's "Hand-off notes".
6. End with a hand-off note: what changed, what is next, open issues.

## Hard rules
- **Header snippet** at the top of EVERY code file (format in `docs/CODING_STANDARDS.md`). Keep it current.
- **Modular:** features live in `feature/*`, talk only via interfaces in `core/core-api`. No feature imports another feature.
- **Small files:** target < 200 lines, hard cap 300.
- **Budgets** (`tools/budgets.json`): download <= 30 MB, idle RAM <= 70 MB, active RAM <= 200 MB, idle battery < 5%/day. No new dependency without a line in `docs/DECISIONS.md` justifying its size.
- **Background:** foreground service ONLY during an active session. No idle services, polling, or wake locks.
- **Safety invariants (never violate):** every remote capability needs a consent prompt + an audit-log entry; no covert mode; session indicator cannot be hidden by an Angel; no password/payment entry by an Angel; sensitive screens masked.
- **More invariants (F-09, see docs/THREAT_MODEL.md):** screen share never starts without a User tap on their own device in that session; no Angel UI to hide/bypass the indicator or stay connected after Stop; invites are single-use, expiring, identity-blind until User confirms; guidance overlays are non-interactive and labelled with the Angel's name; any new remote capability needs a threat-model entry.
- **Privacy:** never log message content, contact data, screen frames, tokens.
- **UX:** plain language, one primary action per screen, large text support, always-visible Stop.
- **Do not guess.** If a decision is missing, a needed file is not provided, or a requirement conflicts, STOP and ask the human. Record answers in `docs/DECISIONS.md`.
- **Do not invent versions/APIs.** Verify library versions and Android API behaviour (with network or the human) before using them; mark anything unverified `UNVERIFIED` in the code comment and the card.

## Where things are
See `docs/PROJECT_SUMMARY.md` (architecture) and `docs/CONTEXT_MAP.md` (modules). Backlog: `docs/backlog.json` (source of truth) -> `docs/BACKLOG.md` (generated).
