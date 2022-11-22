import os
import sys
import tempfile
from pathlib import Path

import pytest

import tests


def chaquopy_extract_package(pkg):
    finder = pkg.__loader__.finder
    for path in pkg.__path__:
        chaquopy_extract_dir(finder, finder.zip_path(path))


def chaquopy_extract_dir(finder, zip_dir):
    for filename in finder.listdir(zip_dir):
        zip_path = f"{zip_dir}/{filename}"
        if finder.isdir(zip_path):
            chaquopy_extract_dir(finder, zip_path)
        else:
            finder.extract_if_changed(zip_path)


if __name__ == "__main__":
    os.chdir(Path(__file__).parent.parent)

    if hasattr(sys, "getandroidapilevel"):
        chaquopy_extract_package(tests)

    result = pytest.main(
        [
            # Turn up verbosity
            "-vv",
            # Disable color
            "--color=no",
            # Override the cache directory to be somewhere known writable
            "-o",
            f"cache_dir={tempfile.gettempdir()}/.pytest_cache",
        ]
        + tests.__path__
    )
