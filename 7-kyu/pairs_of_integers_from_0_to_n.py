def generate_pairs(n):
    result = []
    for i in range(n + 1):
        for j in range(i, n + 1):
            result.append([i, j])

    return result
