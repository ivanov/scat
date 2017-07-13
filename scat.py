#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Schrödinger's cat

from __future__ import print_function

import argparse
import sys
import random


def print_file(f, number_lines=True, ignore_blank=False):
    i = 0
    for line in f:
        i, line_num = get_line_num(i, line, number_lines, ignore_blank)

        if random.randint(0,1):
            print(line_num + line[:-1])  # ignore trailing newline

def get_line_num(i, line, number_lines, ignore_blank):
    if not number_lines:
        return i, ''
    if ignore_blank and line == '\n':
        return i, ''
    i += 1

    return i, "% 6d  " % i


def main():
    parser = argparse.ArgumentParser(description="Schrödinger's cat --"
            "concatenate and print files")
    parser.add_argument('files', metavar='file', nargs='*',
            default=['/dev/stdin'], help='files')
    parser.add_argument('-b', dest='ignore_blank', action='store_true',
            help="Number the non-blank output lines, starting at 1.")
    parser.add_argument('-n', dest='number_lines', action='store_true',
            help="Number the non-blank output lines, starting at 1.")

    args = parser.parse_args()

    if args.ignore_blank == True:  # -b implies -n
        args.number_lines = True

    for fname in args.files:
        with open(fname) as f:
            print_file(f, args.number_lines, args.ignore_blank)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
