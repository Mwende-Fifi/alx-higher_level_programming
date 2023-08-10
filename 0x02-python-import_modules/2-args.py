#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 0:
        print("0 arguments.")
    elif len(sys.argv) == 1:
        print("1 argument:")
        print("1: {}".format(len(sys.argv[0])))
else:
    print("Number of arguments: {}".format(len(sys.argv)))
    print("Arguments:")
    for i in range(len(sys.argv)):
        print("{}: {}".format(i + 1, sys.argv[i]))
