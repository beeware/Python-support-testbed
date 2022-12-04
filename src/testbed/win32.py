######################################################################
# Windows App main loop
#######################################################################
import clr

clr.AddReference("System.Windows.Forms")

import System.Windows.Forms as WinForms  # noqa; E402


class TestBed(WinForms.Form):
    def __init__(self):
        super().__init__()

    def run(self):
        WinForms.Application.Run(self)


def main_loop():
    form = TestBed()
    WinForms.Application.Run(form)
