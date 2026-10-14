def is_odd_heavy(arr):
    odds = [item for item in arr if item % 2 == 1]
    if not odds:
        return False
    
    evens = [item for item in arr if item % 2 == 0]
    if not evens:
        return True
    
    min_odd = min(odds)
    max_even = max(evens)
    return min_odd > max_even