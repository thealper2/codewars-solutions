def winner(deck_steve, deck_josh):
    ranks = "23456789TJQKA"
    value = {c: i for i, c in enumerate(ranks)}
    
    steve = josh = 0
    for s, j in zip(deck_steve, deck_josh):
        vs, vj = value[s], value[j]
        if vs > vj:
            steve += 1
        elif vj > vs:
            josh += 1
            
    if steve > josh:
        return f"Steve wins {steve} to {josh}"
    elif josh > steve:
        return f"Josh wins {josh} to {steve}"
    else:
        return "Tie"