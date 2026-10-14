def wave_sort(xs: list[int]) -> None:
    n = len(xs)
    for i in range(n - 1):
        if i % 2 == 0:
            if xs[i] < xs[i + 1]:
                xs[i], xs[i + 1] = xs[i + 1], xs[i]
        else:
            if xs[i] > xs[i + 1]:
                xs[i], xs[i + 1] = xs[i + 1], xs[i]