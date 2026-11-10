// FILE:    build.gradle.kts
// MODULE:  core/core-api
// PURPOSE: Pure Kotlin/JVM module (fast unit tests, no Android dependency).
// DEPENDS: none (add only other core modules)
// USED BY: settings.gradle.kts
// NOTES:   Keep dependency-free where possible.
plugins { alias(libs.plugins.kotlin.jvm) }
