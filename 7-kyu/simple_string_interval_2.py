def solve(st, a, b):
    if b >= len(st):
        b = len(st) - 1
    substring = st[a : b + 1]
    reversed_substring = substring[::-1]
    return st[:a] + reversed_substring + st[b + 1 :]
