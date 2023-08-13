#!/usr/bin/python3

import sys

if __name__ == '__main__':
    av = sys.argv
    l_av = len(av)
    total_sum = 0

    if l_av > 1:
        for i in range(1, l_av):
            total_sum += int(av[i])

            print(total_sum)
