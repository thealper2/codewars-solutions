def pascals_triangle(n):
    result = []
    row = [1]
    for _ in range(n):
        result.extend(row)
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

    return result