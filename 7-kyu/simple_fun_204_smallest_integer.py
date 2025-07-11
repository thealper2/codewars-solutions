def smallest_integer(matrix):
    elements = set()
    for row in matrix:
        for num in row:
            elements.add(num)
    
    candidate = 0
    while True:
        if candidate not in elements:
            return candidate
        candidate += 1
