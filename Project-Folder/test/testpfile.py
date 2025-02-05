import unittest
from team_1 import sample  # Import the Flask app instance

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        """Set up the test client."""
        self.app = sample.test_client()
        self.app.testing = True  # Set testing mode to True

    def test_main_route(self):
        """Test the main route ('/')."""
        response = self.app.get('/')  # Send a GET request to the '/' route
        self.assertEqual(response.status_code, 200, "Main route did not return a 200 status code")
        self.assertIn(b'<h1>', response.data, "Expected <h1> tag not found in the response")
        self.assertIn(b'Welcome to XYZ Company', response.data, "Expected text not found in the response")

    def test_404_error(self):
        """Test for a 404 error on an undefined route."""
        response = self.app.get('/undefined_route')
        self.assertEqual(response.status_code, 404, "Undefined route did not return a 404 status code")

if __name__ == "__main__":
    unittest.main()