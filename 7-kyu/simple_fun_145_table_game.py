def table_game(table):
    a = table[0][0]
    b = table[0][2]
    c = table[2][0]
    d = table[2][2]

    if (
        table[0][1] != a + b
        or table[1][0] != a + c
        or table[1][1] != a + b + c + d
        or table[1][2] != b + d
        or table[2][1] != c + d
    ):
        return [-1]

    return [a, b, c, d]
