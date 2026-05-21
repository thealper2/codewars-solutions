def find_quarter_notes(time_signature):
    top, bottom = map(int, time_signature.split('/'))
    
    if bottom <= 0 or (bottom & (bottom - 1)) != 0:
        return None
    
    if top >= 4096 or bottom >= 256:
        return None
    
    quarter_notes = top * (4 / bottom)
    result = int(quarter_notes)
    return result if result >= 0 else 0