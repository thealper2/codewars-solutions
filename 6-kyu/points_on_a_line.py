def on_line(points):
    if len(points) <= 2:
        return True

    x0, y0 = points[0]
    idx = 1
    while idx < len(points) and points[idx] == (x0, y0):
        idx += 1

    if idx == len(points):
        return True

    x1, y1 = points[idx]
    dx = x1 - x0
    dy = y1 - y0

    for x, y in points[2:]:
        if (x - x0) * dy != (y - y0) * dx:
            return False

    return True