#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for i in my_string:
        if ord(i) not in (ord('c'), ord('C')):
            new_str += i

    return new_str
