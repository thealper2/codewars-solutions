def draw_rectangle(canvas, rectangle):
    x1, y1, x2, y2 = rectangle
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if y == y1 or y == y2:
                if x == x1 or x == x2:
                    canvas[y][x] = "*"
                else:
                    canvas[y][x] = "-"
            else:
                if x == x1 or x == x2:
                    canvas[y][x] = "|"
    return canvas
