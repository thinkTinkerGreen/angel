// FILE:    settings.gradle.kts
// MODULE:  repo
// PURPOSE: Declares all Gradle modules. Add a module here AND a MODULE.md in its folder.
// DEPENDS: none
// USED BY: Gradle
// NOTES:   Repositories limited to google() and mavenCentral() to keep supply chain small.
pluginManagement { repositories { google(); mavenCentral(); gradlePluginPortal() } }
dependencyResolutionManagement { repositories { google(); mavenCentral() } }
rootProject.name = "Angel"
include(":app")
include(":core:core-model", ":core:core-api", ":core:core-permissions", ":core:core-ui", ":core:core-util")
include(
  ":feature:feature-onboarding", ":feature:feature-pairing", ":feature:feature-consent",
  ":feature:feature-session", ":feature:feature-screenshare", ":feature:feature-guidance",
  ":feature:feature-shortcuts", ":feature:feature-comms", ":feature:feature-activitylog"
)
include(":data:data-signalling", ":data:data-storage", ":data:data-push")
