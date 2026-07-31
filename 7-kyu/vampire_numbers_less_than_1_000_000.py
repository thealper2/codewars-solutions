import math

_cache = []
_done_digits = 0

def _generate_block(d):
    lo = 10 ** (d - 1)
    hi = 10 ** d - 1
    found = set()
    for x in range(lo, hi + 1):
        x_zero = (x % 10 == 0)
        xs = str(x)
        for y in range(x, hi + 1):
            if x_zero and y % 10 == 0:
                continue
            z = x * y
            zs = str(z)
            if len(zs) != 2 * d:
                continue
            if sorted(zs) == sorted(xs + str(y)):
                found.add(z)
    return sorted(found)

def _extend_to(k):
    global _done_digits
    while len(_cache) < k:
        _done_digits += 1
        _cache.extend(_generate_block(_done_digits))

def vampire_number(k):
    if k > len(_cache):
        _extend_to(k)
    return _cache[k - 1]
