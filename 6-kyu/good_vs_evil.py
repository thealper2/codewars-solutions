def good_vs_evil(good, evil):
    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]
    
    good_total = sum(int(c) * w for c, w in zip(good.split(), good_worth))
    evil_total = sum(int(c) * w for c, w in zip(evil.split(), evil_worth))
    
    if good_total > evil_total:
        return "Battle Result: Good triumphs over Evil"
    elif evil_total > good_total:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"