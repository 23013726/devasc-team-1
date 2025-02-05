import unittest
import subprocess
import sys

class TestOutput(unittest.TestCase):
    """
    Test case to check if a Python file produces any output.
    """

    def test_output(self):
        """
        Test if the Python file produces any output.
        """
        file_path = sys.argv[1]  # Get the file path from command-line arguments

        try:
            # Run the Python file and capture stdout
            result = subprocess.run(
                [sys.executable, file_path],
                capture_output=True,
                text=True
            )

            # Check if stdout is not empty
            self.assertTrue(result.stdout.strip(), f"No output produced by {file_path}.")

        except Exception as e:
            self.fail(f"Error running {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_output.py <file_path>")
        sys.exit(1)

    # Add the file path to the test arguments
    sys.argv = [sys.argv[0]] + [sys.argv[1]]

    # Run the tests
    unittest.main()
