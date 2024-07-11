#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-07-11
Purpose: Python Coding Club
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python Coding Club',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.text
    vowel_arg = args.vowel
    
    vowels = 'aeiou'
    if args.vowel not in vowels:
        print(f'usage: --vowel "{vowel_arg}" must be a vowel')
        exit(1)
    else:
        if args.vowel == None:
            vowel = 'a'
        else:
            vowel = vowel_arg

    new_text = ''
    if os.path.isfile(str_arg):
        with open(str_arg, 'rt') as f:
            str_arg = f.read().rstrip()
        
    for char in str_arg:
        if char in vowels:
            new_text += vowel
        elif char.upper() in vowels.upper():
            new_text += vowel.upper()
        else:
            new_text += char

    print(new_text)



# --------------------------------------------------
if __name__ == '__main__':
    main()
