def sexy_name(name):
    score = sum([SCORES.get(c.upper(), 0) for c in name])
    if score >= 600:
        return 'THE ULTIMATE SEXIEST'
    elif score >= 301:
        return 'VERY SEXY'
    elif score >= 61:
        return 'PRETTY SEXY'
    else:
        return 'NOT TOO SEXY'
