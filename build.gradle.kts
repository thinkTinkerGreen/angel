// FILE:    build.gradle.kts
// MODULE:  repo
// PURPOSE: Root build file: declares plugin versions (from libs.versions.toml) without applying them.
// DEPENDS: gradle/libs.versions.toml
// USED BY: Gradle
// NOTES:   UNVERIFIED versions - verify at F-01 against current releases.
plugins {
  alias(libs.plugins.android.application) apply false
  alias(libs.plugins.android.library) apply false
  alias(libs.plugins.kotlin.android) apply false
  alias(libs.plugins.kotlin.jvm) apply false
  alias(libs.plugins.kotlin.compose) apply false
}
