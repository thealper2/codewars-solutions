def zero_and_one(s):
    l, r = 1, len(s)
    while l < len(s):
        if s[l] != s[l - 1]:
            r -= 2
            l += 2
        else:
            l += 1
    return r
