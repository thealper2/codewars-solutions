def cyclic_string(s):
    n = len(s)
    for k in range(1, n + 1):
        base = s[:k]
        valid = True
        for i in range(n):
            if s[i] != base[i % k]:
                valid = False
                break
        if valid:
            return k
    return n
