def team_comp(heroes):
    if len(heroes) != 6:
        raise InvalidTeam()
        
    seen = set()
    result = [0, 0, 0]
    for hero in heroes:
        if hero in seen:
            raise InvalidTeam()
            
        seen.add(hero)
        
        if hero in TANK:
            result[0] += 1
        elif hero in DAMAGE:
            result[1] += 1
        elif hero in SUPPORT:
            result[2] += 1
            
    return result
