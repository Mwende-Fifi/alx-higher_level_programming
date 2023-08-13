#!/usr/bin/python3

import sys

if __name__ == "__main__":
    """Prints the number of and the list of its arguments."""
    av = sys.argv[1:]
    l_av = len(av)
    if l_av == 0:
        print(l_av, "arguments:")

    elif l_av == 1:
        print(l_av, "argument:")
        print("{:d}: {}".format(1, av[0]))

    else:
        print(l_av, "arguments:")
        for i in range(l_av):
            print("{:d}: {}".format(i + 1, av[i]))
