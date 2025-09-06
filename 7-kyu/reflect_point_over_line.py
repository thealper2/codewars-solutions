def reflect(point, line):
    x, y = point
    m, b = line
    
    if m == 0:
        return (x, 2 * b - y)
    
    m_perp = -1 / m
    x_int = (x + m * (y - b)) / (1 + m**2)
    y_int = m * x_int + b
    x_ref = 2 * x_int - x
    y_ref = 2 * y_int - y
    return (round(x_ref, 6), round(y_ref, 6))
