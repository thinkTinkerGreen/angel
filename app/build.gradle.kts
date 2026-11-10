// FILE:    build.gradle.kts
// MODULE:  app
// PURPOSE: Thin application shell: release config (R8 + resource shrinking), wires feature modules.
// DEPENDS: all core/feature/data modules
// USED BY: Gradle
// NOTES:   UNVERIFIED config. Release must stay within tools/budgets.json (download 30 MB). Add abi splits at M-27.
plugins { alias(libs.plugins.android.application); alias(libs.plugins.kotlin.android); alias(libs.plugins.kotlin.compose) }
android {
  namespace = "com.angel.remoteassist"; compileSdk = 36
  defaultConfig { applicationId = "com.angel.remoteassist"; minSdk = 29; targetSdk = 36; versionCode = 1; versionName = "0.1.0" }
  buildTypes { release { isMinifyEnabled = true; isShrinkResources = true } }
}
dependencies {
  implementation(project(":core:core-ui"))
  implementation(platform(libs.compose.bom)); implementation(libs.compose.material3); implementation(libs.activity.compose)
}
