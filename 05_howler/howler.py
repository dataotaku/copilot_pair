#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-07-10
Purpose: Python Coding Club
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="Input string or file")

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="str",
        type=str,
        default=None,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_arg = args.outfile
    pos_arg = args.text

    if os.path.isfile(pos_arg):
        with open(pos_arg, "rt") as f:
            pos_arg = f.read().rstrip()
    print(pos_arg.upper(), file=file_arg)


# --------------------------------------------------
if __name__ == "__main__":
    main()
