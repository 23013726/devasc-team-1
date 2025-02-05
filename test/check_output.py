import unittest
import subprocess
import sys

def run_code_and_check_output(file_path):
    try:
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            check=True  # This will raise an error for non-zero exit codes
        )
        
        # Check for stderr (even if exit code is 0)
        if result.stderr.strip():
            print(f"❌ stderr detected in {file_path}:")
            print(result.stderr)
            return False
        
        # Check for stdout
        if not result.stdout.strip():
            print(f"❌ No stdout produced by {file_path}.")
            return False
        
        print(f"✅ Valid output in {file_path}:")
        print(result.stdout)
        return True

    except subprocess.CalledProcessError as e:
        # Handle non-zero exit codes (e.g., exceptions)
        print(f"❌ Error running {file_path} (exit code {e.returncode}):")
        print("=== stderr ===")
        print(e.stderr)
        print("=== stdout ===")
        print(e.stdout)
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_output.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not run_code_and_check_output(file_path):
        sys.exit(1)
