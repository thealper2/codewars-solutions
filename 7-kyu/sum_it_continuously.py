def add(lst):
    cumulative_sums = []
    current_sum = 0
    for num in lst:
        current_sum += num
        cumulative_sums.append(current_sum)
        
    return cumulative_sums
