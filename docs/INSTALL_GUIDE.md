# Installing the test APK on an Android phone (plain-language guide)
1. On GitHub open the repo > **Actions** tab > the latest green run > scroll to **Artifacts** > download **angel-debug-apk** (a zip). Unzip it to get `app-debug.apk`.
2. Copy `app-debug.apk` to the phone (USB, Drive, or email to yourself).
3. On the phone open the file. Android will ask to allow installs from this source (your Files app or browser): switch **Allow from this source** on.
4. If **Play Protect** warns about an unknown app, choose **Install anyway** (this is a test build that is not on Google Play).
5. Open **Angel**. You should see "Angel - build 0.1.0 - setup OK".
Updating: a new build installs over the old one only if it was signed with the same key. If Android refuses, uninstall first.
Remove: Settings > Apps > Angel > Uninstall. To turn off the allow-installs switch, reverse step 3.
