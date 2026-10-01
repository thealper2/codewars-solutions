from itertools import permutations as perm


def permutations(string):
    return sorted(set(''.join(p) for p in perm(string)))