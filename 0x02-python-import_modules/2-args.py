#!/usr/bin/python3

import sys


def print_args(argv):
    """Prints the number of and the list of its arguments."""


if not argv:
    print("0 arguments.")
    return

print(f"Number of arguments: {len(argv)}")
for i in range(len(argv)):
    print(f"{i + 1}: {argv[i]}")


if __name__ == "__main__":
    argv = sys.argv
    print_args(argv)
