#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-08-06
Purpose: Python Coding Club
"""

import argparse
import sys


# --------------------------------------------------
def check_num_days(value):
    ivalue = int(value)
    if ivalue < 1 or ivalue > 12:
        raise argparse.ArgumentTypeError(f'--num "{value}" must be between 1 and 12')
    return ivalue


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Twelve Days of Christmas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--num",
        help="Number of days to sing",
        metavar="days",
        type=check_num_days,
        default=12,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Outfile",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=None,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    day = args.num
    out_fh = args.outfile if args.outfile else sys.stdout
    out_fh.write("\n\n".join([verse(i) for i in range(1, day + 1)]))


# ---------
# Mapping of numbers to ordinal words
ordinal_map = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
}

gift_map = {
    1: "A partridge in a pear tree",
    2: "Two turtle doves",
    3: "Three French hens",
    4: "Four calling birds",
    5: "Five gold rings",
    6: "Six geese a laying",
    7: "Seven swans a swimming",
    8: "Eight maids a milking",
    9: "Nine ladies dancing",
    10: "Ten lords a leaping",
    11: "Eleven pipers piping",
    12: "Twelve drummers drumming",
}


def lowercase_first_letter(s):
    """Lowercase the first letter of a string"""
    return s[0].lower() + s[1:] if s else s


def verse(day):
    """Create a verse"""
    ordinal_day = ordinal_map.get(day, str(day))
    words = []
    words.append(f"On the {ordinal_day} day of Christmas")
    words.append("My true love gave to me")
    if day == 1:
        words.append(gift_map.get(day))
        return ",\n".join(words[:]) + "."
    elif day > 1:
        for i in range(day, 0, -1):
            words.append(gift_map.get(i))
        return (
            ",\n".join(words[:-1]) + ",\nAnd " + lowercase_first_letter(words[-1]) + "."
        )


def test_verse():
    """Test verse"""
    assert verse(1) == "\n".join(
        [
            "On the first day of Christmas,",
            "My true love gave to me,",
            "A partridge in a pear tree.",
        ]
    )
    assert verse(2) == "\n".join(
        [
            "On the second day of Christmas,",
            "My true love gave to me,",
            "Two turtle doves,",
            "And a partridge in a pear tree.",
        ]
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
