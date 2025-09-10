import re

def valid_number(s):
    pattern = r'^[+-]?(\d+)?\.\d{2}$'
    return bool(re.match(pattern, s))
