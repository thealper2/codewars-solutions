def seven(m):
    steps = 0
    while m >= 100:
        x = m // 10
        y = m % 10
        m = x - 2 * y
        steps += 1
        
    return (m, steps)
