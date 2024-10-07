import math

def remainder(a,b):
    m1 = max(a, b)
    m2 = min(a, b)
    if m2 == 0:
        return None
    
    return m1 % m2
