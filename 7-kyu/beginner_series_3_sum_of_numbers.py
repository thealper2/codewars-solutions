def get_sum(a,b):
    if a == b:
        return a
    
    if a < b:
        return sum(range(a, b + 1))
    
    return sum(range(b, a + 1))
