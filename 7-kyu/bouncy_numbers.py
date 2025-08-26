def is_bouncy(number):
    if number < 100:
        return False
    
    s = str(number)
    increasing = True
    decreasing = True
    for i in range(1, len(s)):
        if s[i] > s[i-1]:
            decreasing = False
            
        elif s[i] < s[i-1]:
            increasing = False
        
        if not increasing and not decreasing:
            return True
    
    return False
