import math

def calculate_1RM(w, r):
    if r == 1:
        return w
    
    if r == 0:
        return 0
    
    epley = w * (1 + r / 30)
    mcglothin = (100 * w) / (101.3 - 2.67123 * r)
    lombardi = w * (r ** 0.10)
    return round(max([epley, mcglothin, lombardi]))