import math

def calculate_time(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    distance1 = math.sqrt(x1**2 + y1**2)
    distance2 = math.sqrt(x2**2 + y2**2)
    speed = (distance1 - distance2) / 5
    time = distance2 / speed
    return round(time, 3)