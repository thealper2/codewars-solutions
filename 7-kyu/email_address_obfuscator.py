def obfuscate(email):
    result = ""
    temp = ""
    for c in email:
        if c == ".":
            result += temp + " [dot] "
            temp = ""
        elif c == "@":
            result += temp + " [at] "
            temp = ""
        else:
            temp += c

    result += temp
    return result
