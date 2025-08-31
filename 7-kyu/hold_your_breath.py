def diving_minigame(lst):
    breath = 10
    for alt in lst:
        if alt < 0:
            breath -= 2
        else:
            breath += 4
            
        if breath > 10:
            breath = 10
        
        if breath <= 0:
            return False
            
    return True
