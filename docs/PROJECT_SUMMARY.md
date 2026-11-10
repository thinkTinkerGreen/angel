# Project Summary (keep to one page)

**Product:** Angel - Android remote assist. **User** = phone owner. **Angel** = remote helper (human or AI). Consent per session, per capability; revocable; audited.

**Modes:** Watch (view) -> Guide (draw overlays, send deep links) -> Act (remote tap/type; Phase 2, off by default).

**Current phase:** Phase 0 (foundations) -> Phase 1 (MVP: Watch + Guide). Act, capture, AI Angel come later.

**Tech (proposed, confirm in spikes):** Kotlin, Jetpack Compose + Material 3, multi-module Gradle, MediaProjection + WebRTC (screen/voice), FCM wake-up, serverless signalling (provider chosen AFTER spike F-06), local encrypted storage. Same APK serves both User and Angel roles.

**Architecture in one paragraph:** `app` is a thin shell. `core/*` holds shared models, interfaces (`core-api`), permission engine, UI kit. `feature/*` modules each own one feature and depend only on `core/*`. `data/*` implements network/storage/push behind `core-api` interfaces. New remote abilities are *capabilities* registered with the permission engine so the session core never changes.

**Budgets:** APK <= 30 MB, idle RAM <= 70 MB, active RAM <= 200 MB, idle battery < 5%/day, foreground service only during sessions.

**Glossary:** Capability = one thing an Angel may do (view screen, draw guidance, ...). Session = one consented connection. Shortcut = deep link/intent the Angel sends the User. Cool-off = new Angels get no Act capabilities for 24h.

**Source docs:** `docs/prd/` (PRD, MVP and backlog doc). **Decisions:** `docs/DECISIONS.md`.
