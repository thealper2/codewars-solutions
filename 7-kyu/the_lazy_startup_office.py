def bin_rota(arr):
    m, n = len(arr), len(arr[0])
    result = []

    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                result.append(arr[i][j])
        else:
            for j in range(n):
                result.append(arr[i][-j - 1])

    return result
