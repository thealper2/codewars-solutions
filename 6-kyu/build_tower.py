def tower_builder(n_floors):
    max_floor = n_floors * 2 - 1
    result = []
    for i in range(1, max_floor + 1, 2):
        empty = ' ' * (n_floors - i // 2 - 1)
        floor = empty + '*' * (i) + empty
        result.append(floor)
        
    return result