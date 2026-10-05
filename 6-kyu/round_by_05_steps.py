def solution(n):
    a = int(n)
    b = n - a

    if b < 0.25:
        return a
    elif b < 0.75:
        return a + 0.5
    else:
        return a + 1