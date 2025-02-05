# test_output_keywords.py
import subprocess

def test_output_contains_keywords():
    result = subprocess.run(['python', 'your_script.py'], capture_output=True, text=True)
    expected_keywords = ["Hello"]

    for keyword in expected_keywords:
        assert keyword in result.stdout, f"'{keyword}' not found in the output!"
