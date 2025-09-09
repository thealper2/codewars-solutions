def strange_math(n, k):
    arr = list(range(1, n + 1))
    arr.sort(key=str)
    return arr.index(k) + 1
