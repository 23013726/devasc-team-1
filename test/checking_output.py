import unittest
from unittest.mock import patch
import io

# Sample function that prints output
def my_function():
    print("Hello, World!")

class TestOutput(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_function_output(self, mock_stdout):
        """Test that the function prints the expected output."""
        my_function()
        
        # Get the content of the printed output
        output = mock_stdout.getvalue().strip()
        
        # Check that the output is exactly what we expect
        self.assertEqual(output, "Hello, World!", "Function output did not match expected!")

if __name__ == "__main__":
    unittest.main()
