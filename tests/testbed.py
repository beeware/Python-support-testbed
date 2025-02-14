import os
import sys
import tempfile
import time
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

    # On iOS and macOS, Briefcase needs to use a log streamer. However, this
    # streamer can drop lines of test output due to system load. If the log
    # result sentinel isn't seen in streamed output, the test will fail because
    # the exit status of the test isn't known. As a safety measure on iOS and
    # macOS, output the log sentinel multiple times to decrease the chance of
    # this happening.
    if sys.platform in {"darwin", "ios"}:
        for i in range(0, 6):
            time.sleep(0.5)
            print(f">>>>>>>>>> EXIT {returncode} <<<<<<<<<<")
    else:
        print(f">>>>>>>>>> EXIT {returncode} <<<<<<<<<<")


if __name__ == "__main__":
    # On iOS and macOS, Briefcase needs to use a log streamer. However, this
    # streamer takes time to start up. As a safety measure, wait a couple of seconds
    # at app start, and output some lines to minimize the impact of the streamer
    # startup.
    if sys.platform in {"darwin", "ios"}:
        print("Waiting for log streamer...")
        time.sleep(2.0)
        print("Log streamer should be ready.")

    # Run the app main to stimulate app creation and logging of test conditions.
    app_main()
    # Run the actual test suite.
    run_tests()
