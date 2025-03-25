# pth-tester

This is a package that tests whether `.pth` files are correctly process on
import. It is not designed to be published; it is only useful in the context of
the testbed app.

When installed, it includes `.pth` file that invokes the `pth_tester.init()` method.
This sets the `initialized` attribute of the module to `True`. In this way, it is
possible to tell if `.pth` handling has occurred on app startup.

This project has been compiled into a wheel, stored in the `wheels` directory
of the top-level directory. The wheel can be rebuilt using:

    $ pip install build
    $ python -m build --wheel --outdir ../wheels

If you make any modifications to the code for this project, you will need to
rebuild the wheel.
