###########################################################################
# Linux specific tests
###########################################################################
import os
import sys

from .utils import assert_


def exit(failures):
    sys.exit(failures)


def test_pythonnet():
    "Python.net integration works as expected"
    # Set up CLR
    import clr
    clr.AddReference("System.Windows.Forms")

    # Now use CLR libraries
    from System.Drawing import Image

    image = Image.FromFile(os.path.join(os.path.dirname(__file__), "resources", "test-pattern.png"))
    assert_((image.Size.Width, image.Size.Height) == (1366, 768))
