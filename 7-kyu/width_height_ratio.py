import math


def calculate_ratio(w, h):
    if w <= 0 or h <= 0:
        return "You threw an error"
    
    g = math.gcd(w, h)
    return f"{w // g}:{h // g}"
