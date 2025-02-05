import subprocess
import sys

def check_output(file_path):
    """
    Check if the given Python file produces any output.
    """
    try:
        # Run the Python file and capture stdout
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True
        )

        # Debugging: Print stdout and stderr
        print(f"=== Debug: Output of {file_path} ===")
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)

        # Fail if stdout is empty
        if not result.stdout.strip():
            print(f"❌ No output produced by {file_path}.")
            return False

        print(f"✅ Valid output in {file_path}:\n{result.stdout}")
        return True

    except Exception as e:
        print(f"❌ Error running {file_path}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_output.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not check_output(file_path):
        sys.exit(1)  # Exit with error if no output is produced
