def get_ages(sum_, difference):
    y = (sum_ + difference) / 2
    x = sum_ - y

    if x < 0 or y < 0:
        return None

    if abs(x + y) != sum_ or abs(x - y) != difference:
        return None

    if x > y:
        return (x, y)

    return (y, x)
