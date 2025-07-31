def cat_mouse(map_, moves):
    if "C" not in map_ or "m" not in map_:
        return "boring without two animals"

    rows = map_.split("\n")
    cat_pos = None
    mouse_pos = None

    for i, row in enumerate(rows):
        if "C" in row:
            cat_pos = (i, row.index("C"))
        if "m" in row:
            mouse_pos = (i, row.index("m"))

    distance = abs(cat_pos[0] - mouse_pos[0]) + abs(cat_pos[1] - mouse_pos[1])
    return "Caught!" if distance <= moves else "Escaped!"
