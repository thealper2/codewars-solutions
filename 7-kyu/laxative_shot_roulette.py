def get_chance(n, x, a):
    probability = 1.0
    for i in range(a):
        probability *= (n - x - i) / (n - i)
        
    return round(probability, 2)
