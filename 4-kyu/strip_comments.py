import re

def strip_comments(string, markers):
    if not markers:
        return '\n'.join(line.rstrip() for line in string.split('\n'))

    pattern = '[' + re.escape(''.join(markers)) + ']'
    return '\n'.join(
        re.split(pattern, line)[0].rstrip()
        for line in string.split('\n')
    )