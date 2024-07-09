#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

# 디렉토리 구분자가 /로 되어있어서 윈도우에서 실행이 안됨.
# 하지만 이렇게 하면 파이썬 코드에서 언급된 패키지에서 실행이 가능함.
prg = "C:/Users/unhoc/Documents/copilot_pair/03_picnic/picnic.py"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["", "-h", "--help"]:
        out = getoutput(
            f"C:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg} {flag}"
        )
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(
        f"C:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg} chips"
    )
    assert out.strip() == "You are bringing chips."


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(
        f'C:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg} soda "french fries"'
    )
    assert out.strip() == "You are bringing soda and french fries."


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(
        f"C:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg} {arg}"
    )
    expected = (
        "You are bringing potato chips, coleslaw, " "cupcakes, and French silk pie."
    )
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(
        f"C:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg} -s soda candy"
    )
    assert out.strip() == "You are bringing candy and soda."


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = "bananas apples dates cherries"
    out = getoutput(
        f"C:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe {prg} {arg} --sorted"
    )
    expected = "You are bringing apples, bananas, cherries, and dates."
    assert out.strip() == expected
