###########################################################################
# Linux specific tests
###########################################################################
import importlib
import sys

from .utils import assert_


def exit(failures):
    sys.exit(failures)


def test_dbm_gdbm():
    "The GNU DBM module has been compiled and works"
    from dbm import gnu as gdbm
    import tempfile

    cache_name = f'{tempfile.mkdtemp()}/gdbm'
    with gdbm.open(cache_name, 'c') as db:
        db['hello'] = 'world'

        assert_(db['hello'] == b'world')

