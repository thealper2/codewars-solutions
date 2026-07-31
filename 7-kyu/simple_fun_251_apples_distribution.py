def apples_distribution(apples, capacity, max_left):
    count = 0
    for N in range(1, capacity + 1):
        left = apples % N
        if left <= max_left and left < N:
            count += 1
            
    return count
