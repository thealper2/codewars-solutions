def consecutive(arr):
    if not arr:
        return 0
    
    unique_numbers = set(arr)
    min_val = min(unique_numbers)
    max_val = max(unique_numbers)
    return (max_val - min_val + 1) - len(unique_numbers)