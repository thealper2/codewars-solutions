def find_spaceship(astromap):
    rows = astromap.split("\n")
    for y in range(len(rows)):
        row = rows[len(rows) - 1 - y]
        if "X" in row:
            x = row.index("X")
            return [x, y]

    return "Spaceship lost forever."
