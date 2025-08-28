import math

def area(diagonal, side): 
    if diagonal <= side:
        return "Not a rectangle"
    
    other_side = math.sqrt(diagonal ** 2 - side ** 2)
    area = side * other_side
    return round(area, 2)
