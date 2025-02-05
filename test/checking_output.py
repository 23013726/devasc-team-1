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
        # Get the file path from the command-line arguments
        if len(sys.argv) != 2:
            print("Usage: python check_output.py <file_path>")
            self.fail("Missing file path argument.")  # Fail the test instead of exiting

        file_path = sys.argv[1]

        try:
            # Run the Python file and capture stdout
            result = subprocess.run(
                [sys.executable, file_path],
                capture_output=True,
                text=True
            )

            # Debugging: Print stdout and stderr
            print(f"=== Debug: Output of {file_path} ===")
            print("stdout:", result.stdout)
            print("stderr:", result.stderr)

            # Fail if stdout is empty
            self.assertTrue(result.stdout.strip(), f"No output produced by {file_path}.")

        except Exception as e:
            self.fail(f"Error running {file_path}: {e}")

if __name__ == "__main__":
    # Remove the first argument (the script name) to avoid interfering with unittest
    if len(sys.argv) > 1:
        sys.argv = [sys.argv[0]] + sys.argv[2:]

    # Run the tests
    unittest.main()
