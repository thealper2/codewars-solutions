import math

def is_triangle_number(number: int) -> bool:
    if number < 0:
        return False
    
    test_val = 8 * number + 1
    root = math.isqrt(test_val)
    return root * root == test_val