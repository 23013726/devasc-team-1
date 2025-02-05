import unittest
import subprocess

EXPECTED_OUTPUTS = ["Hello", "World"]

def run_python_file(file_path):
    """Run a Python file and capture its output."""
    try:
        # Run the Python script and capture output
        result = subprocess.run(['python', file_path], capture_output=True, text=True)
        
        # Check if any expected output is found
        output_found = False
        for expected in EXPECTED_OUTPUTS:
            if expected in result.stdout:
                print(f"Expected output '{expected}' found in {file_path}:")
                print(result.stdout)
                output_found = True
        
        if not output_found:
            print(f"Expected output not found in {file_path}.")
        
        return output_found
    except Exception as e:
        print(f"Error running {file_path}: {e}")
        return False

class TestFlaskApp(unittest.TestCase):

    def test_check_output(self):
        """Test to ensure specific output is detected in a Python file."""
        file_path = "sample.py"  # Your Python file to test
        self.assertTrue(run_python_file(file_path))  # Assert that output is found

if __name__ == "__main__":
    unittest.main()
