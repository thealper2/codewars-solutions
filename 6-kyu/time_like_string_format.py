def solution(hour): 
    s = str(hour)
    if len(s) < 3 or len(s) > 4:
        raise Error()
        
    hours, minutes = s[:-2], s[-2:]
    return f"{hours}:{minutes}"
