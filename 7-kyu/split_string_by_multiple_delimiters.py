import re

def multiple_split(string, delimiters=[]):
    if not delimiters:
        return [string] if string else []
    pattern = '|'.join(map(re.escape, delimiters))
    parts = re.split(pattern, string)
    return [part for part in parts if part != '']
