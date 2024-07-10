#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-07-09
Purpose: Python Coding Club
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "item",
        metavar="str",
        help="Item(s) to bring",
        nargs="+",
    )

    parser.add_argument(
        "-s",
        "--sorted",
        help="Sort the items",
        action="store_true",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item

    if args.sorted:
        items.sort()

    if len(items) == 1:
        str_arg = items[0]
        print(f"You are bringing {str_arg}.")
    elif len(items) == 2:
        str_arg = items[0] + " and " + items[1]
        print(f"You are bringing {str_arg}.")
    else:
        str_arg = ", ".join(items[:-1])
        print(f"You are bringing {str_arg}, and {items[-1]}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
