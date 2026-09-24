def first_dup(s):
    n = len(s)
    for i in range(n - 1):
        c = s[i]
        if c in s[i+1:]:
            return c

    return None