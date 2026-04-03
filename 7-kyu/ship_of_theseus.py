def ship_of_theseus(ship):
    n = len(ship)
    if n <= 1:
        return True
    
    for i in range(n - 1):
        a = ship[i]
        b = ship[i + 1]
        if len(a) != len(b):
            return False
        if a == b and i < n - 1:
            return False
        
        diff = sum(1 for x, y in zip(a, b) if x != y)
        if diff > 1:
            return False
        
    return True
