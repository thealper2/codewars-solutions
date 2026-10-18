from collections import Counter


def common(a, b, c):
    ca, cb, cc = Counter(a), Counter(b), Counter(c)
    return sum(
        value * min(ca[value], cb[value], cc[value])
        for value in ca
        if value in cb and value in cc
    )