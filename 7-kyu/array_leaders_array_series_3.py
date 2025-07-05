def array_leaders(numbers):
    n = len(numbers)
    result = []
    for i in range(n):
        if i < n - 1 and numbers[i] > sum(numbers[i+1:]):
            result.append(numbers[i])
        if i == n - 1 and numbers[i] > 0:
            result.append(numbers[i])
        
    return result