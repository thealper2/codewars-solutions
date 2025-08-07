def time_correct(t):
    if t is None:
        return None
    
    if t == "":
        return ""
    
    if len(t) != 8 or t.count(':') != 2:
        return None
    
    parts = t.split(':')
    if len(parts) != 3:
        return None
    
    for part in parts:
        if not part.isdigit() or len(part) != 2:
            return None
        
    hours, minutes, seconds = map(int, t.split(':'))
    if seconds >= 60:
        minutes += seconds // 60
        seconds = seconds % 60
        
    if minutes >= 60:
        hours += minutes // 60
        minutes = minutes % 60
        
    if hours >= 24:
        hours = hours % 24
        
    corrected_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return corrected_time
