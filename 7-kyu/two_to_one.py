def longest(a1, a2):
    a1_set = list(set(a1))
    a2_set = list(set(a2))
    s = ''.join(list(set(a1_set + a2_set)))
    return ''.join(sorted(s))
