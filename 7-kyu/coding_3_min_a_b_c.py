def find_a_b(numbers, c):
    n = len(numbers)
    
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] * numbers[j] == c:
                return [numbers[i], numbers[j]]
            
    return None