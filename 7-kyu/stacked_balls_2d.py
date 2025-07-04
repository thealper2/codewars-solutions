def stack_height_2d(layers):
    if layers == 0:
        return 0
    
    return 1 + (layers - 1) * ((3**0.5) / 2)
