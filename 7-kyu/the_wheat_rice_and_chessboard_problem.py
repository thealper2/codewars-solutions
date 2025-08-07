import math

def squares_needed(grains):
    if grains == 0:
        return 0
    
    return math.floor(math.log2(grains)) + 1
