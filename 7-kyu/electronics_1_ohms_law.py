def ohms_law(s):
    a, b = s.split()
    if a[-1] == 'A' and b[-1] == 'R':
        I = float(a[:-1])
        R = float(b[:-1])
        return f'{round(I * R, 6)}V'
    elif a[-1] == 'R' and b[-1] == 'A':
        I = float(b[:-1])
        R = float(a[:-1])
        return f'{round(I * R, 6)}V'
    elif a[-1] == 'A' and b[-1] == 'V':
        I = float(a[:-1])
        V = float(b[:-1])
        return f'{round(V / I, 6)}R'
    elif a[-1] == 'V' and b[-1] == 'A':
        I = float(b[:-1])
        V = float(a[:-1])
        return f'{round(V / I, 6)}R'
    elif a[-1] == 'V' and b[-1] == 'R':
        V = float(a[:-1])
        R = float(b[:-1])
        return f'{round(V / R, 6)}A'
    elif a[-1] == 'R' and b[-1] == 'V':
        V = float(b[:-1])
        R = float(a[:-1])
        return f'{round(V / R, 6)}A'
    
