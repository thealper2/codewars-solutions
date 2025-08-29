import math


def convert(degrees):
    degrees_int = int(degrees)
    decimal_part = abs(degrees - degrees_int)
    total_seconds = decimal_part * 60 * 60
    
    minutes = int(total_seconds / 60)
    seconds = round(total_seconds % 60)
    
    if seconds == 60:
        minutes += 1
        seconds = 0
    
    if minutes == 60:
        degrees_int += 1
        minutes = 0
        
    if seconds:
        return [degrees_int, minutes, seconds]
    
    if minutes:
        return [degrees_int, minutes]
    
    return [degrees_int]
