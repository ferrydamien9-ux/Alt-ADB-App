[app]
title = Alt-ADB Mobile
package.name = altadb
package.domain = org.ferrydamien9ux
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,adbutils

# Android specific
android.permissions = INTERNET, USB_PERMISSION, WRITE_EXTERNAL_STORAGE
android.api = 33
android.arch = arm64-v8a
