def largest_pair_sum(numbers): 
    first = float('-inf')
    second = float('-inf')
    
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
            
    return first + second
