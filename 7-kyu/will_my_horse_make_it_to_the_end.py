def estimator(obstacles, stamina):
    i = 0
    n = len(obstacles)
    
    while i < n and stamina >= 0:
        if obstacles[i] == 1:
            if i + 2 < n and obstacles[i+1] == 1 and obstacles[i+2] == 1:
                stamina -= 10
                i += 3
            elif i + 1 < n and obstacles[i+1] == 1:
                stamina -= 5
                i += 2
            else:
                stamina -= 2
                i += 1
        else:
            i += 1
            
    return stamina >= 0 and i == n