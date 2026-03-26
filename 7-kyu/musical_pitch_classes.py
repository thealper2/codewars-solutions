def pitch_class(note: str) -> int | None:
    natural_values = {
        "C": 0, "D": 2, "E": 4,
        "F": 5, "G": 7, "A": 9,
        "B": 11,
    }
    
    if not note or len(note) > 2:
        return None
    
    base = note[0].upper()
    if base not in natural_values:
        return None
    
    value = natural_values[base]
    
    if len(note) == 2:
        accidental = note[1]
        if accidental == '#':
            value += 1
        elif accidental == 'b':
            value -= 1
        else:
            return None
        
    return value % 12
