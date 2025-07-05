import math

def new_avg(arr, newavg):
    current_sum = sum(arr)
    n = len(arr)
    required_x = newavg * (n + 1) - current_sum
    
    if required_x <= 0:
        raise ValueError("The required donation is non-positive.")
    
    return math.ceil(required_x) if not isinstance(required_x, int) else required_x