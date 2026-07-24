"""
There's nothing to edit in this module — no exercise.py here.

This test exists purely to prove your environment is set up correctly.
If you see "1 passed" when you run `pytest` from this folder (with your
.venv activated), your setup is good and you're ready for Module 01.
"""

import sys


def test_python_version_is_recent_enough():
    assert sys.version_info >= (3, 9), (
        f"Python {sys.version_info.major}.{sys.version_info.minor} is quite old — "
        "you're probably not using the .venv you just created."
    )


def test_pytest_itself_is_working():
    assert 1 + 1 == 2
