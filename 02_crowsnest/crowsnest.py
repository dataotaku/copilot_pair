#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-07-08
Purpose: Python Coding Club
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Python Coding Club",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="str", help="A positional argument")

    parser.add_argument(
        "-a",
        "--arg",
        help="A named string argument",
        metavar="str",
        type=str,
        default="",
    )

    parser.add_argument(
        "-i",
        "--int",
        help="A named integer argument",
        metavar="int",
        type=int,
        default=0,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="A readable file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default=None,
    )

    parser.add_argument("-o", "--on", help="A boolean flag", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.word

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    # f스트링으로 변환하는 코드가 신기함. ""와  '의 조합이 신기함.
    print(f'file_arg = "{file_arg.name if file_arg else ""}"')
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
