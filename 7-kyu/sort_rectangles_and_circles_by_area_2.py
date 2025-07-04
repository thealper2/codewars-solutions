import math

def sort_by_area(seq): 
    def area(shape):
        if isinstance(shape, (list, tuple)) and len(shape) == 2:
            return shape[0] * shape[1]
        elif isinstance(shape, (int, float)):
            return math.pi * shape ** 2

    return sorted(seq, key=area)
