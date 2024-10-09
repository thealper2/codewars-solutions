def count_streets(streets, drivers):
    street_dict = {}
    i = 1
    for street in streets:
        if street not in street_dict:
            street_dict[street] = i
            i += 1
    
    results = []
    for driver in drivers:
        d1 = street_dict[driver[0]]
        d2 = street_dict[driver[1]]
        if d1 < d2:
            results.append(d2 - d1 - 1)
        else:
            results.append(d1 - d2 - 1)
    
    return results
