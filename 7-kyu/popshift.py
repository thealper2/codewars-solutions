def pop_shift(s):
    first = ""
    second = ""
    third = ""
    l, r = 0, len(s) - 1
    while l < r:
        second += s[l]
        first += s[r]

        l += 1
        r -= 1

    if l == r:
        third += s[l]
    return [first, second, third]
