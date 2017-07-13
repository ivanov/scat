# Schrödinger's cat

from __future__ import print_function

import sys


def print_file(f):
    i = 0
    for line in f:
        i += 1
        line_num = "% 6d  " % i 
        print(line_num + line[:-1])  # ignore trailing newline

if __name__ == "__main__":
    if len(sys.argv) == 1:
        files = ['/dev/stdin']
    for fname in files:
        with open(fname) as f:
            print_file(f)


