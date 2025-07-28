def plant(seed, water, fert, temp):
    if 20 <= temp <= 30:
        stem = '-' * water
        flower = seed * fert
        plant_str = (stem + flower) * water
    else:
        total_stem = '-' * (water * water)
        plant_str = total_stem + seed
        
    return plant_str