# Threat Model: misuse, scams and coercion (F-09)
Scope: MVP (Watch + Guide) first; Phase 2-4 items marked. Mitigations map to backlog IDs. Assessment by agent; review with a safety/legal advisor before public launch.

## 1. Assets to protect
Screen content - voice - messages/contacts (Phase 2) - location - the User's money and accounts - the User's autonomy and ability to say no.

## 2. Actors
| Actor | Motive | Example |
|---|---|---|
| A1 Scammer posing as helper | Money, credentials | Cold-calls an older User, talks them into installing Angel and approving a session |
| A2 Coercive person (partner, relative, carer) | Control, surveillance | Uses Angel as stalkerware or pressures the User to keep access on |
| A3 Compromised/stolen Angel account | Access to many Users | Attacker takes over a family Angel's phone or login |
| A4 Over-helpful family Angel | Good intent, bad boundaries | Reads private chats, changes things without asking |
| A5 Malicious or manipulated AI Angel (Phase 4) | Unintended actions | Prompt injection from on-screen text makes the agent send money or messages |
| A6 Malware already on the User's phone | Abuse overlay/capture | Fake guidance overlay to trick taps |
| A7 Network attacker | Eavesdrop/hijack | Intercepts signalling, replays invites |
| A8 Minor / vulnerable User | Cannot judge risk | Child pressured by a stranger |

## 3. Abuse cases and mitigations
| ID | Abuse case | Actor | Mitigation (backlog) | Residual risk |
|---|---|---|---|---|
| T1 | Stranger gets an invite code and pairs | A1 | Invites short-lived, single-use, rate-limited (M-03); two-sided confirmation naming the person (M-04); cool-off for new Angels (M-23) | User can still be socially engineered into confirming |
| T2 | Scammer on a phone call asks User to open session and read bank app | A1 | Persistent indicator + Stop (M-09, M-14); sensitive screens masked (M-21); scam warning on first session with new Angel and on banking-like screens (A-10, Phase 2); proposed **M-29** verification code | Masking cannot catch every screen |
| T3 | Covert/standing access | A2 | No hidden mode, no hidden icon, no auto-start; Android per-session capture consent (F-08 finding 5); every session needs a User tap (invariant 7); activity log (M-25) | Coercion happens off-device |
| T4 | Pressure to keep Angel paired | A2 | Block/remove in two taps, available inside notification (M-14, M-24); plain-language "you can say no" copy (M-08); optional trusted-contact alert on new pairing (Phase 5) | Cannot detect pressure |
| T5 | Attacker takes over Angel account | A3 | Per-session consent still required; cool-off for new Angels; revoke all in one action (M-05); Angel device binding + re-pairing on new device (M-04) | User approves a real-looking request |
| T6 | Angel reads private content | A4 | Capability-scoped grants (M-06); Watch/Guide only in MVP; per-Angel profiles (M-05); activity log visible to User (M-25) | Screen share shows whatever is on screen |
| T7 | Fake overlay tricks User into tapping | A6, A1 | Overlay only during active session, cleared on end (M-15); overlays non-interactive; Angel-labelled guidance bubble ("Daniel is pointing here") | Malware on the phone is out of scope |
| T8 | Guidance steers User to harmful action | A1, A4 | Shortcuts limited to a safe catalogue (M-16..M-20); no payment/password flows; compose draft never auto-sends (M-17) | User still taps |
| T9 | Prompt injection via on-screen text (Phase 4) | A5 | AI uses same permission engine, cannot self-grant (AI-01); per-step approval for sensitive actions (A-09, AI-05); on-screen text treated as data | Research area; keep AI to suggestions first |
| T10 | Session hijack / eavesdrop | A7 | Encrypted media and signalling; short-lived session tokens; invites bound to device (F-05/F-06 decide transport) | Depends on chosen provider |
| T11 | Child targeted by stranger | A8 | Same consent model; minors flagged in profile; parent Angel disclosure visible to child (PRD FR-30); block/report (M-24); no unknown-Angel Act | Age verification not in scope |
| T12 | Log tampering / deletion to hide abuse | A2, A3 | Append-only local log (M-25); Angel cannot access log; app cannot be hidden by Angel | Rooted devices |

## 4. Safety invariants review (AGENTS.md)
Existing 5 invariants kept. Added after review:
6. A screen-share session never starts without an explicit tap by the User on the User's own device in that session (no standing/pre-approved Watch). This overrides the PRD FR-7 exception for pre-approving Watch.
7. Angel-side UI must never offer a way to hide, mute or bypass the User-side indicator, or to stay connected after the User stops.
8. Invites are single-use, expire, and never reveal the User's identity before the User confirms.
9. Guidance overlays are non-interactive and clearly attributed to the Angel.
10. No remote capability may be added without an entry in this threat model.

## 5. Proposed additions (need human approval)
- **M-29 Verification code (P1, M):** at session start the User's phone shows a 4-digit code the Angel must say or enter, proving the person on the call is the paired Angel. Adds friction but defeats most cold-call scams.
- **First-session briefing (P0, S) in M-08:** one calm screen: "Only allow someone you know. We will never ask you to share bank details."
- Trusted-contact alert on new pairing: backlog S-0x (Phase 5), needs product decision.

## 6. Open questions
1. Is M-29 acceptable friction for elderly Users?
2. Should minors get stricter defaults (parent-only Angels)? PRD open question 2 remains.
3. Who reviews this model (security/legal) before beta M-28?
