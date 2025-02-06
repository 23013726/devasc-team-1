import pytest
import glob
import py_compile

def test_syntax():
    """Check all Python files for syntax errors."""
    python_files = glob.glob("**/*.py", recursive=True)

    for file in python_files:
        if "venv" in file or "tests/" in file:  # Ignore virtual env and test files
            continue  

        try:
            py_compile.compile(file, doraise=True)  # Check for syntax errors
        except py_compile.PyCompileError as e:
            pytest.fail(f"Syntax error in {file}: {e}")
