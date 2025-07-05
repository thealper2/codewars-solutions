import math

def stack_height_3d(layers):
    if layers == 0:
        return 0.0
    
    return 1.0 + (layers - 1) * (math.sqrt(6) / 3)