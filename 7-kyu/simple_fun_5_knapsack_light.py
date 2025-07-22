def knapsack_light(value1, weight1, value2, weight2, max_w):
    max_val = 0
    if weight1 <= max_w:
        max_val = value1
    
    if weight2 <= max_w:
        if value2 > max_val:
            max_val = value2
    
    if weight1 + weight2 <= max_w:
        if value1 + value2 > max_val:
            max_val = value1 + value2

    return max_val