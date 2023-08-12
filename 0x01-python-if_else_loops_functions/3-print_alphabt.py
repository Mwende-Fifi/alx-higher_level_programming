#!/usr/bin/python3
alphabet = ""
for i in range(97, 123):
    if i != 101 and i != 113:
        if i not in exclude:
            alphabet += chr(i)
            if alphabet:
                print(f"{alphabet}"


                    if __name__ == "__main__":
                    exclude = [101, 113]
                    print_alphabet(exclude)
