def has_two_cube_sums(n):
    pairs = []
    a = 1
    while a ** 3 < n:
        b3 = n - a ** 3
        b = round(b3 ** (1 / 3))
        for cand in (b - 1, b, b + 1):
            if cand > 0 and cand ** 3 == b3:
                if a < cand:
                    pairs.append((a, cand))

                break

        a += 1

    return len(pairs) >= 2