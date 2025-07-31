def sc(apple):
    for i, row in enumerate(apple):
        for j, cell in enumerate(row):
            if cell == "B":
                return (i, j)

    return (-1, -1)
