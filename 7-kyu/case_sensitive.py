def case_sensitive(s):
    uppercase_letters = []
    all = True
    for c in s:
        if c.isupper():
            uppercase_letters.append(c)
            all = False

    return [all, uppercase_letters]
