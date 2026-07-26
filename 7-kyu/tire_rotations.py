from math import pi

def tire_rotations(tire_size: str, distance_km: float) -> float:
    if distance_km == 0:
        return 0.0
    
    parts = tire_size.split('/')
    width = int(parts[0])
    
    rest = parts[1]
    
    if 'ZR' in rest:
        aspect_str, rim_str = rest.split('ZR')
        construction = 'ZR'
    elif 'R' in rest:
        aspect_str, rim_str = rest.split('R')
        construction = 'R'
    elif 'B' in rest:
        aspect_str, rim_str = rest.split('B')
        construction = 'B'
    elif 'D' in rest:
        aspect_str, rim_str = rest.split('D')
        construction = 'D'
    else:
        raise ValueError(f"Invalid tire size format: {tire_size}")
    
    aspect = int(aspect_str)
    rim_diameter_inches = int(rim_str)
    
    sidewall_height_mm = width * (aspect / 100.0)
    rim_diameter_mm = rim_diameter_inches * 25.4
    tire_diameter_mm = rim_diameter_mm + 2 * sidewall_height_mm
    
    circumference_mm = pi * tire_diameter_mm
    
    distance_mm = distance_km * 1000 * 1000
    
    rotations = distance_mm / circumference_mm
    
    return rotations
