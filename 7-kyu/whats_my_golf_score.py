def golf_score_calculator(par_string, score_string):
    if len(par_string) != 18 and len(score_string) != 18:
        return -1
    
    total = 0
    for p, s in zip(par_string, score_string):
        total += int(s) - int(p)
        
    return total
