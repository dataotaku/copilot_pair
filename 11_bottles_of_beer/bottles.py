#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-07-17
Purpose: Python Coding Club
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Bottles of beer song",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--number",
        help="How many bottles",
        metavar="number",
        type=int,
        default=10,
    )

    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--num "{args.number}" must be greater than 0')

    return args


def verse(bottle):
    """Sing a verse"""

    next_ = bottle - 1

    s1 = "" if bottle == 1 else "s"
    s2 = "" if next_ == 1 else "s"
    num_next = "No more" if next_ == 0 else next_

    return "\n".join(
        [
            f"{bottle} bottle{s1} of beer on the wall,",
            f"{bottle} bottle{s1} of beer,",
            f"Take one down, pass it around,",
            f"{num_next} bottle{s2} of beer on the wall!",
        ]
    )


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num = args.number

    for n in range(num, 0, -1):
        if n == 1:
            print(verse(n))
        else:
            print(verse(n))
            print()


# --------------------------------------------------
if __name__ == "__main__":
    main()
