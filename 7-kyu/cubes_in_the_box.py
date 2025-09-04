def f(x, y, z):
    max_d = min(x, y, z)
    area = x * y * z
    count = 0
    for size in range(1, max_d + 1):
        count += (x - size + 1) * (y - size + 1) * (z - size + 1)
        
    return count
