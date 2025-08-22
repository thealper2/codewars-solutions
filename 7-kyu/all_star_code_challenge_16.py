def no_repeat(string):
    for c in string:
        if string.count(c) == 1:
            return c
