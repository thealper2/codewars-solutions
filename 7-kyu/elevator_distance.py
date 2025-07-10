def elevator_distance(array):
    n = len(array)
    distance = 0
    for i in range(n - 1):
        distance += abs(array[i+1] - array[i])
        
    return distance