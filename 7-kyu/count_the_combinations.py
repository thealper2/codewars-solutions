def num_combo(xs: list, n: int):
    l = len(xs)
    count = 0

    for i in range(l):
        s = sum(xs[:i]) + sum(xs[i + 1 :])
        if s == n:
            count += 1

    return count
