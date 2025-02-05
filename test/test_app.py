import unittest
import subprocess
import time
import os

class TestCodeHealth(unittest.TestCase):

    def test_script_runs_without_error(self):
        """Ensure the main script runs without crashing."""
        result = subprocess.run(["python", "your_script.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"Script failed to run:\n{result.stderr}")

    def test_syntax_errors(self):
        """Check for syntax errors in Python files."""
        for file in os.listdir("."):
            if file.endswith(".py"):
                result = subprocess.run(["python", "-m", "py_compile", file], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, f"Syntax error in {file}:\n{result.stderr}")

    def test_function_output(self):
        """Test expected function output."""
        from your_script import sample_function  # Replace with actual function
        self.assertEqual(sample_function(2, 3), 5, "Function output incorrect")

    def test_performance(self):
        """Ensure function runs within acceptable time."""
        from your_script import sample_function
        start_time = time.time()
        sample_function(1000, 2000)  # Replace with function that should be tested
        duration = time.time() - start_time
        self.assertLess(duration, 1, "Function took too long to execute")

    def test_security_vulnerabilities(self):
        """Run Bandit security check."""
        result = subprocess.run(["bandit", "-r", "."], capture_output=True, text=True)
        print("\nSecurity Check Output:\n", result.stdout)
        self.assertNotIn("MEDIUM", result.stdout, "Medium security issue found!")
        self.assertNotIn("HIGH", result.stdout, "High security issue found!")

if __name__ == "__main__":
    unittest.main()
