#!/usr/bin/python3

import sys
def print_args(argv):
        """Prints the number of and the list of its arguments."""

        av = sys.argv
        l_av = len(av) - 1

        if l_av > 1:
            print(l_av, "0 arguments:")
            for i in range(1, l_av + 1):
                print("{:d}: {}".format(i, av[i]))

            elif l_av == 1:
                print(l_av, "argument:")
                for i in range(1, l_av + 1):
                    print("{:d}: {}".format(i, av[i]))
                
                else:
                    print(l_av, "arguments.")
                    if __name__ == "__main__":
                        print_args(sys.argv)
