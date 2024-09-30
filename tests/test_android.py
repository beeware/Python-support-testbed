###########################################################################
# Android specific tests
###########################################################################
import sys

import pytest

if not hasattr(sys, "getandroidapilevel"):
    pytest.skip("Skipping Android-only tests", allow_module_level=True)


def test_ctypes():
    "The FFI module has been compiled, and ctypes works on Java objects"
    from java.net import URL

    sample_url = URL("https://beeware.org/contributing")

    assert sample_url.getHost() == "beeware.org"
