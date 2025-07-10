def fly_by(lamps, drone):
    lamps = list(lamps)
    
    for i in range(min(len(drone), len(lamps))):
        if lamps[i] == 'x':
            lamps[i] = 'o'
                   
    return ''.join(lamps)