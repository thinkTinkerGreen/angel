# Backlog (generated from docs/backlog.json - do not edit by hand)

Status: todo, in-progress, review, done, blocked, human (needs device/human), planned


## Phase 0: Foundations and De-risking

| ID | Item | Pri | Size | Module | Status | Deps |
|---|---|---|---|---|---|---|
| F-01 | Repo, folder structure, Gradle multi-module skeleton | P0 | M | repo | review |  |
| F-02 | AGENTS.md, PROJECT_SUMMARY.md, task-card template | P0 | S | docs | review | F-01 |
| F-03 | Build tools: header checker, context map, size check | P0 | M | tools | review | F-01 |
| F-04 | CI pipeline: build, lint, tests, budget report | P0 | M | ci | review | F-03 |
| F-08 | Google Play policy review and declarations plan | P0 | S | docs | review | F-02 |
| F-09 | Threat model for misuse (scam, coercion) | P0 | M | docs | review | F-02 |
| F-12 | Distribution: signed APK, release hosting, in-app update check | P1 | M | app | review | F-04 |
| F-10 | Design system: colours, type, large-text mode, core components | P1 | M | core/core-ui | todo | F-01 |
| F-05 | Spike: MediaProjection + WebRTC screen stream; measure size/RAM/latency | P0 | L | spikes/F-05 | todo | F-01 |
| F-06 | Spike: signalling + TURN on free tier; document limits | P0 | L | spikes/F-06 | todo | F-01 |
| F-07 | Spike: draw-over-apps overlay for guidance on 4 OEMs | P0 | M | spikes/F-07 | todo | F-01 |
| F-11 | User research: 8-10 older adults and families | P1 | L | docs | human | F-02 |

## Phase 1: MVP (Watch and Guide)

| ID | Item | Pri | Size | Module | Status | Deps |
|---|---|---|---|---|---|---|
| M-02 | Role selection: User or Angel mode | P0 | S | feature/feature-onboarding | todo | F-01 |
| M-03 | Invite generation (link, QR, short code) | P0 | M | feature/feature-pairing | todo | F-06, M-02 |
| M-04 | Pairing with two-sided confirmation | P0 | L | feature/feature-pairing | todo | M-03 |
| M-06 | Capability model and permission engine | P0 | L | core/core-permissions | todo | F-01 |
| M-05 | Multiple Angels and per-Angel permission profile | P0 | M | feature/feature-pairing | todo | M-04, M-06 |
| M-07 | Session request and wake-up via push | P0 | M | data/data-push | todo | F-06, M-06 |
| M-08 | Per-session consent prompt screen | P0 | M | feature/feature-consent | todo | M-06, F-10 |
| M-09 | Foreground service and persistent session indicator | P0 | M | feature/feature-session | todo | F-05, M-08 |
| M-14 | Always-visible Stop control and instant revoke | P0 | M | feature/feature-session | todo | M-09 |
| M-10 | Screen share from User device (view only) | P0 | L | feature/feature-screenshare | todo | F-05, M-09 |
| M-11 | Angel viewer screen with pan and zoom | P0 | M | feature/feature-screenshare | todo | M-10 |
| M-12 | Voice channel | P0 | M | feature/feature-comms | todo | M-10 |
| M-15 | Guidance overlay: arrow, highlight, text | P0 | L | feature/feature-guidance | todo | F-07, M-10 |
| M-16 | Shortcut: open system setting deep link | P0 | M | feature/feature-shortcuts | todo | M-08 |
| M-17 | Shortcut: compose message draft | P0 | S | feature/feature-shortcuts | todo | M-16 |
| M-21 | Mask sensitive screens (secure windows, password fields) | P0 | M | feature/feature-screenshare | todo | M-10 |
| M-23 | Cool-off period for new Angels | P0 | S | core/core-permissions | todo | M-06 |
| M-25 | Local activity log and viewer | P0 | M | feature/feature-activitylog | todo | M-08 |
| M-01 | Onboarding flow with plain-language permission explainers | P0 | M | feature/feature-onboarding | todo | F-10, M-02 |
| M-13 | Text chat | P1 | M | feature/feature-comms | todo | M-10 |
| M-18 | Shortcut: contact search | P1 | S | feature/feature-shortcuts | todo | M-16 |
| M-19 | Shortcut: maps search | P1 | S | feature/feature-shortcuts | todo | M-16 |
| M-20 | Shortcut: calendar event | P1 | S | feature/feature-shortcuts | todo | M-16 |
| M-22 | Reconnect and graceful degradation | P1 | M | feature/feature-session | todo | M-10, M-12 |
| M-24 | Block and report | P1 | M | feature/feature-pairing | todo | M-05 |
| M-26 | Accessibility pass | P0 | M | core/core-ui | todo | M-01, M-08 |
| M-27 | Performance pass: size, RAM, battery budgets | P0 | L | app | todo | M-22, M-15 |
| M-29 | Session verification code (proposed, needs approval) | P1 | M | feature/feature-consent | todo | M-08 |
| M-28 | Closed beta with 10 real families | P0 | L | docs | human | M-27, M-25, M-23 |

## Phase 2: Act (Human Angels)

| ID | Item | Pri | Size | Module | Status | Deps |
|---|---|---|---|---|---|---|
| A-01 | Accessibility service shell with policy-compliant disclosure | P0 | L | TBD | planned |  |
| A-02 | Remote tap, swipe, scroll | P0 | L | TBD | planned |  |
| A-03 | Remote text entry, back, home, recents | P0 | M | TBD | planned |  |
| A-04 | Capability: send message (with confirmation) | P0 | M | TBD | planned |  |
| A-05 | Capability: read messages and notifications | P0 | M | TBD | planned |  |
| A-06 | Capability: contacts (hidden-contact list) | P1 | M | TBD | planned |  |
| A-07 | Capability: rotate screen, volume, brightness | P1 | M | TBD | planned |  |
| A-08 | Capability: maps and location sharing | P1 | M | TBD | planned |  |
| A-09 | In-the-moment confirmation framework | P0 | L | TBD | planned |  |
| A-10 | Scam-resistance warnings | P0 | M | TBD | planned |  |
| A-11 | Mid-session capability request flow | P1 | M | TBD | planned |  |
| A-12 | Web viewer for Angels | P2 | L | TBD | planned |  |

## Phase 3: Capture and Booking

| ID | Item | Pri | Size | Module | Status | Deps |
|---|---|---|---|---|---|---|
| C-01 | Remote photo capture with preview and approval | P0 | L | TBD | planned |  |
| C-02 | Remote video capture | P1 | L | TBD | planned |  |
| C-03 | Remote audio recording with indicator | P0 | M | TBD | planned |  |
| C-04 | Local storage and optional share of captures | P1 | M | TBD | planned |  |
| C-05 | Appointment and calendar booking flow | P1 | L | TBD | planned |  |
| C-06 | Optional session recording (off by default) | P2 | M | TBD | planned |  |

## Phase 4: AI Angel and On-Device SLM

| ID | Item | Pri | Size | Module | Status | Deps |
|---|---|---|---|---|---|---|
| AI-01 | Agent control API shared with human Angels | P0 | L | TBD | planned |  |
| AI-02 | Screen understanding (accessibility tree first) | P0 | L | TBD | planned |  |
| AI-03 | Natural-language goal to plan, shown for approval | P0 | L | TBD | planned |  |
| AI-04 | Step log, pause, stop, human takeover | P0 | M | TBD | planned |  |
| AI-05 | Guardrails: scope, rate limits, no payment/password | P0 | M | TBD | planned |  |
| AI-06 | On-device SLM for intent classification (optional download) | P1 | L | TBD | planned |  |
| AI-07 | SLM-generated prompts for cloud frontier LLM | P1 | L | TBD | planned |  |
| AI-08 | Cloud LLM gateway: free-tier quotas, caching, fallback | P1 | M | TBD | planned |  |

## Phase 5: Scale, Polish and Growth

| ID | Item | Pri | Size | Module | Status | Deps |
|---|---|---|---|---|---|---|
| S-01 | Multi-language and RTL support | P1 | L | TBD | planned |  |
| S-02 | Tablet layouts | P2 | M | TBD | planned |  |
| S-03 | Professional Angel verification | P2 | L | TBD | planned |  |
| S-04 | Subscription tiers and billing | P2 | L | TBD | planned |  |
| S-05 | Lawful-authority flow for Users unable to consent | P1 | L | TBD | planned |  |
| S-06 | Staged rollout, monitoring, crash-free dashboards | P0 | M | TBD | planned |  |
