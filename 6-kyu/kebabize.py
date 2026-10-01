def kebabize(st):
    result = ''
    n = len(st)
    for i, c in enumerate(st):
        if c.isalpha():
            if c.isupper():
                result += '-' + c.lower() if i != 0 else c.lower()
            else:
                result += c

    return result