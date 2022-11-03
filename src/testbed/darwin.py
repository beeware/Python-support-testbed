######################################################################
# macOS App main loop
#######################################################################
from rubicon.objc import ObjCClass
from rubicon.objc.runtime import load_library


appkit = load_library("AppKit")

NSApplication = ObjCClass('NSApplication')
NSApplication.declare_class_property("sharedApplication")


def main_loop():
    app = NSApplication.sharedApplication
    app.setActivationPolicy(0)
    app.run()
