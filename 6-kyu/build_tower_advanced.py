def tower_builder(n_floors, block_size):
    w, h = block_size
    result = []
    total_width = (2 * n_floors - 1) * w
    
    for floor in range(1, n_floors + 1):
        stars = '*' * (2 * floor - 1) * w
        line = stars.center(total_width)
        for _ in range(h):
            result.append(line)
            
    return result