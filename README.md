# Python Support Testbed

This is a testbed application that can be used to do basic verification checks
of the support package builds used by BeeWare (Python-Apple-support and
Python-Android-support). It is not a comprehensive Python unit test suite; it
checks modules that have a history of being misconfigured or broken in builds.

The app can be deployed with Briefcase. When executed, the app will generate
output on the console log that is similar to a unit test suite. If it returns 0
test failures, you can have some confidence that the support build is
functioning as expected.

Before running, ensure that the template and support package paths point at the
builds you want to test. The paths committed in the repo assume that you have a
directory layout that looks something like:

- (your projects folder)
  - support
    - Python-Apple-support
      - dist
        - ...
    - Python-Android-support
      - dist
        - ...
  - templates
    - briefcase-Android-gradle-template
    - briefcase-iOS-Xcode-template
    - briefcase-macOS-Xcode-template
