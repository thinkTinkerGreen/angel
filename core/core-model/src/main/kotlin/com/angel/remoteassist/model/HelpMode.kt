/**
 * FILE:    HelpMode.kt
 * MODULE:  core-model
 * PURPOSE: Help modes: WATCH (view), GUIDE (draw + shortcuts), ACT (remote control, Phase 2, off by default).
 * DEPENDS: none
 * USED BY: core-permissions, feature-session
 * NOTES:   ACT must not be grantable in the MVP.
 */
package com.angel.remoteassist.model

enum class HelpMode { WATCH, GUIDE, ACT }
