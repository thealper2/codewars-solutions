import math

def compare_powers(n1, n2):
    b1, e1 = n1
    b2, e2 = n2
    v1 = e1 * math.log(b1)
    v2 = e2 * math.log(b2)
    if v1 > v2:
        return -1
    elif v1 < v2:
        return 1
    else:
        return 0