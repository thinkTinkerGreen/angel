# Decisions (append-only: date | decision | why)

| Date | Decision | Why |
|---|---|---|
| 2026-10-08 | Angel client = same Android app in Angel mode (no web viewer in MVP) | One codebase, smaller scope |
| 2026-10-08 | Dev workflow = Claude Code / CLI agent in repo | User choice |
| 2026-10-08 | Backend provider for signalling = undecided until spike F-06 | User choice; avoid lock-in, keep behind `core-api` |
| 2026-10-08 | Budgets: APK 30 MB, idle RAM 70 MB, active RAM 200 MB, idle battery <5%/day | User-revised from 15/40/150/1% |
| 2026-10-08 | Working package id `com.angel.remoteassist`; minSdk 29 (Android 10) | Assumption from PRD; CONFIRM with human at F-01 |
| 2026-10-08 | MVP uses NO AccessibilityService (MediaProjection + overlay + intents only) | F-08: Accessibility policy tightened; Act mode is high platform risk |
| 2026-10-08 | OPEN: Phase 2 path (Accessibility declaration vs Guide-only fallback vs non-Play build) | Needs human decision; see docs/spikes/F-08.md section 4 |
| 2026-10-08 | OPEN: AI Angel must not autonomously execute actions via Accessibility; require per-step human approval or limit to Guide/shortcuts | Play policy wording on autonomous action (VERIFY) |
| 2026-10-08 | Invariants 6-10 added; Watch can no longer be pre-approved (overrides PRD FR-7 exception) | F-09 threat model |
| 2026-10-08 | Initial distribution = directly installed APK; Play approval NOT required for first release. Play remains optional later | Human answer. Play declarations (F-08) become optional/deferred |
| 2026-10-08 | Phase 2 Act may use AccessibilityService in the sideload build; user must enable it manually (Android restricted-settings step for sideloaded apps - VERIFY). Android 17 Advanced Protection may still block it | Human answer + F-08 finding 3 |
| 2026-10-08 | Guide-only is an acceptable fallback for Phase 2; remote tapping may be re-requested later | Human answer |
| 2026-10-08 | M-29 verification code approved | Human answer |
| 2026-11-10 | Build toolchain: AGP 8.13.2, Gradle 8.13, Kotlin 2.3.20, JDK 17, compileSdk/targetSdk 36, minSdk 29 | Checked on official release pages; AGP 9.2 / Gradle 9.4 / Kotlin 2.4 exist but not chosen for the first build (fewer moving parts). UNPROVEN until first CI run |
| 2026-11-10 | First APK has zero third-party dependencies; Compose arrives at F-10 (verified: ui 1.12.1, material3 1.4.0) | Smallest APK, lowest build risk |
| 2026-11-10 | No Gradle wrapper committed yet; CI uses Gradle 8.13 via setup-gradle | Wrapper jar cannot be downloaded offline; add later with `gradle wrapper` |
| 2026-11-10 | Test distribution = CI debug APK artifact; release signing deferred (docs/RELEASE_SIGNING.md) | Human decision: sideload, no Play |
