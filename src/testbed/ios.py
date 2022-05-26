###########################################################################
# iOS specific tests
###########################################################################
from rubicon.objc import ObjCClass

from .utils import assert_


UIResponder = ObjCClass('UIResponder')

# iOS apps need an AppDelegate or they crash
class PythonAppDelegate(UIResponder):
    pass


# Don't quit the process at the end of the suite.
def exit(failures):
    pass


def test_ctypes():
    "The FFI module has been compiled, and ctypes works on ObjC objects"
    from rubicon.objc import ObjCClass

    NSURL = ObjCClass("NSURL")

    base = NSURL.URLWithString("https://beeware.org/")
    full = NSURL.URLWithString("contributing", relativeToURL=base)
    absolute = full.absoluteURL
    assert_(absolute.description == "https://beeware.org/contributing")


def test_subprocess():
    "Subprocesses should raise exceptions"
    import errno
    import subprocess

    try:
        subprocess.call(['uname', '-a'])
        raise AssertionError('Subprocesses should not be possible')
    except RuntimeError as e:
        # RuntimeError is raised on Py3.10 and lower
        assert_(str(e) == "Subprocesses are not supported on ios")
    except OSError as e:
        # OSError is raised on Py3.11+
        assert_(e.errno == errno.ENOTSUP)
        assert_(str(e) == "[Errno 45] ios does not support processes.")