import re


def wheres_wally(s):
    match_ = re.search(r' Wally\b', f' {s}')
    return match_.start() if match_ else -1