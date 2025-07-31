def is_sator_square(tablet):
    n = len(tablet)
    if n == 0:
        return False

    for i in range(n):
        for j in range(n):
            if (
                tablet[i][j] != tablet[j][i]
                or tablet[i][j] != tablet[n - 1 - i][n - 1 - j]
            ):
                return False

    return True
