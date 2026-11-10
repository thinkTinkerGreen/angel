// FILE:    build.gradle.kts
// MODULE:  app
// PURPOSE: Thin application shell. First APK has NO third-party dependencies (smallest, lowest build risk).
// DEPENDS: none yet (feature modules are wired in as tasks add them)
// USED BY: Gradle, CI (assembleDebug -> installable test APK)
// NOTES:   Release uses R8 + resource shrinking. Debug APK is auto-signed so it installs on any phone for testing.
plugins { alias(libs.plugins.android.application); alias(libs.plugins.kotlin.android) }
android {
  namespace = "com.angel.remoteassist"
  compileSdk = 36
  defaultConfig {
    applicationId = "com.angel.remoteassist"
    minSdk = 29; targetSdk = 36
    versionCode = 1; versionName = "0.1.0"
  }
  buildTypes {
    release {
      isMinifyEnabled = true; isShrinkResources = true
      proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
    }
  }
  compileOptions { sourceCompatibility = JavaVersion.VERSION_17; targetCompatibility = JavaVersion.VERSION_17 }
  kotlinOptions { jvmTarget = "17" }
}
