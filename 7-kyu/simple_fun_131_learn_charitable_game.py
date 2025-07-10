def learn_charitable_game(arr):
    if all(x == 0 for x in arr):
        return False
    
    total = sum(arr)
    n = len(arr)
    if total % n != 0:
        return False
    
    initial = total // n
    if initial <= 0:
        return False
    
    return True
