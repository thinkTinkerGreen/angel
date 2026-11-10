# Release signing and distribution (F-12 draft)
- **Test builds:** debug APK from CI, auto-signed with a debug key. Fine for testing; do not give to the public.
- **Public sideload release (later):** create ONE release keystore locally: `keytool -genkeypair -v -keystore angel-release.jks -alias angel -keyalg RSA -keysize 4096 -validity 10000`. Back it up offline (loss = users cannot update). NEVER commit it (`*.jks`, `*.keystore` are git-ignored).
- **CI signing:** store the keystore (base64) and passwords as GitHub Actions *secrets*; add a signing step only when a release build is needed.
- **Hosting:** attach the signed APK + a small `version.json` to a GitHub Release.
- **Update check (design, no background work):** when the User opens Angel, fetch `version.json` once (at most daily); if newer, show a plain-language prompt that opens the download. No service, no polling.
- **Size note:** update code must stay tiny; record any added dependency in DECISIONS.md.
