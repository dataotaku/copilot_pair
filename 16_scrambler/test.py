#!/usr/bin/env python3
"""tests for scrambler.py"""

import os
import re
from subprocess import getstatusoutput, getoutput

interpreter = "c:/Users/unhoc/Documents/copilot_pair/.copilot_pair/Scripts/python.exe"

prg = "c:/Users/unhoc/Documents/copilot_pair/16_scrambler/scrambler.py"

fox = "c:/Users/unhoc/Documents/copilot_pair/inputs/fox.txt"
bustle = "c:/Users/unhoc/Documents/copilot_pair/inputs/the-bustle.txt"
spiders = "c:/Users/unhoc/Documents/copilot_pair/inputs/spiders.txt"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{interpreter} {prg} {flag}")
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_text1():
    """Text"""

    out = getoutput(f"{interpreter} {prg} foobar -s 1")
    assert out.strip() == "faobor"


# --------------------------------------------------
def test_text2():
    """Text"""

    text = "The quick brown fox jumps over the lazy dog."
    expected = "The qicuk bworn fox jpmus over the lzay dog."
    out = getoutput(f'{interpreter} {prg} "{text}" -s 2')
    assert out.strip() == expected


# --------------------------------------------------
def test_file_bustle():
    """File input"""

    expected = """
The blutse in a hosue
The mrinong afetr daeth
Is seosnmelt of iinuetdrss
Etecand upon etrah,--

The sweenipg up the herat,
And pniuttg lvoe away
We slahl not want to use again
Unitl eettnriy.
    """.strip()

    out = getoutput(f"{interpreter} {prg} --seed 3 {bustle}")
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_file_fox():
    """File input"""

    out = getoutput(f"{interpreter} {prg} --seed 4 {fox}")
    assert out.strip() == "The qciuk bworn fox jpums oevr the lzay dog."


# --------------------------------------------------
def test_file_spiders():
    """File input"""

    out = getoutput(f"{interpreter} {prg} --seed 9 {spiders}")
    expected = "Do'nt wrory, sedrpis,\nI keep hsoue\ncalusaly."
    assert out.strip() == expected
