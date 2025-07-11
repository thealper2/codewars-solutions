import math


def gps(s, x):
    if len(x) <= 1:
        return 0
    
    max_speed = 0
    for i in range(1, len(x)):
        distance = x[i] - x[i-1]
        speed = (distance * 3600) / s
        if speed > max_speed:
            max_speed = speed
    return math.floor(max_speed)
