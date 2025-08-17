import re


def nothing_special(st):
    if not isinstance(st, str):
        return "Not a string!"

    filtered = re.sub(r'[^A-Za-z0-9\s]', '', st)
    return filtered
