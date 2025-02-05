import subprocess
import os
import sys

# Specific keywords to look for in the output
EXPECTED_OUTPUTS = ["Hello", "World"]

def run_python_file(file_path):
    """Run a Python file and capture its output."""
    try:
        # Run the Python script and capture output
        result = subprocess.run(['python', file_path], capture_output=True, text=True)
        
        # Check if any expected output is found
        output_found = False
        for expected in EXPECTED_OUTPUTS:
            if expected in result.stdout:
                print(f"Expected output '{expected}' found in {file_path}:")
                print(result.stdout)
                output_found = True
        
        if not output_found:
            print(f"Expected output not found in {file_path}.")
        
        return output_found
    except Exception as e:
        print(f"Error running {file_path}: {e}")
        return False

def get_changed_files():
    """Get the list of changed Python files from the latest commit."""
    try:
        # Use git to get the changed Python files from the latest commit
        result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error getting the list of changed files.")
            return []
        
        # Filter the Python files
        changed_files = [file for file in result.stdout.splitlines() if file.endswith('.py')]
        return changed_files
    except Exception as e:
        print(f"Error checking changed files: {e}")
        return []

def main():
    # Get the changed Python files from the latest commit
    changed_files = get_changed_files()
    
    if not changed_files:
        print("No Python files changed in the latest commit.")
        sys.exit(0)  # Exit normally if no Python files are changed
    
    output_found = False
    
    for file in changed_files:
        print(f"Checking {file}...")
        if run_python_file(file):
            output_found = True
    
    if output_found:
        print("Expected output found in at least one Python file.")
        sys.exit(0)  # Exit with success (0) if expected output is found
    else:
        print("Expected output not found in any Python files!")
        sys.exit(1)  # Exit with failure (1) if expected output is not found

if __name__ == "__main__":
    main()
