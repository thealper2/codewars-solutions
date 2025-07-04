def content_weight(bottle_weight, scale):
    scale = scale.split()
    digit, is_larger = int(scale[0]), 1 if scale[-1] == 'larger' else 0 
    if is_larger:
        return bottle_weight - (bottle_weight / (digit + 1))
    
    return (bottle_weight / (digit + 1))
