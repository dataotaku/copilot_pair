#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-07-11
Purpose: Python Coding Club
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        help="Input file(s)",
        metavar="FILE",
        nargs="*",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_arg = args.file

    if len(file_arg) == 1:
        file_arg = file_arg[0]
        num_lines = num_words = num_chars = 0
        for line in file_arg:
            num_lines += 1
            num_words += len(line.split())
            num_chars += len(line)
        print(f"{num_lines:8}{num_words:8}{num_chars:8} {file_arg.name}")
    else:
        total_lines = total_words = total_chars = 0
        for file in file_arg:
            num_lines = num_words = num_chars = 0
            for line in file:
                num_lines += 1
                num_words += len(line.split())
                num_chars += len(line)
            total_lines += num_lines
            total_words += num_words
            total_chars += num_chars
            print(
                f"{num_lines:8}{num_words:8}{num_chars:8} {file.name}",
                end="" if len(file_arg) == 0 else "\n",
            )
        print(f"{total_lines:8}{total_words:8}{total_chars:8} total", end="")


# --------------------------------------------------
if __name__ == "__main__":
    main()
