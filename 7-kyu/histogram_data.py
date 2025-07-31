def histogram(values, bin_width):
    if not values:
        return []

    bars = [0 for _ in range(0, max(values) + 1, bin_width)]
    for value in values:
        bars[value // bin_width] += 1

    return bars
