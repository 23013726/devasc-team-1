import unittest
import sys
import os

# Add the Project-Folder directory to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from team_1 import sample  # Import the Flask app instance

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        """Set up the test client."""
        self.app = sample.test_client()
        self.app.testing = True

    def test_main_route(self):
        """Test the main route ('/')."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to XYZ Company', response.data)

if __name__ == "__main__":
    unittest.main()
