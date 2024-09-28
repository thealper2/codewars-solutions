import re

def is_digit(n):
    found = re.findall('[\d]', n)
    if found:
        return found[0] == n
    else:
        return False