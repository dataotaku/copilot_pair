#!/usr/bin/env python3
"""tests for hello.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = "C:/Users/unhoc/Documents/copilot_pair/01_hello/hello.py"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_runnable():
    """Runs using python3"""

    out = getoutput(
        f"C:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg}"
    )
    assert out.strip() == "Hello, World!"


# --------------------------------------------------
def test_executable():
    """Says 'Hello, World!' by default"""

    out = getoutput(
        f"C:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg}"
    )
    assert out.strip() == "Hello, World!"


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(
            f"C:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg} {flag}"
        )
        assert rv == 0
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_input():
    """test for input"""

    for val in ["Universe", "Multiverse"]:
        for option in ["-n", "--name"]:
            rv, out = getstatusoutput(
                f"C:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg} {option} {val}"
            )
            assert rv == 0
            assert out.strip() == f"Hello, {val}!"
