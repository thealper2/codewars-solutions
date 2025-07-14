def calculator(distance, bus_drive, bus_walk):
    walk_speed = 5
    bus_speed = 8
    walk_time = distance / walk_speed
    bus_time = (bus_walk / walk_speed) + (bus_drive / bus_speed)
    
    if walk_time > 2:
        return "Bus"
    if walk_time < (10/60):
        return "Walk"
    
    if walk_time <= bus_time:
        return "Walk"
    else:
        return "Bus"