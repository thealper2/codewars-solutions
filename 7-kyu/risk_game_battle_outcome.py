def battle_outcome(attacker, defender):
    attacker.sort(reverse=True)
    defender.sort(reverse=True)
    
    attacker_losses = 0
    defender_losses = 0
    
    min_length = min(len(attacker), len(defender))
    
    for i in range(min_length):
        if attacker[i] > defender[i]:
            defender_losses += 1
        else:
            attacker_losses += 1
    
    return (attacker_losses, defender_losses)
