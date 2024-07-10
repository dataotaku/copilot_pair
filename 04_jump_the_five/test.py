#!/usr/bin/env python3
"""tests for jump.py"""

import os
from subprocess import getstatusoutput

prg = "c:/Users/unhoc/Documents/copilot_pair/04_jump_the_five/jump.py"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(
            f"c:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg} {flag}"
        )
        assert rv == 0
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_01():
    """test"""

    rv, out = getstatusoutput(
        f"c:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg} 123-456-7890"
    )
    assert rv == 0
    assert out == "987-604-3215"


# --------------------------------------------------
def test_02():
    """test"""

    rv, out = getstatusoutput(
        f'c:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg} "That number to call is 098-765-4321."'
    )
    assert rv == 0
    assert out.rstrip() == "That number to call is 512-340-6789."
