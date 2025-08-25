def sea_sick(sea):
    n = len(sea)
    changes = 0
    
    for i in range(1, n):
        if sea[i] != sea[i - 1]:
            changes += 1
            
    if changes > 0.2 * n:
        return "Throw Up"
    else:
        return "No Problem"
