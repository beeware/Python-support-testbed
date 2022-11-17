import os
import tempfile
from pathlib import Path

import pytest

if __name__ == "__main__":
    os.chdir(Path(__file__).parent.parent)
    result = pytest.main(
        [
            # Turn up verbosity
            "-vv",
            # Disable color
            "--color=no",
            # Override the cache directory to be somewhere known writable
            "-o",
            f"cache_dir={tempfile.gettempdir()}/.pytest_cache",
            # Run only the test folder
            "tests",
        ]
    )
