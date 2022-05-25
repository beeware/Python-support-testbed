###########################################################################
# Android specific tests
###########################################################################
from .utils import assert_


# Don't quit the process at the end of the suite.
def exit(failures):
    pass


def test_ctypes():
    "The FFI module has been compiled, and ctypes works on Java objects"
    from rubicon.java import JavaClass

    URL = JavaClass("java/net/URL")

    sample_url = URL("https://beeware.org/contributing")

    assert_(sample_url.getHost() == "beeware.org")
