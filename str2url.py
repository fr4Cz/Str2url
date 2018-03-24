#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: zorko
# Year: 2018
import sys
import argparse as ap

unicode = False
double = False


def main(argv):
    global unicode
    global double

    p = ap.ArgumentParser(description='')
    p.add_argument('-s', '--string', type=str, help='String to convert')
    p.add_argument('-u', '--unicode', default=False, action='store_true', help='Convert to unicode not hex')
    p.add_argument('-d', '--double', default=False, action='store_true',
                   help='Enable double encoding, converts % to %25')

    try:
        arguments = validate_arguments(p.parse_args())
        unicode = arguments.unicode
        double = arguments.double
    except ValueError as ve:
        sys.exit(ve)

    print(convert(arguments.string))

    return


def convert(target):
    global double
    global unicode

    the_string = ''

    for c in target:
        if unicode:
            char = '{:04d}'.format(ord(c))
        else:
            char = '{}'.format(hex(ord(c)).split('x')[-1])

        if double:
            char = '%25{}'.format(char)
        else:
            char = '%{}'.format(char)

        the_string += char

    return the_string


def validate_arguments(argument_list):
    error_msg = "Check your input: {}"

    if not argument_list.string:
        sys.exit(error_msg.format('No string to convert...'))

    return argument_list


if __name__ == '__main__':
    main(sys.argv)
