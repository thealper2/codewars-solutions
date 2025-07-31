def create_box(m, n):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    layers = (min(m, n) + 1) // 2
    for layer in range(layers):
        value = layer + 1
        for col in range(layer, m - layer):
            if matrix[layer][col] == 0:
                matrix[layer][col] = value
            if n - 1 - layer >= 0 and matrix[n - 1 - layer][col] == 0:
                matrix[n - 1 - layer][col] = value

        for row in range(layer + 1, n - layer - 1):
            if matrix[row][layer] == 0:
                matrix[row][layer] = value
            if m - 1 - layer >= 0 and matrix[row][m - 1 - layer] == 0:
                matrix[row][m - 1 - layer] = value

    return matrix
