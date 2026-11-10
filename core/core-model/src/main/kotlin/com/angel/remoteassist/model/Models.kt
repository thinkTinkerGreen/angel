/**
 * FILE:    Models.kt
 * MODULE:  core-model
 * PURPOSE: Core data types: Role, Angel, Grant, SessionState. Plain Kotlin, no Android types.
 * DEPENDS: Capability
 * USED BY: core-permissions, core-api, features
 * NOTES:   Time values are epoch millis. Angel.pairedAt starts the 24h cool-off.
 */
package com.angel.remoteassist.model

enum class Role { USER, ANGEL }

data class Angel(val id: String, val displayName: String, val isAi: Boolean, val pairedAt: Long)

data class Grant(val angelId: String, val capability: Capability, val expiresAt: Long?)

enum class SessionState { REQUESTED, AWAITING_CONSENT, ACTIVE, ENDED }
