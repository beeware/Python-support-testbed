###########################################################################
# Testing utilities
###########################################################################
from functools import wraps


class SkippedTest(Exception):
    pass


def assert_(condition, msg=None):
    if not condition:
        raise AssertionError(msg if msg else "Test assertion failed")


def skipIf(condition, explanation):
    def _skipper(method):
        @wraps(method)
        def _method():
            if condition:
                raise SkippedTest(explanation)
            else:
                method()
        return _method
    return _skipper
