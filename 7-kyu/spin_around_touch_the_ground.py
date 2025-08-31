def spin_around(lst):
    degree = 0
    for item in lst:
        if item == 'right':
            degree += 90
        elif item == 'left':
            degree -= 90
            
    result = abs(degree) // 360
    return result
