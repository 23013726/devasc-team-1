# test_app.py
import unittest
from app import add_numbers

class TestApp(unittest.TestCase):

    def test_add_numbers(self):
        """Test if add_numbers correctly adds two numbers"""
        self.assertEqual(add_numbers(2, 3), 5)  # This will fail because app.py returns -1

    def test_negative_numbers(self):
        """Test adding negative numbers"""
        self.assertEqual(add_numbers(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
