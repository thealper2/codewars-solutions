import math

def geometric_meanI(arr):
    valid = []
    invalid_count = 0
    for x in arr:
        if isinstance(x, (int, float)) and x >= 0:
            valid.append(x)
        else:
            invalid_count += 1
            
    n = len(arr)
    max_invalid = 1 if 2 <= n <= 10 else int(0.1 * n)
    
    if invalid_count > max_invalid or not valid:
        return 0
        
    product = 1
    for num in valid:
        product *= num
        
    return math.pow(product, 1/len(valid))
