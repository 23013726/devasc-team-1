import unittest
import subprocess
import sys

def run_code_and_check_output(file_path):
    """
    Run a Python file and check if it produces valid output and no errors.
    """
    try:
        # Run the Python file and capture output and errors
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Check for errors in stderr
        if result.stderr.strip():
            print(f"❌ Error in {file_path}:")
            print(result.stderr)
            return False
        
        # Check if there is any valid output in stdout
        if result.stdout.strip():
            print(f"✅ Output produced by {file_path}:")
            print(result.stdout)
            return True
        else:
            print(f"❌ No output produced by {file_path}.")
            return False
    except subprocess.CalledProcessError as e:
        # Handle cases where the script exits with a non-zero status
        print(f"❌ Error running {file_path}:")
        print(e.stderr)
        return False

if __name__ == "__main__":
    # Check if a file path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python check_output.py <file_path>")
        sys.exit(1)
    
    # Get the file path from the command-line argument
    file_path = sys.argv[1]
    
    # Run the check and exit with an error if it fails
    if not run_code_and_check_output(file_path):
        sys.exit(1)
