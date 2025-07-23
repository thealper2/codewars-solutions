def count_min_rotations(dice):
    opposites = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    min_rotations = float('inf')
    
    for target in range(1, 7):
        rotations = 0
        for face in dice:
            if face == target:
                continue
            elif opposites[face] == target:
                rotations += 2
            else:
                rotations += 1
        
        if rotations < min_rotations:
            min_rotations = rotations
    
    return min_rotations