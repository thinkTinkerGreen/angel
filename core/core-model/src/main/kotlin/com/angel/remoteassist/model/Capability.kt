/**
 * FILE:    Capability.kt
 * MODULE:  core-model
 * PURPOSE: Enum of things an Angel may be allowed to do. MVP = view/guide/voice only; Act capabilities arrive in Phase 2.
 * DEPENDS: none
 * USED BY: core-permissions, features
 * NOTES:   Add new capabilities here AND register them in the permission engine. Risk level drives consent UX.
 */
package com.angel.remoteassist.model

enum class Risk { LOW, SENSITIVE }

enum class Capability(val risk: Risk) {
    VIEW_SCREEN(Risk.LOW),
    DRAW_GUIDANCE(Risk.LOW),
    VOICE_CHAT(Risk.LOW),
    SEND_SHORTCUT(Risk.LOW),
}
