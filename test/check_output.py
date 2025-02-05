import subprocess
import sys

def check_output(file_path):
    try:
        # Run the script and capture its output
        result = subprocess.run(['python', file_path], capture_output=True, text=True, check=True)
        
        # If the script has output
        if result.stdout.strip():
            print(f"Output detected in {file_path}:")
            print(result.stdout)
        else:
            print(f"No output detected in {file_path}.")
            return False

        # If the script raises an error in stderr, reject it
        if result.stderr.strip():
            print(f"Error in {file_path}:")
            print(result.stderr)
            return False
        
        return True

    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        print(f"Error while executing {file_path}:")
        print(e.stderr)
        return False

# Example usage:
if __name__ == '__main__':
    file_path = 'your_script.py'  # Replace with the script you want to check
    if not check_output(file_path):
        sys.exit(1)  # Exit with error code 1 if the script has no output or errors
    else:
        print(f"{file_path} passed the check and has valid output!")
