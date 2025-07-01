def cost(mins):
    if mins <= 60:
        return 30
    
    total = 30
    remaining_mins = mins - 60 - 5
    
    if remaining_mins > 0:
        total += (remaining_mins + 29) // 30 * 10
    
    return total