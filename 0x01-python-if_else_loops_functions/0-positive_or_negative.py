#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number = input("Enter the number:")
number = int(number)
if (number > 0):
    print("{} is positive".format(number))
elif (number == 0):
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
