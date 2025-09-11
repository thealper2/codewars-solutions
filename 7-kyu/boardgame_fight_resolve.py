def fight_resolve(defender, attacker): 
    if defender.islower() == attacker.islower():
        return -1
    
    beats = {
        'a': 's',
        's': 'p',
        'p': 'k',
        'k': 'a'
    }
    d, a = defender.lower(), attacker.lower()
    if beats.get(d) == a:
        return defender
    elif beats.get(a) == d:
        return attacker
    else:
        return attacker
