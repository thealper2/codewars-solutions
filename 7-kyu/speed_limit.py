def speed_limit(speed, signals):
    result = 0
    for limit in signals:
        excess = speed - limit
        if 10 <= excess <= 19:
            result += 100
        elif 20 <= excess <= 29:
            result += 250
        elif excess >= 30:
            result += 500
            
    return result
