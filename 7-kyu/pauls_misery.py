def paul(x):
    d = {
        'kata': 5,
        'Petes kata': 10,
        'life': 0,
        'eating': 1        
    }
    
    s = sum([d.get(c, 0) for c in x])
    if s < 40:
        return 'Super happy!'
    elif s < 70:
        return 'Happy!'
    elif s < 100:
        return 'Sad!'
    else:
        return 'Miserable!'
