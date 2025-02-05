# test_app.py
import unittest
from app import add_numbers  # Import function from app.py

class TestApp(unittest.TestCase):

    def test_add_numbers(self):
        """Test if add_numbers correctly adds two numbers"""
        self.assertEqual(add_numbers(2, 3), 5)  # Expected output: 5

    def test_negative_numbers(self):
        """Test adding negative numbers"""
        self.assertEqual(add_numbers(-1, -1), -2)

    def test_zero(self):
        """Test adding zero"""
        self.assertEqual(add_numbers(0, 5), 5)

if __name__ == '__main__':
    unittest.main()