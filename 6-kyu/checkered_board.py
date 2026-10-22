def checkered_board(n):
    dark = '\u25A0'
    light = '\u25A1'
    rows = []
    for r in range(n):
        row = []
        for c in range(n):
            if n % 2 == 0:
                row.append(light if (r + c) % 2 == 0 else dark)
            else:
                row.append(dark if (r + c) % 2 == 0 else light)

        rows.append(' '.join(row))

    return '\n'.join(rows)