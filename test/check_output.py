import unittest
import subprocess
import sys
import os

class TestPythonFiles(unittest.TestCase):
    """
    Test cases for checking Python files.
    """

    def test_file_output(self):
        """
        Test if the Python file produces valid output and no errors.
        """
        file_path = sys.argv[1]  # Get the file path from command-line arguments

        try:
            # Run the Python file and capture output and errors
            result = subprocess.run(
                [sys.executable, file_path],
                capture_output=True,
                text=True,
                check=True
            )

            # Check for errors in stderr
            self.assertFalse(result.stderr.strip(), f"Errors found in {file_path}:\n{result.stderr}")

            # Check if there is any valid output in stdout
            self.assertTrue(result.stdout.strip(), f"No output produced by {file_path}.")

        except subprocess.CalledProcessError as e:
            # Handle cases where the script exits with a non-zero status
            self.fail(f"Error running {file_path} (exit code {e.returncode}):\n{e.stderr}")

if __name__ == "__main__":
    # Check if a file path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python check_output.py <file_path>")
        sys.exit(1)

    # Add the file path to the test arguments
    sys.argv = [sys.argv[0]] + [sys.argv[1]]

    # Run the tests
    unittest.main()
