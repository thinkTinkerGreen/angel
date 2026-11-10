# Coding Standards

## File header (required on every code file; update when purpose/deps change)
```kotlin
/**
 * FILE:    <Name>.kt
 * MODULE:  <module-name>
 * PURPOSE: <1-2 lines: what this file does>
 * DEPENDS: <modules/types it relies on>
 * USED BY: <files that use it>
 * NOTES:   <constraints, gotchas>
 */
```
Python/Shell/JS: same fields in a leading comment block. Checked by `tools/check_headers.py`.

## Structure
- One public type per file where practical; files < 200 lines (cap 300).
- State: unidirectional (ViewModel exposes immutable UI state; events in).
- No Android framework types in domain/ViewModel code unless unavoidable (keeps unit tests fast).
- Strings in `strings.xml`; colours/sizes from `core-ui` theme. No hard-coded UI values.
- Errors: user-facing message says what happened + what to do next.
- Dependencies: justify in `docs/DECISIONS.md` with size impact. Prefer platform APIs.

## Testing
Unit tests beside the module. Safety-critical logic (permission engine, consent, cool-off) requires tests before merge.

## Definition of Done (every task)
Headers ok - module tests pass - budgets respected - no background work outside sessions - consent+audit for any remote capability - MODULE.md/CONTEXT_MAP/CHANGELOG/backlog status updated - hand-off note written.
