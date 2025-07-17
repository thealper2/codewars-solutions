import math

def layers(n):
    if n == 1:
        return 1
    
    k = math.ceil((1 + math.sqrt(n)) / 2)
    return k
