#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-08-06
Purpose: Python Coding Club
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word to rhyme")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word


# ----------------------------------------------------
def stammer():
    """Return leading consonants (if any), and 'stem' of word"""
    pass


# ----------------------------------------------------
def test_stemmer():
    """test the stammer function"""
    assert stammer("") == ("", "")
    assert stammer("cake") == ("c", "ake")
    assert stammer("chair") == ("ch", "air")
    assert stammer("APPLE") == ("", "apple")
    assert stammer("RDNZL") == ("rdnzl", "")
    assert stammer("123") == ("123", "")


# --------------------------------------------------
if __name__ == "__main__":
    main()
