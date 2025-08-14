def axis_aligned_bounding_box(x, y):
    min_x = min(x)
    max_x = max(x)
    min_y = min(y)
    max_y = max(y)
    width = max_x - min_x
    height = max_y - min_y
    return width * height
