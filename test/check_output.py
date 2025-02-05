import unittest
import subprocess
import sys

def run_code_and_check_output(file_path):
    try:
        # Run the Python file and capture the output and errors
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Check for errors in stderr
        if result.stderr.strip():
            print(f"Error in {file_path}: {result.stderr}")
            return False
        
        # Check if there is any valid output in stdout
        if result.stdout.strip():
            print(f"Output produced by {file_path}: {result.stdout}")
            return True
        else:
            print(f"No output produced by {file_path}.")
            return False
    except subprocess.CalledProcessError as e:
        # Handle cases where the script exits with a non-zero status
        print(f"Error running {file_path}: {e.stderr}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_output.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not run_code_and_check_output(file_path):
        sys.exit(1)  # Exit with error if the script fails
