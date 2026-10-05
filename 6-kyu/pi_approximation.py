import math

def iter_pi(epsilon):
    terms = 0
    result = 0.0
    sign = 1.0
    
    while abs(4 * result - math.pi) >= epsilon:
        result += sign / (2.0 * terms +1.0)
        sign = -sign
        terms += 1
        
    result = round(4 * result, 10)
    return [terms, result]