def twos_difference(lst):
    s = set(lst)
    return sorted((x, x + 2) for x in s if x + 2 in s)