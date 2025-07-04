def make_latin_square(n):
    if n <= 0:
        return []
    
    latin_square = []
    for i in range(n):
        row = [(j % n) + 1 for j in range(i, i + n)]
        latin_square.append(row)

    return latin_square
