def turn(current, target):
    directions = ['N', 'E', 'S', 'W']
    c_idx = directions.index(current)
    t_idx = directions.index(target)
    diff = (c_idx - t_idx) % 4
    diff2 = (t_idx - c_idx) % 4
    
    if diff >= diff2:
        return 'right'
    else:
        return 'left'
