#!/usr/bin/python3

def print_alphabet(exclude):
    """Prints the alphabets, except for the letters in the exclude list."""

if __name__ == "__main__":
    alphabet = ""
for i in range(97, 123):
    if i != 101 and i != 113:
        exclude = [101, 113]
        if i not in exclude:
            alphabet += chr(i)
            if alphabet:
                print(f"{alphabet}")
                print_alphabet(exclude)
