def four_piles(n, y):
    denominator = (y + 1) ** 2
    if denominator == 0:
        return []

    if (n * y) % denominator != 0:
        return []

    x = (n * y) // denominator
    if x <= 0:
        return []

    if x % y != 0:
        return []

    pile1 = x + y
    if pile1 <= 0:
        return []

    pile2 = x - y
    if pile2 <= 0:
        return []

    pile3 = x * y
    if pile3 <= 0:
        return []

    pile4 = x // y
    if pile4 <= 0:
        return []

    return [pile1, pile2, pile3, pile4]
