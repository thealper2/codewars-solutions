def win_round(you, opp):
    p1 = 0
    p2 = 0
    p1_max = max(you)
    p1 += 10 * p1_max
    you.remove(p1_max)
    p1 += max(you)
    p2_max = max(opp)
    p2 += 10 * p2_max
    opp.remove(p2_max)
    p2 += max(opp)
    
    return p1 > p2
