def is_square(arr):
    if not arr:
        return None
    
    for item in arr:
        d = int(item**0.5)
        if d ** 2 != item:
            return False
        
    return True
