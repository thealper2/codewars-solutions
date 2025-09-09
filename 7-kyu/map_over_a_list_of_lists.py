def grid_map(inp, op):
    return [[op(element) for element in row] for row in inp]
