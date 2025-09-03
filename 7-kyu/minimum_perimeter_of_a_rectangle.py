def minimum_perimeter(area):
    min_perimeter = float('inf')
    for w in range(1, int(area**0.5) + 1):
        if area % w == 0:
            h = area // w
            perimeter = 2 * (w + h)
            min_perimeter = min(min_perimeter, perimeter)
            
    return min_perimeter
