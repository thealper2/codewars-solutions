def avg_array(arrs):
    m, n = len(arrs), len(arrs[0])
    averages = [0] * n
    for i in range(m):
        for j in range(n):
            averages[j] += arrs[i][j]

    averages = [row / m for row in averages]
    return averages
