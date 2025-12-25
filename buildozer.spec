[app]
title = Alt-ADB Mobile
package.name = altadb
package.domain = org.ferrydamien9ux
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Added Pillow (needed for Kivy images) and set versions
requirements = python3,kivy==2.3.0,pillow

# Android specific
android.permissions = INTERNET, USB_PERMISSION, WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# CRITICAL: This allows the GitHub "Robot" to skip the license prompts
android.accept_sdk_license = True
android.skip_update = False

# Build settings
fullscreen = 1
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

