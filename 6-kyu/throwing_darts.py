def score_throws(radii):
    score = 0
    all_5 = True
    for r in radii:
        if r < 5:
            score += 10
        else:
            if r <= 10:
                score += 5
            
            all_5 = False
            
    if radii and all_5:
        score += 100
        
    return score