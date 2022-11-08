import os
import sys
from pathlib import Path

import pytest

if __name__ == "__main__":
    os.chdir(Path(__file__).parent.parent)
    result = pytest.main(["-vv", "--color=no", "tests"])
    if result:
        print(">>>>>>>>>> Test Suite Failed <<<<<<<<<<")
    else:
        print(">>>>>>>>>> Test Suite Passed <<<<<<<<<<")
    sys.exit(result)
