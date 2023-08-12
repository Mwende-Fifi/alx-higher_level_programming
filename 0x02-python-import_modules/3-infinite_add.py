#!/usr/bin/python3

import sys

def infinite_add(*args):
    """Prints the result of the addition of all arguments."""
    sum = 0
    for arg in args:
        sum += int(arg)

        print(sum)

        if __name__ == "__main__":
            infinite_add(*sys.argv[1:])
