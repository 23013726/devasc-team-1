import unittest
import subprocess
import os
import subprocess

# List of expected outputs we are looking for (case-insensitive)
EXPECTED_OUTPUTS = ["Hello", "World"]

def run_python_file(file_path):
    """Run a Python file and capture its output."""
    try:
        # Run the Python script and capture its output
        result = subprocess.run(['python', file_path], capture_output=True, text=True)
        
        # Print the actual output for debugging
        print(f"Output from {file_path}:\n{result.stdout}")

        # Convert the output to lowercase for case-insensitive comparison
        output = result.stdout.lower()

        # Check if any expected output is found (case-insensitive)
        output_found = False
        for expected in EXPECTED_OUTPUTS:
            if expected.lower() in output:  # Compare in lowercase
                print(f"Expected output '{expected}' found in {file_path}:")
                print(result.stdout)
                output_found = True
                break  # Once one expected output is found, no need to continue checking
        
        if not output_found:
            print(f"Expected output not found in {file_path}.")
        
        return output_found
    except Exception as e:
        print(f"Error running {file_path}: {e}")
        return False

def get_changed_files():
    """Get the list of Python files changed in the current commit."""
    result = subprocess.run(
        ['git', 'diff', '--name-only', '--diff-filter=ACM', 'HEAD~1'],
        capture_output=True,
        text=True
    )
    changed_files = result.stdout.splitlines()
    return [file for file in changed_files if file.endswith('.py')]  # Filter for Python files only

class TestPythonOutput(unittest.TestCase):
    """Test class to check for specific outputs in committed Python files."""
    
    def test_check_output(self):
        """Test to ensure specific output is detected in all committed Python files."""
        changed_files = get_changed_files()  # Get the changed Python files in this commit
        
        if not changed_files:
            print("No Python files changed in this commit.")
        
        # Run the output check for each changed Python file
        for file_path in changed_files:
            with self.subTest(file=file_path):
                result = run_python_file(file_path)
                self.assertTrue(result, f"Expected output not found in {file_path}")  # Assert that output is found

if __name__ == "__main__":
    unittest.main()
