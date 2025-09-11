def amaro_plan(pirate_num):
    total = 20 * pirate_num
    result = [total] + [0 for _ in range(pirate_num - 1)]
    for i in range(pirate_num):
        if i > 0 and i % 2 == 0:
            result[i] += 1
            result[0] -= 1
            
    return result
