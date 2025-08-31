def shortest_distance(a, b, c):
    paths = [
        ((a + b)**2 + c**2) ** 0.5,
        ((a + c)**2 + b**2) ** 0.5,
        ((b + c)**2 + a**2) ** 0.5
    ]
    
    return min(paths)
