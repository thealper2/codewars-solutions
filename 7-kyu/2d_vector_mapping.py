import math


def map_vector(vector, circle1, circle2):
    x, y = vector
    c1_x, c1_y, r1 = circle1
    c2_x, c2_y, r2 = circle2
    
    dx = x - c1_x
    dy = y - c1_y
    
    distance = math.sqrt(dx**2 + dy**2)
    if distance == 0:
        return (round(c2_x, 2), round(c2_y, 2))
    
    scale = r2 / r1
    new_dx = dx * scale
    new_dy = dy * scale
    
    new_x = c2_x + new_dx
    new_y = c2_y + new_dy
    
    return (round(new_x, 2), round(new_y, 2))
