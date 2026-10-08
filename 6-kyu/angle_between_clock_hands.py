import math

def hand_angle(hours: int, minutes: int) -> float:
    hour_angle = (hours % 12) * 30 + minutes * 0.5
    minute_angle = minutes * 6
    diff = abs(hour_angle - minute_angle)
    smaller = min(diff, 360 - diff)
    return smaller * math.pi / 180