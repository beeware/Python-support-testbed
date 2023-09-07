######################################################################
# iOS App configuration
#######################################################################
from rubicon.objc import ObjCClass

UIResponder = ObjCClass("UIResponder")


class PythonAppDelegate(UIResponder):
    pass
