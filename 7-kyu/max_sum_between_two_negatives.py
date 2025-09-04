def max_sum_between_two_negatives(arr):
    negatives = []
    for i, num in enumerate(arr):
        if num < 0:
            negatives.append(i)
            
    if len(negatives) < 2:
        return -1
    
    max_sum = -1
    n = len(negatives)
    for i in range(n - 1):
        start = negatives[i] + 1
        end = negatives[i+1]
        current_sum = 0
        for j in range(start, end):
            if arr[j] >= 0:
                current_sum += arr[j]
        
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum
