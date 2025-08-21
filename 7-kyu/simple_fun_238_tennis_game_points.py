def tennis_game_points(score): 
    a, b = score.split('-')
    total = 0
    if a.isdigit():
        int_a = int(a)
        if int_a > 15:
            total += int(a) // 10 - 1
        else:
            total += 1
    
    if b.isdigit():
        int_b = int(b)
        if int_b > 15:
            total += int(b) // 10 - 1
        else:
            total += 1
        
    if a == 'all' or b == 'all':
        return total * 2
        
    return total
