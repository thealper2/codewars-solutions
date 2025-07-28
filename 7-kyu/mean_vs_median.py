def mean_vs_median(numbers):
    numbers.sort()
    sum_ = sum(numbers)
    n = len(numbers)
    mean = sum_ / n
    median = numbers[n // 2]
    
    if mean > median:
        return 'mean'
    elif median > mean:
        return 'median'
    
    return 'same'