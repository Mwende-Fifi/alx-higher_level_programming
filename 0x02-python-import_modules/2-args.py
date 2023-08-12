#!/usr/bin/python3

import sys

if __name__ == "__main__":
    def print_args(argv):
        """Prints the number of and the list of its arguments."""
        argv = sys.argv
        if len(argv) == 0:
            print("0 arguments.")
            return
        print(f"{len(argv)} arguments:")
        for i in range(len(argv)):
            print(f"{i + 1}: {argv[i]}")

            print_args(argv)
