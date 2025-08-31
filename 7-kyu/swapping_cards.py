def swap_cards(n1, n2):
    paul = list(str(n1))
    opp = list(str(n2))
    min_paul = min(paul)
    index = paul.index(min_paul)
    paul[index], opp[0] = opp[0], paul[index]
    new_paul = int(''.join(paul))
    new_opp = int(''.join(opp))
    return new_paul > new_opp
