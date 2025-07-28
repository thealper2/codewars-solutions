def collision(x1, y1, radius1, x2, y2, radius2): 
    radius = radius1 + radius2
    x = x2 - x1
    y = y2 - y1
    return (y ** 2) + (x ** 2) <= (radius ** 2)