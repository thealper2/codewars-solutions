def generate_pairs(m, n):
    result = []
    for i in range(m, n + 1):
        for j in range(i, n + 1):
            result.append((i, j))
            
    return result
