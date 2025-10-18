def typist(s):
    taps = 0
    caps_lock = False
    
    for c in s:
        if c.isupper() != caps_lock:
            taps += 1
            caps_lock = not caps_lock
            
        taps += 1
        
    return taps
