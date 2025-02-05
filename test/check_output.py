import subprocess

def check_output(file_path):
    try:
        # Run the script and capture its output
        result = subprocess.run(['python', file_path], capture_output=True, text=True, check=True)
        
        # If there is any output, print it
        if result.stdout.strip():
            print(f"Output detected in {file_path}:")
            print(result.stdout)
        else:
            print(f"No output detected in {file_path}.")
            return False
        
        return True

    except subprocess.CalledProcessError as e:
        # Handle errors if the script fails to execute
        print(f"Error while executing {file_path}: {e}")
        return False

# Example usage:
if __name__ == '__main__':
    file_path = 'your_script.py'  # Replace with the script you want to check
    check_output(file_path)
