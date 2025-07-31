def convert(st):
    result = ""
    for c in st:
        if c == "o":
            result += "u"
        elif c == "a":
            result += "o"
        else:
            result += c

    return result
