def solve(before, after):
    avg1, dist1 = before
    avg2, dist2 = after
    
    total_liters = (avg2 * dist2 - avg1 * dist1) / 100
    distance_during = dist2 - dist1
    if distance_during != 0:
        avg_during = (total_liters / distance_during) * 100
    else:
        avg_during = 0
    
    return round(avg_during, 1)
