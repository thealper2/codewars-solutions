def rotate_matrix(arr):
    n, m = len(arr), len(arr[0])
    result = [[0 for _ in range(n)]] * m
    rotated = []
    for j in range(m - 1, -1, -1):
        new_row = []
        for i in range(n):
            new_row.append(arr[i][j])

        rotated.append(new_row)

    return rotated
