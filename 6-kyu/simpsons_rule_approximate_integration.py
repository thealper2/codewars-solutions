import math

def simpson(n):
    a = 0.0
    b = math.pi
    h = (b - a) / n
    
    f = lambda x: (3.0 / 2.0) * math.sin(x) ** 3
    
    total = f(a) + f(b)
    
    for i in range(1, n // 2 + 1):
        total += 4 * f(a + (2 * i - 1) * h)
        
    for i in range(1, n // 2):
        total += 2 * f(a + 2 * i * h)
        
    return (b - a) / (3 * n) * total