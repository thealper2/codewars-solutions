def isomorph(a, b):
    if len(a) != len(b):
        return False
    
    map_ab = {}
    map_ba = {}
    for ca, cb in zip(a, b):
        if ca in map_ab:
            if map_ab[ca] != cb:
                return False
            
        else:
            map_ab[ca] = cb
            
        if cb in map_ba:
            if map_ba[cb] != ca:
                return False
            
        else:
            map_ba[cb] = ca
            
    return True