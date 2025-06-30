def is_uppercase(inp):
    for i in inp:
        if i.isalpha() and i.islower():
            return False

    return True
