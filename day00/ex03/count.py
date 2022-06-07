

def lowecase(text):
    counter = 0
    for c in text:
        if c.islower():
            counter += 1
    return (counter)

def uppercase(text):
    counter = 0
    for c in text:
        if c.isupper():
            counter += 1
    return (counter)

def space(text):
    counter = 0
    for c in text:
        if c.isspace():
            counter += 1
    return (counter)

def marks(text):
    counter = 0
    for c in text:
        if c in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?" ):
            counter += 1
    return (counter)

def  text_analyzer(text = ""):
    print("- ",uppercase(text)," upper letters")
    print("- ",lowecase(text)," lower letters")
    print("- ",marks(text)," punctuation marks")
    print("- ",space(text)," spaces")