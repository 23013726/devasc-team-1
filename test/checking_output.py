import unittest
import subprocess
import os
import subprocess

# List of expected outputs we are looking for (case-insensitive)
EXPECTED_OUTPUTS = ["Hello", "World"]

def run_python_file(file_path):
    """Run a Python file and capture its output."""
    try:
        # Run the Python script and capture its output
        result = subprocess.run(['python', file_path], capture_output=True, text=True)
        
        # Print the actual output for debugging
        print(f"Output from {file_path}:\n{result.stdout}")

        # Convert the output to lowercase for case-insensitive comparison
        output = result.stdout.lower()

        # Check if any expected output is found (case-insensitive)
        output_found = False
        for expected in EXPECTED_OUTPUTS:
            if expected.lower() in output:  # Compare in lowercase
                print(f"Expected output '{expected}' found in {file_path}:")
                print(result.stdout)
                output_found = True
                break  # Once one expected output is found, no need to continue checking
        
        if not output_found:
            print(f"Expected outpu
