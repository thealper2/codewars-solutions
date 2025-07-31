def series_sum(n):
    if n == 0:
        return "0.00"
    total = 1.0 if n >= 1 else 0.0
    denominator = 4.0

    for _ in range(1, n):
        total += 1.0 / denominator
        denominator += 3.0

    return f"{total:.2f}"
