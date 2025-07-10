def even_last(numbers): 
    if not numbers:
        return 0
    
    last_number = numbers[-1]
    return sum(numbers[i] * last_number for i in range(0, len(numbers), 2))