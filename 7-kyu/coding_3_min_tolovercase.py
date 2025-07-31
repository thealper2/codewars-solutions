def to_lover_case(string):
    result = ""
    for c in string:
        if c.isalpha():
            c_ord = (ord(c.upper()) - ord("A")) % 4
            result += ["L", "O", "V", "E"][c_ord]
        else:
            result += c

    return "".join(result)
