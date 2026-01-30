import subprocess
import sys
from pathlib import Path

import pytest


# Path to the script under test
SCRIPT_PATH = Path(__file__).resolve().parents[1] / "hw-loops-7boom" / "7boom-advanced.py"


def run_script_with_input(value: int) -> str:
    """Run the 7boom script with the provided integer and return stdout."""
    completed = subprocess.run(
        [sys.executable, str(SCRIPT_PATH)],
        input=str(value),
        text=True,
        capture_output=True,
        check=False,
    )
    # Script prints the prompt "Enter num!" without newline; remove it for assertions.
    return completed.stdout.replace("Enter num!", "").strip()


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, ""),
        (7, "Boom"),
        (777, "Boom"),
        (14, "Boom"),  # divisible by 7, no digit 7
        (1523, ""),
        (444, ""),
        (175714, "Boom"),
    ],
)
def test_boom_only_when_digit_seven_present(value: int, expected: str):
    """Boom should appear iff the input number's decimal digits include 7."""
    output = run_script_with_input(value)
    assert output == expected
