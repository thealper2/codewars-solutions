import math


def find_time_to_break(bearing_A, bearing_B):
    v = 1.5
    theta1 = math.radians(bearing_A)
    theta2 = math.radians(bearing_B)
    dx = v * (math.sin(theta1) - math.sin(theta2))
    dy = v * (math.cos(theta1) - math.cos(theta2))
    rel_speed = math.sqrt(dx**2 + dy**2)
    if rel_speed == 0:
        return float('inf')
    
    time = 40 / rel_speed
    return round(time, 2)
