import re


def whitespace(string):
    return bool(re.fullmatch(r"\s*", string))
