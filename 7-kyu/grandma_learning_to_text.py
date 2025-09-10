import re


def textin(s):
    return re.sub(r'(?i)too|two|to', '2', s)
