def traffic_jam(traffic, green_light_duration):
    cycles = 0
    current_time = 0
    for speed in traffic:
        if current_time + speed > green_light_duration:
            cycles += 1
            current_time = speed
        else:
            current_time += speed
    
    if current_time > 0:
        cycles += 1
        
    return cycles
