def beasts(heads, tails):
    numerator = heads - 2 * tails
    if numerator % 3 != 0:
        return "No solutions"

    h = numerator // 3
    o = tails - h

    if h < 0 or o < 0:
        return "No solutions"

    return [o, h]
