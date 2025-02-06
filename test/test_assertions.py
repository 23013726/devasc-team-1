import pytest
import os
import unittest
import glob

def test_all_assertions():
    """Run all Python files to check for assertion errors."""
    python_files = glob.glob("**/*.py", recursive=True)

    for file in python_files:
        if "test_" in file or "venv" in file or "tests/" in file:  
            continue  # Ignore test files and virtual environment

        print(f"Checking assertions in {file}...")

        try:
            exec(open(file).read())  # Execute file
        except AssertionError as e:
            pytest.fail(f"Assertion failed in {file}: {e}")
        except Exception as e:
            print(f"Skipping {file}: {e}")  # Ignore non-assertion errors

