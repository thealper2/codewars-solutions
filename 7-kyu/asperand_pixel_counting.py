def count_pixels(k):
    if k == 1:
        return 11
    
    return 8 * k + 2 * (k + 1) - (k * 2)
