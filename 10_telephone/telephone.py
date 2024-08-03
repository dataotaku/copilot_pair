#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-07-11
Purpose: Python Coding Club
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Telephone", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="int", type=int, default=None
    )

    parser.add_argument(
        "-m",
        "--mutations",
        help="Percent mutations",
        metavar="mutations",
        type=float,
        default=0.1,
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, "rt") as f:
            args.text = f.read().rstrip()

    if args.mutations > 1 or args.mutations < 0:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    print(f'You said: "{args.text}"')

    alpha = "".join(sorted(string.ascii_letters + string.punctuation))

    if args.mutations:
        charlist = list(args.text)
        num_mutations = round(len(charlist) * args.mutations)
        idxes = random.sample(range(len(charlist)), num_mutations)

        for idx in idxes:
            charlist[idx] = random.choice([ch for ch in alpha if ch != charlist[idx]])

        args.text = "".join(charlist)

    print(f'I heard : "{args.text}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
