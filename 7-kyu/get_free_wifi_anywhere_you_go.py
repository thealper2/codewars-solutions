def nonstop_hotspot(area):
    p_index = area.index('P')
    left = area[:p_index]
    right = area[p_index+1:]
    count = 0
    
    for i in range(len(left) - 1, -1, -1):
        if left[i] == '#':
            break
            
        if left[i] == '*':
            count += 1
            
    for i in range(len(right)):
        if right[i] == '#':
            break
            
        if right[i] == '*':
            count += 1
            
    return count
    
