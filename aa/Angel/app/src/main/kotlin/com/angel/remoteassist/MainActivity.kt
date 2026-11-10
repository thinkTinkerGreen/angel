/**
 * FILE:    MainActivity.kt
 * MODULE:  app
 * PURPOSE: Placeholder launcher screen (platform views only, no libraries) so the first APK builds and installs.
 * DEPENDS: android.app.Activity
 * USED BY: AndroidManifest.xml
 * NOTES:   Replaced by the Compose nav host at M-02/M-01 once F-10 adds the UI kit.
 */
package com.angel.remoteassist

import android.app.Activity
import android.os.Bundle
import android.view.Gravity
import android.widget.TextView

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(TextView(this).apply {
            text = "Angel\nbuild 0.1.0 - setup OK"
            textSize = 28f
            gravity = Gravity.CENTER
        })
    }
}
