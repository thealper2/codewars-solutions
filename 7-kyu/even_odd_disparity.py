def solve(a):
    c = 0
    for x in a:
        if type(x) in [float, int]:
            if x % 2 == 0:
                c += 1
            else:
                c -= 1

    return c
