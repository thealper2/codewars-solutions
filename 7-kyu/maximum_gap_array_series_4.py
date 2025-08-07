def max_gap(numbers):
    numbers.sort()
    n = len(numbers)
    max_gap = float('-inf')
    for i in range(1, n):
        diff = abs(numbers[i] - numbers[i - 1])
        max_gap = max(max_gap, diff)
        
    return max_gap
