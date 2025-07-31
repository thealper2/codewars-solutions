def abacaba(k):
    def helper(i, pos):
        if i == 1:
            return "a"
        mid = 2 ** (i - 1)
        if pos == mid:
            return chr(ord("a") + i - 1)
        elif pos < mid:
            return helper(i - 1, pos)
        else:
            return helper(i - 1, pos - mid)

    return helper(26, k)
