from preloaded import CHAR_TO_MORSE


def encryption(string):
    result = []
    for c in string:
        if c != " ":
            result.append(CHAR_TO_MORSE[c])
        else:
            result.append(c)

    return " ".join(result)
