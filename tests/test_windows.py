###########################################################################
# Windows specific tests
###########################################################################
import os
import sys

import pytest

if sys.platform != "win32":
    pytest.skip("Skipping Windows-only tests", allow_module_level=True)



def test_pythonnet():
    "Python.net integration works as expected"
    # Set up CLR
    import clr
    clr.AddReference("System.Windows.Forms")

    # Now use CLR libraries
    from System.Drawing import Image

    image = Image.FromFile(os.path.join(os.path.dirname(__file__), "resources", "test-pattern.png"))
    assert (image.Size.Width, image.Size.Height) == (1366, 768)
