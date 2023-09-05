import os
import tempfile
from pathlib import Path

import pytest

from testbed.app import main as app_main


def run_tests():
    project_path = Path(__file__).parent.parent
    os.chdir(Path(__file__).parent.parent)
    returncode = pytest.main(
        [
            # Turn up verbosity
            "-vv",
            # Disable color
            "--color=no",
            # Overwrite the cache directory to somewhere writable
            "-o",
            f"cache_dir={tempfile.gettempdir()}/.pytest_cache",
            project_path / "tests",
        ]
    )

    print(f">>>>>>>>>> EXIT {returncode} <<<<<<<<<<")


if __name__ == "__main__":
    # Run the app main to stimulate app creation and logging of test conditions.
    app_main()
    # Run the actual test suite.
    run_tests()
