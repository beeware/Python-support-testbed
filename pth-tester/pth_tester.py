initialized = False
has_socket = False


# The pth_tester module should be initialized by processing the `.pth` file
# created on installation.
def init():
    global initialized
    global has_socket

    initialized = True

    # At the time that the module is initialized, it *should* have access
    # to all of the standard library. This might not be true, depending on
    # the initialization order of the site module and sys.path.
    try:
        import socket  # NOQA: F401

        has_socket = True
    except ImportError:
        pass
