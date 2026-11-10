#!/usr/bin/env python3
"""
FILE:    apply_f01_update.py
MODULE:  tools
PURPOSE: One-off: records the 2026-11-10 decisions, updates F-01/F-04/F-12 in the backlog, regenerates cards. Run from the repo root.
DEPENDS: docs/backlog.json, tools/backlog.py
USED BY: human, once
NOTES:   Idempotent (skips if already applied). Delete after use.
"""
import json, pathlib, subprocess, sys
R = pathlib.Path(".")
dec = R / "docs/DECISIONS.md"
if not dec.exists() or not (R / "tools/backlog.py").exists(): sys.exit("Run from the Angel repo root.")
if "AGP 8.13.2" in dec.read_text(): sys.exit("Already applied.")
with dec.open("a") as f: f.write("""| 2026-11-10 | Build toolchain: AGP 8.13.2, Gradle 8.13, Kotlin 2.3.20, JDK 17, compileSdk/targetSdk 36, minSdk 29 | Checked on official release pages; AGP 9.2 / Gradle 9.4 / Kotlin 2.4 exist but not chosen for the first build (fewer moving parts). UNPROVEN until first CI run |
| 2026-11-10 | First APK has zero third-party dependencies; Compose arrives at F-10 (verified: ui 1.12.1, material3 1.4.0) | Smallest APK, lowest build risk |
| 2026-11-10 | No Gradle wrapper committed yet; CI uses Gradle 8.13 via setup-gradle | Wrapper jar cannot be downloaded offline; add later with `gradle wrapper` |
| 2026-11-10 | Test distribution = CI debug APK artifact; release signing deferred (docs/RELEASE_SIGNING.md) | Human decision: sideload, no Play |
""")
with (R / "docs/CHANGELOG.md").open("a") as f:
    f.write("2026-11-10 | F-01/F-04/F-12 | Verified versions, buildable dependency-free APK shell, CI uploads debug APK, install + signing docs\n")
p = R / "docs/backlog.json"; d = json.loads(p.read_text())
for i in d["items"]:
    if i["id"] == "F-01": i["acceptance"] = ["All modules in settings.gradle.kts exist with MODULE.md and build.gradle.kts", "First CI run succeeds (human confirms green run)", "Versions recorded in DECISIONS.md (done 2026-11-10)", "Package id + minSdk confirmed with human"]
    if i["id"] == "F-04": i["acceptance"] = ["Workflow runs header check, context map, Gradle test, assembleDebug", "Debug APK uploaded as artifact 'angel-debug-apk'", "Human confirms first green run on GitHub"]
    if i["id"] == "F-12": i["status"] = "review"
p.write_text(json.dumps(d, indent=1) + "\n")
for t in ("F-01", "F-04"):
    (R / f"docs/tasks/{t}.md").unlink(missing_ok=True)
subprocess.run([sys.executable, "tools/backlog.py", "render"], check=True)
notes = {"F-01": "2026-11-10: versions verified and recorded; app shell has no dependencies. Not built by the agent (no network). Needs first CI run. Package id/minSdk still need human CONFIRM.",
         "F-04": "2026-11-10: workflow builds + uploads a debug APK. UNVERIFIED: sdkmanager package names and the Gradle/AGP/Kotlin combination - fix from the first CI log if it fails."}
for t, n in notes.items():
    with (R / f"docs/tasks/{t}.md").open("a") as f: f.write("\n" + n + "\n")
subprocess.run([sys.executable, "tools/check_headers.py"])
print("applied. Delete apply_f01_update.py")
