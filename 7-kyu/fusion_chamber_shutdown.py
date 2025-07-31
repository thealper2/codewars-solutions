def burner(c, h, o):
    water = min(h // 2, o)
    h = max(h - (water * 2), 0)
    o = max(o - water, 0)

    co2 = min(c, o // 2)
    c = max(c - co2, 0)
    o = max(o - (co2 * 2), 0)

    methane = min(c, h // 4)
    return water, co2, methane
