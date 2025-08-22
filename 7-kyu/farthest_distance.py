import math


def furthest_distance(points):
    n = len(points)
    max_dist = float('-inf')
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            max_dist = max(max_dist, dist)
            
    return round(max_dist, 2)
