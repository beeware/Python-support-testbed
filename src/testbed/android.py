######################################################################
# Android App configuration
#######################################################################
from java import dynamic_proxy
from org.beeware.android import IPythonApp, MainActivity


class PythonApp(dynamic_proxy(IPythonApp)):
    def __init__(self, app):
        super().__init__()
        self._impl = app
        MainActivity.setPythonApp(self)
        print("Python app launched & stored in Android Activity class")
