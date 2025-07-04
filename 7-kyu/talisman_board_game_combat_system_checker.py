def get_required(player, enemy):
    x = player[0] + player[1] - enemy[0]-enemy[1]
    if x >= 6:
        return 'Auto-win'
    if x <= -6:
        return 'Auto-lose'
    if x == 0:
        return 'Random'
    if x == -5:
        return 'Pray for a tie!'
    
    if x < 0:
        return f"(1..{5 + x})"
    
    return f"({7 - x}..6)"
