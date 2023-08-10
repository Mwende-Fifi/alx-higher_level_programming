#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 0:
        print("0 arguments.")
else:
    print("Number of arguments: {}".format(len(sys.argv)))
    print("Arguments:")
    for i in range(len(sys.argv)):
        print("{}: {}".format(i + 1, sys.argv[i]))
