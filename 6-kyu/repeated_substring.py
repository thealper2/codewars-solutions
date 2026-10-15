def f(s):
    n = len(s)
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            pattern = s[:length]
            if pattern * (n // length) == s:
                return (pattern, n // length)

    return (s, 1)