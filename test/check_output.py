import unittest
import subprocess
import sys

def run_code_and_check_output(file_path):
    try:
        # Run the Python file and capture the output
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Check if there is any output
        if result.stdout.strip():
            print(f"Output produced by {file_path}: {result.stdout}")
            return True
        else:
            print(f"No output produced by {file_path}.")
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error running {file_path}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_output.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not run_code_and_check_output(file_path):
        sys.exit(1)  # Exit with error if no output is produced
