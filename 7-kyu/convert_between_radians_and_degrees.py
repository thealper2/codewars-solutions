def degrees(rad):
    result = round((180 * rad) / math.pi, 2)
    if result.is_integer():
        return f"{int(result)}deg"
    else:
        return f"{result}deg"
    
def radians(deg):
    result = round((deg * math.pi) / 180, 2)
    if result.is_integer():
        return f"{int(result)}rad"
    else:
        return f"{result}rad"
    
math.degrees=degrees
math.radians=radians
