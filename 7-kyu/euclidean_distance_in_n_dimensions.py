def euclidean_distance(point1, point2):
    distance = 0
    for a, b in zip(point1, point2):
        distance += (b - a) ** 2
        
    return round(distance ** 0.5, 2)
