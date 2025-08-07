def crap(garden, bags, cap):
    total_cap = bags * cap
    for gard in garden:
        for g in gard:
            if g == '@':
                total_cap -= 1

            if g == 'D':
                return 'Dog!!'
            
            
    return 'Clean' if total_cap >= 0 else 'Cr@p'
