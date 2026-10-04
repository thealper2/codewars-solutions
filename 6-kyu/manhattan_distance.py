def manhattan_distance(pointA, pointB):
    return sum(abs(a - b) for a, b in zip(pointA, pointB))