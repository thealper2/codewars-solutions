def mountains_of_hoiyama(width):
    total = 0
    layers = (width + 1) // 2
    for i in range(layers):
        n = i
        center = width - i
        layer = sum(i for i in range(center - n, center + 1))
        layer_sum = layer * 2 - center
        total += layer_sum
        
    return total
