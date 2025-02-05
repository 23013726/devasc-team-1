import subprocess
import os
import sys

def run_python_file(file_path):
    """Run a Python file and capture its output."""
    try:
        # Run the Python script and capture output
        result = subprocess.run(['python', file_path], capture_output=True, text=True)
        
        # Check if there is any output
        if result.stdout.strip():  # If there is any output
            print(f"Output detected in {file_path}:\n{result.stdout}")
            return True
        elif result.stderr.strip():  # Check if there is any error output
            print(f"Error detected in {file_path}:\n{result.stderr}")
            return False
        else:
            return False  # No output or error
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
        print("Output detected in at least one Python file.")
        sys.exit(0)  # Exit with success (0) if output is found
    else:
        print("No output detected in any Python files!")
        sys.exit(1)  # Exit with failure (1) if no output is found

if __name__ == "__main__":
    main()
