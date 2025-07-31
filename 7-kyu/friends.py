import math


def friends(n):
    if n < 3:
        return 0

    return math.ceil(math.log2(n)) - 1
