import importlib
import platform
import sys


def main():
    print("=" * 80)
    print(f"Python {platform.python_version()} Verification Suite")
    print(f"Running on {platform.platform()}")
    print("=" * 80)

    # Load the platform module
    if hasattr(sys, "getandroidapilevel"):
        module_path = ".android"
    else:
        module_path = f".{sys.platform}"

    # Import the platform module, so we get any import side effects.
    importlib.import_module(module_path, "testbed")
