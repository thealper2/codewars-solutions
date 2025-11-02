def itinerary(travel): 
    if not travel:
        return ""
    
    result = [travel[0]['in']]
    for i, flight in enumerate(travel):
        if i > 0 and flight['in'] != travel[i - 1]['out']:
            result.append(flight['in'])
            
        result.append(flight['out'])
        
    return '-'.join(result)
