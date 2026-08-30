def two_sum(numbers, target):
    for i, number in enumerate(numbers):
        diff = target - number
        if diff in numbers:
            j = numbers.index(diff)
            if i != j:
                return (i, j)
            
    return None