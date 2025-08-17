def operate(pitch_set, operation):
    if operation[-1] == 'I':
        is_inversion = True
        n = int(operation[1:-1])
    else:
        is_inversion = False
        n = int(operation[1:])
    
    result = []
    for pitch in pitch_set:
        if is_inversion:
            transformed_pitch = (12 - pitch + n) % 12
        else:
            transformed_pitch = (pitch + n) % 12
            
        result.append(transformed_pitch)
    
    return sorted(result)
