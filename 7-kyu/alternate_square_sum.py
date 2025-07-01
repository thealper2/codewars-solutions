def alternate_sq_sum(arr):
    n = len(arr)
    square_sum = 0
    for i in range(n):
        if i % 2 == 1:
            square_sum += arr[i] ** 2
        else:
            square_sum += arr[i]
    
    return square_sum