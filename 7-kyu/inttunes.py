def is_tune(notes):
    if not notes:
        return False
    
    major_scale_pattern = {0, 2, 4, 5, 7, 9, 11}
    
    for key in range(12):
        valid = True
        for note in notes:
            pitch_class = note % 12
            relative_note = (pitch_class - key) % 12
            if relative_note not in major_scale_pattern:
                valid = False
                break
                
        if valid:
            return True
    
    return False