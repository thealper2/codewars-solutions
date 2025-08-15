import math


def drink_water(bottle_height, bottle_radius, water_height, crow_mouth, little_stones):
    if water_height + crow_mouth >= bottle_height:
        return []
    
    initial_volume = math.pi * (bottle_radius ** 2) * water_height
    required_height = bottle_height - crow_mouth
    required_volume = math.pi * (bottle_radius ** 2) * required_height
    additional_volume_needed = required_volume - initial_volume
    
    if additional_volume_needed <= 0:
        return []
    
    used_stones = []
    current_volume = initial_volume
    
    for stone in little_stones:
        current_volume += stone
        used_stones.append(stone)
        new_height = current_volume / (math.pi * (bottle_radius ** 2))
        if new_height + crow_mouth >= bottle_height:
            return used_stones
    
    return "The crow is dead."
