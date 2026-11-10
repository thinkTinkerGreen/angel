/**
 * FILE:    MainActivity.kt
 * MODULE:  app
 * PURPOSE: Placeholder launcher activity; replaced by nav host at M-02/M-01.
 * DEPENDS: androidx.activity.compose, material3
 * USED BY: AndroidManifest.xml
 * NOTES:   No logic here; keep the shell thin.
 */
package com.angel.remoteassist

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.Text

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { Text("Angel") }
    }
}
