def find_caterer(budget, people):
    if people == 0 or budget < 15 * people:
        return -1
    
    basic = 15 * people
    economy = 20 * people
    premium = 30 * people
    if people > 60:
        premium *= 0.8
    
    if premium <= budget:
        return 3
    
    if economy <= budget:
        return 2
    
    if basic <= budget:
        return 1
    
    return -1
