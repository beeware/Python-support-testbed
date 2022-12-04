###########################################################################
# iOS specific tests
###########################################################################
import sys

import pytest

if sys.platform != "ios":
    pytest.skip("Skipping iOS-only tests", allow_module_level=True)


def test_ctypes():
    "The FFI module has been compiled, and ctypes works on ObjC objects"
    from rubicon.objc import ObjCClass

    NSURL = ObjCClass("NSURL")

    base = NSURL.URLWithString("https://beeware.org/")
    full = NSURL.URLWithString("contributing", relativeToURL=base)
    absolute = full.absoluteURL
    assert absolute.description == "https://beeware.org/contributing"


def test_subprocess():
    "Subprocesses should raise exceptions"
    import errno
    import subprocess

    try:
        subprocess.call(["uname", "-a"])
        raise AssertionError("Subprocesses should not be possible")
    except RuntimeError as e:
        # RuntimeError is raised on Py3.10 and lower
        assert str(e) == "Subprocesses are not supported on ios"
    except OSError as e:
        # OSError is raised on Py3.11+
        assert e.errno == errno.ENOTSUP
        assert str(e) == "[Errno 45] ios does not support processes."
