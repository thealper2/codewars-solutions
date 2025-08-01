def is_defended(attackers, defenders):
    a_survivors = 0
    d_survivors = 0
    max_length = max(len(attackers), len(defenders))
    
    for i in range(max_length):
        a_power = attackers[i] if i < len(attackers) else None
        d_power = defenders[i] if i < len(defenders) else None
        
        if a_power is not None and d_power is not None:
            if a_power > d_power:
                a_survivors += 1
            elif d_power > a_power:
                d_survivors += 1
        else:
            if a_power is not None:
                a_survivors += 1
            elif d_power is not None:
                d_survivors += 1
    
    if d_survivors > a_survivors:
        return True
    elif a_survivors > d_survivors:
        return False
    else:
        total_attack = sum(attackers)
        total_defend = sum(defenders)
        if total_defend >= total_attack:
            return True
        else:
            return False
