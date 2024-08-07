#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-08-06
Purpose: Python Coding Club
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Ransom Note",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="int", type=int, default=None
    )

    args = parser.parse_args()
    if os.path.isfile(args.text):
        with open(args.text, "rt") as f:
            args.text = f.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    state = random.getstate()
    random.seed(args.seed)

    ransom = "".join(map(choose, args.text))
    print(ransom)
    random.setstate(state)


def choose(char):
    return char.upper() if random.choice([False, True]) else char.lower()


def test_choose():
    """Test choose"""

    state = random.getstate()
    random.seed(1)
    assert choose("a") == "a"
    assert choose("b") == "b"
    assert choose("c") == "C"
    assert choose("d") == "d"
    random.setstate(state)


# --------------------------------------------------
if __name__ == "__main__":
    main()
