import unittest
import sys
import os
import subprocess

# Add the Project-Folder directory to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from team_1 import sample  # Import the Flask app instance

class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Flask test client before running any tests
        cls.app = sample.app.test_client()
        cls.app.testing = True  # Enable testing mode for the Flask client

    def run_script_and_capture_output(self, script_name):
        """Helper function to run a script and capture its output."""
        result = subprocess.run(['python', script_name], capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode

    def test_script_output(self):
        """Test that the script produces output when executed."""
        stdout, stderr, returncode = self.run_script_and_capture_output('team_1/sample.py')  # Adjust file path as needed
        
        # Check if the script has output (i.e., it should not be empty)
        self.assertNotEqual(stdout.strip(), '', "Script did not produce any output!")
        
        # Optionally check for specific content in the output
        self.assertIn("Expected output text", stdout, "Expected output was not found in the script's output.")

    def test_script_error(self):
        """Test that the script does not produce any errors."""
        stdout, stderr, returncode = self.run_script_and_capture_output('team_1/sample.py')
        
        # Ensure there are no errors in stderr
        self.assertEqual(stderr, '', "Script produced an error: " + stderr)

        # Ensure that the script's return code is 0 (success)
        self.assertEqual(returncode, 0, f"Script failed with return code {returncode}.")

    def test_script_output_with_expected_content(self):
        """Test if the script's output matches an expected pattern or content."""
        stdout, stderr, returncode = self.run_script_and_capture_output('team_1/sample.py')

        # Example check: ensure output contains 'Hello, World!' or any specific string
        self.assertIn("Hello, World!", stdout, "Script did not print the expected 'Hello, World!'")

if __name__ == "__main__":
    unittest.main()
