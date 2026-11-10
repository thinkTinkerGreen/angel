/**
 * FILE:    Interfaces.kt
 * MODULE:  core-api
 * PURPOSE: Contracts features use instead of depending on each other: InviteService, SessionTransport.
 * DEPENDS: core-model
 * USED BY: feature-pairing, feature-session, data-signalling
 * NOTES:   Keep provider-agnostic: signalling backend is chosen after spike F-06.
 */
package com.angel.remoteassist.api

interface InviteService {
    suspend fun createInvite(): Result<String>             // returns short code
    suspend fun redeemInvite(code: String): Result<String> // returns peer id
}

interface SessionTransport {
    suspend fun requestSession(angelId: String): Result<String> // returns session id
    suspend fun end(sessionId: String)
}
