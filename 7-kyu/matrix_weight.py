def thin_or_fat(matrix):
    n = len(matrix)
    width_sums = []
    height_sums = [0] * n
    for row in matrix:
        row_sum = sum(row)
        if row_sum < 0:
            return None
        
        width_sums.append(row_sum**0.5)
        for j, val in enumerate(row):
            height_sums[j] += val
            
    for h in height_sums:
        if h < 0:
            return None
        
    sum_width = sum(width_sums)
    sum_height = sum(h**0.5 for h in height_sums)
    if abs(sum_width - sum_height) < 1e-10:
        return "perfect"
    elif sum_width > sum_height:
        return "fat"
    else:
        return "thin"
