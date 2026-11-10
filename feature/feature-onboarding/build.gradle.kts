// FILE:    build.gradle.kts
// MODULE:  feature/feature-onboarding
// PURPOSE: Android library module.
// DEPENDS: core modules only (never another feature)
// USED BY: app
// NOTES:   UNVERIFIED config - confirm compileSdk/minSdk at F-01.
plugins { alias(libs.plugins.android.library); alias(libs.plugins.kotlin.android) }
android { namespace = "com.angel.remoteassist.featureonboarding"; compileSdk = 36; defaultConfig { minSdk = 29 } }
