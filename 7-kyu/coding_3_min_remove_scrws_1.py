def sc(s):
    current = s[0]
    s = s[1:]
    n = len(s)
    total_time = 1
    
    for i in range(n):
        total_time += 1
        if current != s[i]:
            total_time += 5
            current = s[i]
            
        total_time += 1
        
    return total_time
