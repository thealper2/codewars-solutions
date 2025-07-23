def calculate_bricks_count(width, height):
    brick_counts = [0, 0, 0]
    rows = height // 5
    
    for i in range(rows):
        if (i + 1) % 3 != 1:
            brick_counts[2] += 1
            brick_counts[1] += 1
            brick_counts[0] += width // 60 - 1
        else:
            brick_counts[0] += width // 60
    
    result = []
    if brick_counts[0] > 0:
        result.append(f"{brick_counts[0]}L")
    if brick_counts[1] > 0:
        result.append(f"{brick_counts[1]}M")
    if brick_counts[2] > 0:
        result.append(f"{brick_counts[2]}S")
    
    return ''.join(result)