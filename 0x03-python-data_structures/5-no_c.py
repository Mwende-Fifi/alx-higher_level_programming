#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string."""
    new_string = ""
    for char in my_string:
        if char != "c" and char != "C":
            new_string += char

            return new_string

        if __name__ == "__main__":
            my_string = "Best School"
            print(no_c(my_string))

            my_string = "Chicago"
            print(no_c(my_string))

            my_string = "C is fun"
            print(no_c(my_string))
