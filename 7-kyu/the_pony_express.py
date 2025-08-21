def riders(stations):
    riders = 1
    distance = 0
    for s in stations:
        if distance + s > 100:
            riders += 1
            distance = s
        else:
            distance += s
            
    return riders
