import sys


def isInt(str):
    for e in str:
        if not e.isdigit():
            return 0
    return 1

def handleErrors(argv):
    length = len(argv)
    if (length > 2):
        print("AssertionError: more than one argument is provided")
        return (0)
    elif (length == 2 and not isInt(argv[1])):
        print("AssertionError: argument is not integer")
        return 0
    return 1




if handleErrors(sys.argv):
    nbr = int(sys.argv[1])
    if (nbr == 0):
        print("I’m Zero.")
    elif (nbr % 2 == 0):
        print("I’m Even.")
    else:
        print("I’m Odd.")