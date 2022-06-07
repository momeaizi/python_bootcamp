from curses.ascii import islower
import sys

def convertCase(string):
    new_string = ""
    for e in string:
        if e.islower():
            new_string += e.upper()
        elif e.isupper():
            new_string += e.lower()
        else:
            new_string += e
    return new_string

def reverse(string):
    return string[::-1]

i = len(sys.argv) - 1;
while (i > 0):
    str = convertCase(sys.argv[i])
    print(reverse(str))
    i -= 1