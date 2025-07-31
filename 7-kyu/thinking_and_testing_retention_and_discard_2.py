def mystery(s, n):
    bin_n = []
    while n > 0:
        bin_n.append(str(n % 2))
        n //= 2

    n = "".join(bin_n[::-1])
    return "".join(y for x, y in zip(n, s) if x == "1")
