def set_clock(time, buttons):
    h, m = map(int, time.split(':'))
    
    for b in buttons:
        if b == 'H':
            h += 1
            if h > 24:
                h = 1
        elif b == 'M':
            m += 1
            if m == 60:
                m = 0
    
    if h == 24 and m == 0:
        return "24:00"
    
    return f"{h}:{m:02d}"
