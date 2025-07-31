def letter_check(arr):
    if not arr[1]:
        return True
    
    chars = map(str.lower, list(set(arr[1])))
    target = arr[0].lower()
    for c in chars:
        if c not in target:
            return False
        
    return True
