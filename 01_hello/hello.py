"""
Author : 장운호 <unho.chang@gmail.com>
Date   : 2024-07-08
"""

import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument(
        "-n", "--name", default="World", metavar="name", help="Name to greet"
    )
    return parser.parse_args()


def main():
    args = get_args()
    print("Hello, " + args.name + "!")


if __name__ == "__main__":
    main()
