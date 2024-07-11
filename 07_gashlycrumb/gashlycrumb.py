#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-07-11
Purpose: Python Coding Club
"""

import argparse
from pathlib import Path

current_dir = Path.cwd()
file_path = "c:/Users/unhoc/Documents/copilot_pair/07_gashlycrumb/gashlycrumb.txt"


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter",
        metavar="letter",
        nargs="+",
        help="Letter(s)",
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default=file_path,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    letter_dict = {}
    with args.file as file:
        for line in file:
            letter_dict[line[0]] = line.strip()

    for letter in args.letter:
        if letter.upper() in letter_dict:
            print(letter_dict[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()
