import importlib
import os
import platform
import sys


def main():
    print("=" * 80)
    print(f"Python {platform.python_version()} Verification Suite")
    print(f"Running on {platform.platform()}")
    print("=" * 80)
    print(f"{sys.platform=}")
    print(f"{sys.implementation=}")
    print("-" * 80)
    print(f"{platform.architecture()=}")
    print(f"{platform.machine()=}")
    print(f"{platform.node()=}")
    print(f"{platform.processor()=}")
    print(f"{platform.release()=}")
    print(f"{platform.system()=}")
    print(f"{platform.version()=}")
    print(f"{platform.uname()=}")
    print("-" * 80)
    print(f"{os.name=}")
    if hasattr(os, "uname"):
        print(f"{os.uname()=}")
    else:
        # Windows
        print("os.uname() not available")
    print("=" * 80)

    # Load the platform module
    if hasattr(sys, "getandroidapilevel"):
        module_path = ".android"
    else:
        module_path = f".{sys.platform}"

    # Import the platform module, so we get any import side effects.
    importlib.import_module(module_path, "testbed")
