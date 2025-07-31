def calculate_time(battery, charger):
    fast_charge = (battery * 0.85) / charger
    decreasing_charge = (battery * 0.1) / (charger * 0.5)
    trickle_charge = (battery * 0.05) / (charger * 0.2)
    return round(fast_charge + decreasing_charge + trickle_charge, 2)
