import subprocess
import sys


def test_sample_program():
    command = [sys.executable, "samples/sample.py"]
    process = subprocess.run(command, capture_output=True, text=True, check=True)
    expected_output = (
        "1 + 2 = 3.0\n"
        "3 - 1 = 2.0\n"
        "2 * 3 = 6.0\n"
        "6 / 2 = 3.0\n"
        "Error: Cannot divide by zero!\n"
    )
    assert process.stdout == expected_output


def test_interactive_sample_program():
    command = [sys.executable, "samples/interactive_sample.py"]
    input_data = "add 1 2\nsub 5 3\nexit\n"
    process = subprocess.run(
        command, input=input_data, capture_output=True, text=True, check=True
    )
    assert "Interactive Calculator. Type 'exit' or 'quit' to end." in process.stdout
    assert ">>> Result: 3.0" in process.stdout
    assert ">>> Result: 2.0" in process.stdout
    assert ">>> " in process.stdout
