# Schrödinger's cat

from __future__ import print_function

import sys
import random


def print_file(f, number_lines=True, ignore_whitespace=False):
    i = 0
    for line in f:
        i, line_num = get_line_num(i, line, number_lines, ignore_whitespace)

        if random.randint(0,1):
            print(line_num + line[:-1])  # ignore trailing newline

def get_line_num(i, line, number_lines, ignore_whitespace):
    if not number_lines:
        return i, ''
    if ignore_whitespace and line == '':
        return i, ''
    i += 1

    return i, "% 6d  " % i


if __name__ == "__main__":
    if len(sys.argv) == 1:
        files = ['/dev/stdin']
    else:
        files = sys.argv[1:]

    for fname in files:
        with open(fname) as f:
            print_file(f, number_lines=True, ignore_whitespace=True)


